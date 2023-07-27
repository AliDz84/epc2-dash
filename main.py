import dash
from dash import html,dcc
import dash_bootstrap_components as dbc
import pandas as pd
import openpyxl





app=dash.Dash(__name__,external_stylesheets=[dbc.themes.SUPERHERO])
server=app.server
imageList=pd.read_excel("data.xlsx", engine="openpyxl")
ph1=imageList['desc'].loc[imageList.index[0]]

app.layout=dbc.Container([
    dbc.Row([
        
            dbc.Col(html.Div("alilo Dashboards",
                             style={'frontsize':50,'textAlign':'center'}))
            ]),
        dbc.Row(
            [               
                dbc.Col(
                    [
                            html.Img(src="1.jpg"),

                            html.P(ph1,
                           style={"color": "white",
                                  "font-size": "15px",
                                  'margin-top': '15px',
                                  'margin-bottom': '15px',
                                  'line-height': '1.2',
                                  'text-align': 'center'
                                  }
                           )   
                        ],
                    className='',
                    xs=6,sm=6,md=6,lg=6,xl=6,xxl=6
                    ),

                html.Br(),
                
                ])

       ], fluid=True)


if __name__=="__main__":
    app.run(debug=True)


    
