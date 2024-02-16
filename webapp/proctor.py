import uuid 
from nicegui import ui
from datetime import datetime

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