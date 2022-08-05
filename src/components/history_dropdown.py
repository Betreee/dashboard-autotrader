from dash import Dash,html,dcc 
from . import ids

def render(app: Dash) -> html.Div:
    all_history = ["buy_history","sell_history"]
    return html.Div(
        children=[
            html.H6("History"),
            dcc.Dropdown(
                id=ids.HISTORY_DROPDOWN,
                options=[{"label": history, "value": history} for history in all_history],
                value=all_history,
                multi=True,
            )
        ]
    )