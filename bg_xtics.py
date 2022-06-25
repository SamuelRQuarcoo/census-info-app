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
    html.H2('BACKGROUND CHARACTERISTICS', style={'color': 'navy', 'margin': '10px', 'backgroundColor': 'white'}),
    dbc.Row([
        # regions
        dbc.Col([
            html.Span('REGION', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='bg_xtics_region_dd',
                style={'color': 'black'},
                options=[{'label': REGION, 'value': REGION} for REGION in REGIONS]
            ),
        ], width=2, style={'marginLeft': '20px', 'marginTop': '5px', 'marginBottom': '5px'}),

        html.Br(),

        dbc.Col([
            html.Span('DISTRICT', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='bg_xtics_district_dd',
                style={'color': 'black'},
            ),
        ], width=2, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px'}),

        dbc.Col([
            dbc.Button('SEARCH',
                id='search_btn_background',
                n_clicks=0,
                className='me-1',
                size='lg',
               style={'marginTop': '20px'},
            ),
        ], width=1, style={'width':'6%','marginLeft': '40px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

        dbc.Col([
            dbc.Button('CLEAR',
                id='clear_all_btn_background',
                n_clicks=0,
                className='me-1',
                size='lg',
               style={'marginTop': '20px'},
            ),
        ], width=1, style={'marginLeft': '0px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

        dbc.Col([
            html.A('Marital Status', href='#ethnicity',
                   style={'textDecoration': 'none', 'backgroundColor': '#ba68c8', 'color': 'white', 'fontSize': '15px'}, className='border badge badge-pill'),
            html.A('Ethnicity', href='#ethnicity',
                   style={'textDecoration': 'none', 'backgroundColor': '#4caf50', 'color': 'white', 'fontSize': '15px'}, className='border badge badge-pill'),
            html.A('Insurance', href='#insurance',
                   style={'textDecoration': 'none', 'backgroundColor': '#ff6f00', 'color': 'white', 'fontSize': '15px'}, className='border badge badge-pill'),
        ], width=2, style={'marginLeft': '50px', 'marginTop': '20px', 'fontWeight': 'bold'}),

        dbc.Col([
            html.Span([
                html.Strong(id='reg_lab_bg', style={'color': 'red', 'marginLeft': '10px', 'fontSize': '15px'}),
                html.Strong('|', style={'color': 'red', 'marginLeft': '5px', 'fontSize': '15px'}),
                html.Strong(id='dist_lab_bg', style={'color': 'red', 'marginLeft': '5px', 'fontSize': '15px'})
            ]),
        ], width=2, style={'marginLeft': '90px', 'marginTop': '20px', 'fontWeight': 'bold'}),

        html.Br(),

    ], style={'backgroundColor': '#eeeff3', 'color': 'navy', 'fontSize': '20px', 'paddingBottom': '10px'}),

    html.Hr(),
    html.P(id='marital'),
    html.H3('Marital Status | Population 12 years and older',
            style={'color': 'navy', 'marginLeft': '18px'}),
    dbc.Row([
        dbc.Row([
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("BOTH SEXES", color="#2e7d32", text_color='white',  className="border me-3", style={'fontSize': '16px'}),
                ]),
            ], width=3, style={'marginLeft': '0px'}),
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("MALE", color='#B39100', text_color='white', className='border me-3', style={'fontSize': '16px'}),
                ]),
            ], width=3, style={'marginLeft': '0px'}),
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("FEMALE", color="#5080C3", text_color='white', className="border me-3", style={'fontSize': '16px'}),
                ]),
            ], width=3, style={'marginLeft': '0px'}),
        ], style={'backgroundColor': 'navy', 'marginBottom': '15px'}),


        #ALL
        dbc.Col([
            dbc.CardBody([
                html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'}),
                            html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_all_total',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                    dbc.Badge(
                                        id='bg_all_percent',
                                        color="#1b5e20",
                                        pill=True,
                                        text_color="white",
                                        style={'float':'right',}
                                    ),
                                  ]),

                              ])
                          ], style={'float':'right'}),

                html.Br(),
                html.Div([html.Span('Never Married: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_nvr_marr_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                    dbc.Badge(
                                        id='bg_nvr_marr',
                                        color="#1b5e20",
                                        pill=True,
                                        text_color="white",
                                        className='',
                                        style={'float':'right',}
                                    ),
                                  ]),

                              ])
                          ], style={'float':'right'}),



                ]),
                html.Div([html.Span('Informal/Living Together: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_inf_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_inf',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                ]),

                html.Div([html.Span('Married, Registered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_marr_reg_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_marr_reg',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                ]),

                html.Div([html.Span('Married, Not Registered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_marr_not_reg_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_marr_not_reg',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                ]),

                html.Div([html.Span('Separated: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_sep_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_sep',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                ]),

                html.Div([html.Span('Divorce: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_div_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_div',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                ]),

                html.Div([html.Span('Widowed: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_wid_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_wid',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                ]),
            ]),
        ], width=3, style={'marginTop': '-30px'}),

        #MALE
        dbc.Col([
            dbc.CardBody([
                html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'}),
                            html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_male_total',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_male_percent',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                html.Br(),
                html.Div([html.Span('Never Married: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_nvr_marr_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_nvr_marr_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),
                html.Div([html.Span('Informal/Living Together: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_inf_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_inf_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Married, Registered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_marr_reg_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_marr_reg_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Married, Not Registered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_marr_not_reg_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_marr_not_reg_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Separated: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_sep_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_sep_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Divorce: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_div_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_div_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Widowed: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_wid_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_wid_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),
            ]),
        ], width=3, style={'marginTop': '-30px'}),

        #FEMALE
        dbc.Col([
            dbc.CardBody([
                html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'}),
                            html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_female_total',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_female_percent',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                html.Br(),
                html.Div([html.Span('Never Married: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_nvr_marr_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_nvr_marr_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),
                html.Div([html.Span('Informal/Living Together: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_inf_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_inf_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Married, Registered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_marr_reg_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_marr_reg_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Married, Not Registered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_marr_not_reg_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_marr_not_reg_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Separated: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_sep_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_sep_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Divorce: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_div_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_div_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Widowed: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_wid_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_wid_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),
            ]),
        ], width=3, style={'marginTop': '-30px'}),

    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),

    # ETHNICITY
    html.Hr(),
    html.H3(id='ethnicity'),
    html.H3('Major Ethnic Groups',
            style={'color': 'navy', 'marginLeft': '18px'}),
    dbc.Row([

        dbc.Row([
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("BOTH SEXES", color="#2e7d32", text_color='white',  className="border me-3", style={'fontSize': '16px'}),
                ]),
            ], width=3, style={'marginLeft': '0px'}),
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("MALE", color='#B39100', text_color='white', className='border me-3', style={'fontSize': '16px'}),
                ]),
            ], width=3, style={'marginLeft': '0px'}),
            dbc.Col([
                dbc.CardBody([
                    dbc.Badge("FEMALE", color="#5080C3", text_color='white', className="border me-3", style={'fontSize': '16px'}),
                ]),
            ], width=3, style={'marginLeft': '0px'}),
        ], style={'backgroundColor': 'navy', 'marginBottom': '15px'}),

        dbc.Col([
            dbc.CardBody([
                html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'}),
                            html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_ethn_all_total',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_ethn_all_percent',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                html.Br(),
                html.Div([html.Span('Akan: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_akan_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_akan',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),
                html.Div([html.Span('Ga-Adangme: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_ga_adangme_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_ga_adangme',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Ewe: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_ewe_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_ewe',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Guan: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_guan_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_guan',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Gurma: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_gurma_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_gurma',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Mole-Dagbani: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_mole_dagbani_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_mole_dagbani',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Grusi: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_grusi_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_grusi',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),

                html.Div([html.Span('Mande: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_mande_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_mande',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),

                html.Div([html.Span('Others: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_others_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_others',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),
            ]),
        ], width=3, style={'marginTop': '0px'}),

        # MALE
        dbc.Col([
            dbc.CardBody([
                html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'}),
                            html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_ethn_male_total',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_ethn_male_percent',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                html.Br(),
                html.Div([html.Span('Akan: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_akan_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_akan_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),
                html.Div([html.Span('Ga-Adangme: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_ga_adangme_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_ga_adangme_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Ewe: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_ewe_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_ewe_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Guan: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_guan_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_guan_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Gurma: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_gurma_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_gurma_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Mole-Dagbani: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_mole_dagbani_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_mole_dagbani_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Grusi: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_grusi_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_grusi_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),

                html.Div([html.Span('Mande: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_mande_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_mande_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),

                html.Div([html.Span('Others: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_others_male_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_others_male',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),
            ]),
        ], width=3, style={'marginTop': '0px'}),

        # FEMALE
        dbc.Col([
            dbc.CardBody([
                html.Span('Total: ', style={'color': 'white', 'fontWeight': 'bold'}),
                            html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_ethn_female_total',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_ethn_female_percent',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                html.Br(),
                html.Div([html.Span('Akan: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_akan_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_akan_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),
                html.Div([html.Span('Ga-Adangme: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_ga_adangme_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_ga_adangme_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Ewe: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_ewe_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_ewe_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Guan: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_guan_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_guan_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Gurma: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_gurma_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_gurma_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Mole-Dagbani: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_mole_dagbani_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_mole_dagbani_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                          ]),

                html.Div([html.Span('Grusi: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_grusi_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_grusi_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),

                html.Div([html.Span('Mande: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_mande_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_mande_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),

                html.Div([html.Span('Others: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='bg_others_female_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='bg_others_female',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),
            ]),
        ], width=3, style={'marginTop': '0px'}),

    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),

    # INSURANCE COVERAGE
    html.Hr(),
    html.H3(id='insurance'),
    html.H3('Insurance Coverage',
            style={'color': 'navy', 'marginLeft': '18px'}),

    dbc.Row([
        dbc.Col([
            dbc.CardBody([
                dbc.Badge("GENERAL STATISTICS", color="#2e7d32", text_color='white', className="border me-3",
                          style={'fontSize': '16px'}),
            ]),

            #REGION
            dbc.CardBody([
                html.Div([html.Span('Regional Share: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_reg_total_pop_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),

                                    html.Td([
                                      dbc.Badge(
                                          id='insu_reg_percent_pop_val',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                ]),

                    html.Div([html.Span('Total Covered, Region: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_reg_total_pop_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_reg_total_pop_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),
                ]),

                html.Div([html.Span('Males Covered, Region: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_reg_male_pop_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_reg_male_pop_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                ]),

                html.Div([html.Span('Females Covered, Region: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_reg_female_pop_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_reg_female_pop_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),
            ]),

        ], width=3, style={'marginTop': '0px'}),

        #DISTRICT COVERED
        dbc.Col([
            dbc.CardBody([
                dbc.Badge("DISTRICT, COVERED", color="#2e7d32", text_color='white', className="border me-3",
                          style={'fontSize': '16px'}),
            ]),
            dbc.CardBody([
                html.Div([html.Span('Population, District: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_dist_pop_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),

                                  html.Td([
                                      dbc.Badge(
                                          id='insu_dist_pop_val_percent',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),
                              ])
                          ], style={'float': 'right'}),

                ]),

                html.Div([html.Span('Total, Covered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_dist_total_pop_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_dist_total_pop_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                ]),

                html.Div([html.Span('Males, Covered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_dist_male_pop_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_dist_male_pop_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                ]),

                html.Div([html.Span('Females, Covered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_dist_female_pop_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_dist_female_pop_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                ]),
            ]),
        ], width=3, style={'marginTop': '0px'}),

        #DISTRICT, NOT COVERED
        dbc.Col([
            dbc.CardBody([
                dbc.Badge("DISTRICT, NOT COVERED", color="#2e7d32", text_color='white', className="border me-3",
                          style={'fontSize': '16px'}),
            ]),
            dbc.CardBody([
                html.Div([html.Span('Population, District: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_dist_pop_not_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),

                                   html.Td([
                                      dbc.Badge(
                                          id='insu_dist_pop_not_val_percent',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),

                html.Div([html.Span('Total, Not Covered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_dist_total_pop_not_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_dist_total_pop_not_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),

                html.Div([html.Span('Males, Not Covered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_dist_male_pop_not_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_dist_male_pop_not_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),

                html.Div([html.Span('Females, Not Covered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_dist_female_pop_not_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_dist_female_pop_not_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                          ]),
            ]),
        ], width=2, style={'marginTop': '0px'}),

        #URBAN
        dbc.Col([
            dbc.CardBody([
                dbc.Badge("URBAN", color="#2e7d32", text_color='white', className="border me-3",
                          style={'fontSize': '16px'}),
            ]),
            dbc.CardBody([

                html.Div([html.Span('Population, Urban: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_urban_pop_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),

                                    html.Td([
                                      dbc.Badge(
                                          id='insu_urban_pop_val_percent',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),
                              ])
                          ], style={'float': 'right'}),

                ]),

                html.Div([html.Span('Urban, Covered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_pop_urban_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_pop_urban_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                ]),

                html.Div([html.Span('Urban, Not Covered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_pop_urban_not_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_pop_urban_not_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                ]),
            ]),
        ], width=2, style={'marginTop': '0px'}),

        #RURAL
        dbc.Col([
            dbc.CardBody([
                dbc.Badge("RURAL", color="#2e7d32", text_color='white', className="border me-3",
                          style={'fontSize': '16px'}),
            ]),
            dbc.CardBody([
                html.Div([html.Span('Population, Rural: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_rural_pop_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),

                                   html.Td([
                                      dbc.Badge(
                                          id='insu_rural_pop_val_percent',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),
                              ])
                          ], style={'float': 'right'}),

                          ]),

                html.Div([html.Span('Rural, Covered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_pop_rural_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_pop_rural_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                ]),

                html.Div([html.Span('Rural, Not Covered: ', style={'color': 'white'}),
                          html.Table([
                              html.Tr([
                                  html.Td([
                                      html.Span(id='insu_pop_rural_not_cov_val',
                                                style={'color': '#eca50b', 'fontWeight': 'bold',
                                                       'fontSize': '14px',
                                                       'float': 'right'}),
                                  ]),
                                  html.Td([
                                      dbc.Badge(
                                          id='insu_pop_rural_not_cov',
                                          color="#1b5e20",
                                          pill=True,
                                          text_color="white",
                                          className='',
                                          style={'float': 'right', }
                                      ),
                                  ]),

                              ])
                          ], style={'float': 'right'}),

                ]),
            ]),
        ], width=2, style={'marginTop': '0px'}),

    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),

])

def create_bg_xtics():
    layout = html.Div([
        nav,
        header
    ])

    return layout