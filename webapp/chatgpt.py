from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, YoutubeLoader, BSHTMLLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

class DocumentProcessor:
    def load_pdf_documents(self, file_path):
        loader = PyPDFLoader(file_path)
        pdf_docs = loader.load()
        pdf_text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        return pdf_text_splitter.split_documents(pdf_docs)

    def load_html_documents(self, file_path):
        loader = BSHTMLLoader(file_path)
        pdf_docs = loader.load()
        pdf_text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        return pdf_text_splitter.split_documents(pdf_docs)

    def load_video_documents(self, video_urls):
        video_splits = []
        video_text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
        for url in video_urls:
            loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
            video_doc = loader.load()
            video_splits += video_text_splitter.split_documents(video_doc)
        return video_splits

    def embed_documents(self, documents):
        vectorstore = Chroma.from_documents(documents=documents, embedding=OpenAIEmbeddings())
        return vectorstore.as_retriever()

class RagChainGenerator:
    def __init__(self, retriever):
        self.prompt_template = """
        You are an expert assisting an end-user without experience in robotics to solve a robot programming task. 
        This task is part of an experiment where participants are invited to try a block-based programming language, 
        and they will ask you questions about robot programming. Use the following rules, question and context to answer the prompt asked by the participants.

        Rules: Never tell participants to physically interact with the robot or play with the robot operating system, as they should only use the programming language interface in this experiment.
        Never tell participants to manually teach robot positions, as the necessary positions for this task will be given beforehand.
        Never tell participants to change robot settings. Never tell participants to refer to external resources, including but not limited to technical manuals or video tutorials.
        If you don't know the answer, tell the participant you don't know how to answer his question.

        Context: In this experiment, participants will be using the ABB Wizard Easy Programming Tool to program a one-armed collaborative robot for a pick-and-place task.
        This tool consists of a block-based programming language made by the ABB robot manufacturer for collaborative robots.
        We will be using the version 1.5.2 of this tool in our experiment.
        In our study, we will also be using the ABB CRB 15000 (also known as ABB GoFa) as our robot.
        Installed on this robot there will be an OnRobot smart gripper to pick and place objects on the scene.
        In this experiment, participants will only have access to the block-based programming language.
        They will not touch or interact with the robot. Other requirements such as setting up the system or teaching robot positions will be provided beforehand for this experiment, 
        so participants can focus solely on the programming aspects of the task. 

        Question: {question}
        Context: {context}
        Answer:
        """
        self.prompt_t = ChatPromptTemplate.from_messages([
            ("system", self.prompt_template)
        ])
        self.llm = ChatOpenAI(model_name="gpt-4", temperature=0)
        self.retriever = retriever

    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def generate_response(self, question):
        rag_chain = (
            {"context": self.retriever | self.format_docs, "question": RunnablePassthrough()}
            | self.prompt_t
            | self.llm
            | StrOutputParser()
        )
        return rag_chain.invoke(question)

if __name__ == "__main__":
    load_dotenv()
    processor = DocumentProcessor()
    html_splits = processor.load_html_documents("abb_wizard_manual.html")
    video_urls = [
        "https://www.youtube.com/watch?v=Kmv5jUI3WF0",
        # "https://www.youtube.com/watch?v=zPnEOQX4jUA", This video has no transcript available.
        # "https://www.youtube.com/watch?v=eUgqXsWMmwI", This video has no transcript available.
        # "https://www.youtube.com/watch?v=nj0X8fLj1SE", This video has no transcript available.
        "https://www.youtube.com/watch?v=zizcQSnPyyE",
    ]
    video_splits = processor.load_video_documents(video_urls)
    retriever = processor.embed_documents(html_splits + video_splits)

    rag_generator = RagChainGenerator(retriever)

    response = rag_generator.generate_response("How do I create buttons on the screen for the user to define where the robot should go next?")
    print(response)

