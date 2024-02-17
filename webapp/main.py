import uuid 
import chat
import feedback
import resources
import render_video
import render_document
from datetime import datetime
from nicegui import ui

ui.header.default_style('background-color: #080808; color: white; font-size: 36px; font-weight: 400;')
ui.row.default_style('font-size: 20px; font-weight: 400;')

form_categories = ["I don’t know what I want the robot to do…",\
              "I think I know what I want the robot to do, but I don’t know what to use…",\
              "I think I know what things to use, but I don't know how to make them work together…",\
              "I think I know what to use, but I don't know how to use it…",\
              "I thought I knew how to use this, but it didn’t do what I expected…",\
              "I think I know why it didn’t do what I expected, but I don’t know how to check…",\
              "Other"]

requests = {}
participant_id = uuid.uuid4().hex
experiment_status = {'participand_id': participant_id, 'is_active': True}

@ui.page('/')
async def main():
    ui.query('body').style('background-color: #f2f2f2;')

    def create_request(description, category):
        request_id = uuid.uuid4().hex
        requests[request_id] = {'request_id': request_id,
                                'participant_id': participant_id,
                                'request_description': description,
                                'request_category': category,
                                'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                'closed_at': None,
                                'messages': [],
                                'interactions': []}
        ui.open('/resources/' + request_id)

    with ui.header().classes('place-content-center'):
        ui.html('Assistance Center')

    with ui.row().classes('w-full place-content-center'):
        with ui.row().classes('w-6/12 p-12'):
            with ui.row().classes('w-full').style('font-size: 36px; font-weight: bold;'):
                ui.html('Request Form')

            with ui.row().classes('w-full'):
                ui.html('Use the form below to define what type of assistance you are looking for:')

            with ui.row().classes('w-full'):
                form_option = ui.radio(form_categories, value = "Other")
                with ui.row().classes('w-full'):
                    form_text = ui.textarea(label='Describe your request in detail').props('rounded outlined clearable').classes('w-full')
                with ui.row().classes('w-full place-content-center'):
                    ui.button(text="Request Assistance", color="blue", on_click=lambda: create_request(form_text.value, form_option.value)).style('font-size: 16px;')

chat.create(requests)
resources.create()
feedback.create()
render_video.create()
render_document.create()
ui.run(favicon="H")