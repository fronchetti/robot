import os
import json
import uuid 
import chat
import feedback
import resources
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

    def set_experiment_values(participant_id = None, is_active = None):
        if not os.path.isdir('data'):
            os.mkdir('data')

        with open('data/experiment_status.json', 'w') as status_file:
            if participant_id == None:
                participant_id = uuid.uuid4().hex
            if is_active == None:
                is_active = True

            experiment_status = {'participant_id': str(participant_id), 'is_active': is_active}
            status_file.write(json.dumps(experiment_status))

        return experiment_status

    def get_experiment_status():
        # If status file does not exist, create one
        if not os.path.isfile('data/experiment_status.json'):
            experiment_status = set_experiment_values()
        else:
            with open('data/experiment_status.json', 'r') as status_file:
                experiment_status = json.load(status_file)

        return experiment_status

    def close_experiment():
        experiment_status = get_experiment_status()
        set_experiment_values(participant_id = experiment_status['participant_id'], is_active = False)
        start_experiment_area.refresh()
    
    def start_experiment():
        set_experiment_values()
        start_experiment_area.refresh()

    @ui.refreshable
    def start_experiment_area():
        experiment_status = get_experiment_status()    

        with ui.row().classes('w-full place-content-center'):
            if experiment_status['is_active']:
                with ui.row().classes('w-full place-content-center'):
                    with ui.row().classes('w-6/12 p-12'):
                        ui.html('Status').classes('w-full').style('font-size: 36px; font-weight: bold;')
                        ui.html('There is an experiment in progress. The proctor must resume or end the current experiment.').classes('w-full')
                        ui.html('Participant identifier: ' + experiment_status['participant_id']).classes('w-full')

                        ui.html('Later Checklist').classes('w-full').style('font-size: 36px; font-weight: bold;')
                        ui.html('After the experiment, the proctor must cover the following steps with the participant:').classes('w-full')
                        ui.checkbox('Open the questionnaire and answer the proctor-related questions. The identifier informed must be the same available above.').classes('w-full')
                        ui.checkbox('Once the proctor-related questions are completed, invite the participant to answer the following questions.').classes('w-full')
                        ui.checkbox('With the questionnaire complete, end the experiment by clicking the "end experiment" button.').classes('w-full')

                        with ui.row().classes('w-full place-content-center'):
                            with ui.row().classes('w-2/12'):
                                ui.button(text="Resume experiment", color="gray", on_click=lambda: print()).classes('full-width')

                            with ui.row().classes('w-2/12'):
                                ui.button(text="End experiment", color="red", on_click=lambda: close_experiment()).classes('full-width')
            else:
                with ui.row().classes('w-full place-content-center'):
                    with ui.row().classes('w-6/12 p-12'):
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
                                ui.button(text="Start experiment", color="green", on_click=lambda: start_experiment()).classes('full-width')

    with ui.header().classes('place-content-center'):
        ui.html('Experiment')

    start_experiment_area()

chat.create(None)
resources.create()
feedback.create()
render_video.create()
render_document.create()
ui.run(favicon="🐔")