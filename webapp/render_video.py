from nicegui import ui

def create():
    @ui.page('/video/{request_id}/')
    async def video_page(request_id: str, video_url: str):
        ui.page_title('Video')
        ui.query('body').style('background-color: #f2f2f2;')

        with ui.header().classes('place-content-center'):
            ui.html('Video')
        with ui.row().classes('w-full place-content-center'):
            with ui.row().classes('w-full place-content-center'):
                ui.html('<iframe width="1280" height="720" src="https://www.youtube.com/embed/' + video_url + '&rel=0&amp;controls=0" title="YouTube video player"\
                        frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; autoplay; picture-in-picture;\
                        web-share" allowfullscreen></iframe>')

            with ui.row().classes('w-2/12'):
                ui.button(text="Return to resources", color="gray", on_click=lambda: ui.open('/resources/' + request_id)).style('color: white;').classes('full-width')