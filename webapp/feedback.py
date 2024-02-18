from nicegui import ui

def create():
    @ui.page('/feedback/{request_id}')
    async def feedback(request_id: str):
        ui.page_title('Feedback')
        ui.query('body').style('background-color: #f2f2f2;')

        with ui.header().classes('place-content-center'):
            ui.html('Feedback')

        with ui.row().classes('w-full place-content-center'):
            with ui.row().classes('w-full place-content-center'):
                ui.html('<b>Rate your satisfaction with the assistance given for this request:</b>')

            with ui.row().classes('w-full place-content-center'):
                satisfaction_Scale = ui.radio(['Very Dissatisfied', 'Dissatisfied', 'Neutral', 'Satisfied', 'Very Satisfied'], value=1).props('inline')

            with ui.row().classes('w-full place-content-center'):
                ui.html('<b>What category of information was the most useful for this request?</b>')

            with ui.row().classes('w-full place-content-center'):
                useful_action = ui.radio(['Chat', 'Read', 'Watch'], value=1).props('inline')

            with ui.row().classes('w-full place-content-center'):
                ui.html('<b>In this request, you stated that: "I don’t know what I want the robot to do…".<br>Was this statement correct? If not, we will ask you to assign the correct description.</b>')

            with ui.row().classes('w-full place-content-center'):
                useful_action = ui.radio(['Yes', 'No'], value=1).props('inline')

            with ui.row().classes('w-2/12'):
                ui.button(text="Close request", color="red", on_click=lambda: ui.open('/')).style('color: white;').classes('full-width')

            with ui.row().classes('w-2/12'):
                ui.button(text="Return to request", color="gray", on_click=lambda: ui.open('/resources/' + request_id)).style('color: white;').classes('full-width')
