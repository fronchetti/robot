import database
from nicegui import ui
from datetime import datetime

def create():
    @ui.page('/chat/{participant_id}/{request_id}/{interaction_id}/')
    async def chat_page(participant_id: str, request_id: str, interaction_id: str):
        interaction_data = database.read_interaction(participant_id, request_id, interaction_id)
        request_data = database.read_request(participant_id, request_id)

        ui.page_title(request_data['description'])
        ui.timer(1.0, lambda: chat_message_area.refresh())

        def close_chat():
            database.close_interaction(participant_id, request_id, interaction_id)
            ui.open('/resources/' + participant_id + '/' + request_id)

        def record_participant_message(chat_field):
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            interaction_data['content']['messages'].append({'user_type': 'participant', 'text': chat_field.value, 'timestamp': timestamp})
            database.update_interaction(**interaction_data)
            chat_message_area.refresh()
            chat_field.clear()

        @ui.refreshable
        def chat_message_area():
            with ui.row().classes('w-full p-10').style('background-color: #f2f2f2; border-radius: 16px;'):
                ui.chat_message(name='Request System', text='Please wait a moment while we connect you with an expert...<br><br><b>Request category:</b> ' + request_data['category'] + '<br><b>Request description:</b> ' + request_data['description'], sent=False, text_html=True).classes('w-full')
                interaction_data = database.read_interaction(participant_id, request_id, interaction_id)

                for message in interaction_data['content']['messages']:
                    message_on_left = True if message['user_type'] == 'participant' else False
                    ui.chat_message(name=message['user_type'].capitalize(), text=message['text'], stamp=message['timestamp'], sent=message_on_left).classes('w-full')

        def chat_input_area():
            with ui.row().classes('w-full'):
                chat_field = ui.textarea(label='Write a message...').props('rounded outlined clearable').classes(' w-full')

            with ui.row().classes('w-full place-content-center p-5'):
                with ui.row().classes('w-2/12'):
                    send_button = ui.button(text="Send message", color="blue", on_click=lambda: record_participant_message(chat_field)).classes('full-width')
                    send_button.on('click', lambda: chat_field.set_value(''))

                    with ui.row().classes('w-2/12'):
                        ui.button(text="Return to resources", color="gray", on_click=lambda: close_chat()).style('color: white;').classes('full-width')

        with ui.header().classes('place-content-center'):
            ui.html('Chat').style('font-size: 36px; font-weight: 400; color: white;')

        chat_message_area()
        chat_input_area()