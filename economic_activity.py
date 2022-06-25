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
    html.H2('ECONOMIC ACTIVITY', style={'color': 'navy', 'margin': '10px', 'backgroundColor': 'white'}),
    dbc.Row([
        # regions
        dbc.Col([
            html.Span('REGION', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='econ_act_region_dd',
                style={'color': 'black'},
                options=[{'label': REGION, 'value': REGION} for REGION in REGIONS]
            ),
        ], width=2, style={'marginLeft': '20px', 'marginTop': '5px', 'marginBottom': '5px'}),

        html.Br(),

        dbc.Col([
            html.Span('DISTRICT', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='econ_act_district_dd',
                style={'color': 'black'},
            ),
        ], width=2, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px'}),

        dbc.Col([
            dbc.Button('SEARCH',
                id='econ_act_search_btn',
                n_clicks=0,
                className='me-1',
                size='lg',
               style={'marginTop': '20px'},
            ),
        ], width=1, style={'width':'6%','marginLeft': '40px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

        dbc.Col([
            dbc.Button('CLEAR',
                id='econ_act_clear_all',
                n_clicks=0,
                className='me-1',
                size='lg',
               style={'marginTop': '20px'},
            ),
        ], width=1, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

        html.Br(),

    ], style={'backgroundColor': '#eeeff3', 'color': 'navy', 'fontSize': '20px', 'paddingBottom': '10px'}),

    html.Hr(),

    html.H3(' Population 15 years and older by economic activity status, sex and district ',
            style={'color': 'navy', 'marginLeft': '18px'}),
    dbc.Row([
        dbc.Row([
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("BOTH SEXES", color="", text_color='white', className="col-12 btn btn-primary",
                              style={'fontSize': '16px', 'margin-left': '0px'}),
                ]),
            ], width=4, style={'marginLeft': '0px'}),
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("MALE", color='', text_color='white', className='col-12 btn btn-primary', style={'fontSize': '16px'}),
                ]),
            ], width=4, style={'marginLeft': '0px'}),
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("FEMALE", color="", text_color='white', className="col-12 btn btn-primary", style={'fontSize': '16px'}),
                ]),
            ], width=4, style={'marginLeft': '0px'}),
        ], style={'backgroundColor': 'navy', 'marginBottom': '15px'}),


        #ALL
        dbc.Col([
            html.Table([

                html.Tr([

                ]),
                html.Tr([
                    html.Td(html.Span('-')),
                    html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(html.Span('-')),
                    html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                ]),

                #Total
                html.Tr([
                    html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='econ_act_reg_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='econ_act_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                #Labor Force
                html.Tr([
                    html.Td(html.Span('Labor Force: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='econ_act_labor_fx_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_labor_fx_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='econ_act_labor_fx_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_labor_fx_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                #Employed
                html.Tr([
                    html.Td(html.Span('Employed: ',
                                      style={'color': 'white', 'fontWeight': 'normal', 'font-style': 'italic'})),
                    html.Td(
                        [html.Span(id='econ_act_employ_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_employ_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='econ_act_employ_all_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_employ_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Unemployed
                html.Tr([
                    html.Td(html.Span('Unemployed: ',
                                      style={'color': 'white', 'fontWeight': 'normal', 'font-style': 'italic'})),
                    html.Td(
                        [html.Span(id='econ_act_unemploy_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_unemploy_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='econ_act_unemploy_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_unemploy_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Population outside labour force
                html.Tr([
                    html.Td(html.Span('Population Outside Labor: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='econ_act_pop_outs_labor_fx_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='econ_act_pop_outs_labor_fx_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='econ_act_pop_outs_labor_fx_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='econ_act_pop_outs_labor_fx_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '500px'})
        ], width=4),

        # MALE
        dbc.Col([
            html.Table([

                html.Tr([

                ]),
                html.Tr([
                    html.Td(html.Span('-')),
                    html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(html.Span('-')),
                    html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                ]),

                # Total
                html.Tr([
                    html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='econ_act_reg_male_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_reg_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='econ_act_male_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # Labor Force
                html.Tr([
                    html.Td(html.Span('Labor Force: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='econ_act_labor_fx_reg_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_labor_fx_reg_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='econ_act_labor_fx_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_labor_fx_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Employed
                html.Tr([
                    html.Td(html.Span('Employed: ',
                                      style={'color': 'white', 'fontWeight': 'normal', 'font-style': 'italic'})),
                    html.Td(
                        [html.Span(id='econ_act_employ_reg_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_employ_reg_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='econ_act_employ_male_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_employ_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Unemployed
                html.Tr([
                    html.Td(html.Span('Unemployed: ',
                                      style={'color': 'white', 'fontWeight': 'normal', 'font-style': 'italic'})),
                    html.Td(
                        [html.Span(id='econ_act_unemploy_reg_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_unemploy_reg_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='econ_act_unemploy_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_unemploy_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Population outside labor
                html.Tr([
                    html.Td(html.Span('Population Outside Labor: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='econ_act_pop_outs_labor_fx_reg_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='econ_act_pop_outs_labor_fx_reg_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='econ_act_pop_outs_labor_fx_male_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='econ_act_pop_outs_labor_fx_male_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '500px'})
        ], width=4),


        # FEMALE
        dbc.Col([
            html.Table([

                html.Tr([

                ]),
                html.Tr([
                    html.Td(html.Span('-')),
                    html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(html.Span('-')),
                    html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                ]),

                # Total
                html.Tr([
                    html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='econ_act_reg_female_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_reg_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='econ_act_female_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # Labor Force
                html.Tr([
                    html.Td(html.Span('Labor Force: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='econ_act_labor_fx_reg_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_labor_fx_reg_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='econ_act_labor_fx_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_labor_fx_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Employed
                html.Tr([
                    html.Td(html.Span('Employed: ',
                                      style={'color': 'white', 'fontWeight': 'normal', 'font-style': 'italic'})),
                    html.Td(
                        [html.Span(id='econ_act_employ_reg_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_employ_reg_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='econ_act_employ_female_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_employ_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Unemployed
                html.Tr([
                    html.Td(html.Span('Unemployed: ',
                                      style={'color': 'white', 'fontWeight': 'normal', 'font-style': 'italic'})),
                    html.Td(
                        [html.Span(id='econ_act_unemploy_reg_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_unemploy_reg_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='econ_act_unemploy_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='econ_act_unemploy_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Population outside labor
                html.Tr([
                    html.Td(html.Span('Population Outside Labor: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='econ_act_pop_outs_labor_fx_reg_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='econ_act_pop_outs_labor_fx_reg_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='econ_act_pop_outs_labor_fx_female_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='econ_act_pop_outs_labor_fx_female_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '500px'})
        ], width=4),

    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'})
])

def create_economic_activity():
    layout = html.Div([
        nav,
        header
    ])

    return layout