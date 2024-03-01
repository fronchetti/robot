from nicegui import ui

def create():
    @ui.page('/document/{request_id}/')
    async def document_page(request_id: str, document_url: str):
        ui.page_title('Document')
        ui.query('body').style('background-color: #f2f2f2;')

        with ui.header().classes('place-content-center'):
            ui.html('Document')
        with ui.row().classes('w-full place-content-center'):
            with ui.row().classes('w-full place-content-center'):
                ui.html('<embed src="' + document_url + '" width="1280" height="720" type="application/pdf">')

            with ui.row().classes('w-2/12'):
                ui.button(text="Return to resources", color="gray", on_click=lambda: ui.open('/resources/' + request_id)).style('color: white;').classes('full-width')