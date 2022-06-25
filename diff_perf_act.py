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

    html.H2('DIFFICULTY IN PERFORMING ACTIVITIES',
            style={'color': 'navy', 'margin': '10px', 'backgroundColor': 'white'}),

    dbc.Row([
    html.Hr(),

    # regions
    dbc.Col([
        html.Span('REGION', style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='dpa_region_dd',
            style={'color': 'black'},
            options=[{'label': REGION, 'value': REGION} for REGION in REGIONS]
        ),
    ], width=2, style={'marginLeft': '10px', 'marginTop': '5px', 'marginBottom': '5px'}),

    html.Br(),

    dbc.Col([
        html.Span('DISTRICT', style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='dpa_district_dd',
            style={'color': 'black'},
        ),
    ], width=2, style={'marginLeft': '-13px', 'marginTop': '5px', 'marginBottom': '5px'}),

    dbc.Col([
        html.Span('CATEGORY', style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='dpa_category_dd',
            style={'color': 'black'},
        ),
    ], width=2, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px'}),

    html.Br(),

    dbc.Col([
        dbc.Button('SEARCH',
            id='dpa_search_btn',
            n_clicks=0,
            className='me-1',
            size='lg',
           style={'marginTop': '20px'},
        ),
    ], width=1, style={'width':'6%', 'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

    dbc.Col([
        dbc.Button('CLEAR',
            id='dpa_clear_btn',
            n_clicks=0,
            className='me-1',
            size='lg',
           style={'marginTop': '20px'},
        ),
    ], width=1, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

    html.Span(id='diff_perf_act_district_label', style={'color': 'red', 'marginLeft': '10px'}),

    ], style={'backgroundColor': '#eeeff3', 'color': 'navy', 'fontSize': '18px', 'paddingBottom': '10px'}),

    html.H3([
        html.Span('Severity of Difficulty | Population 5 years and Older', style={'color': 'navy', 'marginLeft': '18px'}),
    ]),

    dbc.Row([
        dbc.Row([
            dbc.Col([
                html.H5('CATEGORY:', style={'color': 'white', 'marginTop': '20px', 'marginLeft': '0px'}),
            ], width=2, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('BOTH:', style={'color': 'white', 'marginTop': '20px', 'marginLeft':'0px'}),
            ], width=2, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('MALE:', style={'color': 'white', 'marginTop': '20px'}),
            ], width=1, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('FEMALE:', style={'color': 'white', 'marginTop': '20px', 'float': 'right'}),
            ], width=1, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('URBAN(BOTH):', style={'color': 'white', 'marginTop': '20px', 'float': 'right'}),
            ], width=2, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('RURAL (BOTH):', style={'color': 'white', 'marginTop': '20px', 'float': 'right'}),
            ], width=2, style={'marginLeft': '0px'}),
        ], style={'backgroundColor': 'navy', 'marginBottom': '15px'}),

        # Categories
        dbc.Row([
            dbc.Col([
                html.Div([
                    # seeing
                    html.Table([
                        html.Tr([
                            html.Td(html.Span('Total: '), style={'fontSize': '16px', 'color': 'white'}),
                        ]),
                        html.Tr([
                            html.Td(html.Span('No Difficulty: '), style={'fontSize': '16px', 'color': 'white'}),
                        ]),

                        html.Tr([
                            html.Td(html.Span('Some Difficulty: '), style={'fontSize': '16px', 'color': 'white'}),
                        ]),

                        html.Tr([
                            html.Td(html.Span('Lot of Difficulty: ', style={'fontSize': '16px', 'color': 'white'}), style={'width':'50%'}),
                        ]),

                        html.Tr([
                            html.Td(html.Span('Cannot do at all: '), style={'fontSize': '16px', 'color': 'white'}),
                        ]),
                    ], style={'width': '100%'}),


                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=1, style={'marginTop': '-50px'}),

            #Both
            dbc.Col([
                html.Div([
                    # seeing
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_all_total_val', style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300', 'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_all_percent', className='sm-1', pill=True, color="#1b5e20", text_color="white",))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_all_no_diff_val', style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300', 'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_all_no_diff_percent', className='sm-1', pill=True, color="#1b5e20", text_color="white",))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_all_some_diff_val', style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300', 'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_all_some_diff_percent', pill=True, color="#1b5e20", text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_all_lot_diff_val', style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300', 'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_all_lot_diff_percent', className='sm-1', pill=True, color="#1b5e20", text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_all_cannot_do_at_all_val', style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300', 'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_all_cannot_do_at_all_percent', className='sm-1', pill=True, color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),


                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=2, style={'marginTop': '-50px'}),

            #MALE
            dbc.Col([
                html.Div([
                    # seeing
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_male_total_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300', 'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_male_percent', className='sm-1', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_male_no_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300', 'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_male_no_diff_percent', className='sm-1', pill=True, color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_male_some_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300', 'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_male_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_male_lot_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300', 'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_male_lot_diff_percent', className='sm-1', pill=True, color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_male_cannot_do_at_all_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300', 'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_male_cannot_do_at_all_percent', className='sm-1', pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=2, style={'marginTop': '-50px'}),

            #FEMALE
            dbc.Col([
                html.Div([
                    # seeing
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_female_total_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_female_percent', className='sm-1', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_female_no_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_female_no_diff_percent', className='sm-1', pill=True, color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_female_some_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_female_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_female_lot_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_female_lot_diff_percent', className='sm-1', pill=True, color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_female_cannot_do_at_all_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_female_cannot_do_at_all_percent', className='sm-1', pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=1, style={'marginTop': '-50px'}),

            # URBAN ALL
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_total_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_urban_percent', className='sm-1', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_no_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_urban_no_diff_percent', className='sm-1', pill=True, color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_some_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_urban_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_lot_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_urban_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_cannot_do_at_all_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_urban_cannot_do_at_all_percent', className='sm-1', pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=2, style={'marginTop': '-50px'}),

            # RURAL ALL
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_total_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_rural_percent', className='sm-1', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_no_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_rural_no_diff_percent', className='sm-1', pill=True, color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_some_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_rural_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_lot_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_rural_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_cannot_do_at_all_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_rural_cannot_do_at_all_percent', className='sm-1', pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=2, style={'marginTop': '-50px'}),
        ]),

    ], style={'backgroundColor': 'navy', 'marginBottom': 'px'}),


    html.P([
        html.Hr(),
    ], style={'backgroundColor': 'white'}),

    #URBAN/RURAL, MALE/FEMALE
    dbc.Row([

        dbc.Row([
            dbc.Col([
                html.H5('CATEGORY:', style={'color': 'white', 'marginTop': '20px', 'marginLeft': '15px'}),
            ], width=1, style={'marginLeft': '0px'}),

            dbc.Col([
                html.H5('URBAN (MALE):', style={'color': 'white', 'marginTop': '20px', 'float': 'right'}),
            ], width=2, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('URBAN (FEMALE):', style={'color': 'white', 'marginTop': '20px', 'float': 'right'}),
            ], width=2, style={'marginLeft': '0px'}),

            dbc.Col([
                html.H5('RURAL (MALE):', style={'color': 'white', 'marginTop': '20px', 'float': 'right'}),
            ], width=2, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('RURAL (FEMALE):', style={'color': 'white', 'marginTop': '20px', 'float': 'right'}),
            ], width=2, style={'marginLeft': '0px'}),
        ], style={'backgroundColor': 'navy', 'marginBottom': '15px'}),

        dbc.Row([
            dbc.Col([
                html.Div([
                    # seeing
                    html.Table([
                        html.Tr([
                            html.Td(html.Span('Total: '), style={'fontSize': '16px', 'color': 'white'}),
                        ]),
                        html.Tr([
                            html.Td(html.Span('No Difficulty: '), style={'fontSize': '16px', 'color': 'white'}),
                        ]),

                        html.Tr([
                            html.Td(html.Span('Some Difficulty: '), style={'fontSize': '16px', 'color': 'white'}),
                        ]),

                        html.Tr([
                            html.Td(html.Span('Lot of Difficulty: ', style={'fontSize': '16px', 'color': 'white'}), style={'width':'50%'}),
                        ]),

                        html.Tr([
                            html.Td(html.Span('Cannot do at all: '), style={'fontSize': '16px', 'color': 'white'}),
                        ]),
                    ], style={'width': '100%'}),


                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=1, style={'marginTop': '-50px'}),

            # URBAN MALE
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_male_total_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_urban_male_percent', className='sm-1', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_male_no_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_urban_male_no_diff_percent', className='sm-1', pill=True, color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_male_some_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_urban_male_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_male_lot_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_urban_male_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_male_cannot_do_at_all_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_urban_male_cannot_do_at_all_percent', className='sm-1', pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=2, style={'marginTop': '-50px'}),

            # URBAN FEMALE
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_female_total_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_urban_female_percent', className='sm-1', pill=True,
                                              color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_female_no_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_urban_female_no_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_female_some_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_urban_female_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_female_lot_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_urban_female_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_urban_female_cannot_do_at_all_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_urban_female_cannot_do_at_all_percent', className='sm-1',
                                              pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=2, style={'marginTop': '-50px'}),


            # RURAL MALE
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_male_total_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_rural_male_percent', className='sm-1', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_male_no_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_rural_male_no_diff_percent', className='sm-1', pill=True, color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_male_some_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_rural_male_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_male_lot_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_rural_male_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_male_cannot_do_at_all_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_rural_male_cannot_do_at_all_percent', className='sm-1', pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=2, style={'marginTop': '-50px'}),

            # RURAL FEMALE
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_female_total_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_rural_female_percent', className='sm-1', pill=True,
                                              color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_female_no_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_rural_female_no_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_female_some_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_rural_female_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_female_lot_diff_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_rural_female_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_rural_female_cannot_do_at_all_val',
                                               style={'marginLeft': '120px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_rural_female_cannot_do_at_all_percent', className='sm-1',
                                              pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=2, style={'marginTop': '-50px'}),

        ])

    ], style={'backgroundColor': 'navy', 'marginBottom': 'px'}),

    # ALL DOMAINS
    html.H3([
        html.Span('Severity of Difficulty | All Domains', style={'color': 'navy', 'marginLeft': '18px'}),
    ]),

    #ALL DOMAINS
    dbc.Row([

        dbc.Row([
            dbc.Col([
                html.H5('CATEGORY:', style={'color': 'white', 'marginTop': '20px', 'marginLeft': '15px', 'fontSize':'18px'}),
            ], width=2, style={'marginLeft': '0px'}),

            dbc.Col([
                html.H5('BOTH:', style={'color': 'white', 'marginTop': '20px', 'float': 'right', 'fontSize':'18px'}),
            ], width=1, style={'marginLeft': '-70px'}),
            dbc.Col([
                html.H5('MALE:', style={'color': 'white', 'marginTop': '20px', 'float': 'right', 'fontSize':'18px'}),
            ], width=1, style={'marginLeft': '50px'}),

            dbc.Col([
                html.H5('FEMALE:', style={'color': 'white', 'marginTop': '20px', 'float': 'right', 'fontSize':'18px'}),
            ], width=1, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('URBAN (BOTH):', style={'color': 'white', 'marginTop': '20px', 'float': 'right', 'fontSize':'18px'}),
            ], width=1, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('URBAN MALE:', style={'color': 'white', 'marginTop': '20px', 'float': 'right', 'fontSize':'18px'}),
            ], width=1, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('URBAN FEMALE:', style={'color': 'white', 'marginTop': '20px', 'float': 'right', 'fontSize':'18px'}),
            ], width=1, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('RURAL (BOTH):', style={'color': 'white', 'marginTop': '20px', 'float': 'right', 'fontSize':'18px'}),
            ], width=1, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('RURAL MALE:', style={'color': 'white', 'marginTop': '20px', 'float': 'right', 'fontSize':'18px'}),
            ], width=1, style={'marginLeft': '0px'}),
            dbc.Col([
                html.H5('RURAL FEMALE:', style={'color': 'white', 'marginTop': '20px', 'float': 'right', 'fontSize':'18px'}),
            ], width=1, style={'marginLeft': '0px'}),
        ], style={'backgroundColor': 'navy', 'marginBottom': '15px'}),

        dbc.Row([
            dbc.Col([
                html.Div([
                    # seeing
                    html.Table([
                        html.Tr([
                            html.Td(html.Span('Total: '), style={'fontSize': '16px', 'color': 'white'}),
                        ]),
                        html.Tr([
                            html.Td(html.Span('No Difficulty: '), style={'fontSize': '16px', 'color': 'white'}),
                        ]),

                        html.Tr([
                            html.Td(html.Span('Some difficulty in at least one Domain: '), style={'fontSize': '16px', 'color': 'white'}),
                        ]),

                        html.Tr([
                            html.Td(html.Span('A lot of difficulty in at least one Domain: ', style={'fontSize': '16px', 'color': 'white'}), style={'width':'50%'}),
                        ]),

                        html.Tr([
                            html.Td(html.Span('Cannot do at all in at least one Domain:'), style={'fontSize': '16px', 'color': 'white'}),
                        ]),
                    ], style={'width': '100%'}),


                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=2, style={'marginTop': '-50px'}),

            # BOTH
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_total_val',
                                               style={'marginLeft': '0px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_all_total_percent', className='sm-1', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_no_diff_val',
                                               style={'marginLeft': '0px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_all_no_diff_percent', className='sm-1', pill=True, color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_some_diff_val',
                                               style={'marginLeft': '0px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_all_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_lot_diff_val',
                                               style={'marginLeft': '0px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_all_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_cannot_do_at_all_val',
                                               style={'marginLeft': '0px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_all_cannot_do_at_all_percent', className='sm-1', pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '-50px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=2, style={'marginTop': '-50px', 'marginLeft': '-80px'}),

            # MALE
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_male_total_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_all_male_percent', className='sm-1', pill=True,
                                              color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_male_no_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_all_male_no_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_male_some_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_all_male_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_male_lot_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_all_male_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_male_cannot_do_at_all_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_all_male_cannot_do_at_all_percent', className='sm-1',
                                              pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=1, style={'marginTop': '-50px'}),


            # FEMALE
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_female_total_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_all_female_percent', className='sm-1', pill=True,
                                              color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_female_no_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_all_female_no_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_female_some_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_all_female_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_female_lot_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_all_female_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_all_female_cannot_do_at_all_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_all_female_cannot_do_at_all_percent', className='sm-1',
                                              pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=1, style={'marginTop': '-50px'}),

            # URBAN BOTH
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_both_total_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_urban_both_percent', className='sm-1', pill=True,
                                              color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_both_no_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_urban_both_no_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_both_some_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_urban_both_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_both_lot_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_urban_both_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_both_cannot_do_at_all_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_urban_both_cannot_do_at_all_percent', className='sm-1',
                                              pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=1, style={'marginTop': '-50px'}),

        # URBAN MALE
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_male_total_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_urban_male_percent', className='sm-1', pill=True,
                                              color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_male_no_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_urban_male_no_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_male_some_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_urban_male_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_male_lot_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_urban_male_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_male_cannot_do_at_all_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_urban_male_cannot_do_at_all_percent', className='sm-1',
                                              pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=1, style={'marginTop': '-50px'}),

        # URBAN FEMALE
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_female_total_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_urban_female_percent', className='sm-1', pill=True,
                                              color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_female_no_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_urban_female_no_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_female_some_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_urban_female_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_female_lot_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_urban_female_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_urban_female_cannot_do_at_all_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_urban_female_cannot_do_at_all_percent', className='sm-1',
                                              pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=1, style={'marginTop': '-50px'}),

            # RURAL BOTH
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_both_total_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_rural_both_percent', className='sm-1', pill=True,
                                              color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_both_no_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_rural_both_no_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_both_some_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_rural_both_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_both_lot_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_rural_both_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_both_cannot_do_at_all_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_rural_both_cannot_do_at_all_percent', className='sm-1',
                                              pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=1, style={'marginTop': '-50px'}),

            # RURAL MALE
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_male_total_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_rural_male_percent', className='sm-1', pill=True,
                                              color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_male_no_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_rural_male_no_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_male_some_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_rural_male_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_male_lot_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_rural_male_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_male_cannot_do_at_all_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_rural_male_cannot_do_at_all_percent', className='sm-1',
                                              pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=1, style={'marginTop': '-50px'}),

            # RURAL FEMALE
            dbc.Col([
                html.Div([
                    html.Table([
                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_female_total_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_rural_female_percent', className='sm-1', pill=True,
                                              color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_female_no_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_rural_female_no_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_female_some_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_rural_female_some_diff_percent', pill=True, color="#1b5e20",
                                              text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_female_lot_diff_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(
                                dbc.Badge(id='dpa_domain_rural_female_lot_diff_percent', className='sm-1', pill=True,
                                          color="#1b5e20",
                                          text_color="white", ))
                        ]),

                        html.Tr([
                            html.Td([html.Span(id='dpa_domain_rural_female_cannot_do_at_all_val',
                                               style={'marginLeft': '-100px', 'float': 'right', 'color': '#FFC300',
                                                      'fontWeight': 'bold'})]),
                            html.Td(dbc.Badge(id='dpa_domain_rural_female_cannot_do_at_all_percent', className='sm-1',
                                              pill=True,
                                              color="#1b5e20", text_color="white", ))
                        ]),
                    ], style={'width': '100%'}),

                ], style={'marginLeft': '10px', 'marginTop': '40px', 'marginBottom': '10px'}),

            ], width=1, style={'marginTop': '-50px'}),

        ])

    ], style={'backgroundColor': 'navy', 'marginBottom': 'px'}),

])


def create_diff_perf_act():
    layout = html.Div([
        nav,
        header
    ])

    return layout