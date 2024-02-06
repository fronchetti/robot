from datetime import datetime
from nicegui import ui
import uuid 

ui.header.default_style('background-color: #080808; color: black;')
ui.row.default_style('font-size: 22px; font-weight: 400;')

categories = ["I don’t know what I want the robot to do…",\
              "I think I know what I want the robot to do, but I don’t know what to use…",\
              "I think I know what things to use, but I don't know how to make them work together…",\
              "I think I know what to use, but I don't know how to use it…",\
              "I thought I knew how to use this, but it didn’t do what I expected…",\
              "I think I know why it didn’t do what I expected, but I don’t know how to check…",\
              "Other"]

participant_id = uuid.uuid1()
requests = {}

@ui.page('/')
async def main():
    global requests 
    ui.page_title('Help Center')

    def create_request(description, category):
        request_id = str(uuid.uuid1())
        requests[request_id] = {'participant_id': participant_id, 'request_id': request_id, 'description': description, 'category': category, 'messages': []}
        ui.open('/chat/participant/' + str(request_id), new_tab=True)

    def request_form():
        with ui.row().classes('p-5').style('background-color: #f2f2f2; border-radius: 16px;'):
            with ui.row().classes('w-full'):
                ui.html('Request assistance').style('font-size: 28px;')

            with ui.row().classes('w-full'):
                ui.html('Use the form below to receive instant help from an expert:')

            with ui.row().classes('w-full'):
                form_option = ui.radio(categories, value = "Other")
                with ui.column().classes('w-full'):
                    form_text = ui.textarea(label='Describe your request in detail').props('rounded outlined clearable').classes('flex-grow w-full')
                with ui.column().classes('w-full'):
                    ui.button(text="Request Assistance", color="blue", on_click=lambda: create_request(form_text.value, form_option.value))

    def resources():
        with ui.row().classes('w-full p-5').style('background-color: #f2f2f2; border-radius: 16px;'):
            ui.html('Resources').style('font-size: 28px;').classes('w-full')
            ui.html('Manual').style('font-size: 18px; font-weight: bold;').classes('w-full')
            ui.link(text='Application Manual - Wizard Easy Programming', target='https://search.abb.com/library/Download.aspx?DocumentID=3HAC073766&LanguageCode=en&DocumentPartId=&Action=Launch', new_tab=True)
            ui.html('Videos').style('font-size: 18px; font-weight: bold;').classes('w-full')
            ui.link(text='ABB Wizard Easy Programming 1.3', target='https://www.youtube.com/watch?v=KduqW6EQ67E', new_tab=True)
            ui.link(text='How to program collaborative robot GoFa with Wizard Easy Programming', target='https://www.youtube.com/watch?v=zPnEOQX4jUA', new_tab=True)
            ui.link(text='Step-by-step guide on pick and place application with Wizard Easy Programming tool', target='https://www.youtube.com/watch?v=eUgqXsWMmwI', new_tab=True)
            ui.link(text='The right way to activate lead-through on GoFa Cobot', target='https://www.youtube.com/watch?v=-3d3wygOSSY', new_tab=True)
            ui.link(text='GoFa™ CRB 15000 - Using ASI in Auto mode', target='https://www.youtube.com/watch?v=IvTEZgdDUvg', new_tab=True)

    with ui.header().classes('place-content-center'):
        ui.html('Help Center').style('font-size: 36px; font-weight: 800; color: white;')

    with ui.row().classes('w-full'):
        with ui.column().classes('w-5/12'):
            request_form()

        with ui.column().classes('w-5/12'):
            resources()

@ui.page('/chat/{user_type}/{request_id}')
async def chat_page(user_type: str, request_id: str):
    global requests
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

    with ui.header().classes('place-content-center'):
        ui.html('Chat').style('font-size: 36px; font-weight: 800; color: white;')

    chat_message_area()
    chat_input_area()

@ui.page('/proctor')
async def proctor_page():
    def update_experiment_settings():
        global user_id
        user_id = uuid.uuid1()
        experiment_settings.refresh()

    @ui.refreshable
    def experiment_settings():
        with ui.row().classes('p-5 w-full').style('background-color: #f2f2f2; border-radius: 16px;'):
            with ui.expansion("Experiment Settings", icon='settings').classes('w-full'):
                ui.html('<b>Participant ID:</b> ' + str(user_id))
                ui.html('<b>Date:</b> ' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                ui.button('Start experiment', color="green", on_click=lambda: update_experiment_settings())

    with ui.header().classes('place-content-center'):
        ui.html('Proctor').style('font-size: 36px; font-weight: 800; color: white;')

    with ui.row().classes('w-full'):
        with ui.column().classes('w-5/12'):
            experiment_settings()

ui.run(favicon="H")