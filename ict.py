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
    html.H2('INFORMATION & COMMUNICATION TECHNOLOGY', style={'color': 'navy', 'margin': '10px', 'backgroundColor': 'white'}),
    dbc.Row([
        # regions
        dbc.Col([
            html.Span('REGION', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='ict_region_dd',
                style={'color': 'black'},
                options=[{'label': REGION, 'value': REGION} for REGION in REGIONS]
            ),
        ], width=2, style={'marginLeft': '20px', 'marginTop': '5px', 'marginBottom': '5px'}),

        html.Br(),

        dbc.Col([
            html.Span('DISTRICT', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='ict_district_dd',
                style={'color': 'black'},
            ),
        ], width=2, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px'}),

        dbc.Col([
            dbc.Button('SEARCH',
                id='ict_search_btn',
                n_clicks=0,
                className='me-1',
                size='lg',
               style={'marginTop': '20px'},
            ),
        ], width=1, style={'width':'6%','marginLeft': '40px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

        dbc.Col([
            dbc.Button('CLEAR',
                id='ict_clear_all',
                n_clicks=0,
                className='me-1',
                size='lg',
               style={'marginTop': '20px'},
            ),
        ], width=1, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

        html.Br(),

    ], style={'backgroundColor': '#eeeff3', 'color': 'navy', 'fontSize': '20px', 'paddingBottom': '10px'}),

    html.Hr(),

    html.H3('Population 6 years and older by Ownership of Functional ICT Devices, Sex, Type of Locality and District',
            style={'color': 'navy', 'marginLeft': '18px'}),

    dbc.Row([
        dbc.Row([
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("ALL LOCALITIES", color="", text_color='white', className="col-12 btn btn-primary",
                              style={'fontSize': '16px', 'margin-left': '0px'}),
                ]),
            ], width=4, style={'marginLeft': '0px'}),
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("URBAN", color='', text_color='white', className='col-12 btn btn-primary',
                              style={'fontSize': '16px'}),
                ]),
            ], width=4, style={'marginLeft': '0px'}),
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("RURAL", color="", text_color='white', className="col-12 btn btn-primary",
                              style={'fontSize': '16px'}),
                ]),
            ], width=4, style={'marginLeft': '0px'}),
        ], style={'backgroundColor': 'navy', 'marginBottom': '15px'}),

        # ALL, BOTH
        dbc.Col([
            dbc.Row([
                html.H3('BOTH SEXES', style={'color': '#FFC300', 'fontWeight': 'bold', 'margin-left': '10px'})
            ]),
            html.Table([

                html.Tr([

                ]),
                html.Tr([
                    html.Td(html.Span('-')),
                    html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(html.Span('-')),
                    html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                ]),

                # both sexes - total
                html.Tr([
                    html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='ict_reg_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # mobile phone (smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Smart): ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Mobile Phone (non-smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Non-smart): ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_non_smart_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='ict_mob_phone_non_smart_all_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Tablet
                html.Tr([
                    html.Td(html.Span('Tablet: ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_tablet_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_tablet_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Laptop
                html.Tr([
                    html.Td(html.Span('Laptop: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_laptop_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_laptop_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # None
                html.Tr([
                    html.Td(html.Span('None: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_none_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_none_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '500px'}),



            # #ALL, MALES
            dbc.Row([
                html.H3('MALES', style={'color': '#FFC300', 'fontWeight': 'bold', 'margin-left': '10px'})
            ]),
            html.Table([

                html.Tr([

                ]),
                html.Tr([
                    html.Td(html.Span('-')),
                    html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(html.Span('-')),
                    html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                ]),

                # all - males
                html.Tr([
                    html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='ict_reg_all_male_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_reg_all_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_all_male_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_all_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # mobile phone (smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Smart): ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_reg_all_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_reg_all_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_all_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_all_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Mobile Phone (non-smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Non-smart): ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_non_smart_reg_all_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_reg_all_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='ict_mob_phone_non_smart_all_male_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_all_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Tablet
                html.Tr([
                    html.Td(html.Span('Tablet: ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_tablet_reg_all_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_reg_all_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_tablet_all_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_all_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Laptop
                html.Tr([
                    html.Td(html.Span('Laptop: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_laptop_reg_all_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_reg_all_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_laptop_all_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_all_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # None
                html.Tr([
                    html.Td(html.Span('None: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_none_reg_all_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_reg_all_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_none_all_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_all_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '500px'}),



            # #ALL, FEMALES
            dbc.Row([
                html.H3('FEMALES', style={'color': '#FFC300', 'fontWeight': 'bold', 'margin-left': '10px'})
            ]),
            html.Table([

                html.Tr([

                ]),
                html.Tr([
                    html.Td(html.Span('-')),
                    html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(html.Span('-')),
                    html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                ]),

                # all - males
                html.Tr([
                    html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='ict_reg_all_female_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_reg_all_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_all_female_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_all_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # mobile phone (smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Smart): ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_reg_all_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_reg_all_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_all_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_all_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Mobile Phone (non-smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Non-smart): ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_non_smart_reg_all_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_reg_all_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='ict_mob_phone_non_smart_all_female_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_all_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Tablet
                html.Tr([
                    html.Td(html.Span('Tablet: ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_tablet_reg_all_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_reg_all_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_tablet_all_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_all_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Laptop
                html.Tr([
                    html.Td(html.Span('Laptop: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_laptop_reg_all_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_reg_all_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_laptop_all_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_all_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # None
                html.Tr([
                    html.Td(html.Span('None: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_none_reg_all_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_reg_all_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_none_all_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_all_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '500px'}),
        ], width=4),

        #********************
        # URBAN, BOTH SEXES
        #********************
        dbc.Col([
            html.Table([

                dbc.Row([
                    html.H3('--', style={'color': '#FFC300', 'fontWeight': 'bold', 'margin-left': '10px'})
                ]),
                html.Tr([
                    html.Td(html.Span('-')),
                    html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(html.Span('-')),
                    html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                ]),

                # both sexes - total
                html.Tr([
                    html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='ict_reg_urban_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_reg_urban_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_urban_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_urban_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # mobile phone (smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Smart): ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_reg_urban_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_reg_urban_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_urban_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_urban_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Mobile Phone (non-smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Non-smart): ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_non_smart_reg_urban_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_reg_urban_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='ict_mob_phone_non_smart_urban_all_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_urban_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Tablet
                html.Tr([
                    html.Td(html.Span('Tablet: ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_tablet_reg_urban_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_reg_urban_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_tablet_urban_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_urban_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Laptop
                html.Tr([
                    html.Td(html.Span('Laptop: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_laptop_reg_urban_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_reg_urban_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_laptop_urban_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_urban_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # None
                html.Tr([
                    html.Td(html.Span('None: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_none_reg_urban_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_reg_urban_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_none_urban_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_urban_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '500px'}),


            # URBAN, MALES
            html.Table([

                dbc.Row([
                    html.H3('--', style={'color': '#FFC300', 'fontWeight': 'bold', 'margin-left': '10px'})
                ]),
                html.Tr([
                    html.Td(html.Span('-')),
                    html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(html.Span('-')),
                    html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                ]),

                # both sexes - total
                html.Tr([
                    html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='ict_reg_urban_male_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_reg_urban_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_urban_male_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_urban_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # mobile phone (smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Smart): ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_reg_urban_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_reg_urban_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_urban_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_urban_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Mobile Phone (non-smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Non-smart): ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_non_smart_reg_urban_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_reg_urban_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='ict_mob_phone_non_smart_urban_male_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_urban_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Tablet
                html.Tr([
                    html.Td(html.Span('Tablet: ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_tablet_reg_urban_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_reg_urban_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_tablet_urban_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_urban_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Laptop
                html.Tr([
                    html.Td(html.Span('Laptop: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_laptop_reg_urban_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_reg_urban_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_laptop_urban_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_urban_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # None
                html.Tr([
                    html.Td(html.Span('None: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_none_reg_urban_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_reg_urban_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_none_urban_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_urban_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '500px'}),


            # URBAN, FEMALES
            html.Table([

                dbc.Row([
                    html.H3('--', style={'color': '#FFC300', 'fontWeight': 'bold', 'margin-left': '10px'})
                ]),
                html.Br(),
                html.Tr([
                    html.Td(html.Span('-')),
                    html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(html.Span('-')),
                    html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                ]),

                # both sexes - total
                html.Tr([
                    html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='ict_reg_urban_female_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_reg_urban_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_urban_female_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_urban_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # mobile phone (smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Smart): ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_reg_urban_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_reg_urban_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_urban_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_urban_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Mobile Phone (non-smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Non-smart): ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_non_smart_reg_urban_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_reg_urban_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='ict_mob_phone_non_smart_urban_female_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_urban_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Tablet
                html.Tr([
                    html.Td(html.Span('Tablet: ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_tablet_reg_urban_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_reg_urban_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_tablet_urban_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_urban_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Laptop
                html.Tr([
                    html.Td(html.Span('Laptop: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_laptop_reg_urban_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_reg_urban_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_laptop_urban_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_urban_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # None
                html.Tr([
                    html.Td(html.Span('None: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_none_reg_urban_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_reg_urban_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_none_urban_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_urban_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '500px'}),

        ], width=4),


        # ********************
        # RURAL, BOTH SEXES
        # ********************
        dbc.Col([
            html.Table([

                dbc.Row([
                    html.H3('--', style={'color': '#FFC300', 'fontWeight': 'bold', 'margin-left': '10px'})
                ]),
                html.Tr([
                    html.Td(html.Span('-')),
                    html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(html.Span('-')),
                    html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                ]),

                # both sexes - total
                html.Tr([
                    html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='ict_reg_rural_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_reg_rural_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_rural_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_rural_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # mobile phone (smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Smart): ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_reg_rural_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_reg_rural_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_rural_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_rural_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Mobile Phone (non-smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Non-smart): ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_non_smart_reg_rural_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_reg_rural_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='ict_mob_phone_non_smart_rural_all_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_rural_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Tablet
                html.Tr([
                    html.Td(html.Span('Tablet: ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_tablet_reg_rural_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_reg_rural_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_tablet_rural_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_rural_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Laptop
                html.Tr([
                    html.Td(html.Span('Laptop: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_laptop_reg_rural_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_reg_rural_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_laptop_rural_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_rural_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # None
                html.Tr([
                    html.Td(html.Span('None: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_none_reg_rural_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_reg_rural_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_none_rural_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_rural_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '500px'}),

            #***************
            # RURAL, MALES
            #***************
            html.Table([

                dbc.Row([
                    html.H3('--', style={'color': '#FFC300', 'fontWeight': 'bold', 'margin-left': '10px'})
                ]),
                html.Tr([
                    html.Td(html.Span('-')),
                    html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(html.Span('-')),
                    html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                ]),

                # both sexes - total
                html.Tr([
                    html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='ict_reg_rural_male_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_reg_rural_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_rural_male_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_rural_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # mobile phone (smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Smart): ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_reg_rural_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_reg_rural_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_rural_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_rural_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Mobile Phone (non-smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Non-smart): ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_non_smart_reg_rural_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_reg_rural_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='ict_mob_phone_non_smart_rural_male_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_rural_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Tablet
                html.Tr([
                    html.Td(html.Span('Tablet: ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_tablet_reg_rural_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_reg_rural_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_tablet_rural_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_rural_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Laptop
                html.Tr([
                    html.Td(html.Span('Laptop: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_laptop_reg_rural_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_reg_rural_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_laptop_rural_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_rural_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # None
                html.Tr([
                    html.Td(html.Span('None: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_none_reg_rural_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_reg_rural_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_none_rural_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_rural_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '500px'}),

            #****************
            # RURAL, FEMALES
            #****************
            html.Table([

                dbc.Row([
                    html.H3('--', style={'color': '#FFC300', 'fontWeight': 'bold', 'margin-left': '10px'})
                ]),
                html.Br(),
                html.Tr([
                    html.Td(html.Span('-')),
                    html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(html.Span('-')),
                    html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                ]),

                # both sexes - total
                html.Tr([
                    html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='ict_reg_rural_female_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_reg_rural_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_rural_female_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_rural_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # mobile phone (smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Smart): ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_reg_rural_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_reg_rural_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='ict_mob_phone_smart_rural_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_smart_rural_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Mobile Phone (non-smart)
                html.Tr([
                    html.Td(html.Span('Mobile Phone (Non-smart): ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_mob_phone_non_smart_reg_rural_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_reg_rural_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='ict_mob_phone_non_smart_rural_female_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_mob_phone_non_smart_rural_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Tablet
                html.Tr([
                    html.Td(html.Span('Tablet: ',
                                      style={'color': 'white', 'fontWeight': 'bold', 'font-style': 'normal'})),
                    html.Td(
                        [html.Span(id='ict_tablet_reg_rural_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_reg_rural_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_tablet_rural_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='ict_tablet_rural_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Laptop
                html.Tr([
                    html.Td(html.Span('Laptop: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_laptop_reg_rural_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_reg_rural_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_laptop_rural_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_laptop_rural_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # None
                html.Tr([
                    html.Td(html.Span('None: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='ict_none_reg_rural_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_reg_rural_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='ict_none_rural_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='ict_none_rural_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '500px'}),

        ], width=4),

    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'})

])

def create_ict():
    layout = html.Div([
        nav,
        header
    ])

    return layout