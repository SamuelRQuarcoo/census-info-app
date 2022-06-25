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

    html.H2('LITERACY & EDUCATION', style={'color': 'navy', 'margin': '10px', 'backgroundColor': 'white'}),
    dbc.Row([

        html.Hr(),

        # regions
        dbc.Col([
            html.Span('REGION', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='lit_edu_region_dd',
                style={'color': 'black'},
                options=[{'label': REGION, 'value': REGION} for REGION in REGIONS]
            ),
        ], width=2, style={'marginLeft': '10px', 'marginTop': '5px', 'marginBottom': '5px'}),

        html.Br(),

        dbc.Col([
            html.Span('DISTRICT', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='lit_edu_district_dd',
                style={'color': 'black'},
            ),
        ], width=2, style={'marginLeft': '-10px', 'marginTop': '5px', 'marginBottom': '5px'}),

        html.Br(),

        dbc.Col([
            dbc.Button('CLEAR',
                       id='clear_lit_edu_btn',
                       n_clicks=0,
                       className='me-1',
                       size='lg',
                       style={'marginTop': '20px'},
                       ),
        ], width=1,
            style={'marginLeft': '30px', 'marginTop': '5px', 'marginBottom': '5px', 'fontWeight': 'bold'}),

        html.Span(id='district_label', style={'color': 'red', 'marginLeft': '10px'}),

    ], style={'backgroundColor': '#eeeff3', 'color': 'navy', 'fontSize': '18px', 'paddingBottom': '10px'}),

    html.Br(),

    #LITERACY RATES - 3D3a
    html.H3([
        html.Span('Literacy Rates (%) | Population 15 years and older', style={'color': 'navy', 'marginLeft': '18px'}),
        ]),

    dbc.Row([
        dbc.Col([
            dbc.CardBody([html.H4('BOTH SEXES', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                  html.Span([html.H5(id='lit_edu_all_lit',
                                     style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'align': 'right'})]),
            ]),

        ], width=1, style={'marginLeft': '0px'}),

        #ALL, MALE
        dbc.Col([
            dbc.CardBody([html.H4('MALE', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                  html.Span([html.H5(id='lit_edu_all_male_lit',
                                     style={'color': '#eca50b', 'fontWeight': 'bold',
                                            'fontSize': '18px', 'align': 'right'})]),
            ]),

        ], width=1, style={'marginLeft': '0px'}),

        #ALL, FEMALE
        dbc.Col([
            dbc.CardBody([html.H4('FEMALE', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                          html.Span([html.H5(id='lit_edu_all_female_lit',
                                     style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'align': 'right'})]),
                          ]),

        ], width=2, style={'marginLeft': '0px'}),

        #URBAN, MALE
        dbc.Col([
            dbc.CardBody([html.H4('URBAN, MALE', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                          html.Span([html.H5(id='lit_edu_urban_male_lit',
                                             style={'color': '#eca50b', 'fontWeight': 'bold',
                                                    'fontSize': '18px', 'align': 'right'})])
                          ]),

        ], class_name='borderRight', width=2, style={'marginLeft': '0px'}),

        #URBAN, FEMALE
        dbc.Col([
            dbc.CardBody(
                [html.H4('URBAN, FEMALE', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                 html.Span([html.H5(id='lit_edu_urban_female_lit',
                                    style={'color': '#eca50b', 'fontWeight': 'bold',
                                           'fontSize': '18px', 'align': 'right'})]),
                 ]),

        ], width=2, style={'marginLeft': '0px'}),

        dbc.Col([
            dbc.CardBody(
                [html.H4('RURAL, MALE', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                 html.Span([html.H5(id='lit_edu_rural_male_lit',
                                    style={'color': '#eca50b', 'fontWeight': 'bold',
                                           'fontSize': '18px', 'align': 'right'})]),
                 ]),

        ], width=1, style={'marginLeft': '0px'}),

        dbc.Col([
            dbc.CardBody(
                [html.H4('RURAL, FEMALE', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                 html.Span([html.H5(id='lit_edu_rural_female_lit',
                                    style={'color': '#eca50b', 'fontWeight': 'bold',
                                           'fontSize': '18px', 'align': 'right'})]),
                 ]),

        ], width=2, style={'marginLeft': '0px'}),

    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),


    dbc.Row([
        dbc.Col([
            dbc.CardBody([html.H4('-', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),

            ]),

        ], width=1, style={'marginLeft': '0px'}),

        dbc.Col([
            dbc.CardBody([html.H4('-', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),

          ]),
        ], width=1, style={'marginLeft': '0px'}),

        dbc.Col([
            dbc.CardBody([html.H4('-', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),

          ]),
        ], width=2, style={'marginLeft': '0px'}),

        dbc.Col([
            dbc.CardBody([html.H4('URBAN, BOTH', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                          html.Span([html.H5(id='lit_edu_urban_both_lit',
                                             style={'color': '#eca50b', 'fontWeight': 'bold',
                                                    'fontSize': '18px', 'align': 'right'})])
                          ]),

        ], width=4, style={'marginLeft': '0px'}),

        #RURAL, BOTH
        dbc.Col([
            dbc.CardBody(
                [html.H4('RURAL, BOTH', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                 html.Span([html.H5(id='lit_edu_rural_both_lit',
                                    style={'color': '#eca50b', 'fontWeight': 'bold',
                                           'fontSize': '18px', 'align': 'right'})]),
                 ]),
        ], width=2, style={'marginLeft': '0px'}),

    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),

    html.Hr(),
    html.H3('School Attendance Status (%) | Population 3 years and older', style={'color': 'navy', 'marginLeft': '18px'}),

    #SCHOOl ATTENDANCE STATUS - 3D6a
    dbc.Row([
        dbc.Col([
            dbc.CardBody([
                  html.H5([
                    html.H5('ALL', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px', 'marginLeft': '180px'}),
                    html.Span('CURRENT: ', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                    html.Span(id='lit_edu_att_all_now', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft':'100px'}),
                  ]),
                  html.H5([
                    html.Span('PAST: ', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px', 'align': 'right'}),
                    html.Span(id='lit_edu_att_all_past', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '135px'}),
                  ]),
                  html.H5([
                    html.Span('NEVER: ', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px', 'align': 'right'}),
                    html.Span(id='lit_edu_att_all_never', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '120px'}),
                  ]),
            ]),

        ], width=2, style={'marginLeft': '0px'}),

        # ALL, MALE
        dbc.Col([
            dbc.CardBody([html.H4('ALL, MALE', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                  html.H5([html.Span(id='lit_edu_att_all_male_now', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                  html.H5([html.Span(id='lit_edu_att_all_male_past',style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                  html.H5([html.Span(id='lit_edu_att_all_male_never',style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
            ]),

        ], width=1, style={'marginLeft': '0px'}),

        # ALL, FEMALE
        dbc.Col([
            dbc.CardBody([html.H4('ALL, FEMALE', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                  html.H5([html.Span(id='lit_edu_att_all_female_now', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                  html.H5([html.Span(id='lit_edu_att_all_female_past', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                  html.H5([html.Span(id='lit_edu_att_all_female_never', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
            ]),

        ], width=1, style={'marginLeft': '0px'}),

        # URBAN, ALL
        dbc.Col([
            dbc.CardBody(
                [html.H4('URBAN, ALL', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                 html.H5([html.Span(id='lit_edu_att_all_urban_now', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                 html.H5([html.Span(id='lit_edu_att_all_urban_past', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                html.H5([html.Span(id='lit_edu_att_all_urban_never', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
             ]),
        ], width=1, style={'marginLeft': '0px'}),

        # URBAN, MALE
        dbc.Col([
            dbc.CardBody(
                [html.H4('URBAN, MALE', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                 html.H5([html.Span(id='lit_edu_att_urban_male_now', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                 html.H5([html.Span(id='lit_edu_att_urban_male_past', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                 html.H5([html.Span(id='lit_edu_att_urban_male_never', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
             ]),
        ], width=1, style={'marginLeft': '0px'}),

        # URBAN, FEMALE
        dbc.Col([
            dbc.CardBody(
                [html.H4('URBAN, FEMALE', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                 html.H5([html.Span(id='lit_edu_att_urban_female_now', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                 html.H5([html.Span(id='lit_edu_att_urban_female_past', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                 html.H5([html.Span(id='lit_edu_att_urban_female_never', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
            ]),
        ], width=2, style={'marginLeft': '0px'}),

        #RURAL, ALL
        dbc.Col([
            dbc.CardBody(
                [html.H4('RURAL, ALL', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                 html.H5([html.Span(id='lit_edu_att_all_rural_now', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                 html.H5([html.Span(id='lit_edu_att_all_rural_past', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                 html.H5([html.Span(id='lit_edu_att_all_rural_never', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
             ]),
        ], width=1, style={'marginLeft': '0px'}),

        #RURAL, MALE
        dbc.Col([
            dbc.CardBody(
                [html.H4('RURAL, MALE', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                 html.H5([html.Span(id='lit_edu_att_rural_male_now', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                 html.H5([html.Span(id='lit_edu_att_rural_male_past', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                 html.H5([html.Span(id='lit_edu_att_rural_male_never', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
            ]),
        ], width=1, style={'marginLeft': '0px'}),

        # RURAL, FEMALE
        dbc.Col([
            dbc.CardBody(
                [html.H4('RURAL, FEMALE', style={'color': 'white', 'fontWeight': 'bold', 'fontSize': '16px'}),
                 html.H5([html.Span(id='lit_edu_att_rural_female_now', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                 html.H5([html.Span(id='lit_edu_att_rural_female_past', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
                 html.H5([html.Span(id='lit_edu_att_rural_female_never', style={'color': '#eca50b', 'fontWeight': 'bold', 'fontSize': '18px', 'marginLeft': '5px'})]),
             ]),
        ], width=2, style={'marginLeft': '0px'}),

    ], style={'backgroundColor': 'navy', 'marginBottom': '0px'}),

])

def create_lit_edu():
    layout = html.Div([
        nav,
        header
    ])

    return layout