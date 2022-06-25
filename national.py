from dash import html
from navbar import create_navbar
import dash_bootstrap_components as dbc

nav = create_navbar();
header = html.Div([
        dbc.Row([
                html.H2('NATIONAL', style={'color': 'navy', 'margin': '10px', 'backgroundColor': 'white'}),
                dbc.Col([
                    dbc.CardBody([
                        html.H5([html.H5('Population (M):', style={'color': 'white'}),
                            dbc.Badge('30.8', color='#5080C3', text_color='navy', pill=False, className="border me-3", style={'fontSize': '18px', 'fontWeight': 'bold'}),
                        ])
                    ])
                ], width=3, style={'marginLeft': '0px', 'marginTop': '5px'}),

                dbc.Col([
                    dbc.CardBody(
                        html.H5([html.H5('Females (%):', style={'color': 'white'}),
                            dbc.Badge("50.7", color="#5080C3", text_color='white', pill=False, className="border me-3", style={'fontSize': '18px', 'fontWeight': 'bold'}),
                        ])
                    )
                ], width=3, style={'marginLeft': '0px', 'marginTop': '5px'}),

                dbc.Col([
                    dbc.CardBody(
                        html.H5([html.H5('Average Household Size:', style={'color': 'white'}),
                                dbc.Badge("3.6", color="#5080C3", text_color='white', pill=False, className="border me-3", style={'fontSize': '18px', 'fontWeight': 'bold'}),
                        ])
                    )
                ], width=3, style={'marginLeft': '0px', 'marginTop': '5px'}),

                dbc.Col([
                    dbc.CardBody(
                        html.H5([html.H5('Structures (M):', style={'color': 'white'}),
                            dbc.Badge("10.7", color="#5080C3", text_color='white', pill=False, className="border me-3", style={'fontSize': '18px', 'fontWeight': 'bold'}),
                        ])
                    )
                ], width=3, style={'marginLeft': '0px', 'marginTop': '5px'}),

            ], style={'backgroundColor': 'navy'}),
        # dbc.Row([
        #
        #     html.Iframe(src='https://experience.arcgis.com/experience/0a80de552e5e4caab77de2f3a7ce1063/',
        #         style={'height': '1067px', 'width': '100%'}),
        #
        # ])
    ])

def create_national():
    layout = html.Div([
        nav,
        header
    ])

    return layout