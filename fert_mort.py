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

    html.H2('FERTILITY & MORTALITY', style={'color': 'navy', 'margin': '15px', 'backgroundColor': 'white'}),
    dbc.Row([

        # regions
        dbc.Col([
            html.Span('REGION', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='fert_mort_region_dd',
                style={'color': 'black'},

                options=[{'label': REGION, 'value': REGION} for REGION in REGIONS]
            ),
        ], width=2, style={'marginLeft': '20px', 'marginTop': '10px', 'marginBottom': '5px'}),

        html.Br(),

        dbc.Col([
            html.Span('DISTRICT', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='fert_mort_district_dd',
                style={'color': 'black'},
            ),
        ], width=2, style={'marginLeft': '0px', 'marginTop': '10px', 'marginBottom': '5px'}),

        html.Br(),

        dbc.Col([
            dbc.Button('SEARCH',
                id='fert_mort_search_btn',
                n_clicks=0,
                className='me-1',
                size='lg',
               style={'marginTop': '20px'},
            ),
        ], width=1, style={'width':'6%', 'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

        dbc.Col([
            dbc.Button('CLEAR',
                id='fert_mort_clear_btn',
                n_clicks=0,
                className='me-1',
                size='lg',
               style={'marginTop': '20px'},
            ),
        ], width=1, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

    ], style={'backgroundColor': '#eeeff3', 'color': 'navy', 'fontSize': '18px', 'paddingBottom': '10px'}),

    html.Hr(),

    html.H3('Regional', style={'color': 'navy', 'marginLeft': '18px'}),

    # Data - Row #1 REGIONAL
    dbc.Row([
        dbc.Col([
            dbc.CardBody([
                html.H5('Children Ever Born', style={'color': 'white', 'fontSize': '18px'}),
                html.H5(id='fert_mort_chd_ever_born_tot',
                        style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '30px'}),

        dbc.Col([
            dbc.CardBody([
                html.H5('Children Surviving', style={'color': 'white', 'fontSize': '18px'}),
                html.H5(id='fert_mort_chd_surv_tot',
                        style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '30px'}),

        dbc.Col([
            dbc.CardBody([
                html.H5('Mean Children Surviving', style={'color': 'white', 'fontSize': '18px'}),
                html.H5(id='fert_mort_mean_chd_surv_tot',
                        style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '30px'}),

    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),

    html.Hr(),

    html.H3('District', style={'color': 'navy', 'marginLeft': '18px'}),

    # Data - Row #1 DISTRICT
    dbc.Row([
        dbc.Col([
            dbc.CardBody([
                    html.H5('Children Ever Born', style={'color': 'white', 'fontSize': '18px'}),
                             html.H5(id='fert_mort_chd_ever_born', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ]),

        ], width=2, style={'marginLeft': '30px'}),

        dbc.Col([
            dbc.CardBody([
                html.H5('Children Surviving', style={'color': 'white', 'fontSize': '18px'}),
                         html.H5(id='fert_mort_chd_surv',
                                   style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '30px'}),

        dbc.Col([
            dbc.CardBody([
                html.H5('Mean Children Surviving', style={'color': 'white', 'fontSize': '18px'}),
                         html.H5(id='fert_mort_mean_chd_surv',
                                   style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '30px'}),

    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),
])

def create_fert_mort():
    layout = html.Div([
        nav,
        header
    ])

    return layout