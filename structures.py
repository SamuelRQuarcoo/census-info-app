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
    html.H2('STRUCTURES', style={'color': 'navy', 'margin': '10px', 'backgroundColor': 'white'}),
    dbc.Row([
        # regions
        dbc.Col([
            html.Span('REGION', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='struct_region_dd',
                style={'color': 'black'},
                options=[{'label': REGION, 'value': REGION} for REGION in REGIONS]
            ),
        ], width=2, style={'marginLeft': '20px', 'marginTop': '5px', 'marginBottom': '5px'}),

        html.Br(),

        dbc.Col([
            html.Span('DISTRICT', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='struct_district_dd',
                style={'color': 'black'},
            ),
        ], width=2, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px'}),

        dbc.Col([
            dbc.Button('SEARCH',
                id='struct_search_btn',
                n_clicks=0,
                className='me-1',
                size='lg',
               style={'marginTop': '20px'},
            ),
        ], width=1, style={'width':'6%','marginLeft': '40px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

        dbc.Col([
            dbc.Button('CLEAR',
                id='struct_clear_all',
                n_clicks=0,
                className='me-1',
                size='lg',
               style={'marginTop': '20px'},
            ),
        ], width=1, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

        html.Br(),

    ], style={'backgroundColor': '#eeeff3', 'color': 'navy', 'fontSize': '20px', 'paddingBottom': '10px'}),

    html.Hr(),

    html.H3('Level of Completion of Structures by Type of Locality and District',
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
                    dbc.Badge("URBAN", color='', text_color='white', className='col-12 btn btn-primary', style={'fontSize': '16px'}),
                ]),
            ], width=4, style={'marginLeft': '0px'}),
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("RURAL", color="", text_color='white', className="col-12 btn btn-primary", style={'fontSize': '16px'}),
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
                        [html.Span(id='struct_reg_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_all_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                #Fully Completed
                html.Tr([
                    html.Td(html.Span('Fully Completed: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_fully_compl_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_fully_compl_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='struct_fully_compl_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_fully_compl_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                #Completely Roofed but Uncompleted
                html.Tr([
                    html.Td(html.Span('Completely Roofed but Uncompleted: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_compl_roofed_uncom_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_compl_roofed_uncom_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='struct_compl_roofed_uncom_all_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_compl_roofed_uncom_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                #Partially Roofed
                html.Tr([
                    html.Td(html.Span('Partially Roofed: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_part_roofed_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_part_roofed_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_part_roofed_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_part_roofed_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                #Roofing Level with Improvised Roof
                html.Tr([
                    html.Td(html.Span('Roofing Level with Improvised Roof: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_roof_lvl_improv_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='struct_roof_lvl_improv_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_roof_lvl_improv_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='struct_roof_lvl_improv_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                #Lintel Level with Improvised Roof
                html.Tr([
                    html.Td(html.Span('Lintel Level with Improvised Roof: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='struct_lintel_improv_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_lintel_improv_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_lintel_improv_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_lintel_improv_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                #roofing level without roof
                html.Tr([
                    html.Td(html.Span('Roofing Level without Roof: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_roof_lvl_wout_roof_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_roof_lvl_wout_roof_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_roof_lvl_wout_roof_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_roof_lvl_wout_roof_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                #lintel level without roof
                html.Tr([
                    html.Td(html.Span('Lintel Level without Roof: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_lintel_wout_roof_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_lintel_wout_roof_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_lintel_wout_roof_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_lintel_wout_roof_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                #window level
                html.Tr([
                    html.Td(html.Span('Window Level: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_window_lvl_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_window_lvl_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_window_lvl_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_window_lvl_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                #concrete/metal pillars level
                html.Tr([
                    html.Td(html.Span('Concrete/Metal Pillars Level: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_concr_metal_pill_lvl_reg_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_concr_metal_pill_lvl_reg_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_concr_metal_pill_lvl_all_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_concr_metal_pill_lvl_all_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '600px'})
        ], width=4),



        # URBAN
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
                        [html.Span(id='struct_reg_urban_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ]),

                    html.Td([
                        dbc.Badge(
                            id='struct_reg_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_urban_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'left'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # Fully Completed
                html.Tr([
                    html.Td(html.Span('Fully Completed: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_fully_compl_reg_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_fully_compl_reg_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='struct_fully_compl_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_fully_compl_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Completely Roofed but Uncompleted
                html.Tr([
                    html.Td(html.Span('Completely Roofed but Uncompleted: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_compl_roofed_uncom_reg_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_compl_roofed_uncom_reg_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='struct_compl_roofed_uncom_urban_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_compl_roofed_uncom_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Partially Roofed
                html.Tr([
                    html.Td(html.Span('Partiurbany Roofed: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_part_roofed_reg_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_part_roofed_reg_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_part_roofed_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_part_roofed_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Roofing Level with Improvised Roof
                html.Tr([
                    html.Td(html.Span('Roofing Level with Improvised Roof: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_roof_lvl_improv_reg_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='struct_roof_lvl_improv_reg_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_roof_lvl_improv_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='struct_roof_lvl_improv_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Lintel Level with Improvised Roof
                html.Tr([
                    html.Td(html.Span('Lintel Level with Improvised Roof: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='struct_lintel_improv_reg_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_lintel_improv_reg_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_lintel_improv_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_lintel_improv_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # roofing level without roof
                html.Tr([
                    html.Td(html.Span('Roofing Level without Roof: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_roof_lvl_wout_roof_reg_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_roof_lvl_wout_roof_reg_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_roof_lvl_wout_roof_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_roof_lvl_wout_roof_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # lintel level without roof
                html.Tr([
                    html.Td(html.Span('Lintel Level without Roof: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_lintel_wout_roof_reg_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_lintel_wout_roof_reg_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_lintel_wout_roof_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_lintel_wout_roof_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # window level
                html.Tr([
                    html.Td(html.Span('Window Level: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_window_lvl_reg_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_window_lvl_reg_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_window_lvl_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_window_lvl_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # concrete/metal pillars level
                html.Tr([
                    html.Td(html.Span('Concrete/Metal Pillars Level: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_concr_metal_pill_lvl_reg_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_concr_metal_pill_lvl_reg_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_concr_metal_pill_lvl_urban_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_concr_metal_pill_lvl_urban_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '600px'})
        ], width=4),



        # RURAL
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
                        [html.Span(id='struct_reg_rural_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '0px'}),
                         ]),

                    html.Td([
                        dbc.Badge(
                            id='struct_reg_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_rural_total',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px',
                                          'margin-top': '4px', 'margin-left': '20px'}),
                         ], style={'text-align': 'left'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                ]),

                # Fully Completed
                html.Tr([
                    html.Td(html.Span('Fully Completed: ', style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_fully_compl_reg_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_fully_compl_reg_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                    html.Td(
                        [html.Span(id='struct_fully_compl_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_fully_compl_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Completely Roofed but Uncompleted
                html.Tr([
                    html.Td(html.Span('Completely Roofed but Uncompleted: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_compl_roofed_uncom_reg_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_compl_roofed_uncom_reg_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td([
                        html.Span(id='struct_compl_roofed_uncom_rural_val',
                                  style={'color': '#eca50b', 'fontWeight': 'bold',
                                         'fontSize': '14px', 'margin-left': '0px',
                                         'margin-top': '4px', }),
                    ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_compl_roofed_uncom_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Partially Roofed
                html.Tr([
                    html.Td(html.Span('Partiruraly Roofed: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_part_roofed_reg_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_part_roofed_reg_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_part_roofed_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_part_roofed_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Roofing Level with Improvised Roof
                html.Tr([
                    html.Td(html.Span('Roofing Level with Improvised Roof: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_roof_lvl_improv_reg_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='struct_roof_lvl_improv_reg_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_roof_lvl_improv_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),
                    html.Td([
                        dbc.Badge(
                            id='struct_roof_lvl_improv_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # Lintel Level with Improvised Roof
                html.Tr([
                    html.Td(html.Span('Lintel Level with Improvised Roof: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),

                    html.Td(
                        [html.Span(id='struct_lintel_improv_reg_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_lintel_improv_reg_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_lintel_improv_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_lintel_improv_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # roofing level without roof
                html.Tr([
                    html.Td(html.Span('Roofing Level without Roof: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_roof_lvl_wout_roof_reg_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_roof_lvl_wout_roof_reg_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_roof_lvl_wout_roof_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_roof_lvl_wout_roof_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # lintel level without roof
                html.Tr([
                    html.Td(html.Span('Lintel Level without Roof: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_lintel_wout_roof_reg_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_lintel_wout_roof_reg_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_lintel_wout_roof_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_lintel_wout_roof_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # window level
                html.Tr([
                    html.Td(html.Span('Window Level: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_window_lvl_reg_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_window_lvl_reg_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_window_lvl_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_window_lvl_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

                # concrete/metal pillars level
                html.Tr([
                    html.Td(html.Span('Concrete/Metal Pillars Level: ',
                                      style={'color': 'white', 'fontWeight': 'bold'})),
                    html.Td(
                        [html.Span(id='struct_concr_metal_pill_lvl_reg_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_concr_metal_pill_lvl_reg_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),

                    html.Td(
                        [html.Span(id='struct_concr_metal_pill_lvl_rural_val',
                                   style={'color': '#eca50b', 'fontWeight': 'bold',
                                          'fontSize': '14px', 'margin-left': '0px',
                                          'margin-top': '4px', }),
                         ], style={'text-align': 'right'}),

                    html.Td([
                        dbc.Badge(
                            id='struct_concr_metal_pill_lvl_rural_percent',
                            color="#1b5e20",
                            pill=False,
                            text_color="white",
                            className='',
                            style={'margin-top': '4px', 'margin-left': '0px'}
                        ),
                    ], style={'text-align': 'left'}),
                ]),

            ], style={'margin': '10px', 'text-align': 'right', 'width': '600px'})
        ], width=4),

    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'})
])

def create_structures():
    layout = html.Div([
        nav,
        header
    ])

    return layout