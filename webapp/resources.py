from nicegui import ui

def create():
    @ui.page('/resources/{request_id}')
    async def resources(request_id: str):        
        ui.page_title('Resources')
        ui.query('body').style('background-color: #f2f2f2;')

        with ui.header().classes('place-content-center'):
            ui.html('Resources')

        with ui.row().classes('w-full place-content-center'):
            with ui.row().classes('w-6/12 p-5').style('background-color: #e8e8e8; border-radius: 16px;'):
                with ui.row().classes('w-full place-content-center'):
                    ui.html('Use the resources below to complete your request. Once you are done, hit the close request button:')
                with ui.row().classes('w-full place-content-center'):
                    ui.button('Close request', on_click=lambda: ui.open('/feedback/' + request_id), color='red').style('font-size: 16px;')

        with ui.row().classes('w-full place-content-center'):
            with ui.row().classes('w-3/12 p-5').style('background-color: #e8e8e8; border-radius: 16px;'):
                with ui.row().classes('w-full').style('font-size: 28px; font-weight: bold;'):
                    ui.html('Chat')

                with ui.row().classes('w-full'):
                    ui.html('Start a conversation with an expert by clicking the button:')
                
                with ui.row().classes('w-full'):
                    ui.button('Speak to an expert', on_click=lambda: ui.notify('!')).style('font-size: 22px;')
                
            with ui.row().classes('w-3/12 p-5').style('background-color: #e8e8e8; border-radius: 16px;'):
                with ui.row().classes('w-full').style('font-size: 28px; font-weight: bold;'):
                    ui.html('Read')

                ui.html('On the teaching pendant, click on the Help button and select the Manual option to get learn how to program the solution:')

                ui.link(text='Application Manual - Wizard Easy Programming', target='https://search.abb.com/library/Download.aspx?DocumentID=3HAC073766&LanguageCode=en&DocumentPartId=&Action=Launch')

            with ui.row().classes('w-3/12 p-5').style('background-color: #e8e8e8; border-radius: 16px;'):
                with ui.row().classes('w-full').style('font-size: 28px; font-weight: bold;'):
                    ui.html('Watch')

                ui.link(text='ABB Wizard Easy Programming 1.3', target='https://www.youtube.com/watch?v=KduqW6EQ67E')
                ui.link(text='How to program collaborative robot GoFa with Wizard Easy Programming', target='https://www.youtube.com/watch?v=zPnEOQX4jUA')
                ui.link(text='Step-by-step guide on pick and place application with Wizard Easy Programming tool', target='https://www.youtube.com/watch?v=eUgqXsWMmwI')
                ui.link(text='The right way to activate lead-through on GoFa Cobot', target='https://www.youtube.com/watch?v=-3d3wygOSSY')
                ui.link(text='GoFa™ CRB 15000 - Using ASI in Auto mode', target='https://www.youtube.com/watch?v=IvTEZgdDUvg')

