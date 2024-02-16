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
                with ui.row().classes('w-full').style('font-size: 36px; font-weight: bold;'):
                    ui.html('Chat')

                with ui.row().classes('w-full'):
                    ui.html('Start a conversation with an expert by clicking the button:')
                
                with ui.row().classes('w-full'):
                    ui.button('Start conversation', on_click=lambda: ui.open('/chat/participant/' + request_id), color='gray').classes('full-width').style('font-size: 16px; color: white;')
                
            with ui.row().classes('w-3/12 p-5').style('background-color: #e8e8e8; border-radius: 16px;'):
                with ui.row().classes('w-full').style('font-size: 36px; font-weight: bold;'):
                    ui.html('Read')

                ui.html('On the teaching pendant, click on the Help (?) button and select the Manual option to access the documentation:')
                ui.image('pendant.jpg')
                ui.html('Or refer to the document below:')

                with ui.row().classes('w-full p-2 rounded items-center place-content-center').style('background-color: #dbdbdb;'):
                    ui.markdown('Application Manual: Wizard Easy Programming')
                # ui.link(text='Application Manual - Wizard Easy Programming', target='https://search.abb.com/library/Download.aspx?DocumentID=3HAC073766&LanguageCode=en&DocumentPartId=&Action=Launch')

            with ui.row().classes('w-3/12 p-5').style('background-color: #e8e8e8; border-radius: 16px;'):
                with ui.row().classes('w-full').style('font-size: 36px; font-weight: bold;'):
                    ui.html('Watch')

                ui.html('Click in one of the videos below to start watching:')

                with ui.row().classes('w-full p-2 rounded items-center').style('background-color: #dbdbdb;'):
                    with ui.row().classes('w-5/12'):
                        ui.image('https://img.youtube.com/vi/KduqW6EQ67E/0.jpg').classes('w-64 h-32')
                    with ui.row().classes('w-6/12'):
                        ui.html('ABB Wizard Easy Programming')

                with ui.row().classes('w-full p-2 rounded items-center').style('background-color: #dbdbdb;'):
                    with ui.row().classes('w-5/12'):
                        ui.image('https://img.youtube.com/vi/-3d3wygOSSY/0.jpg').classes('w-64 h-32')
                    with ui.row().classes('w-6/12'):
                        ui.markdown('The right way to activate lead-through on GoFa Cobot')

                with ui.row().classes('w-full p-2 rounded items-center').style('background-color: #dbdbdb;'):
                    with ui.row().classes('w-5/12'):
                        ui.image('https://img.youtube.com/vi/zPnEOQX4jUA/0.jpg').classes('w-64 h-32')
                    with ui.row().classes('w-6/12'):
                        ui.markdown('How to program collaborative robot GoFa with Wizard Easy Programming')

                with ui.row().classes('w-full p-2 rounded items-center').style('background-color: #dbdbdb;'):
                    with ui.row().classes('w-5/12'):
                        ui.image('https://img.youtube.com/vi/eUgqXsWMmwI/0.jpg').classes('w-64 h-32')
                    with ui.row().classes('w-6/12'):
                        ui.markdown('Step-by-step guide on pick and place application with Wizard Easy Programming tool')

                with ui.row().classes('w-full p-2 rounded items-center').style('background-color: #dbdbdb;'):
                    with ui.row().classes('w-5/12'):
                        ui.image('https://img.youtube.com/vi/IvTEZgdDUvg/0.jpg').classes('w-64 h-32')
                    with ui.row().classes('w-6/12'):
                        ui.markdown('GoFa™ CRB 15000 - Using ASI in Auto mode')
