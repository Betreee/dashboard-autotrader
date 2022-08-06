from dash  import Dash,html

from src.components import bar_chart
from . import history_dropdown
def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className = "app-div",
        children= [
            html.H1(app.title),
            html.Div(className="dropdown-container", children=[ history_dropdown.render(app)] ),
            bar_chart.render(app)
        ]
    )