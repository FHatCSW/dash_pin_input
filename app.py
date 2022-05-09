import dash_bootstrap_components as dbc
from dash import Input, Output, html, Dash, callback_context, dcc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

text_input = html.Div(
    [
        dbc.Input(id="input", placeholder="Type something...", type="text"),
        html.Br(),
        html.P(id="output"),
    ]
)

row_1_3 = html.Div([
    dbc.Button(
        "1", id="button_1", className="pin_btn", n_clicks=0
    ),
    dbc.Button(
        "2", id="button_2", className="pin_btn", n_clicks=0
    ),
    dbc.Button(
        "3", id="button_3", className="pin_btn", n_clicks=0
    )
])

row_4_6 = html.Div([
    dbc.Button(
        "4", id="button_4", className="pin_btn", n_clicks=0
    ),
    dbc.Button(
        "5", id="button_5", className="pin_btn", n_clicks=0
    ),
    dbc.Button(
        "6", id="button_6", className="pin_btn", n_clicks=0
    )
])

row_7_9 = html.Div([
    dbc.Button(
        "7", id="button_7", className="pin_btn", n_clicks=0
    ),
    dbc.Button(
        "8", id="button_8", className="pin_btn", n_clicks=0
    ),
    dbc.Button(
        "9", id="button_9", className="pin_btn", n_clicks=0
    )
])

app.layout = html.Div(dbc.Container([
    dbc.Row([
        row_1_3
    ]),
    dbc.Row([
        row_4_6
    ]),
    dbc.Row([
        row_7_9
    ]),
        dbc.Button("Delete", id="delete_pin", n_clicks=0, style={'margin': '20px'}),
    dcc.Store(id='pin_code'),
    html.Div(id="pin_output"),
    html.Div(id="submit_result")
])
)


@app.callback([Output("pin_output", "children"),
               Output("pin_code", "data"),
               Output("submit_result", "children")],
              [Input("button_1", "n_clicks"),
               Input("button_2", "n_clicks"),
               Input("button_3", "n_clicks"),
               Input("button_4", "n_clicks"),
               Input("button_5", "n_clicks"),
               Input("button_6", "n_clicks"),
               Input("button_7", "n_clicks"),
               Input("button_8", "n_clicks"),
               Input("button_9", "n_clicks"),
               Input("delete_pin", "n_clicks"),
               Input('pin_code', 'data')])
def output_text(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, delete_pin,
                pin_code):
    ctx = callback_context
    changed_id = ctx.triggered[0]['prop_id'].split('.')[0]
    submit_result = html.Div()

    if "delete_pin" in changed_id or pin_code is None:
        pin_code = ""

    if len(pin_code) < 3:

        if "button_1" in changed_id: pin_code = pin_code + "1"
        if "button_2" in changed_id: pin_code = pin_code + "2"
        if "button_3" in changed_id: pin_code = pin_code + "3"
        if "button_4" in changed_id: pin_code = pin_code + "4"
        if "button_5" in changed_id: pin_code = pin_code + "5"
        if "button_6" in changed_id: pin_code = pin_code + "6"
        if "button_7" in changed_id: pin_code = pin_code + "7"
        if "button_8" in changed_id: pin_code = pin_code + "8"
        if "button_9" in changed_id: pin_code = pin_code + "9"

    pin = len(pin_code) * "*"

    if pin_code == "152":
        pin_output = dbc.Input(value=pin, valid=True, className="mb-3", disabled=True, style={'width': '80px',
                                                                                              'margin-left': '20px'})
        submit_result = dbc.Button("Login", id="login", n_clicks=0, style={'margin-left': '20px'})
    else:
        pin_output = dbc.Input(value=pin, invalid=True, className="mb-3", disabled=True, style={'width': '80px',
                                                                                               'margin-left': '20px'})

    return [pin_output, pin_code, submit_result]


if __name__ == "__main__":
    app.run_server()
