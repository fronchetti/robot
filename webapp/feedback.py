from nicegui import ui

def create():
    @ui.page('/feedback/{request_id}')
    async def feedback(request_id: str):
        ui.page_title('Feedback')

        with ui.header().classes('place-content-center'):
            ui.html('Feedback')