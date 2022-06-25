#IMPORT STATEMENTS
from dash import html
from navbar import create_navbar
import dash_bootstrap_components as dbc
import dash_core_components as dcc


#REGIONS
REGIONS = ['Ahafo', 'Ashanti', 'Bono', 'Bono East', 'Central', 'Eastern', 'Greater Accra', 'North East', 'Northern',
           'Oti', 'Savannah', 'Upper East', 'Upper West', 'Volta', 'Western North', 'Western']

nav = create_navbar();

header = html.Div([

# REGION
            html.H2('POPULATIONS PYRAMIDS - By Age and Sex', style={'color': 'navy', 'margin': '15px', 'backgroundColor': 'white'}),
            dbc.Row([

                # regions
                dbc.Col([
                    html.Span('REGION', style={'fontWeight': 'bold'}),
                    dcc.Dropdown(
                        id='pyramid_region_dd',
                        style={'color': 'black'},

                        options=[{'label': REGION, 'value': REGION} for REGION in REGIONS]
                    ),
                ], width=2, style={'marginLeft': '20px', 'marginTop': '10px', 'marginBottom': '5px'}),

                html.Br(),

                dbc.Col([
                    html.Span('DISTRICT', style={'fontWeight': 'bold'}),
                    dcc.Dropdown(
                        id='pyramid_district_dd',
                        style={'color': 'black'},
                    ),
                ], width=2, style={'marginLeft': '0px', 'marginTop': '10px', 'marginBottom': '5px'}),

                html.Br(),

                dbc.Col([
                    dbc.Button('SEARCH',
                        id='pyramid_search_btn',
                        n_clicks=0,
                        className='me-1',
                        size='lg',
                       style={'marginTop': '20px'},
                    ),
                ], width=1, style={'width':'6%', 'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

                dbc.Col([
                    dbc.Button('CLEAR',
                        id='pyramid_clear_btn',
                        n_clicks=0,
                        className='me-1',
                        size='lg',
                       style={'marginTop': '20px'},
                    ),
                ], width=1, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

            ], style={'backgroundColor': '#eeeff3', 'color': 'navy', 'fontSize': '18px', 'paddingBottom': '10px'}),

            html.Hr(),

            html.H3(id='', style={'color': 'navy', 'marginLeft': '18px'}),

            dbc.Row([
                dbc.Col([
                    dbc.CardBody([
                    html.Div(id='age_pyramid')
                    ]),

                ], width=2, style={'marginLeft': '0px'}),

            ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),

])

def create_population_pyramid():
    layout = html.Div([
        nav,
        header
    ])

    return layout