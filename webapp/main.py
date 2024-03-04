import chat
import database
import feedback
import resources
import assistance
import render_video
import render_document
from nicegui import ui

ui.header.default_style('background-color: #080808; color: white; font-size: 36px; font-weight: 400;')
ui.row.default_style('font-size: 20px; font-weight: 400;')
ui.button.default_style('color: white;')

@ui.page('/')
async def main():
    ui.page_title('Experiment')
    ui.query('body').style('background-color: #f2f2f2;')

    def start_experiment(proctor_password):
        if str(proctor_password).lower() == 'selab':
            participant_id = database.create_experiment()
            ui.open('/assistance/' + participant_id, new_tab=True)
            start_experiment_area.refresh()
        else:
            ui.notify('To start a new experiment, insert your password above.')
            ui.notify('If you need help, send a message to Felipe at (804) 298-0694 or on Discord at @fronchetti.')

    def resume_experiment(proctor_password, participant_id):
        if str(proctor_password).lower() == 'selab':
            ui.open('/assistance/' + participant_id, new_tab=True)
        else:
            ui.notify('To resume the experiment, insert your password above.')
            ui.notify('If you need help, send a message to Felipe at (804) 298-0694 or on Discord at @fronchetti.')

    def close_experiment(proctor_password, participant_id):
        if str(proctor_password).lower() == 'selab':
            database.close_experiment(participant_id=participant_id)
            start_experiment_area.refresh()
        else:
            ui.notify('To end the experiment, insert your password above.')
            ui.notify('If you need help, send a message to Felipe at (804) 298-0694 or on Discord at @fronchetti.')

    @ui.refreshable
    def start_experiment_area():
        experiment_data = database.read_last_experiment()    

        with ui.row().classes('w-full place-content-center'):
            if experiment_data and experiment_data['closed_at'] is None:
                with ui.row().classes('w-full place-content-center'):
                    with ui.row().classes('w-6/12 p-12'):
                        ui.html('Status').classes('w-full').style('font-size: 36px; font-weight: bold;')
                        ui.html('There is an experiment in progress. The proctor must resume or end the current experiment.').classes('w-full')
                        ui.html('Participant identifier: ' + experiment_data['participant_id']).classes('w-full')

                        ui.html('Post Checklist').classes('w-full').style('font-size: 36px; font-weight: bold;')
                        ui.html('After the experiment, the proctor must cover the following steps with the participant:').classes('w-full')
                        ui.checkbox('Open the survey and answer the proctor-related questions. The identifier informed must be the same available above.').classes('w-full')
                        ui.checkbox('Once the proctor-related questions are completed, invite the participant to answer the following questions.').classes('w-full')
                        ui.checkbox('With the survey complete, finish the experiment by clicking the "end experiment" button.').classes('w-full')

                        with ui.row().classes('w-full place-content-center'):
                            with ui.row().classes('w-2/12'):
                                password_field = ui.input(label='Proctor Password', password=True)

                        with ui.row().classes('w-full place-content-center'):
                            with ui.row().classes('w-2/12'):
                                ui.button(text="Resume experiment", color="gray", on_click=lambda: resume_experiment(password_field.value, experiment_data['participant_id'])).classes('full-width')

                            with ui.row().classes('w-2/12'):
                                ui.button(text="End experiment", color="red", on_click=lambda: close_experiment(password_field.value, experiment_data['participant_id'])).classes('full-width')
            else:
                with ui.row().classes('w-full place-content-center'):
                    with ui.row().classes('w-6/12 p-12'):
                        ui.html('Status').classes('w-full').style('font-size: 36px; font-weight: bold;')
                        ui.html('There is no experiment running at the moment, and a proctor can start a new one.').classes('w-full')

                        ui.html('Preliminary Checklist').classes('w-full').style('font-size: 36px; font-weight: bold;')
                        ui.html('Before proceeding with the experiment, the proctor must cover the following steps with the participant:').classes('w-full')
                        ui.checkbox('Play the training videos to the participant in the conference room').classes('w-full')
                        ui.checkbox('Bring and introduce participant to the experiment area').classes('w-full')
                        ui.checkbox('Introduce praticipant to the robot and teaching pendant').classes('w-full')
                        ui.checkbox('Emphasize the task and the expected result').classes('w-full')
                        ui.checkbox('Emphasize the programming language').classes('w-full')
                        ui.checkbox('Emphasize the resource center in the programming language').classes('w-full')
                        ui.checkbox('Bring and introduce participant to the help desk').classes('w-full')
                        ui.checkbox('Start the experiment').classes('w-full')

                        with ui.row().classes('w-full place-content-center'):
                            with ui.row().classes('w-2/12'):
                                password_field = ui.input(label='Proctor Password', password=True)

                        with ui.row().classes('w-full place-content-center'):
                            with ui.row().classes('w-2/12'):
                                ui.button(text="Start experiment", color="green", on_click=lambda: start_experiment(password_field.value)).classes('full-width')

    with ui.header().classes('place-content-center'):
        ui.html('Experiment')

    start_experiment_area()

assistance.create()
chat.create(None)
resources.create()
feedback.create()
render_video.create()
render_document.create()
ui.run(favicon="🐔")