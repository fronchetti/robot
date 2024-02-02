from datetime import datetime
from typing import List, Tuple
from nicegui import ui
import uuid 

categories = ["I don’t know what I want the robot to do…",\
              "I think I know what I want the robot to do, but I don’t know what to use…",\
              "I think I know what things to use, but I don't know how to make them work together…",\
              "I think I know what to use, but I don't know how to use it…",\
              "I thought I knew how to use this, but it didn’t do what I expected…",\
              "I think I know why it didn’t do what I expected, but I don’t know how to check…",\
              "Other"]

user_id = uuid.uuid1()
chat_messages: List[Tuple[str, str, str, bool]] = []

def send_chat_message(message, is_participant):
    name = 'Participant' if is_participant else 'Expert'
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    chat_messages.append((name, message, timestamp, is_participant))
    chat.refresh()

def update_experiment_settings():
    global user_id
    user_id = uuid.uuid1()
    experiment_settings.refresh()

ui.header.default_style('background-color: #ffd25a; color: black;')
ui.row.default_style('font-size: 18px; font-weight: 400;')

def header():
    with ui.header().classes('place-content-center'):
        ui.html('Help Desk').style('font-size: 32px; font-weight: 400;')

def ticket_form():
    with ui.row().classes('p-5').style('background-color: #f2f2f2; border-radius: 16px;'):
        with ui.row().classes('w-full'):
            ui.html('Request assistance').style('font-size: 28px;')

        with ui.row().classes('w-full'):
            ui.html('Use the form below to receive instant help from an expert:')

        with ui.row().classes('w-full'):
            form_option = ui.radio(categories)
            with ui.column().classes('w-full'):
                form_text = ui.textarea(label='Describe your issue', on_change=None).props('rounded outlined input-class=mx-3').classes('flex-grow w-full')
            with ui.column().classes('w-full'):
                ui.button(text="Submit", icon="input", color="green", on_click=lambda: send_chat_message("I need help!", True))
                ui.button(text="Answer", icon="input", color="red", on_click=lambda: send_chat_message("Let me help you!", False))

@ui.refreshable
def experiment_settings():
    with ui.row().classes('p-5 w-full').style('background-color: #f2f2f2; border-radius: 16px;'):
        with ui.expansion("Experiment Settings (Staff Only)", icon='settings').classes('w-full'):
            ui.html('<b>Participant ID:</b> ' + str(user_id))
            ui.html('<b>Date:</b> ' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            ui.button('Restart experiment', icon="delete_outline", color="red", on_click=lambda: update_experiment_settings())

@ui.refreshable
def chat():
        with ui.row().classes('w-full p-5').style('background-color: #f2f2f2; border-radius: 16px;'):
            with ui.scroll_area().classes('max-h-screen').style('min-height: 70vh;') as scroll_area:
                for name, text, stamp, sent in chat_messages:
                    ui.chat_message(name=name, text=text, stamp=stamp, sent=sent).classes('w-full')
                scroll_area.scroll_to(percent=100)

@ui.page('/')
async def main():
    header()

    with ui.row().classes('w-full'):
        with ui.column().classes('w-4/12'):
            ticket_form()
            experiment_settings()

        with ui.column().classes('w-4/12'):
            chat()

        with ui.column().classes('w-3/12'):
            ui.label("Progress will go here.")

ui.run()