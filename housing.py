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

html.H2('HOUSING - Stock of Residential Structures, Households by Region & Types of Locality', style={'color': 'navy', 'margin': '15px', 'backgroundColor': 'white'}),

    dbc.Row([
        # regions
        dbc.Col([
            html.Span('REGION', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='housing_region_dd',
                style={'color': 'black'},

                options=[{'label': REGION, 'value': REGION} for REGION in REGIONS]
            ),
        ], width=2, style={'marginLeft': '20px', 'marginTop': '10px', 'marginBottom': '5px'}),

        html.Br(),

        dbc.Col([
            html.Span('DISTRICT', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='housing_district_dd',
                style={'color': 'black'},
            ),
        ], width=2, style={'marginLeft': '0px', 'marginTop': '10px', 'marginBottom': '5px'}),

        html.Br(),

        dbc.Col([
            dbc.Button('SEARCH',
                id='housing_search_btn',
                n_clicks=0,
                className='me-1',
                size='lg',
               style={'marginTop': '20px'},
            ),
        ], width=1, style={'width':'6%', 'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

        dbc.Col([
            dbc.Button('CLEAR',
                id='housing_clear_btn',
                n_clicks=0,
                className='me-1',
                size='lg',
               style={'marginTop': '20px'},
            ),
        ], width=1, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

    ], style={'backgroundColor': '#eeeff3', 'color': 'navy', 'fontSize': '18px', 'paddingBottom': '10px'}),

    html.Hr(),

    html.H3('REGIONAL - Summary Statistics', style={'color': 'navy', 'marginLeft': '18px'}),

    # Data - REGIONAL
    dbc.Row([
        dbc.Col([
            dbc.CardBody([
                html.H5('Population', style={'color': 'white', 'fontSize': '18px'}),
                html.H5(id='housing_tot_pop', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ]),

        ], width=2, style={'marginLeft': '0px'}),

        dbc.Col([
            dbc.CardBody([
                html.H5('Total Household Population', style={'color': 'white', 'fontSize': '18px'}),
                html.H5(id='housing_tot_hh_pop',
                        style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '30px'}),

        dbc.Col([
            dbc.CardBody([
                html.H5('No. of Households', style={'color': 'white', 'fontSize': '18px'}),
                html.H5(id='housing_tot_hh',
                        style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '30px'}),

        dbc.Col([
            dbc.CardBody([
                html.H5('Average Household Size', style={'color': 'white', 'fontSize': '18px'}),
                html.H5(id='housing_avg_hh_size',
                        style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '0px'}),



    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),

    html.Hr(),

    html.H3('DISTRICT - Residential Structures', style={'color': 'navy', 'marginLeft': '18px'}),

    # Residential structures
    dbc.Row([
        dbc.Col([
            dbc.CardBody([
                html.H5('Total', style={'color': 'white', 'fontSize': '18px'}),
                html.H5(id='housing_tot_resi_struct',
                        style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '0px'}),

        dbc.Col([
            dbc.CardBody([
                html.H5('Urban', style={'color': 'white', 'fontSize': '18px'}),
                html.H5(id='housing_tot_resi_struct_urban',
                        style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '0px'}),

        dbc.Col([
            dbc.CardBody([
                html.H5('Rural', style={'color': 'white', 'fontSize': '18px'}),
                html.H5(id='housing_tot_resi_struct_rural',
                        style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '0px'}),

        dbc.Col([
            dbc.CardBody([
                html.H5('Urban Share', style={'color': 'white', 'fontSize': '18px'}),
                html.H5(id='housing_resi_struct_urban_share',
                        style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '0px'}),

        dbc.Col([
            dbc.CardBody([
                html.H5('Percent Distribution', style={'color': 'white', 'fontSize': '18px'}),
                html.H5(id='housing_resi_distrib_percent',
                        style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
            ])
        ], width=2, style={'marginLeft': '0px'}),

    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),

])

def create_housing():
    layout = html.Div([
        nav,
        header
    ])

    return layout