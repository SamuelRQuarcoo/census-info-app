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
            html.H2('POPULATIONS OF REGIONS & DISTRICTS - by Sex, Type of Residence and Type of Locality.', style={'color': 'navy', 'margin': '15px', 'backgroundColor': 'white'}),
            dbc.Row([

                # regions
                dbc.Col([
                    html.Span('REGION', style={'fontWeight': 'bold'}),
                    dcc.Dropdown(
                        id='pop_reg_dist_region_dd',
                        style={'color': 'black'},

                        options=[{'label': REGION, 'value': REGION} for REGION in REGIONS]
                    ),
                ], width=2, style={'marginLeft': '20px', 'marginTop': '10px', 'marginBottom': '5px'}),

                html.Br(),

                dbc.Col([
                    html.Span('DISTRICT', style={'fontWeight': 'bold'}),
                    dcc.Dropdown(
                        id='pop_reg_dist_district_dd',
                        style={'color': 'black'},
                    ),
                ], width=2, style={'marginLeft': '0px', 'marginTop': '10px', 'marginBottom': '5px'}),

                html.Br(),

                dbc.Col([
                    dbc.Button('SEARCH',
                        id='pop_dist_search_btn',
                        n_clicks=0,
                        className='me-1',
                        size='lg',
                       style={'marginTop': '20px'},
                    ),
                ], width=1, style={'width':'6%', 'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

                dbc.Col([
                    dbc.Button('CLEAR',
                        id='pop_dist_clear_btn',
                        n_clicks=0,
                        className='me-1',
                        size='lg',
                       style={'marginTop': '20px'},
                    ),
                ], width=1, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

            ], style={'backgroundColor': '#eeeff3', 'color': 'navy', 'fontSize': '18px', 'paddingBottom': '10px'}),

            html.Hr(),

            html.H3('General Statistics of Region', style={'color': 'navy', 'marginLeft': '18px'}),

            dbc.Row([
                dbc.Col([
                    dbc.CardBody([
                        html.H5('Population', style={'color': 'white', 'fontSize': '18px'}),
                        html.H5(id='total_all', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                    ]),

                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Percentage', style={'color': 'white', 'fontSize': '18px'}),
                        html.H5(id='total_percent',
                                style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'}),
                    ])
                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Males', style={'color': 'white', 'fontSize': '18px'}),
                        html.Div([
                            html.Span(id='total_male',
                                      style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'}),
                            dbc.Badge(
                                      id='total_male_percent',
                                      color="#1b5e20",
                                      pill=False,
                                      text_color="white",
                                      className='',
                                      style={'margin-top': '4px', 'margin-left': '10px'}
                                      ),
                        ]),
                    ])
                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Females', style={'color': 'white', 'fontSize': '18px'}),
                        html.Div([
                            html.Span(id='total_female',
                                style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'}),
                            dbc.Badge(
                                id='total_female_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '0px'}
                            ),
                        ]),
                    ])
                ], width=2, style={'marginLeft': '0px'}),

            ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),

            html.Br(),

            dbc.Row([

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Urban, All', style={'color': 'white', 'fontSize': '18px'}),
                        html.Div([
                            html.Span(id='urban_all_total',
                                      style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'}),
                        ]),
                    ])
                ], width=1, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Male, Urban', style={'color': 'white', 'fontSize': '18px'}),
                        html.Div([
                            html.Span(id='total_male_urban',
                                      style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'}),
                        ]),
                    ])
                ], width=1, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Female, Urban', style={'color': 'white', 'fontSize': '18px'}),
                        html.Div([
                            html.Span(id='total_female_urban',
                                      style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'}),
                        ]),
                    ])
                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Rural, All', style={'color': 'white', 'fontSize': '18px'}),
                        html.Div([
                            html.Span(id='rural_all_total',
                                      style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'}),
                        ]),
                    ])
                ], width=1, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Males, Rural', style={'color': 'white', 'fontSize': '18px'}),
                        html.Div([
                            html.Span(id='total_male_rural',
                                      style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'}),
                        ]),
                    ])
                ], width=1, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Female, Rural', style={'color': 'white', 'fontSize': '18px'}),
                        html.Div([
                            html.Span(id='total_female_rural',
                                      style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'}),
                        ]),
                    ])
                ], width=1, style={'marginLeft': '0px'}),

            ], style={'background-color': 'navy', 'marginLeft': '0px'}),

            html.Br(),

            #characteristics of region
            dbc.Row([

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Area (km2)', style={'color': 'white', 'fontSize': '18px'}),
                        html.H5(id='reg_area_km_2',
                                  style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                    ])
                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Population Density (pers/km2):', style={'color': 'white', 'fontSize': '18px'}),
                                 html.H5(id='reg_pop_density',
                                           style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                    ])
                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('No. of Households:', style={'color': 'white', 'fontSize': '18px'}),
                                 dbc.Label(id='reg_no_of_hh',
                                           style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                    ])

                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Average Household Size:', style={'color': 'white', 'fontSize': '18px'}),
                                 html.H5(id='reg_avg_hh_size',
                                           style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                    ])
                ], width=2, style={'marginLeft': '0px'}),

            ], style={'background-color': 'navy', 'marginLeft': '0px'}),


            #District details

            html.Hr(),

            html.H3('District Population By Sex and Locality', style={'color': 'navy', 'marginLeft': '18px'}),

            dbc.Row([

                dbc.Row([
                    dbc.Col([
                        dbc.CardBody([
                                html.H5('Total, All', style={'color': 'white', 'fontSize': '18px'}),
                                         html.H5(id='total_dist_all', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                        ]),

                    ], width=2, style={'marginLeft': '0px'}),

                    dbc.Col([
                        dbc.CardBody([
                            html.H5('Male, All', style={'color': 'white', 'fontSize': '18px'}),
                                     html.H5(id='male_dist_all',
                                               style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                        ])
                    ], width=2, style={'marginLeft': '0px'}),

                    dbc.Col([
                        dbc.CardBody([
                            html.H5('Urban, All', style={'color': 'white', 'fontSize': '18px'}),
                                     html.H5(id='urban_dist_all',
                                               style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                        ])
                    ], width=2, style={'marginLeft': '0px'}),

                    dbc.Col([
                        dbc.CardBody([
                            html.H5('Male, Urban', style={'color': 'white', 'fontSize': '18px'}),
                                     html.H5(id='urban_dist_male',
                                               style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                        ])
                    ], width=2, style={'marginLeft': '0px'}),

                    dbc.Col([
                        dbc.CardBody([
                            html.H5('Male, Rural', style={'color': 'white', 'fontSize': '18px'}),
                                    html.H5(id='rural_dist_male',
                                               style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                        ])
                    ], width=2, style={'marginLeft': '0px'}),

                ]),

            ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),

            # Data Values - Row #1
            dbc.Row([

                dbc.Col([
                    dbc.CardBody([
                        html.H5('-', style={'color': 'white', 'fontSize': '18px'}),

                    ])
                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Female, All', style={'color': 'white', 'fontSize': '18px'}),
                        html.H5(id='female_dist_all',
                               style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                    ])
                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                        dbc.CardBody([
                            html.H5('Rural, All', style={'color': 'white', 'fontSize': '18px'}),
                            html.H5(id='rural_dist_all',
                                    style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                        ])
                    ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Female, Urban', style={'color': 'white', 'fontSize': '18px'}),
                        html.H5(id='urban_dist_female',
                                style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                    ])
                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Female, Rural', style={'color': 'white', 'fontSize': '18px'}),
                        html.H5(id='rural_dist_female',
                                  style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                    ])
                ], width=2, style={'marginLeft': '0px'}),

            ], style={'backgroundColor': 'navy', 'marginBottom': '2px'}),

            html.Hr(),

            #GENERAL STATISTICS OF DISTRICTS
            html.H3('General Statistics of District', style={'color': 'navy', 'marginLeft': '18px'}),

            dbc.Row([

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Area (km2)', style={'color': 'white', 'fontSize': '18px'}),
                        html.H5(id='area_km_2',
                                  style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                    ])
                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Population Density (pers/km2):', style={'color': 'white', 'fontSize': '18px'}),
                                 html.H5(id='pop_density',
                                           style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                    ])
                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('No. of Households:', style={'color': 'white', 'fontSize': '18px'}),
                                 dbc.Label(id='no_of_hh',
                                           style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                    ])

                ], width=2, style={'marginLeft': '0px'}),

                dbc.Col([
                    dbc.CardBody([
                        html.H5('Average Household Size:', style={'color': 'white', 'fontSize': '18px'}),
                                 html.H5(id='avg_hh_size',
                                           style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px'})
                    ])
                ], width=2, style={'marginLeft': '0px'}),

            ], style={'background-color': 'navy', 'marginLeft': '0px'}),
])

def create_region_district():
    layout = html.Div([
        nav,
        header
    ])

    return layout

