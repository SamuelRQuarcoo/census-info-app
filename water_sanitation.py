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

    html.H2('WATER & SANITATION', style={'color': 'navy', 'margin': '15px', 'backgroundColor': 'white'}),

    dbc.Row([
            # regions
            dbc.Col([
                html.Span('REGION', style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='ws_region_dd',
                    style={'color': 'black'},

                    options=[{'label': REGION, 'value': REGION} for REGION in REGIONS]
                ),
            ], width=2, style={'marginLeft': '20px', 'marginTop': '10px', 'marginBottom': '5px'}),

            html.Br(),

            dbc.Col([
                html.Span('DISTRICT', style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='ws_district_dd',
                    style={'color': 'black'},
                ),
            ], width=2, style={'marginLeft': '0px', 'marginTop': '10px', 'marginBottom': '5px'}),

            html.Br(),

            dbc.Col([
                dbc.Button('SEARCH',
                    id='water_sanit_search_btn',
                    n_clicks=0,
                    className='me-1',
                    size='lg',
                   style={'marginTop': '20px'},
                ),
            ], width=1, style={'width':'6%', 'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

            dbc.Col([
                dbc.Button('CLEAR',
                    id='water_sanit_clear_btn',
                    n_clicks=0,
                    className='me-1',
                    size='lg',
                   style={'marginTop': '20px'},
                ),
            ], width=1, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

    ], style={'backgroundColor': '#eeeff3', 'color': 'navy', 'fontSize': '18px', 'paddingBottom': '10px'}),

    html.Hr(),

    html.H3('Main Source of Drinking  Water by Type of Locality and District', style={'color': 'navy', 'marginLeft': '18px'}),

        dbc.Row([

            #summary statistics
            dbc.Col([
                dbc.CardBody([
                    html.Table([
                        html.Tr([
                            html.H3('ALL WATER SOURCES', className='btn btn-primary', style={'fontWeight': 'bold', 'fontSize': '16px', 'marginLeft': '0px'}),
                        ]),

                        html.Tr([
                            html.Td([
                                html.Span('Total Water Sources: ', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px',
                                                 'marginLeft': '0px'}),
                            ]),
                            html.Td([
                                html.Span(id='ws_reg_total',
                                          style={'color': '#eca50b', 'fontWeight': 'bold',
                                                 'fontSize': '16px', 'float': 'right'}),
                            ]),
                            html.Td([
                                dbc.Badge(
                                  id='ws_reg_percent',
                                  color="#1b5e20",
                                  pill=False,
                                  text_color="white",
                                  className='',
                                  style={'float': 'right', 'margin-top': '4px', 'margin-left': '10px'}
                                ),
                            ]),
                        ]),

                        #total improved water sources
                        html.Tr([
                            html.Td([
                                html.Span('Improved Water Sources: ', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px',
                                                 'marginLeft': '0px'}),
                            ]),
                            html.Td([
                                html.Span(id='ws_impr_water_src_all_total',
                                          style={'color': '#eca50b', 'fontWeight': 'bold',
                                                 'fontSize': '16px',
                                                 'float': 'right'}),
                            ]),

                            #percent improved water sources
                            html.Td([
                                dbc.Badge(
                                  id='ws_impr_water_src_all_percent',
                                  color="#1b5e20",
                                  pill=False,
                                  text_color="white",
                                  className='',
                                  style={'float': 'right', 'margin-top': '4px', 'margin-left': '10px'}
                                ),
                            ]),
                        ]),

                    #total unimproved water sources - urban
                        html.Tr([
                            html.Td([
                                html.Span('Unimproved Water Sources: ', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px',
                                                 'marginLeft': '0px'}),
                            ]),

                            html.Td([
                                html.Span(id='ws_unimpr_water_src_all_total',
                                          style={'color': '#eca50b', 'fontWeight': 'bold',
                                                 'fontSize': '16px',
                                                 'float': 'right'}),
                            ]),

                            #percent unimproved water sources - urban
                            html.Td([
                                dbc.Badge(
                                  id='ws_unimpr_water_src_all_percent',
                                  color="#1b5e20",
                                  pill=False,
                                  text_color="white",
                                  className='',
                                  style={'float': 'right', 'margin-top': '4px', 'margin-left': '10px'}
                                ),
                            ]),
                        ]),

                    ], style={'width': '350px'}),

                ])
            ], width=3, style={'marginLeft': '0px'}),

            #URBAN
            dbc.Col([
                dbc.CardBody([
                    html.Table([
                        html.Tr([
                            html.H3('URBAN', className='btn btn-primary', style={'fontWeight': 'bold', 'fontSize': '16px', 'marginLeft': '0px'}),
                        ]),

                        html.Tr([
                            html.Td([
                                html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px',
                                                 'marginLeft': '0px'}),
                            ]),
                            html.Td([
                                html.Span(id='ws_reg_total_urban',
                                          style={'color': '#eca50b', 'fontWeight': 'bold',
                                                 'fontSize': '16px', 'float': 'right'}),
                            ]),
                            html.Td([
                                dbc.Badge(
                                  id='ws_reg_urban_percent',
                                  color="#1b5e20",
                                  pill=False,
                                  text_color="white",
                                  className='',
                                  style={'float': 'right', 'margin-top': '4px', 'margin-left': '10px'}
                                ),
                            ]),
                        ]),

                        #total improved water sources - urban
                        html.Tr([
                            html.Td([
                                html.Span('Improved Water Sources: ', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px',
                                                 'marginLeft': '0px'}),
                            ]),
                            html.Td([
                                html.Span(id='ws_impr_water_src_urban',
                                          style={'color': '#eca50b', 'fontWeight': 'bold',
                                                 'fontSize': '16px',
                                                 'float': 'right'}),
                            ]),

                            #percent improved water sources - urban
                            html.Td([
                                dbc.Badge(
                                  id='ws_impr_water_src_urban_percent',
                                  color="#1b5e20",
                                  pill=False,
                                  text_color="white",
                                  className='',
                                  style={'float': 'right', 'margin-top': '4px', 'margin-left': '0px'}
                                ),
                            ]),
                        ]),

                        #total unimproved water sources - urban
                        html.Tr([
                            html.Td([
                                html.Span('Unimproved Water Sources: ', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px',
                                                 'marginLeft': '0px'}),
                            ]),
                            html.Td([
                                html.Span(id='ws_unimpr_water_src_urban',
                                          style={'color': '#eca50b', 'fontWeight': 'bold',
                                                 'fontSize': '16px',
                                                 'float': 'right'}),
                            ]),

                            #percent improved water sources - urban
                            html.Td([
                                dbc.Badge(
                                  id='ws_unimpr_water_src_urban_percent',
                                  color="#1b5e20",
                                  pill=False,
                                  text_color="white",
                                  className='',
                                  style={'float': 'right', 'margin-top': '4px', 'margin-left': '0px'}
                                ),
                            ]),
                        ]),
                    ], style={'width': '350px'}),

                ]),
            ], width=3, style={'marginLeft': '100px'}),

            #RURAL
            dbc.Col([
                dbc.CardBody([
                    html.Table([
                        html.Tr([
                            html.H3('RURAL', className='btn btn-primary',
                                    style={'fontWeight': 'bold', 'fontSize': '16px', 'marginLeft': '0px'}),
                        ]),

                        html.Tr([
                            html.Td([
                                html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px',
                                                            'marginLeft': '0px'}),
                            ]),
                            html.Td([
                                html.Span(id='ws_reg_total_rural',
                                          style={'color': '#eca50b', 'fontWeight': 'bold',
                                                 'fontSize': '16px', 'float': 'right'}),
                            ]),
                            html.Td([
                                dbc.Badge(
                                    id='ws_reg_rural_percent',
                                    color="#1b5e20",
                                    pill=False,
                                    text_color="white",
                                    className='',
                                    style={'float': 'right', 'margin-top': '4px', 'margin-left': '10px'}
                                ),
                            ]),
                        ]),

                        # total improved water sources - urban
                        html.Tr([
                            html.Td([
                                html.Span('Improved Water Sources: ',
                                          style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px',
                                                 'marginLeft': '0px'}),
                            ]),
                            html.Td([
                                html.Span(id='ws_impr_water_src_rural',
                                          style={'color': '#eca50b', 'fontWeight': 'bold',
                                                 'fontSize': '16px',
                                                 'float': 'right'}),
                            ]),

                            # percent improved water sources - urban
                            html.Td([
                                dbc.Badge(
                                    id='ws_impr_water_src_rural_percent',
                                    color="#1b5e20",
                                    pill=False,
                                    text_color="white",
                                    className='',
                                    style={'float': 'right', 'margin-top': '4px', 'margin-left': '0px'}
                                ),
                            ]),
                        ]),

                        # total unimproved water sources - urban
                        html.Tr([
                            html.Td([
                                html.Span('Unimproved Water Sources: ',
                                          style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px',
                                                 'marginLeft': '0px'}),
                            ]),
                            html.Td([
                                html.Span(id='ws_unimpr_water_src_rural',
                                          style={'color': '#eca50b', 'fontWeight': 'bold',
                                                 'fontSize': '16px',
                                                 'float': 'right'}),
                            ]),

                            # percent improved water sources - urban
                            html.Td([
                                dbc.Badge(
                                    id='ws_unimpr_water_src_rural_percent',
                                    color="#1b5e20",
                                    pill=False,
                                    text_color="white",
                                    className='',
                                    style={'float': 'right', 'margin-top': '4px', 'margin-left': '0px'}
                                ),
                            ]),
                        ]),
                    ], style={'width': '350px'}),

                ]),
            ], width=3, style={'marginLeft': '100px'}),
        ], style={'backgroundColor': 'navy', 'margin-bottom': '0px'}),

    html.H3('Sources of Drnking Water', style={'color': 'navy', 'marginLeft': '18px', 'margin': '10px'}),

    #DISTRICT DATA SUMMARY
    #Improved Water Sources
    dbc.Row([

        #header
        dbc.Row([
            dbc.Col([
                dbc.CardBody([
                    html.H3('IMPROVED WATER SOURCES, ALL LOCALITIES', className='col-12 btn btn-primary',  style={'fontWeight': 'bold', 'fontSize': '16px', 'marginLeft': '18px'}),
                ]),
            ], width=6),

            dbc.Col([
                dbc.CardBody([
                    html.H3('UNIMPROVED WATER SOURCES, ALL LOCALITIES', className='col-12 btn btn-primary',  style={'fontWeight': 'bold', 'fontSize': '16px', 'marginLeft': '18px'}),
                ]),
            ], width=6),
        ]),

        #data
        dbc.Row([

            # improved water sources
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
                    html.Tr([
                        html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_impr_water_src_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px',
                                              'margin-top': '4px', 'margin-left': '0px'}),
                             ]),

                        # percent unimproved water sources - rural
                        html.Td([
                            dbc.Badge(
                              id='ws_impr_water_src_reg_all_percent',
                              color="#1b5e20",
                              pill=False,
                              text_color="white",
                              className='',
                              style={'margin-top': '4px', 'margin-left': '0px'}
                              ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_impr_water_src_dist_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px',
                                              'margin-top': '4px', 'margin-left': '20px'}),
                        ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_impr_water_src_dist_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '0px'}
                            ),
                        ], style={'text-align': 'center'}),

                    ]),

                    html.Tr([
                        html.Td(html.Span('Pipe-borne inside dwelling: ', style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_pipe_in_dw_reg_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px',}),
                            ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                 id='ws_pipe_in_dw_reg_all_percent',
                                 color="#1b5e20",
                                 pill=False,
                                 text_color="white",
                                 className='',
                                 style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),
                        html.Td(
                            [html.Span(id='ws_pipe_in_dw_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '20px',
                                          'margin-top': '4px',}),
                            ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                 id='ws_pipe_in_dw_all_percent',
                                 color="#1b5e20",
                                 pill=False,
                                 text_color="white",
                                 className='',
                                 style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Pipe-borne outside dwelling but on compound: ', style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_pipe_out_dw_on_cmd_reg_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px',}),
                            ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                 id='ws_pipe_out_dw_on_cmd_reg_all_percent',
                                 color="#1b5e20",
                                 pill=False,
                                 text_color="white",
                                 className='',
                                 style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td([
                            html.Span(id='ws_pipe_out_dw_on_cmd_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_out_dw_on_cmd_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Pipe-borne outside dwelling but on neighbor\'s compound: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_pipe_out_dw_on_neb_cmd_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'float': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_out_dw_on_neb_cmd_reg_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_pipe_out_dw_on_neb_cmd_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                            ],  style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_out_dw_on_neb_cmd_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'} ),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Pipe tap / Stand pipe: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_pipe_tap_stand_pipe_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '0px',
                                              'margin-top': '4px', }),
                             ]),
                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_tap_stand_pipe_reg_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_pipe_tap_stand_pipe_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),
                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_tap_stand_pipe_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Borehole/Tube well: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_bore_hole_tube_well_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_bore_hole_tube_well_reg_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_bore_hole_tube_well_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_bore_hole_tube_well_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Protected well: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_protected_well_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_protected_well_reg_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_protected_well_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_protected_well_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Rain Water: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_rain_water_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_rain_water_reg_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_rain_water_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_rain_water_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Protected spring: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_protected_spring_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_protected_spring_reg_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_protected_spring_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_protected_spring_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),


                    html.Tr([
                        html.Td(html.Span('Bottled water: ', style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_bottled_water_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_bottled_water_reg_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_bottled_water_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_bottled_water_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),


                    html.Tr([
                        html.Td(html.Span('Sachet Water: ', style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_sachet_water_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_sachet_water_reg_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_sachet_water_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_sachet_water_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ])

                ], style={'margin': '10px', 'text-align': 'right', 'width': '800px'})
            ], width=6),

            # Unimproved Water Sources
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
                    html.Tr([
                        html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_unimpr_water_src_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px',
                                              'margin-top': '4px', 'margin-left': '0px'}),
                             ]),

                        # percent ununimproved water sources - rural
                        html.Td([
                            dbc.Badge(
                              id='ws_unimpr_water_src_reg_all_percent',
                              color="#1b5e20",
                              pill=False,
                              text_color="white",
                              className='',
                              style={'margin-top': '4px', 'margin-left': '0px'}
                              ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_unimpr_water_src_dist_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px',
                                              'margin-top': '4px', 'margin-left': '20px'}),
                        ], style={'text-align': 'left'}),

                        #percent ununimproved water sources - rural
                        html.Td([
                            dbc.Badge(
                                id='ws_unimpr_water_src_dist_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '0px'}
                            ),
                        ], style={'text-align': 'center'}),

                    ]),

                    html.Tr([
                        html.Td(html.Span('Tanker supplied/Vendor provided: ', style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_tanker_vendor_reg_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px',}),
                            ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                 id='ws_tanker_vendor_reg_all_percent',
                                 color="#1b5e20",
                                 pill=False,
                                 text_color="white",
                                 className='',
                                 style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),
                        html.Td(
                            [html.Span(id='ws_tanker_vendor_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '20px',
                                          'margin-top': '4px',}),
                            ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                 id='ws_tanker_vendor_all_percent',
                                 color="#1b5e20",
                                 pill=False,
                                 text_color="white",
                                 className='',
                                 style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Unprotected well: ', style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_unprotec_well_reg_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px',}),
                            ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                 id='ws_unprotec_well_reg_all_percent',
                                 color="#1b5e20",
                                 pill=False,
                                 text_color="white",
                                 className='',
                                 style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td([
                            html.Span(id='ws_unprotec_well_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_unprotec_well_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Unprotected spring: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='unprotec_spring_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'float': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='unprotec_spring_reg_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='unprotec_spring_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                            ],  style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='unprotec_spring_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'} ),
                    ]),

                    html.Tr([
                        html.Td(html.Span('River / Stream: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='river_stream_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '0px',
                                              'margin-top': '4px', }),
                             ]),
                        html.Td([
                            dbc.Badge(
                                id='river_stream_reg_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='river_stream_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),
                        html.Td([
                            dbc.Badge(
                                id='river_stream_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Dugout/Pond/Lake/Dam/Canal: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='dugout_pond_lake_dam_canal_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='dugout_pond_lake_dam_canal_reg_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='dugout_pond_lake_dam_canal_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='dugout_pond_lake_dam_canal_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Other: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='other_reg_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='other_reg_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='other_all_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='other_all_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                ], style={'margin': '10px', 'text-align': 'right', 'width': '600px'})
            ], width=6),

        ]),


    ], style={'backgroundColor': 'navy', }),


    #Improved Water Sources - URBAN
    dbc.Row([
        dbc.Row([
            dbc.Col([
                dbc.CardBody([
                    html.H3('IMPROVED WATER SOURCES, URBAN', className='col-12 btn btn-primary',  style={'fontWeight': 'bold', 'fontSize': '16px', 'marginLeft': '18px'}),
                ]),
            ], width=6),
            dbc.Col([
                dbc.CardBody([
                    html.H3('UNIMPROVED WATER SOURCES, URBAN', className='col-12 btn btn-primary',  style={'fontWeight': 'bold', 'fontSize': '16px', 'marginLeft': '18px'}),
                ]),
            ], width=6)
        ]),

        dbc.Row([
            dbc.Col([
                html.Table([
                    html.Tr([
                        html.Td(html.Span('-')),
                        html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(html.Span('-')),
                        html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    ]),
                    html.Tr([
                        html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_impr_water_src_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px',
                                              'margin-top': '4px', 'margin-left': '0px'}),
                             ]),

                        # percent unimproved water sources - rural
                        html.Td([
                            dbc.Badge(
                              id='ws_impr_water_src_reg_urban_percent',
                              color="#1b5e20",
                              pill=False,
                              text_color="white",
                              className='',
                              style={'margin-top': '4px', 'margin-left': '0px'}
                              ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_impr_water_src_dist_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px',
                                              'margin-top': '4px', 'margin-left': '20px'}),
                        ], style={'text-align': 'left'}),

                        #percent unimproved water sources - rural
                        html.Td([
                            dbc.Badge(
                                id='ws_impr_water_src_dist_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '0px'}
                            ),
                        ], style={'text-align': 'center'}),

                    ]),

                    html.Tr([
                        html.Td(html.Span('Pipe-borne inside dwelling: ', style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_pipe_in_dw_reg_urban_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px',}),
                            ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                 id='ws_pipe_in_dw_reg_urban_percent',
                                 color="#1b5e20",
                                 pill=False,
                                 text_color="white",
                                 className='',
                                 style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),
                        html.Td(
                            [html.Span(id='ws_pipe_in_dw_urban_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '20px',
                                          'margin-top': '4px',}),
                            ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                 id='ws_pipe_in_dw_urban_percent',
                                 color="#1b5e20",
                                 pill=False,
                                 text_color="white",
                                 className='',
                                 style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Pipe-borne outside dwelling but on compound: ', style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_pipe_out_dw_on_cmd_reg_urban_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px',}),
                            ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                 id='ws_pipe_out_dw_on_cmd_reg_urban_percent',
                                 color="#1b5e20",
                                 pill=False,
                                 text_color="white",
                                 className='',
                                 style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td([
                            html.Span(id='ws_pipe_out_dw_on_cmd_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_out_dw_on_cmd_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Pipe-borne outside dwelling but on neighbor\'s compound: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_pipe_out_dw_on_neb_cmd_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_out_dw_on_neb_cmd_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_pipe_out_dw_on_neb_cmd_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                            ],  style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_out_dw_on_neb_cmd_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'} ),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Pipe tap / Stand pipe: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_pipe_tap_stand_pipe_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '0px',
                                              'margin-top': '4px', }),
                             ]),
                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_tap_stand_pipe_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_pipe_tap_stand_pipe_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),
                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_tap_stand_pipe_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Borehole/Tube well: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_bore_hole_tube_well_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_bore_hole_tube_well_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_bore_hole_tube_well_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_bore_hole_tube_well_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Protected well: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_protected_well_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_protected_well_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_protected_well_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_protected_well_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Rain Water: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_rain_water_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_rain_water_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_rain_water_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_rain_water_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),



                    html.Tr([
                        html.Td(html.Span('Protected spring: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_protected_spring_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_protected_spring_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_protected_spring_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_protected_spring_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),


                    html.Tr([
                        html.Td(html.Span('Bottled water: ', style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_bottled_water_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_bottled_water_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_bottled_water_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_bottled_water_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),


                    html.Tr([
                        html.Td(html.Span('Sachet Water: ', style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_sachet_water_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_sachet_water_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_sachet_water_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_sachet_water_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ])

                ], style={'margin': '10px', 'text-align': 'right', 'width': '800px'})
            ], width=6),

            # Unimproved Water Sources
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
                    html.Tr([
                        html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_unimpr_water_src_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px',
                                              'margin-top': '4px', 'margin-left': '0px'}),
                             ]),

                        # percent ununimproved water sources - rural
                        html.Td([
                            dbc.Badge(
                                id='ws_unimpr_water_src_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '0px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_unimpr_water_src_dist_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px',
                                              'margin-top': '4px', 'margin-left': '20px'}),
                             ], style={'text-align': 'left'}),

                        # percent ununimproved water sources - rural
                        html.Td([
                            dbc.Badge(
                                id='ws_unimpr_water_src_dist_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '0px'}
                            ),
                        ], style={'text-align': 'center'}),

                    ]),

                    html.Tr([
                        html.Td(html.Span('Tanker supplied/Vendor provided: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_tanker_vendor_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '0px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_tanker_vendor_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),
                        html.Td(
                            [html.Span(id='ws_tanker_vendor_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_tanker_vendor_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Unprotected well: ', style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_unprotec_well_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '0px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_unprotec_well_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td([
                            html.Span(id='ws_unprotec_well_urban_total',
                                      style={'color': '#eca50b', 'fontWeight': 'bold',
                                             'fontSize': '14px', 'margin-left': '20px',
                                             'margin-top': '4px', }),
                        ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_unprotec_well_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Unprotected spring: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='unprotec_spring_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'float': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='unprotec_spring_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='unprotec_spring_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='unprotec_spring_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('River / Stream: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='river_stream_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '0px',
                                              'margin-top': '4px', }),
                             ]),
                        html.Td([
                            dbc.Badge(
                                id='river_stream_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='river_stream_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),
                        html.Td([
                            dbc.Badge(
                                id='river_stream_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Dugout/Pond/Lake/Dam/Canal: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='dugout_pond_lake_dam_canal_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='dugout_pond_lake_dam_canal_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='dugout_pond_lake_dam_canal_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='dugout_pond_lake_dam_canal_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Other: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='other_reg_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='other_reg_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='other_urban_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='other_urban_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                ], style={'margin': '10px', 'text-align': 'right', 'width': '600px'})
            ], width=6),

        ]),

    ], style={'backgroundColor': 'navy', }),

    # Improved Water Sources - RURAL
    dbc.Row([
        dbc.Row([
            dbc.Col([
                dbc.CardBody([
                    html.H3('IMPROVED WATER SOURCES, RURAL', className='col-12 btn btn-primary',
                            style={'fontWeight': 'bold', 'fontSize': '16px', 'marginLeft': '18px'}),
                ]),
            ], width=6),
            dbc.Col([
                dbc.CardBody([
                    html.H3('UNIMPROVED WATER SOURCES, RURAL', className='col-12 btn btn-primary',
                            style={'fontWeight': 'bold', 'fontSize': '16px', 'marginLeft': '18px'}),
                ]),
            ], width=6)
        ]),

        dbc.Row([
            dbc.Col([
                html.Table([
                    html.Tr([
                        html.Td(html.Span('-')),
                        html.Td(html.Span('Region: ', style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(html.Span('-')),
                        html.Td(html.Span('District: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    ]),
                    html.Tr([
                        html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_impr_water_src_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px',
                                              'margin-top': '4px', 'margin-left': '0px'}),
                             ]),

                        # percent unimproved water sources - rural
                        html.Td([
                            dbc.Badge(
                                id='ws_impr_water_src_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '0px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_impr_water_src_dist_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px',
                                              'margin-top': '4px', 'margin-left': '20px'}),
                             ], style={'text-align': 'left'}),

                        # percent unimproved water sources - rural
                        html.Td([
                            dbc.Badge(
                                id='ws_impr_water_src_dist_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '0px'}
                            ),
                        ], style={'text-align': 'center'}),

                    ]),

                    html.Tr([
                        html.Td(
                            html.Span('Pipe-borne inside dwelling: ', style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_pipe_in_dw_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '0px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_in_dw_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),
                        html.Td(
                            [html.Span(id='ws_pipe_in_dw_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_in_dw_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Pipe-borne outside dwelling but on compound: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_pipe_out_dw_on_cmd_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '0px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_out_dw_on_cmd_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td([
                            html.Span(id='ws_pipe_out_dw_on_cmd_rural_total',
                                      style={'color': '#eca50b', 'fontWeight': 'bold',
                                             'fontSize': '14px', 'margin-left': '20px',
                                             'margin-top': '4px', }),
                        ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_out_dw_on_cmd_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Pipe-borne outside dwelling but on neighbor\'s compound: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_pipe_out_dw_on_neb_cmd_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_out_dw_on_neb_cmd_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_pipe_out_dw_on_neb_cmd_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_out_dw_on_neb_cmd_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Pipe tap / Stand pipe: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_pipe_tap_stand_pipe_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '0px',
                                              'margin-top': '4px', }),
                             ]),
                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_tap_stand_pipe_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_pipe_tap_stand_pipe_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),
                        html.Td([
                            dbc.Badge(
                                id='ws_pipe_tap_stand_pipe_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Borehole/Tube well: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_bore_hole_tube_well_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_bore_hole_tube_well_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_bore_hole_tube_well_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_bore_hole_tube_well_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Protected well: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_protected_well_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_protected_well_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_protected_well_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_protected_well_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Rain Water: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_rain_water_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_rain_water_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_rain_water_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_rain_water_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Protected spring: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_protected_spring_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_protected_spring_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_protected_spring_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_protected_spring_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Bottled water: ', style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_bottled_water_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_bottled_water_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_bottled_water_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_bottled_water_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Sachet Water: ', style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_sachet_water_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_sachet_water_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_sachet_water_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_sachet_water_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ])

                ], style={'margin': '10px', 'text-align': 'right', 'width': '800px'})
            ], width=6),

            # Unimproved Water Sources
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
                    html.Tr([
                        html.Td(html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='ws_unimpr_water_src_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px',
                                              'margin-top': '4px', 'margin-left': '0px'}),
                             ]),

                        # percent ununimproved water sources - rural
                        html.Td([
                            dbc.Badge(
                                id='ws_unimpr_water_src_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '0px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='ws_unimpr_water_src_dist_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px',
                                              'margin-top': '4px', 'margin-left': '20px'}),
                             ], style={'text-align': 'left'}),

                        # percent ununimproved water sources - rural
                        html.Td([
                            dbc.Badge(
                                id='ws_unimpr_water_src_dist_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '0px'}
                            ),
                        ], style={'text-align': 'center'}),

                    ]),

                    html.Tr([
                        html.Td(html.Span('Tanker supplied/Vendor provided: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_tanker_vendor_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '0px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_tanker_vendor_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),
                        html.Td(
                            [html.Span(id='ws_tanker_vendor_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_tanker_vendor_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Unprotected well: ', style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='ws_unprotec_well_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '0px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_unprotec_well_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td([
                            html.Span(id='ws_unprotec_well_rural_total',
                                      style={'color': '#eca50b', 'fontWeight': 'bold',
                                             'fontSize': '14px', 'margin-left': '20px',
                                             'margin-top': '4px', }),
                        ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='ws_unprotec_well_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Unprotected spring: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='unprotec_spring_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'float': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='unprotec_spring_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='unprotec_spring_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),

                        html.Td([
                            dbc.Badge(
                                id='unprotec_spring_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('River / Stream: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='river_stream_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '0px',
                                              'margin-top': '4px', }),
                             ]),
                        html.Td([
                            dbc.Badge(
                                id='river_stream_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='river_stream_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '20px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'left'}),
                        html.Td([
                            dbc.Badge(
                                id='river_stream_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '20px'}
                            ),
                        ], style={'text-align': 'left'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Dugout/Pond/Lake/Dam/Canal: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),

                        html.Td(
                            [html.Span(id='dugout_pond_lake_dam_canal_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='dugout_pond_lake_dam_canal_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='dugout_pond_lake_dam_canal_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='dugout_pond_lake_dam_canal_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                    html.Tr([
                        html.Td(html.Span('Other: ',
                                          style={'color': 'white', 'fontWeight': 'bold'})),
                        html.Td(
                            [html.Span(id='other_reg_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'right'}),

                        html.Td([
                            dbc.Badge(
                                id='other_reg_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'right'}),

                        html.Td(
                            [html.Span(id='other_rural_total',
                                       style={'color': '#eca50b', 'fontWeight': 'bold',
                                              'fontSize': '14px', 'margin-left': '10px',
                                              'margin-top': '4px', }),
                             ], style={'text-align': 'center'}),

                        html.Td([
                            dbc.Badge(
                                id='other_rural_percent',
                                color="#1b5e20",
                                pill=False,
                                text_color="white",
                                className='',
                                style={'margin-top': '4px', 'margin-left': '10px'}
                            ),
                        ], style={'text-align': 'center'}),
                    ]),

                ], style={'margin': '10px', 'text-align': 'right', 'width': '600px'})
            ], width=6),

        ]),

    ], style={'backgroundColor': 'navy', }),




])

def create_water_sanitation():
    layout = html.Div([
        nav,
        header
    ])

    return layout