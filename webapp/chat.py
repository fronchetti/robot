from nicegui import ui
from datetime import datetime

def create(requests):
    @ui.page('/chat/{user_type}/{request_id}')
    async def chat_page(user_type: str, request_id: str):
        category = requests[request_id]['category']
        description = requests[request_id]['description'] 
        ui.page_title(description)
        ui.timer(1.0, lambda: chat_message_area.refresh())


        def record_chat_message(chat_field):
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            requests[request_id]['messages'].append((user_type, chat_field.value, timestamp))
            chat_message_area.refresh()
            chat_field.clear()

        @ui.refreshable
        def chat_message_area():
            with ui.row().classes('w-full p-10').style('background-color: #f2f2f2; border-radius: 16px;'):
                ui.chat_message(name='Request System', text='One expert was designated to answer your request, please wait a moment.<br><br><b>Category:</b> ' + category + '<br><b>Description:</b> ' + description, sent=False, text_html=True).classes('w-full')

                for (author, message, stamp) in requests[request_id]['messages']:
                    message_on_left = True if author == 'participant' else False
                    ui.chat_message(name=author.capitalize(), text=message, stamp=stamp, sent=message_on_left).classes('w-full')

        def chat_input_area():
            if user_type == 'participant' or user_type == 'expert':
                with ui.row().classes('w-full'):
                    chat_field = ui.textarea(label='Write a message...').props('rounded outlined clearable').classes(' w-full')

                with ui.row().classes('w-full'):
                    ui.button(text="Send message", color="blue", on_click=lambda: record_chat_message(chat_field))
                
                if user_type == 'participant':
                    with ui.row().classes('w-full'):
                        ui.button(text="Close request", color="red", on_click=lambda: record_chat_message(chat_field))

        with ui.header().classes('place-content-center'):
            ui.html('Chat').style('font-size: 36px; font-weight: 400; color: white;')

        chat_message_area()
        chat_input_area()