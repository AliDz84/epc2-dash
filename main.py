import dash
from dash import html,dcc
import dash_bootstrap_components as dbc

app=dash.Dash(__name__,use_pages=True,external_stylesheets=[dbc.themes.SPACELAB])
server=app.server
sidebar=dbc.Nav(
    [
        dbc.NavLink(
            [
                html.Div(page['name'],className="ms-2"),
                         ],
                href=page["path"],
                active="exact", 
                )
            for page in dash.page_registry.values()
            ],
                     vertical=True,
                     pills=True,
                     className="bg-Light",
    style={'overflow':'hidden', 'transition': 'width 0.3s ease-in-out', 
       'background-color':'#343a40'},
                     )


app.layout=dbc.Container([
    dbc.Row([
        
            dbc.Col(html.Div("GCB Dashboards",
                             style={'frontsize':50,'textAlign':'center'}))
            ]),
        html.Hr(),

        dbc.Row([
            dbc.Col([
                sidebar
                ],
                    xs=4,sm=4,md=2,lg=2,xl=2,xxl=2),
            dbc.Col(
                [
                    dash.page_container
                    ],xs=4,sm=4,md=2,lg=2,xl=2,xxl=2)
            ])
       ], fluid=True)


if __name__=="__main__":
    app.run(debug=True)


    
