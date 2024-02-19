from nicegui import ui

def create():
    @ui.page('/feedback/{request_id}')
    async def feedback(request_id: str):
        def close_request():
            if satisfaction_scale.value and useful_action.value and correct_category.value:
                ui.open('/')
            else:
                ui.notify('Before proceeding, answer the mandatory questions in the feedback form.', type='warning')

        ui.page_title('Feedback')
        ui.query('body').style('background-color: #f2f2f2;')

        with ui.header().classes('place-content-center'):
            ui.html('Feedback')

        with ui.row().classes('w-full place-content-center'):
            with ui.row().classes('w-6/12 p-12'):
                with ui.row().classes('w-full').style('font-size: 36px; font-weight: bold;'):
                    ui.html('Questions')

                with ui.row().classes('w-full'):
                    ui.html('Rate your satisfaction with the assistance given for this request:')

                with ui.row().classes('w-full'):
                    satisfaction_scale = ui.radio(['Very Dissatisfied', 'Dissatisfied', 'Neutral', 'Satisfied', 'Very Satisfied']).props('inline')

                with ui.row().classes('w-full'):
                    ui.html('What category of information was the most useful for this request?')

                with ui.row().classes('w-full'):
                    useful_action = ui.radio(['Chat', 'Read', 'Watch']).props('inline')

                with ui.row().classes('w-full'):
                    ui.html('In this request, you described that: <i>" I don’t know what I want the robot to do…"</i>.<br>Was this statement correct? If not, we will ask you to assign another description.')

                with ui.row().classes('w-full'):
                    correct_category = ui.radio(['Yes', 'No']).props('inline')

                with ui.row().classes('w-2/12'):
                    ui.button(text="Close request", color="red", on_click=lambda: close_request()).style('color: white;').classes('full-width')

                with ui.row().classes('w-2/12'):
                    ui.button(text="Return to request", color="gray", on_click=lambda: ui.open('/resources/' + request_id)).style('color: white;').classes('full-width')
