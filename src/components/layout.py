from dash  import Dash,html
from . import history_dropdown
def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className = "app-div",
        children= [
            html.H1(app.title),
            html.Div(
                className="dropdown-container",
                children=[
                    history_dropdown.render(app)
                ]
                
            )
        ]
    )