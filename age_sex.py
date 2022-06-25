#IMPORT STATEMENTS
from dash import html
from navbar import create_navbar
import dash_bootstrap_components as dbc
import dash_core_components as dcc

#REGIONS
REGIONS = ['Ahafo', 'Ashanti', 'Bono', 'Bono East', 'Central', 'Eastern', 'Greater Accra', 'North East', 'Northern',
           'Oti', 'Savannah', 'Upper East', 'Upper West', 'Volta', 'Western North', 'Western']

nav = create_navbar()
header = html.Div([

    html.H2('AGE & SEX', style={'color': 'navy', 'margin': '10px', 'backgroundColor': 'white'}),
    dbc.Row([
    # regions
    dbc.Col([
        html.Span('REGION', style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='age_sex_region_dd',
            style={'color': 'black'},
            options=[{'label': REGION, 'value': REGION} for REGION in REGIONS]
        ),
    ], width=2, style={'marginLeft': '20px', 'marginTop': '5px', 'marginBottom': '5px'}),

    html.Br(),

    dbc.Col([
        html.Span('DISTRICT', style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='age_sex_district_dd',
            style={'color': 'black'},
        ),
    ], width=2, style={'marginLeft': '90px', 'marginTop': '5px', 'marginBottom': '5px'}),

    #age groups
    dbc.Col([
        html.Span('AGE GROUP', style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='age_sex_group_dd',
            style={'color': 'black'},
        ),
    ], width=2, style={'marginLeft': '90px', 'marginTop': '5px', 'marginBottom': '5px'}),

    dbc.Col([
        dbc.Button('SEARCH',
            id='age_sex_search_btn',
            n_clicks=0,
            className='me-1',
            size='lg',
           style={'marginTop': '20px'},
        ),
    ], width=1, style={'width':'6%', 'marginLeft': '20px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

    dbc.Col([
        dbc.Button('CLEAR',
            id='age_sex_clear_btn',
            n_clicks=0,
            className='me-1',
            size='lg',
           style={'marginTop': '20px'},
        ),
    ], width=1, style={'marginLeft': '20px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),


    html.Div([
            html.Span(id='age_sex_label'),
    ], style={'color': 'red', 'marginLeft': '10px'}),


    html.Br(),


], style={'backgroundColor': '#eeeff3', 'color': 'navy', 'fontSize': '20px', 'paddingBottom': '10px'}),

html.Hr(),

html.H3('Age and Sex Profile of District', style={'color': 'navy', 'marginLeft': '18px'}),

dbc.Row([
    dbc.Col([
        dbc.CardBody([
            html.H5('Total, All', style={'color': 'white'}),
                     html.H5(id='age_sex_total',
                               style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
        ]),

    ], width=2, style={'marginLeft': '0px'}),

    dbc.Col([
        dbc.CardBody([
            html.H5('Male, Urban', style={'color': 'white'}),
                     html.H5(id='age_sex_male_urban',
                               style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
        ])
    ], width=2, style={'marginLeft': '120px'}),

    dbc.Col([
        dbc.CardBody([
            html.H5('Female, Urban', style={'color': 'white'}),
                 html.H5(id='age_sex_female_urban',
                           style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
        ])
    ], width=2, style={'marginLeft': '100px'}),

], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),

# Data Values - Row #1
dbc.Row([
    dbc.Col([
        dbc.CardBody(
            html.H5('', style={'color': 'white'}),
        ),

    ], width=2, style={'marginLeft': '0px'}),

    dbc.Col([
        dbc.CardBody([
            html.H5('Male, Rural', style={'color': 'white'}),
            html.H5(id='age_sex_male_rural',
                      style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
        ])
    ], width=2, style={'marginLeft': '120px'}),

    dbc.Col([
        dbc.CardBody([
            html.H5('Female, Rural', style={'color': 'white'}),
            html.H5(id='age_sex_female_rural',
                      style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
        ])
    ], width=2, style={'marginLeft': '100px'}),

], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),


])


def create_age_sex():
    layout = html.Div([
        nav,
        header,
    ])
    return layout

