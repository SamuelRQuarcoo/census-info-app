#***********************************************************************************************************************
#   DEVELOPER:      Samuel Roanne Quarcoo
#   Date:           February 2022
#   Description:    Census Results Dashboard
#**********************************************************************************************************************

#IMPORTS
import app as app
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

#custom pages
from home import create_page_home
from national import create_national
from region_district import create_region_district
from age_sex import create_age_sex
from bg_xtics import create_bg_xtics
from lit_edu import create_lit_edu
from diff_perf_act import create_diff_perf_act
from fert_mort import create_fert_mort
from housing import create_housing
from water_sanitation import create_water_sanitation
from structures import create_structures
from economic_activity import create_economic_activity
from population_pyramid import create_population_pyramid
from ict import create_ict

import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output
import pandas as pd
from flask import send_from_directory
import os
import re
import numpy as np
from PIL import Image
import plotly.express as px

#***********************************************************************************************************************
#                                             DATAFRAMES
#***********************************************************************************************************************

#Census Population Figure
census_figure = 30800000

#REGION & DISTRICTS SETUP
df_reg_dist_setup = pd.read_csv('data/reg_dist_setup.csv')

#POPULATION
df_pop_reg_distr_by_sex = pd.read_csv('data/population/pop_region_district_by_sex.csv')
df_pop_district_profile = pd.read_csv('data/population/pop_district_profile.csv')

#AGE & SEX
df_age_sex_range = pd.read_csv('data/age_sex/age_sex_age_range.csv')

#BACKGROUND CHARACTERISTICS
#marital
db_data_dir = 'data/background_xtics/'

df_bg_xtics_setup = pd.read_csv(db_data_dir + 'setup.csv')

df_bg_xtics_3C2b_western = pd.read_csv(db_data_dir + 'marital_status/bg_xtics_3C2b_western.csv')
df_bg_xtics_3C2b_central = pd.read_csv('data/background_xtics/marital_status/bg_xtics_3C2b_central.csv')
df_bg_xtics_3C2b_greater_accra = pd.read_csv(db_data_dir + 'marital_status/bg_xtics_3C2b_greater_accra.csv')
df_bg_xtics_3C2b_volta = pd.read_csv(db_data_dir + 'marital_status/bg_xtics_3C2b_volta.csv')
df_bg_xtics_3C2b_eastern = pd.read_csv(db_data_dir + 'marital_status/bg_xtics_3C2b_eastern.csv')
df_bg_xtics_3C2b_ashanti = pd.read_csv('data/background_xtics/marital_status/bg_xtics_3C2b_ashanti.csv')
#df_bg_xtics_3C2b_western_north = pd.read_csv(db_data_dir + 'marital_status/bg_xtics_3C2b_western_north.csv')
df_bg_xtics_3C2b_ahafo = pd.read_csv(db_data_dir + 'marital_status/bg_xtics_3C2b_ahafo.csv')
df_bg_xtics_3C2b_bono = pd.read_csv(db_data_dir + 'marital_status/bg_xtics_3C2b_bono.csv')
df_bg_xtics_3C2b_bono_east = pd.read_csv('data/background_xtics/marital_status/bg_xtics_3C2b_bono_east.csv')
df_bg_xtics_3C2b_oti = pd.read_csv(db_data_dir + 'marital_status/bg_xtics_3C2b_oti.csv')
df_bg_xtics_3C2b_northern = pd.read_csv('data/background_xtics/marital_status/bg_xtics_3C2b_northern.csv')
#df_bg_xtics_3C2b_savannah = pd.read_csv(db_data_dir + 'marital_status/bg_xtics_3C2b_savannah.csv')
#df_bg_xtics_3C2b_north_east = pd.read_csv(db_data_dir + 'marital_status/bg_xtics_3C2b_north_east.csv')
#df_bg_xtics_3C2b_upper_east = pd.read_csv(db_data_dir + 'marital_status/bg_xtics_3C2b_upper_east.csv')
#df_bg_xtics_3C2b_upper_west = pd.read_csv(db_data_dir + 'marital_status/bg_xtics_3C2b_upper_west.csv')

#ethnicity
df_bg_xtics_3C3a_western = pd.read_csv(db_data_dir + 'ethnicity/bg_xtics_3C3a_western.csv')
df_bg_xtics_3C3a_central = pd.read_csv(db_data_dir + 'ethnicity/bg_xtics_3C3a_central.csv')

#insurance
df_bg_xtics_3C8a_all = pd.read_csv(db_data_dir + 'insurance/bg_xtics_3C8a_all.csv')

bg_xtics_region_3C2b = {

    'Western': df_bg_xtics_3C2b_western,
    'Central': df_bg_xtics_3C2b_central,
    'Greater Accra': df_bg_xtics_3C2b_greater_accra,
    'Volta': df_bg_xtics_3C2b_volta,
    'Eastern': df_bg_xtics_3C2b_eastern,
    'Ashanti': df_bg_xtics_3C2b_ashanti,
    #'Western North': df_bg_xtics_3C2b_western_north,
    'Ahafo': df_bg_xtics_3C2b_ahafo,
    'Bono': df_bg_xtics_3C2b_bono,
    'Bono East': df_bg_xtics_3C2b_bono_east,
    'Oti': df_bg_xtics_3C2b_oti,
    'Northern': df_bg_xtics_3C2b_northern,
    #'Savannah': df_bg_xtics_3C2b_savannah,
    #'North East': df_bg_xtics_3C2b_north_east,
    #'Upper East': df_bg_xtics_3C2b_upper_east,
    #'Upper West': df_bg_xtics_3C2b_upper_west
}

#DIFFICULTY IN PERFORMING ACTIVITIES
df_dpa_data_dir = 'data/diff_perf_act/'
df_diff_perf_act_3F2a_western = pd.read_csv(df_dpa_data_dir + 'diff_perf_act_3F2a_western.csv')
df_diff_perf_act_3F5a_western = pd.read_csv(df_dpa_data_dir + 'dpa_3F5a_all_domains_western.csv')

df_diff_perf_act_3F2a_central = pd.read_csv(df_dpa_data_dir + 'diff_perf_act_3F2a_central.csv')

dpa_categories = ['Seeing', 'Hearing', 'Walking & Climbing Stairs', 'Remembering & Concentrating', 'Self-Care', 'Communicating']

#LITERACY & EDUCATION
lit_edu_dir_3D3a = 'data/literacy_education/3D3a/'
lit_edu_dir_3D6a = 'data/literacy_education/3D6a/'

#TABLE 3D3a
df_lit_edu_setup                = pd.read_csv('data/literacy_education/lit_edu.csv')
df_lit_edu_3D3a_western         = pd.read_csv(lit_edu_dir_3D3a + 'western_3D3a.csv')
df_lit_edu_3D3a_central         = pd.read_csv(lit_edu_dir_3D3a + 'central_3D3a.csv')
df_lit_edu_3D3a_greater_accra   = pd.read_csv(lit_edu_dir_3D3a + 'greater_accra_3D3a.csv')
df_lit_edu_3D3a_volta           = pd.read_csv(lit_edu_dir_3D3a + 'volta_3D3a.csv')
df_lit_edu_3D3a_eastern         = pd.read_csv(lit_edu_dir_3D3a + 'eastern_3D3a.csv')
df_lit_edu_3D3a_ashanti         = pd.read_csv(lit_edu_dir_3D3a + 'ashanti_3D3a.csv')
df_lit_edu_3D3a_western_north   = pd.read_csv(lit_edu_dir_3D3a + 'western_north_3D3a.csv')
df_lit_edu_3D3a_ahafo           = pd.read_csv(lit_edu_dir_3D3a + 'ahafo_3D3a.csv')
df_lit_edu_3D3a_bono            = pd.read_csv(lit_edu_dir_3D3a + 'bono_3D3a.csv')
df_lit_edu_3D3a_bono_east       = pd.read_csv(lit_edu_dir_3D3a + 'bono_east_3D3a.csv')
df_lit_edu_3D3a_oti             = pd.read_csv(lit_edu_dir_3D3a + 'oti_3D3a.csv')
df_lit_edu_3D3a_northern        = pd.read_csv(lit_edu_dir_3D3a + 'northern_3D3a.csv')
df_lit_edu_3D3a_savannah        = pd.read_csv(lit_edu_dir_3D3a + 'savannah_3D3a.csv')
df_lit_edu_3D3a_north_east      = pd.read_csv(lit_edu_dir_3D3a + 'north_east_3D3a.csv')
df_lit_edu_3D3a_upper_east      = pd.read_csv(lit_edu_dir_3D3a + 'upper_east_3D3a.csv')
df_lit_edu_3D3a_upper_west      = pd.read_csv(lit_edu_dir_3D3a + 'upper_west_3D3a.csv')

lit_edu_region_3D3a = {

    'Western': df_lit_edu_3D3a_western,
    'Central': df_lit_edu_3D3a_central,
    'Greater Accra': df_lit_edu_3D3a_greater_accra,
    'Volta': df_lit_edu_3D3a_volta,
    'Eastern': df_lit_edu_3D3a_eastern,
    'Ashanti': df_lit_edu_3D3a_ashanti,
    'Western North': df_lit_edu_3D3a_western_north,
    'Ahafo': df_lit_edu_3D3a_ahafo,
    'Bono': df_lit_edu_3D3a_bono,
    'Bono East': df_lit_edu_3D3a_bono_east,
    'Oti': df_lit_edu_3D3a_oti,
    'Northern': df_lit_edu_3D3a_northern,
    'Savannah': df_lit_edu_3D3a_savannah,
    'North East': df_lit_edu_3D3a_north_east,
    'Upper East': df_lit_edu_3D3a_upper_east,
    'Upper West': df_lit_edu_3D3a_upper_west

}

#TABLE 3D6a
df_lit_edu_3D6a_western         = pd.read_csv(lit_edu_dir_3D6a + 'western_3D6a.csv')
df_lit_edu_3D6a_central         = pd.read_csv(lit_edu_dir_3D6a + 'central_3D6a.csv')
df_lit_edu_3D6a_greater_accra   = pd.read_csv(lit_edu_dir_3D6a + 'greater_accra_3D6a.csv')
df_lit_edu_3D6a_volta           = pd.read_csv(lit_edu_dir_3D6a + 'volta_3D6a.csv')
df_lit_edu_3D6a_eastern         = pd.read_csv(lit_edu_dir_3D6a + 'eastern_3D6a.csv')
df_lit_edu_3D6a_ashanti         = pd.read_csv(lit_edu_dir_3D6a + 'ashanti_3D6a.csv')
df_lit_edu_3D6a_western_north   = pd.read_csv(lit_edu_dir_3D6a + 'western_north_3D6a.csv')
df_lit_edu_3D6a_ahafo           = pd.read_csv(lit_edu_dir_3D6a + 'ahafo_3D6a.csv')
df_lit_edu_3D6a_bono            = pd.read_csv(lit_edu_dir_3D6a + 'bono_3D6a.csv')
df_lit_edu_3D6a_bono_east       = pd.read_csv(lit_edu_dir_3D6a + 'bono_east_3D6a.csv')
df_lit_edu_3D6a_oti             = pd.read_csv(lit_edu_dir_3D6a + 'oti_3D6a.csv')
df_lit_edu_3D6a_northern        = pd.read_csv(lit_edu_dir_3D6a + 'northern_3D6a.csv')
df_lit_edu_3D6a_savannah        = pd.read_csv(lit_edu_dir_3D6a + 'savannah_3D6a.csv')
df_lit_edu_3D6a_north_east      = pd.read_csv(lit_edu_dir_3D6a + 'north_east_3D6a.csv')
df_lit_edu_3D6a_upper_east      = pd.read_csv(lit_edu_dir_3D6a + 'upper_east_3D6a.csv')
df_lit_edu_3D6a_upper_west      = pd.read_csv(lit_edu_dir_3D6a + 'upper_west_3D6a.csv')

lit_edu_region_3D6a = {

    'Western': df_lit_edu_3D6a_western,
    'Central': df_lit_edu_3D6a_central,
    'Greater Accra': df_lit_edu_3D6a_greater_accra,
    'Volta': df_lit_edu_3D6a_volta,
    'Eastern': df_lit_edu_3D6a_eastern,
    'Ashanti': df_lit_edu_3D6a_ashanti,
    #'Western North': df_lit_edu_3D6a_western_north,
    'Ahafo': df_lit_edu_3D6a_ahafo,
    'Bono': df_lit_edu_3D6a_bono,
    'Bono East': df_lit_edu_3D6a_bono_east,
    'Oti': df_lit_edu_3D6a_oti,
    'Northern': df_lit_edu_3D6a_northern,
    'Savannah': df_lit_edu_3D6a_savannah,
    'North East': df_lit_edu_3D6a_north_east,
    'Upper East': df_lit_edu_3D6a_upper_east,
    'Upper West': df_lit_edu_3D6a_upper_west

}

literacy_status = ['Total', 'Not literate', 'Literate']
literacy_indicator_type = ['All', 'All Male', 'All Female', 'Urban Both', 'Urban Male', 'Urban Female', 'Rural Both', 'Rural Male', 'Rural Female']

#FERTILITY & MORTALITY
df_fert_mort = pd.read_csv('data/fertility_mortality/fertility_mortality_3H5a.csv')

#HOUSING
df_housing = pd.read_csv('data/housing/housing_3K1a.csv')

# WATER & SANITATION
df_water_sanit_western = pd.read_csv('data/water_sanitation/water_sanitation_3M1a_western.csv')
df_water_sanitation_dic = {

    'Western': df_water_sanit_western
}

#STRUCTURES
df_structures_western = pd.read_csv('data/structures/structure_3N1a_all_western.csv')
df_structures_dic = {
    'Western': df_structures_western
}

#ECONOMIC ACTIVITIES
df_econ_act_western = pd.read_csv('data/economic_activity/econ_act_3E1a_western.csv')
df_econ_act_dic = {
    'Western': df_econ_act_western
}

# ICT
df_ict_western = pd.read_csv('data/ict/ict_3G1_western.csv')
df_ict_dic = {
    'Western': df_ict_western
}
#***********************************************************************************************************************
# Add css file (locally hosted)
local_css_file = "static/m_custom.css"
assets_path = os.getcwd() +'/assets'

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, local_css_file], assets_folder=assets_path)
server = app.server

app.layout = html.Div([
        dbc.Row([
            dbc.Col([
                html.Img(src=app.get_asset_url('logo-censusinfo.png'), alt='GSS logo',
                    style={'width': '200px', 'height': '80%', 'margin': '5px'}),
            ], width=2),
            dbc.Col([
                html.H3('GHANA 2021 POPULATION AND HOUSING CENSUS',
                    style={'background-color': 'white', 'color': 'navy', 'text-align': 'center', 'fontWeight': 'bold', 'fontSize': '20px',
                           'padding-top': '3px', 'padding-bottom': '3px'}),
                html.H1('OFFICIAL STATISTICS', style={'background-color': 'white', 'color': '#FFC300', 'fontWeight': 'bold', 'text-align': 'center',
                              'padding-top': '2px', 'padding-bottom': '2px'}),
            ], width=8)
        ], className='text-center'),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')]
)

# pathnames and pages dictionary
path_to_pages_dic = {
    '/national': create_national(),
    '/region_district': create_region_district(),
    '/age_sex': create_age_sex(),
    '/bg_xtics': create_bg_xtics(),
    '/lit_edu': create_lit_edu(),
    '/diff_perf_act': create_diff_perf_act(),
    '/fert_mort': create_fert_mort(),
    '/housing': create_housing(),
    '/structures': create_structures(),
    '/water_sanitation': create_water_sanitation(),
    '/economic_activity': create_economic_activity(),
    '/population_pyramid': create_population_pyramid(),
    '/ict': create_ict(),
}

#******************************************
#LOAD DATA PAGES BASED ON URL OF MENU ITEMS
#******************************************
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname != None:
        return path_to_pages_dic[pathname]
    else:
        # #when index page loads, use home layout to create page
        return create_page_home()

    # if pathname == '/national':
    #     return create_national()
    # if pathname == '/region_district':
    #     return create_region_district()
    # if pathname == '/age_sex':
    #     return create_age_sex()
    # if pathname == '/bg_xtics':
    #     return create_bg_xtics();
    # if pathname == '/lit_edu':
    #     return create_lit_edu()
    # if pathname == '/diff_perf_act':
    #     return create_diff_perf_act()
    # if pathname =='/fert_mort':
    #     return create_fert_mort()
    # if pathname == '/housing':
    #     return create_housing()
    # if pathname == '/water_sanitation':
    #     return create_water_sanitation()
    # if pathname == '/structures':
    #     return create_structures()
    # if pathname == '/economic_activity':
    #     return create_economic_activity()
    #
    # else:
    #     #when index page loads, use home layout to create page
    #     return create_page_home()

#*****************************************************************************
#   REGIONS AND DISTRICTS SETUPS - CALLBACKS
#*****************************************************************************

# population of regions & districts
@app.callback(
    Output('pop_reg_dist_district_dd', 'options'),
    Input('pop_reg_dist_region_dd', 'value'),
)
def get_districts_pop(region):

    options_districts = []

    if region != None:

        df_districts = df_reg_dist_setup[(df_reg_dist_setup['REGION'] == region) & (df_reg_dist_setup['IS_DISTRICT'] == 1)]['DISTRICT']
        df_districts = df_districts.unique()
        df_districts = sorted(df_districts)

        options_districts = [{'label': opt, 'value': opt} for opt in df_districts]

    return options_districts


# age and sex
@app.callback(
    Output('age_sex_district_dd', 'options'),
    Input('age_sex_region_dd', 'value'))
def get_districts_age_sex(region):

    options_districts = []

    #print(region)
    if region != None:
        df_districts = df_age_sex_range[df_age_sex_range['REGION'] == region]['DISTRICT']
        df_districts = df_districts.unique()
        df_districts = sorted(df_districts)

        options_districts = [{'label': opt, 'value': opt} for opt in df_districts]

    return options_districts

#age groups
@app.callback(
    Output('age_sex_group_dd', 'options'),
    [Input('age_sex_district_dd', 'value')])
def get_districts_age_sex_group(district):

    options_age_groups = []

    if district != None:

        df_age_group = df_age_sex_range[df_age_sex_range['DISTRICT'] == district]['AGE_GROUP']
        #df_age_group = sorted(df_age_group)

        options_age_groups = [{'label': opt, 'value': opt} for opt in df_age_group]

    return options_age_groups

# #background characteristics
@app.callback(
    Output('bg_xtics_district_dd', 'options'),
    [Input('bg_xtics_region_dd', 'value')])
def get_districts_bg_xtics(region):

    options_districts = []

    if region != None:

        df_districts = df_bg_xtics_setup[(df_bg_xtics_setup['REGION'] == region) & (df_bg_xtics_setup['IS_DISTRICT'] == 1)]['DISTRICT']
        df_districts = df_districts.unique()
        df_districts = sorted(df_districts)

        #print(df_districts)

        options_districts = [{'label': opt, 'value': opt} for opt in df_districts]

    return options_districts

# #literacy & education
@app.callback(
    Output('lit_edu_district_dd', 'options'),
    [Input('lit_edu_region_dd', 'value')])
def get_districts_lit_educ(region):

    options_districts = []

    if region != None:

        df_districts = df_lit_edu_setup[(df_lit_edu_setup['REGION'] == region) & (df_lit_edu_setup['IS_DISTRICT'] == 1)]['DISTRICT']
        df_districts = df_districts.unique()
        df_districts = sorted(df_districts)

        options_districts = [{'label': opt, 'value': opt} for opt in df_districts]

    return options_districts

# population pyramid
@app.callback(
    Output('pyramid_district_dd', 'options'),
    [Input('pyramid_region_dd', 'value')])
def get_districts_population_pyramid(region):

    options_districts = []

    if region != None:

        df_districts = df_lit_edu_setup[(df_lit_edu_setup['REGION'] == region) & (df_lit_edu_setup['IS_DISTRICT'] == 1)]['DISTRICT']
        df_districts = df_districts.unique()
        df_districts = sorted(df_districts)

        options_districts = [{'label': opt, 'value': opt} for opt in df_districts]

    return options_districts

# #performing activities
@app.callback(
    Output('dpa_district_dd', 'options'),
    [Input('dpa_region_dd', 'value')])
def get_districts_diff_perf_act(region):

    options_districts = []

    if region != None:

        df_districts = df_reg_dist_setup[(df_reg_dist_setup['REGION'] == region) & (df_reg_dist_setup['IS_DISTRICT'] == 1)]['DISTRICT']
        df_districts = df_districts.unique()
        df_districts = sorted(df_districts)

        #print(df_districts)

        options_districts = [{'label': opt, 'value': opt} for opt in df_districts]

    return options_districts

@app.callback(
    Output('dpa_category_dd', 'options'),
    [Input('dpa_district_dd', 'value')])
def get_districts_diff_perf_act(district):

    options_categories = []

    if district != None:

        options_categories = [{'label': opt, 'value': opt} for opt in dpa_categories]

    return options_categories

#fertility & mortality
@app.callback(
    Output('fert_mort_district_dd', 'options'),
    [Input('fert_mort_region_dd', 'value')]
)
def get_districts_fert_mort(region):

    options_districts = []

    if region != None:

        df_districts = df_reg_dist_setup[(df_reg_dist_setup['REGION'] == region) & (df_reg_dist_setup['IS_DISTRICT'] == 1)]['DISTRICT']
        df_districts = df_districts.unique()
        df_districts = sorted(df_districts)

        #print(df_districts)

        options_districts = [{'label': opt, 'value': opt} for opt in df_districts]

    return options_districts

# housing
@app.callback(
    Output('housing_district_dd', 'options'),
    [Input('housing_region_dd', 'value')]
)
def get_districts_housing(region):

    options_districts = []

    if region != None:

        df_districts = df_reg_dist_setup[(df_reg_dist_setup['REGION'] == region) & (df_reg_dist_setup['IS_DISTRICT'] == 1)]['DISTRICT']
        df_districts = df_districts.unique()
        df_districts = sorted(df_districts)

        #print(df_districts)

        options_districts = [{'label': opt, 'value': opt} for opt in df_districts]

    return options_districts

# water & sanitation
@app.callback(
    Output('ws_district_dd', 'options'),
    [Input('ws_region_dd', 'value')]
)
def get_districts_water_sanitation(region):

    options_districts = []

    if region != None:

        df_districts = df_reg_dist_setup[(df_reg_dist_setup['REGION'] == region) & (df_reg_dist_setup['IS_DISTRICT'] == 1)]['DISTRICT']
        df_districts = df_districts.unique()
        df_districts = sorted(df_districts)

        #print(df_districts)

        options_districts = [{'label': opt, 'value': opt} for opt in df_districts]

    return options_districts

# structures
@app.callback(
    Output('struct_district_dd', 'options'),
    [Input('struct_region_dd', 'value')]
)
def get_districts_structures(region):

    options_districts = []

    if region != None:

        df_districts = df_reg_dist_setup[(df_reg_dist_setup['REGION'] == region) & (df_reg_dist_setup['IS_DISTRICT'] == 1)]['DISTRICT']
        df_districts = df_districts.unique()
        df_districts = sorted(df_districts)

        #print(df_districts)

        options_districts = [{'label': opt, 'value': opt} for opt in df_districts]

    return options_districts


# economic activities
@app.callback(
    Output('econ_act_district_dd', 'options'),
    [Input('econ_act_region_dd', 'value')]
)
def get_districts_structures(region):

    options_districts = []

    if region != None:

        df_districts = df_reg_dist_setup[(df_reg_dist_setup['REGION'] == region) & (df_reg_dist_setup['IS_DISTRICT'] == 1)]['DISTRICT']
        df_districts = df_districts.unique()
        df_districts = sorted(df_districts)

        #print(df_districts)

        options_districts = [{'label': opt, 'value': opt} for opt in df_districts]

    return options_districts


# ict
@app.callback(
    Output('ict_district_dd', 'options'),
    [Input('ict_region_dd', 'value')]
)
def get_districts_structures(region):

    options_districts = []

    if region != None:

        df_districts = df_reg_dist_setup[(df_reg_dist_setup['REGION'] == region) & (df_reg_dist_setup['IS_DISTRICT'] == 1)]['DISTRICT']
        df_districts = df_districts.unique()
        df_districts = sorted(df_districts)

        #print(df_districts)

        options_districts = [{'label': opt, 'value': opt} for opt in df_districts]

    return options_districts
#
# #*****************************************************************************
# #   DATA - CALLBACKS:
# #*****************************************************************************
#
#****************************************
#POPULATION OF REGIONS & DISTRICTS BY SEX
#****************************************
@app.callback(

    #region
    Output('total_all', 'children'),                    #total both sexes
    Output('total_percent', 'children'),                #percent region
    Output('total_male', 'children'),                   #male, region, number
    Output('total_male_percent', 'children'),           #male, region, percent
    Output('total_female', 'children'),                 #male, region, number
    Output('total_female_percent', 'children'),         #female, region, number

    Output('urban_all_total', 'children'),
    Output('total_male_urban', 'children'),
    Output('total_female_urban', 'children'),

    Output('rural_all_total', 'children'),
    Output('total_male_rural', 'children'),
    Output('total_female_rural', 'children'),

    Output('reg_area_km_2', 'children'),                   #male, urban
    Output('reg_pop_density', 'children'),                 #female, urban
    Output('reg_no_of_hh', 'children'),                    #female, rural
    Output('reg_avg_hh_size', 'children'),                 #male, rural

    Output('total_dist_all', 'children'),                  #district total,
    Output('male_dist_all', 'children'),                        #male, district, number
    Output('female_dist_all', 'children'),                      #female, district, number

    Output('urban_dist_all', 'children'),                     #male, district, number
    Output('urban_dist_male', 'children'),                     #male, district, number
    Output('urban_dist_female', 'children'),                   #female, district, number

    Output('rural_dist_all', 'children'),                     #male, district, number
    Output('rural_dist_male', 'children'),                     #male, district, number
    Output('rural_dist_female', 'children'),                   #female, district, number

    #district characteristics
    Output('area_km_2', 'children'),  # male, urban
    Output('pop_density', 'children'),  # female, urban
    Output('no_of_hh', 'children'),  # female, rural
    Output('avg_hh_size', 'children'),  # male, rural

    Input('pop_dist_search_btn', 'n_clicks'),
    Input('pop_reg_dist_region_dd', 'value'),
    Input('pop_reg_dist_district_dd', 'value')
)
def get_pop_reg_distr_by_sex(n_clicks, region, district):

    # region
    total_all = None
    total_percent = None
    total_male = None
    total_male_percent = None
    total_female = None
    total_female_percent = None

    urban_all_total = None
    total_male_urban = None
    total_female_urban = None

    rural_all_total = None
    total_male_rural = None
    total_female_rural = None

    reg_area_km_2 = None
    reg_pop_density = None
    reg_no_households = None
    reg_avg_hh_size = None

    total_all_dist = None
    male_dist_all = None
    female_dist_all = None

    urban_dist_all = None
    urban_dist_male = None
    urban_dist_female = None

    rural_dist_all = None
    rural_dist_male = None
    rural_dist_female = None

    area_km_2 = None
    pop_density = None
    no_households = None
    avg_hh_size = None

    if (n_clicks > 0) & (region != None) & (district != None):

        #print(region, district)

        # ALL
        df_total = df_pop_reg_distr_by_sex[(df_pop_reg_distr_by_sex['District'] == 'Total') & (df_pop_reg_distr_by_sex['Locality_Type'] == 'All')][
            ['Region', 'District', 'Total', 'Male', 'Female', 'Locality_Type']]
        df_total = df_total.reset_index(drop=True)

        # regional stats
        total_all = df_total['Total'][0]
        total_percent = (total_all / census_figure) * 100

        total_male = df_total['Male'][0]
        total_female = df_total['Female'][0]

        total_male_percent = (total_male / total_all) * 100
        total_female_percent = (total_female / total_all) * 100

        #region, urban
        df_reg_urban = df_pop_reg_distr_by_sex[(df_pop_reg_distr_by_sex['Region'] == region) &
                                             (df_pop_reg_distr_by_sex['District'] == 'Total') &
                                             (df_pop_reg_distr_by_sex['Status_Code'] == 0) &
                                             (df_pop_reg_distr_by_sex['Locality_Type'] == 'Urban')][
            ['Region', 'District', 'Total', 'Male', 'Female', 'Locality_Type']]
        df_reg_urban = df_reg_urban.reset_index(drop=True)

        urban_all_total = df_reg_urban['Total'][0]
        total_male_urban = df_reg_urban['Male'][0]
        total_female_urban = df_reg_urban['Female'][0]

        # region, rural
        df_reg_rural = df_pop_reg_distr_by_sex[(df_pop_reg_distr_by_sex['Region'] == region) &
                                               (df_pop_reg_distr_by_sex['District'] == 'Total') &
                                               (df_pop_reg_distr_by_sex['Status_Code'] == 0) &
                                               (df_pop_reg_distr_by_sex['Locality_Type'] == 'Rural')][
            ['Region', 'District', 'Total', 'Male', 'Female', 'Locality_Type']]
        df_reg_rural = df_reg_rural.reset_index(drop=True)

        #print(df_reg_rural)
        rural_all_total = df_reg_rural['Total'][0]
        total_male_rural = df_reg_rural['Male'][0]
        total_female_rural = df_reg_rural['Female'][0]


        #regional characteristics
        df_all_profile = df_pop_district_profile[(df_pop_district_profile['Region'] == region) & (df_pop_district_profile['District'] == 'Total')][
                 ['Region', 'District', 'Number', 'Area_Km_2', 'Pop_Density', 'No_of_HH', 'Avg_HH_Size']]  # pop in percent
        df_all_profile = df_all_profile.reset_index(drop=True)

        reg_area_km_2 = df_all_profile['Area_Km_2'][0]
        reg_pop_density = df_all_profile['Pop_Density'][0]
        reg_no_households = df_all_profile['No_of_HH'][0]
        reg_avg_hh_size = df_all_profile['Avg_HH_Size'][0]

        # district statistics
        #all
        df_total_dist = df_pop_reg_distr_by_sex[
            (df_pop_reg_distr_by_sex['District'] == district) & (df_pop_reg_distr_by_sex['Locality_Type'] == 'All')][
            ['Region', 'District', 'Total', 'Male', 'Female', 'Locality_Type']]
        df_total_dist = df_total_dist.reset_index(drop=True)

        total_all_dist = df_total_dist['Total'][0]
        male_dist_all = df_total_dist['Male'][0]
        female_dist_all = df_total_dist['Female'][0]

        #district, urban
        df_urban_dist = df_pop_reg_distr_by_sex[(df_pop_reg_distr_by_sex['Region'] == region) &
                                                (df_pop_reg_distr_by_sex['District'] == district)  &
                                                (df_pop_reg_distr_by_sex['Locality_Type'] == 'Urban')][
            ['Region', 'District', 'Total', 'Male', 'Female', 'Locality_Type']]
        df_urban_dist = df_urban_dist.reset_index(drop=True)

        urban_dist_all = df_urban_dist['Total'][0]
        urban_dist_male = df_urban_dist['Male'][0]
        urban_dist_female = df_urban_dist['Female'][0]

        # rural
        df_rural_dist = df_pop_reg_distr_by_sex[(df_pop_reg_distr_by_sex['Region'] == region) &
                                                (df_pop_reg_distr_by_sex['District'] == district) &
                                                (df_pop_reg_distr_by_sex['Locality_Type'] == 'Urban')][
            ['Region', 'District', 'Total', 'Male', 'Female', 'Locality_Type']]
        df_rural_dist = df_urban_dist.reset_index(drop=True)

        rural_dist_all = df_urban_dist['Total'][0]
        rural_dist_male = df_urban_dist['Male'][0]
        rural_dist_female = df_urban_dist['Female'][0]

        # district characteristics
        df_dist_profile = df_pop_district_profile[
            (df_pop_district_profile['Region'] == region) & (df_pop_district_profile['District'] == district)][
            ['Region', 'District', 'Number', 'Area_Km_2', 'Pop_Density', 'No_of_HH', 'Avg_HH_Size']]  # pop in percent
        df_dist_profile = df_dist_profile.reset_index(drop=True)

        print('Region:', district)
        area_km_2 = df_dist_profile['Area_Km_2'][0]
        pop_density = df_dist_profile['Pop_Density'][0]
        no_households = df_dist_profile['No_of_HH'][0]
        avg_hh_size = df_dist_profile['Avg_HH_Size'][0]

        # FORMATTING
        total_all = '{:,}'.format(total_all)
        total_percent = '{:.1f}'.format(total_percent)
        total_male = '{:,}'.format(total_male)
        total_male_percent = '{:.1f}'.format(total_male_percent)
        total_female = '{:,}'.format(total_female)
        total_female_percent = '{:.1f}'.format(total_female_percent)

        urban_all_total = '{:,}'.format(urban_all_total)
        total_male_urban = '{:,}'.format(total_male_urban)
        total_female_urban = '{:,}'.format(total_female_urban)

        rural_all_total = '{:,}'.format(rural_all_total)
        total_male_rural = '{:,}'.format(total_male_rural)
        total_female_rural = '{:,}'.format(total_female_rural)

        reg_area_km_2 = '{:,}'.format(reg_area_km_2)
        reg_pop_density = '{:,}'.format(reg_pop_density)
        reg_no_households = '{:,}'.format(reg_no_households)
        reg_avg_hh_size = '{:,}'.format(reg_avg_hh_size)

        #both
        total_all_dist = '{:,}'.format(total_all_dist)
        male_dist_all = '{:,}'.format(male_dist_all)
        female_dist_all = '{:,}'.format(female_dist_all)

        #urban
        urban_dist_all = '{:,}'.format(urban_dist_all)
        urban_dist_male = '{:,}'.format(urban_dist_male)
        urban_dist_female = '{:,}'.format(urban_dist_female)

        #rural
        rural_dist_all = '{:,}'.format(rural_dist_all)
        rural_dist_male = '{:,}'.format(rural_dist_male)
        rural_dist_female = '{:,}'.format(rural_dist_female)

        area_km_2 = '{:,.0f}'.format(area_km_2)
        pop_density = '{:,}'.format(pop_density)
        no_households = '{:,.0f}'.format(no_households)


        #district statistics
        # df_pop_percent_all = df_pop_district_profile[df_pop_district_profile['District'] == district][
        #     ['Region', 'District', 'All', 'Male', 'Female', 'Area_Km_2', 'Pop_Density', 'No_HH', 'Avg_HH_Size']]  # pop in percent
        # area_km2 = df_pop_district_profile[(df_pop_district_profile['Region'] == region) & (df_pop_district_profile['District'] == district)][['Area_Km_2']]  # area
        # pop_density = df_pop_district_profile[(df_pop_district_profile['Region'] == region) & (df_pop_district_profile['District'] == district)][
        #     ['Pop_Density']]  # population density
        # no_households = df_pop_district_profile[(df_pop_district_profile['Region'] == region) & (df_pop_district_profile['District'] == district)][
        #     ['No_HH']]  # population density
        # avg_hh_size = df_pop_district_profile[(df_pop_district_profile['Region'] == region) & (df_pop_district_profile['District'] == district)][
        #     ['Avg_HH_Size']]  # avg household size

        # area_km_2 = area_km_2['Area_Km_2'].values[0]
        # pop_density = pop_density['Pop_Density'].values[0]
        # no_households = no_households['No_HH'].values[0]
        # avg_hh_size = avg_hh_size['Avg_HH_Size'].values[0]
        #
        # pop_density = '{:,}'.format(pop_density)
        # no_households = '{:,.0f}'.format(no_households)
        # area_km2_val = '{:,.0f}'.format(area_km_2)

    return total_all, total_percent, total_male, total_male_percent, total_female, total_female_percent, \
           urban_all_total, total_male_urban, total_female_urban, \
           rural_all_total, total_male_rural, total_female_rural, \
           reg_area_km_2, reg_pop_density, reg_no_households, reg_avg_hh_size, \
           total_all_dist, male_dist_all, female_dist_all, \
           urban_dist_all, urban_dist_male, urban_dist_female, \
           rural_dist_all, rural_dist_male, rural_dist_female, \
           area_km_2, pop_density, no_households, avg_hh_size
        # urban_all_dist, male_urban, female_urban, \
           # rural_all_dist, male_rural, female_rural, \
        #male_rural, female_rural, total_region, percent_region, male_reg_percent, female_reg_percent, \
           # area_km2_val, pop_density, no_households, avg_hh_size


#***************************
# #AGE & SEX
#***************************
@app.callback(
    Output('age_sex_total', 'children'),
    Output('age_sex_male_urban', 'children'),
    Output('age_sex_female_urban', 'children'),
    Output('age_sex_male_rural', 'children'),
    Output('age_sex_female_rural', 'children'),

    [Input('age_sex_search_btn', 'n_clicks')],
    [Input('age_sex_region_dd', 'value')],
    [Input('age_sex_district_dd', 'value')],
    [Input('age_sex_group_dd', 'value')],
)
def get_age_sex_by_district(n_clicks, region, district, age_group):

    total_number = None
    male_urban = None
    female_urban = None
    male_rural = None
    female_rural = None
    #search_str = None

    if (n_clicks > 0) & (region != None) & (district != None) & (age_group != None):

        #total, number
        df_total_number = df_age_sex_range[(df_age_sex_range['DISTRICT'] == district) & (df_age_sex_range['AGE_GROUP'] == age_group)]
        df_total_number = df_total_number.rename(columns={'BOTH_TOTAL_NUMBER': 'ALL', 'MALE_TOTAL_NUMBER': 'MALE', 'FEMALE_TOTAL_NUMBER': 'FEMALE'})
        df_total_number['ALL'] = df_total_number['ALL'].apply(lambda x: format(int(x), ','))

        total_number = df_total_number['ALL']

        # urban, number
        df_urban_number = df_age_sex_range[(df_age_sex_range['DISTRICT'] == district) & (df_age_sex_range['AGE_GROUP'] == age_group)]
        df_urban_number = df_urban_number.rename(columns={'URBAN_BOTH': 'ALL', 'URBAN_MALE': 'MALE', 'URBAN_FEMALE': 'FEMALE'})
        df_urban_number['ALL'] = df_urban_number['ALL'].apply(lambda x: format(int(x), ','))
        df_urban_number['MALE'] = df_urban_number['MALE'].apply(lambda x: format(int(x), ','))
        df_urban_number['FEMALE'] = df_urban_number['FEMALE'].apply(lambda x: format(int(x), ','))

        male_urban = df_urban_number['MALE']
        female_urban = df_urban_number['FEMALE']

        # rural, number
        df_rural_number = df_age_sex_range[(df_age_sex_range['DISTRICT'] == district) & (df_age_sex_range['AGE_GROUP'] == age_group)]
        df_rural_number = df_rural_number.rename(columns={'RURAL_BOTH': 'ALL', 'RURAL_MALE': 'MALE', 'RURAL_FEMALE': 'FEMALE'})
        df_rural_number['ALL'] = df_rural_number['ALL'].apply(lambda x: format(int(x), ','))
        df_rural_number['MALE'] = df_rural_number['MALE'].apply(lambda x: format(int(x), ','))
        df_rural_number['FEMALE'] = df_rural_number['FEMALE'].apply(lambda x: format(int(x), ','))

        male_rural = df_rural_number['MALE']
        female_rural = df_rural_number['FEMALE']

        #search_str = region + '->' + district + ' [' + age_group + ']'

    return total_number, male_urban, female_urban, male_rural, female_rural #search_str


#***************************
##BACKGROUND CHARCTERISTICS
#***************************

#marital status
@app.callback(
    #ALL
    Output('bg_all_total', 'children'),
    Output('bg_all_percent', 'children'),

    #never married - percent
    Output('bg_nvr_marr', 'children'),
    Output('bg_inf', 'children'),
    Output('bg_marr_reg', 'children'),
    Output('bg_marr_not_reg', 'children'),
    Output('bg_sep', 'children'),
    Output('bg_div', 'children'),
    Output('bg_wid', 'children'),

    #never married - values
    Output('bg_nvr_marr_val', 'children'),
    Output('bg_inf_val', 'children'),
    Output('bg_marr_reg_val', 'children'),
    Output('bg_marr_not_reg_val', 'children'),
    Output('bg_sep_val', 'children'),
    Output('bg_div_val', 'children'),
    Output('bg_wid_val', 'children'),

    #MALE
    Output('bg_male_total', 'children'),
    Output('bg_male_percent', 'children'),

    #never married - percent
    Output('bg_nvr_marr_male', 'children'),
    Output('bg_inf_male', 'children'),
    Output('bg_marr_reg_male', 'children'),
    Output('bg_marr_not_reg_male', 'children'),
    Output('bg_sep_male', 'children'),
    Output('bg_div_male', 'children'),
    Output('bg_wid_male', 'children'),

    #never married - values
    Output('bg_nvr_marr_male_val', 'children'),
    Output('bg_inf_male_val', 'children'),
    Output('bg_marr_reg_male_val', 'children'),
    Output('bg_marr_not_reg_male_val', 'children'),
    Output('bg_sep_male_val', 'children'),
    Output('bg_div_male_val', 'children'),
    Output('bg_wid_male_val', 'children'),

    #FEMALE
    Output('bg_female_total', 'children'),
    Output('bg_female_percent', 'children'),

    #never married - percent
    Output('bg_nvr_marr_female', 'children'),
    Output('bg_inf_female', 'children'),
    Output('bg_marr_reg_female', 'children'),
    Output('bg_marr_not_reg_female', 'children'),
    Output('bg_sep_female', 'children'),
    Output('bg_div_female', 'children'),
    Output('bg_wid_female', 'children'),

    #never married - values
    Output('bg_nvr_marr_female_val', 'children'),
    Output('bg_inf_female_val', 'children'),
    Output('bg_marr_reg_female_val', 'children'),
    Output('bg_marr_not_reg_female_val', 'children'),
    Output('bg_sep_female_val', 'children'),
    Output('bg_div_female_val', 'children'),
    Output('bg_wid_female_val', 'children'),

    Output('reg_lab_bg', 'children'),
    Output('dist_lab_bg', 'children'),

    Input('bg_xtics_region_dd', 'value'),
    Input('bg_xtics_district_dd', 'value'),
    Input('search_btn_background', 'n_clicks')
 )
def get_bg_information_data(region, district, n_clicks):

    if (n_clicks > 0) & (region != None) & (district != None):

        all_data_df = bg_xtics_region_3C2b[region]

        #**********
        #ALL
        #**********
        # both
        all_df = all_data_df[(all_data_df['Status_Code'] == '0') & (all_data_df['Type'] == 'All')]
        total_all = all_df[district][0]
        total_all_percent = 100

        # never married
        nvr_marr_df = all_data_df[(all_data_df['Status_Code'] == '1') & (all_data_df['Type'] == 'All')]
        nvr_marr_df = nvr_marr_df.reset_index(drop=True)
        nvr_marr = nvr_marr_df[district][0]
        nvr_marr_percent = '{:.1f}'.format((nvr_marr / total_all) * 100)

        # informal/living together
        inf_df = all_data_df[(all_data_df['Status_Code'] == '2') & (all_data_df['Type'] == 'All')]
        inf_df = inf_df.reset_index(drop=True)
        inf = inf_df[district][0]
        inf_percent = '{:.1f}'.format((inf / total_all) * 100)

        # married registered
        marr_reg_df = all_data_df[(all_data_df['Status_Code'] == '3-1') & (all_data_df['Type'] == 'All')]
        marr_reg_df = marr_reg_df.reset_index(drop=True)
        marr_reg = marr_reg_df[district][0]
        marr_reg_percent = '{:.1f}'.format((marr_reg / total_all) * 100)

        # married not registered
        marr_not_reg_df = all_data_df[(all_data_df['Status_Code'] == '3-2') & (all_data_df['Type'] == 'All')]
        marr_not_reg_df = marr_not_reg_df.reset_index(drop=True)
        marr_not_reg = marr_not_reg_df[district][0]
        marr_not_percent = '{:.1f}'.format((marr_not_reg / total_all) * 100)

        # separated
        sep_df = all_data_df[(all_data_df['Status_Code'] == '4') & (all_data_df['Type'] == 'All')]
        sep_df = sep_df.reset_index(drop=True)
        sep = sep_df[district][0]
        sep_percent = '{:.1f}'.format((sep / total_all) * 100)

        # divorced
        div_df = all_data_df[(all_data_df['Status_Code'] == '5') & (all_data_df['Type'] == 'All')]
        div_df = div_df.reset_index(drop=True)
        div = div_df[district][0]
        div_percent = '{:.1f}'.format((div / total_all) * 100)

        # widowed
        wid_df = all_data_df[(all_data_df['Status_Code'] == '6') & (all_data_df['Type'] == 'All')]
        wid_df = wid_df.reset_index(drop=True)
        wid = wid_df[district][0]
        wid_percent = '{:.1f}'.format((wid / total_all) * 100)

        # **********
        # MALE
        # **********
        # both
        male_df = all_data_df[(all_data_df['Status_Code'] == '0') & (all_data_df['Type'] == 'Male')]
        male_df = male_df.reset_index(drop=True)
        total_male = male_df[district][0]
        total_male_percent = 100

        # never married
        nvr_marr_male_df = all_data_df[(all_data_df['Status_Code'] == '1') & (all_data_df['Type'] == 'Male')]
        nvr_marr_male_df = nvr_marr_male_df.reset_index(drop=True)
        nvr_marr_male = nvr_marr_male_df[district][0]
        nvr_male_percent = '{:.1f}'.format((nvr_marr_male / total_male) * 100)

        # informal/living together
        inf_male_df = all_data_df[(all_data_df['Status_Code'] == '2') & (all_data_df['Type'] == 'Male')]
        inf_male_df = inf_male_df.reset_index(drop=True)
        inf_male = inf_male_df[district][0]
        inf_male_percent = '{:.1f}'.format((inf_male / total_male) * 100)

        # married registered
        marr_reg_male_df = all_data_df[(all_data_df['Status_Code'] == '3-1') & (all_data_df['Type'] == 'Male')]
        marr_reg_male_df = marr_reg_male_df.reset_index(drop=True)
        marr_reg_male = marr_reg_male_df[district][0]
        marr_reg_male_percent = '{:.1f}'.format((marr_reg_male / total_male) * 100)

        # married not registered
        marr_not_reg_male_df = all_data_df[(all_data_df['Status_Code'] == '3-2') & (all_data_df['Type'] == 'Male')]
        marr_not_reg_male_df = marr_not_reg_male_df.reset_index(drop=True)
        marr_not_reg_male = marr_not_reg_male_df[district][0]
        marr_not_male_percent = '{:.1f}'.format((marr_not_reg_male / total_male) * 100)

        # separated
        sep_male_df = all_data_df[(all_data_df['Status_Code'] == '4') & (all_data_df['Type'] == 'Male')]
        sep_male_df = sep_male_df.reset_index(drop=True)
        sep_male = sep_male_df[district][0]
        sep_male_percent = '{:.1f}'.format((sep_male / total_male) * 100)

        # divorced
        div_male_df = all_data_df[(all_data_df['Status_Code'] == '5') & (all_data_df['Type'] == 'Male')]
        div_male_df = div_male_df.reset_index(drop=True)
        div_male = div_male_df[district][0]
        div_male_percent = '{:.1f}'.format((div_male / total_male) * 100)

        # widowed
        wid_male_df = all_data_df[(all_data_df['Status_Code'] == '6') & (all_data_df['Type'] == 'Male')]
        wid_male_df = wid_male_df.reset_index(drop=True)
        wid_male = wid_male_df[district][0]
        wid_male_percent = '{:.1f}'.format((wid_male / total_male) * 100)

        # **********
        # FEMALE
        # **********
        # both
        female_df = all_data_df[(all_data_df['Status_Code'] == '0') & (all_data_df['Type'] == 'Female')]
        female_df = female_df.reset_index(drop=True)
        total_female = female_df[district][0]
        total_female_percent = 100

        # never married
        nvr_marr_female_df = all_data_df[(all_data_df['Status_Code'] == '1') & (all_data_df['Type'] == 'Male')]
        nvr_marr_female_df = nvr_marr_female_df.reset_index(drop=True)
        nvr_marr_female = nvr_marr_female_df[district][0]
        nvr_female_percent = '{:.1f}'.format((nvr_marr_female / total_female) * 100)

        # informal/living together
        inf_female_df = all_data_df[(all_data_df['Status_Code'] == '2') & (all_data_df['Type'] == 'Female')]
        inf_female_df = inf_female_df.reset_index(drop=True)
        inf_female = inf_female_df[district][0]
        inf_female_percent = '{:.1f}'.format((inf_female / total_female) * 100)

        # married registered
        marr_reg_female_df = all_data_df[(all_data_df['Status_Code'] == '3-1') & (all_data_df['Type'] == 'Female')]
        marr_reg_female_df = marr_reg_female_df.reset_index(drop=True)
        marr_reg_female = marr_reg_female_df[district][0]
        marr_reg_female_percent = '{:.1f}'.format((marr_reg_female / total_female) * 100)

        # married not registered
        marr_not_reg_female_df = all_data_df[(all_data_df['Status_Code'] == '3-2') & (all_data_df['Type'] == 'Female')]
        marr_not_reg_female_df = marr_not_reg_female_df.reset_index(drop=True)
        marr_not_reg_female = marr_not_reg_female_df[district][0]
        marr_not_female_percent = '{:.1f}'.format((marr_not_reg_female / total_female) * 100)

        # separated
        sep_female_df = all_data_df[(all_data_df['Status_Code'] == '4') & (all_data_df['Type'] == 'Female')]
        sep_female_df = sep_female_df.reset_index(drop=True)
        sep_female = sep_female_df[district][0]
        sep_female_percent = '{:.1f}'.format((sep_female / total_female) * 100)

        # divorced
        div_female_df = all_data_df[(all_data_df['Status_Code'] == '5') & (all_data_df['Type'] == 'Female')]
        div_female_df = div_female_df.reset_index(drop=True)
        div_female = div_female_df[district][0]
        div_female_percent = '{:.1f}'.format((div_female / total_female) * 100)

        # widowed
        wid_female_df = all_data_df[(all_data_df['Status_Code'] == '6') & (all_data_df['Type'] == 'Female')]
        wid_female_df = wid_female_df.reset_index(drop=True)
        wid_female = wid_female_df[district][0]
        wid_female_percent = '{:.1f}'.format((wid_female / total_female) * 100)

        #ALL FORMATTING
        total_all = '{:,}'.format(total_all)
        nvr_marr = '{:,}'.format(nvr_marr)
        inf = '{:,}'.format(inf)
        marr_reg = '{:,}'.format(marr_reg)
        marr_not_reg = '{:,}'.format(marr_not_reg)
        sep = '{:,}'.format(sep)
        div = '{:,}'.format(div)
        wid = '{:,}'.format(wid)

        # MALE FORMATTING
        total_male = '{:,}'.format(total_male)
        nvr_marr_male = '{:,}'.format(nvr_marr_male)
        inf_male = '{:,}'.format(inf_male)
        marr_reg_male = '{:,}'.format(marr_reg_male)
        marr_not_reg_male = '{:,}'.format(marr_not_reg_male)
        sep_male = '{:,}'.format(sep_male)
        div_male = '{:,}'.format(div_male)
        wid_male = '{:,}'.format(wid_male)

        # FEMALE FORMATTING
        total_female = '{:,}'.format(total_female)
        nvr_marr_female = '{:,}'.format(nvr_marr_female)
        inf_female = '{:,}'.format(inf_female)
        marr_reg_female = '{:,}'.format(marr_reg_female)
        marr_not_reg_female = '{:,}'.format(marr_not_reg_female)
        sep_female = '{:,}'.format(sep_female)
        div_female = '{:,}'.format(div_female)
        wid_female = '{:,}'.format(wid_female)

        #print(total_all_percent)

        return  total_all, total_all_percent, nvr_marr_percent, inf_percent, marr_reg_percent, marr_not_percent, sep_percent, div_percent, wid_percent, \
                nvr_marr, inf, marr_reg, marr_not_reg, sep, div, wid, \
                total_male, total_male_percent, nvr_male_percent, inf_male_percent, marr_reg_male_percent, marr_not_male_percent, sep_male_percent, div_male_percent, wid_male_percent, \
                nvr_marr_male, inf_male, marr_reg_male, marr_not_reg_male, sep_male, div_male, wid_male, \
                total_female, total_female_percent, nvr_female_percent, inf_female_percent, marr_reg_female_percent, marr_not_female_percent, sep_female_percent, div_female_percent, wid_female_percent, \
                nvr_marr_female, inf_female, marr_reg_female, marr_not_reg_female, sep_female, div_female, wid_female, \
                region, district
    else:
        return None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, None, \
               None, None, None, None

#ethinicity
@app.callback(
    # ALL
    Output('bg_ethn_all_total', 'children'),
    Output('bg_ethn_male_total', 'children'),
    Output('bg_ethn_female_total', 'children'),

    Output('bg_ethn_all_percent', 'children'),
    Output('bg_ethn_male_percent', 'children'),
    Output('bg_ethn_female_percent', 'children'),

    Output('bg_akan', 'children'),
    Output('bg_ga_adangme', 'children'),
    Output('bg_ewe', 'children'),
    Output('bg_guan', 'children'),
    Output('bg_gurma', 'children'),
    Output('bg_mole_dagbani', 'children'),
    Output('bg_grusi', 'children'),
    Output('bg_mande', 'children'),
    Output('bg_others', 'children'),
    #9

    Output('bg_akan_val', 'children'),
    Output('bg_ga_adangme_val', 'children'),
    Output('bg_ewe_val', 'children'),
    Output('bg_guan_val', 'children'),
    Output('bg_gurma_val', 'children'),
    Output('bg_mole_dagbani_val', 'children'),
    Output('bg_grusi_val', 'children'),
    Output('bg_mande_val', 'children'),
    Output('bg_others_val', 'children'),
    #9

    # MALE
    Output('bg_akan_male', 'children'),
    Output('bg_ga_adangme_male', 'children'),
    Output('bg_ewe_male', 'children'),
    Output('bg_guan_male', 'children'),
    Output('bg_gurma_male', 'children'),
    Output('bg_mole_dagbani_male', 'children'),
    Output('bg_grusi_male', 'children'),
    Output('bg_mande_male', 'children'),
    Output('bg_others_male', 'children'),
    #9

    Output('bg_akan_male_val', 'children'),
    Output('bg_ga_adangme_male_val', 'children'),
    Output('bg_ewe_male_val', 'children'),
    Output('bg_guan_male_val', 'children'),
    Output('bg_gurma_male_val', 'children'),
    Output('bg_mole_dagbani_male_val', 'children'),
    Output('bg_grusi_male_val', 'children'),
    Output('bg_mande_male_val', 'children'),
    Output('bg_others_male_val', 'children'),
    #9

    # FEMALE
    Output('bg_akan_female', 'children'),
    Output('bg_ga_adangme_female', 'children'),
    Output('bg_ewe_female', 'children'),
    Output('bg_guan_female', 'children'),
    Output('bg_gurma_female', 'children'),
    Output('bg_mole_dagbani_female', 'children'),
    Output('bg_grusi_female', 'children'),
    Output('bg_mande_female', 'children'),
    Output('bg_others_female', 'children'),
    #9

    Output('bg_akan_female_val', 'children'),
    Output('bg_ga_adangme_female_val', 'children'),
    Output('bg_ewe_female_val', 'children'),
    Output('bg_guan_female_val', 'children'),
    Output('bg_gurma_female_val', 'children'),
    Output('bg_mole_dagbani_female_val', 'children'),
    Output('bg_grusi_female_val', 'children'),
    Output('bg_mande_female_val', 'children'),
    Output('bg_others_female_val', 'children'),
    #9

    Input('bg_xtics_region_dd', 'value'),
    Input('bg_xtics_district_dd', 'value'),
    Input('search_btn_background', 'n_clicks')

    #56 variables
)
def get_bg_xtics_ethnicity(region, district, n_clicks):

    if (n_clicks > 0) & (region != None) & (district != None):

        if region == 'Western':
            data_df = df_bg_xtics_3C3a_western.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        elif region == 'Central':
             data_df = df_bg_xtics_3C3a_central.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        # elif region == 'Greater Accra':
        #     data_df = df_bg_xtics_3C3a_western.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        # elif region == 'Volta':
        #     data_df = df_bg_xtics_3C3a_western.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]

        # ALL
        all_total_df = data_df[(data_df['Status_Code'] == 0) & (data_df['Type'] == 'All')][[district]]
        all_akan_df = data_df[(data_df['Status_Code'] == 1) & (data_df['Type'] == 'All')]
        all_ga_adangme_df = data_df[(data_df['Status_Code'] == 2) & (data_df['Type'] == 'All')]
        all_ewe_df = data_df[(data_df['Status_Code'] == 3) & (data_df['Type'] == 'All')]
        all_guan_df = data_df[(data_df['Status_Code'] == 4) & (data_df['Type'] == 'All')]
        all_gurma_df = data_df[(data_df['Status_Code'] == 5) & (data_df['Type'] == 'All')]
        all_mole_dagbani_df = data_df[(data_df['Status_Code'] == 6) & (data_df['Type'] == 'All')]
        all_grusi_df = data_df[(data_df['Status_Code'] == 7) & (data_df['Type'] == 'All')]
        all_mande_df = data_df[(data_df['Status_Code'] == 8) & (data_df['Type'] == 'All')]
        all_others_df = data_df[(data_df['Status_Code'] == 9) & (data_df['Type'] == 'All')]

        all_total_df = all_total_df.reset_index(drop=True)
        all_akan_df = all_akan_df.reset_index(drop=True)
        all_ga_adangme_df = all_ga_adangme_df.reset_index(drop=True)
        all_ewe_df = all_ewe_df.reset_index(drop=True)
        all_guan_df = all_guan_df.reset_index(drop=True)
        all_gurma_df = all_gurma_df.reset_index(drop=True)
        all_mole_dagbani_df = all_mole_dagbani_df.reset_index(drop=True)
        all_grusi_df = all_grusi_df.reset_index(drop=True)
        all_mande_df = all_mande_df.reset_index(drop=True)
        all_others_df = all_others_df.reset_index(drop=True)

        all_total = all_total_df[district][0]
        all_percent = 100
        all_akan = all_akan_df[district][0]
        all_ga_adangme = all_ga_adangme_df[district][0]
        all_ewe = all_ewe_df[district][0]
        all_guan = all_guan_df[district][0]
        all_gurma = all_gurma_df[district][0]
        all_mole_dagbani = all_mole_dagbani_df[district][0]
        all_grusi = all_grusi_df[district][0]
        all_mande = all_mande_df[district][0]
        all_others = all_others_df[district][0]

        # MALE
        male_total_df = data_df[(data_df['Status_Code'] == 0) & (data_df['Type'] == 'Male')][[district]]
        male_akan_df = data_df[(data_df['Status_Code'] == 1) & (data_df['Type'] == 'Male')]
        male_ga_adangme_df = data_df[(data_df['Status_Code'] == 2) & (data_df['Type'] == 'Male')]
        male_ewe_df = data_df[(data_df['Status_Code'] == 3) & (data_df['Type'] == 'Male')]
        male_guan_df = data_df[(data_df['Status_Code'] == 4) & (data_df['Type'] == 'Male')]
        male_gurma_df = data_df[(data_df['Status_Code'] == 5) & (data_df['Type'] == 'Male')]
        male_mole_dagbani_df = data_df[(data_df['Status_Code'] == 6) & (data_df['Type'] == 'Male')]
        male_grusi_df = data_df[(data_df['Status_Code'] == 7) & (data_df['Type'] == 'Male')]
        male_mande_df = data_df[(data_df['Status_Code'] == 8) & (data_df['Type'] == 'Male')]
        male_others_df = data_df[(data_df['Status_Code'] == 9) & (data_df['Type'] == 'Male')]

        male_total_df = male_total_df.reset_index(drop=True)
        male_akan_df = male_akan_df.reset_index(drop=True)
        male_ga_adangme_df = male_ga_adangme_df.reset_index(drop=True)
        male_ewe_df = male_ewe_df.reset_index(drop=True)
        male_guan_df = male_guan_df.reset_index(drop=True)
        male_gurma_df = male_gurma_df.reset_index(drop=True)
        male_mole_dagbani_df = male_mole_dagbani_df.reset_index(drop=True)
        male_grusi_df = male_grusi_df.reset_index(drop=True)
        male_mande_df = male_mande_df.reset_index(drop=True)
        male_others_df = male_others_df.reset_index(drop=True)

        male_total = male_total_df[district][0]
        male_percent = 100
        male_akan = male_akan_df[district][0]
        male_ga_adangme = male_ga_adangme_df[district][0]
        male_ewe = male_ewe_df[district][0]
        male_guan = male_guan_df[district][0]
        male_gurma = male_gurma_df[district][0]
        male_mole_dagbani = male_mole_dagbani_df[district][0]
        male_grusi = male_grusi_df[district][0]
        male_mande = male_mande_df[district][0]
        male_others = male_others_df[district][0]

        # FEMALE
        female_total_df = data_df[(data_df['Status_Code'] == 0) & (data_df['Type'] == 'Female')][[district]]
        female_akan_df = data_df[(data_df['Status_Code'] == 1) & (data_df['Type'] == 'Female')]
        female_ga_adangme_df = data_df[(data_df['Status_Code'] == 2) & (data_df['Type'] == 'Female')]
        female_ewe_df = data_df[(data_df['Status_Code'] == 3) & (data_df['Type'] == 'Female')]
        female_guan_df = data_df[(data_df['Status_Code'] == 4) & (data_df['Type'] == 'Female')]
        female_gurma_df = data_df[(data_df['Status_Code'] == 5) & (data_df['Type'] == 'Female')]
        female_mole_dagbani_df = data_df[(data_df['Status_Code'] == 6) & (data_df['Type'] == 'Female')]
        female_grusi_df = data_df[(data_df['Status_Code'] == 7) & (data_df['Type'] == 'Female')]
        female_mande_df = data_df[(data_df['Status_Code'] == 8) & (data_df['Type'] == 'Female')]
        female_others_df = data_df[(data_df['Status_Code'] == 9) & (data_df['Type'] == 'Female')]

        female_total_df = female_total_df.reset_index(drop=True)
        female_akan_df = female_akan_df.reset_index(drop=True)
        female_ga_adangme_df = female_ga_adangme_df.reset_index(drop=True)
        female_ewe_df = female_ewe_df.reset_index(drop=True)
        female_guan_df = female_guan_df.reset_index(drop=True)
        female_gurma_df = female_gurma_df.reset_index(drop=True)
        female_mole_dagbani_df = female_mole_dagbani_df.reset_index(drop=True)
        female_grusi_df = female_grusi_df.reset_index(drop=True)
        female_mande_df = female_mande_df.reset_index(drop=True)
        female_others_df = female_others_df.reset_index(drop=True)

        female_total = female_total_df[district][0]
        female_percent = 100
        female_akan = female_akan_df[district][0]
        female_ga_adangme = female_ga_adangme_df[district][0]
        female_ewe = female_ewe_df[district][0]
        female_guan = female_guan_df[district][0]
        female_gurma = female_gurma_df[district][0]
        female_mole_dagbani = female_mole_dagbani_df[district][0]
        female_grusi = female_grusi_df[district][0]
        female_mande = female_mande_df[district][0]
        female_others = female_others_df[district][0]

        #all format
        all_akan_percent = '{:.1f}'.format((all_akan / all_total) * 100)
        all_ga_adangme_percent = '{:.1f}'.format((all_ga_adangme / all_total) * 100)
        all_ewe_percent = '{:.1f}'.format((all_ewe / all_total) * 100)
        all_guan_percent = '{:.1f}'.format((all_guan / all_total) * 100)
        all_gurma_percent = '{:.1f}'.format((all_gurma / all_total) * 100)
        all_mole_dagbani_percent = '{:.1f}'.format((all_mole_dagbani / all_total) * 100)
        all_grusi_percent = '{:.1f}'.format((all_grusi / all_total) * 100)
        all_mande_percent = '{:.1f}'.format((all_mande / all_total) * 100)
        all_others_percent = '{:.1f}'.format((all_others / all_total) * 100)

        #male format
        male_akan_percent = '{:.1f}'.format((male_akan / male_total) * 100)
        male_ga_adangme_percent = '{:.1f}'.format((male_ga_adangme / male_total) * 100)
        male_ewe_percent = '{:.1f}'.format((male_ewe / male_total) * 100)
        male_guan_percent = '{:.1f}'.format((male_guan / male_total) * 100)
        male_gurma_percent = '{:.1f}'.format((male_gurma / male_total) * 100)
        male_mole_dagbani_percent = '{:.1f}'.format((male_mole_dagbani / male_total) * 100)
        male_grusi_percent = '{:.1f}'.format((male_grusi / male_total) * 100)
        male_mande_percent = '{:.1f}'.format((male_mande / male_total) * 100)
        male_others_percent = '{:.1f}'.format((male_others / all_total) * 100)

        # female format
        female_akan_percent = '{:.1f}'.format((female_akan / female_total) * 100)
        female_ga_adangme_percent = '{:.1f}'.format((female_ga_adangme / female_total) * 100)
        female_ewe_percent = '{:.1f}'.format((female_ewe / female_total) * 100)
        female_guan_percent = '{:.1f}'.format((female_guan / female_total) * 100)
        female_gurma_percent = '{:.1f}'.format((female_gurma / female_total) * 100)
        female_mole_dagbani_percent = '{:.1f}'.format((female_mole_dagbani / female_total) * 100)
        female_grusi_percent = '{:.1f}'.format((female_grusi / female_total) * 100)
        female_mande_percent = '{:.1f}'.format((female_mande / female_total) * 100)
        female_others_percent = '{:.1f}'.format((female_others / all_total) * 100)

        all_total = '{:,.0f}'.format(all_total)
        male_total = '{:,.0f}'.format(male_total)
        female_total = '{:,.0f}'.format(female_total)

        all_akan = '{:,}'.format(all_akan)
        all_ga_adangme = '{:,}'.format(all_ga_adangme)
        all_ewe = '{:,}'.format(all_ewe)
        all_guan = '{:,}'.format(all_guan)
        all_gurma = '{:,}'.format(all_gurma)
        all_mole_dagbani = '{:,}'.format(all_mole_dagbani)
        all_grusi = '{:,}'.format(all_grusi)
        all_mande = '{:,}'.format(all_mande)
        all_others = '{:,}'.format(all_others)

        male_akan = '{:,}'.format(male_akan)
        male_ga_adangme = '{:,}'.format(male_ga_adangme)
        male_ewe = '{:,}'.format(male_ewe)
        male_guan = '{:,}'.format(male_guan)
        male_gurma = '{:,}'.format(male_gurma)
        male_mole_dagbani = '{:,}'.format(male_mole_dagbani)
        male_grusi = '{:,}'.format(male_grusi)
        male_mande = '{:,}'.format(male_mande)
        male_others = '{:,}'.format(male_others)

        female_akan = '{:,}'.format(female_akan)
        female_ga_adangme = '{:,}'.format(female_ga_adangme)
        female_ewe = '{:,}'.format(female_ewe)
        female_guan = '{:,}'.format(female_guan)
        female_gurma = '{:,}'.format(female_gurma)
        female_mole_dagbani = '{:,}'.format(female_mole_dagbani)
        female_grusi = '{:,}'.format(female_grusi)
        female_mande = '{:,}'.format(female_mande)
        female_others = '{:,}'.format(female_others)

        return all_total, male_total, female_total, all_percent, male_percent, female_percent, all_akan_percent, all_ga_adangme_percent, all_ewe_percent, all_guan_percent, all_gurma_percent, \
               all_mole_dagbani_percent, all_grusi_percent, all_mande_percent, all_others_percent, \
               all_akan, all_ga_adangme, all_ewe, all_guan, all_gurma, all_mole_dagbani, all_grusi, all_mande, all_others, \
               male_akan_percent, male_ga_adangme_percent, male_ewe_percent, male_guan_percent, male_gurma_percent, \
               male_mole_dagbani_percent, male_grusi_percent, male_mande_percent, male_others_percent, \
               male_akan, male_ga_adangme, male_ewe, male_guan, male_gurma, male_mole_dagbani, male_grusi, male_mande, male_others, \
               female_akan_percent, female_ga_adangme_percent, female_ewe_percent, female_guan_percent, female_gurma_percent, \
               female_mole_dagbani_percent, female_grusi_percent, female_mande_percent, female_others_percent, \
               female_akan, female_ga_adangme, female_ewe, female_guan, female_gurma, female_mole_dagbani, female_grusi, female_mande, female_others
    else:
        return None, None, None, None, None, None, None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None

#insurance
@app.callback(
    #general stats
    Output('insu_reg_total_pop_val', 'children'),
    Output('insu_reg_total_pop_cov_val', 'children'),
    Output('insu_reg_total_pop_cov', 'children'),
    Output('insu_reg_male_pop_cov_val', 'children'),
    Output('insu_reg_male_pop_cov', 'children'),
    Output('insu_reg_female_pop_cov_val', 'children'),
    Output('insu_reg_female_pop_cov', 'children'),

    #district, covered
    Output('insu_dist_pop_val', 'children'),
    Output('insu_dist_total_pop_cov_val', 'children'),
    Output('insu_dist_total_pop_cov', 'children'),
    Output('insu_dist_male_pop_cov_val', 'children'),
    Output('insu_dist_male_pop_cov', 'children'),
    Output('insu_dist_female_pop_cov_val', 'children'),
    Output('insu_dist_female_pop_cov', 'children'),

    #district, not covered
    Output('insu_dist_pop_not_val', 'children'),
    Output('insu_dist_total_pop_not_cov_val', 'children'),
    Output('insu_dist_total_pop_not_cov', 'children'),
    Output('insu_dist_male_pop_not_cov_val', 'children'),
    Output('insu_dist_male_pop_not_cov', 'children'),
    Output('insu_dist_female_pop_not_cov_val', 'children'),
    Output('insu_dist_female_pop_not_cov', 'children'),

    #urban
    Output('insu_urban_pop_val', 'children'),
    Output('insu_pop_urban_cov_val', 'children'),
    Output('insu_pop_urban_cov', 'children'),
    Output('insu_pop_urban_not_cov_val', 'children'),
    Output('insu_pop_urban_not_cov', 'children'),

    #rural
    Output('insu_rural_pop_val', 'children'),
    Output('insu_pop_rural_cov_val', 'children'),
    Output('insu_pop_rural_cov', 'children'),
    Output('insu_pop_rural_not_cov_val', 'children'),
    Output('insu_pop_rural_not_cov', 'children'),

    Input('bg_xtics_region_dd', 'value'),
    Input('bg_xtics_district_dd', 'value'),
    Input('search_btn_background', 'n_clicks')
)
def get_bg_xtics_insurance(region, district, n_clicks):

    if (n_clicks > 0) & (region != None) & (district != None):

        # GENERAL STATISTICS
        # *******************
        # reg pop

        gen_stats_df = df_bg_xtics_3C8a_all[(df_bg_xtics_3C8a_all['REGION'] == region) & (df_bg_xtics_3C8a_all['DISTRICT'] == region) & (df_bg_xtics_3C8a_all['IS_DISTRICT'] == 0)]
        gen_stats_df = gen_stats_df.reset_index(drop=True)
        reg_pop = gen_stats_df['TOT_POP'][0]
        reg_pop = '{:,}'.format(reg_pop)


        reg_pop_cov = gen_stats_df['TOT_COV'][0]                    # reg pop covered
        reg_pop_cov_percent = gen_stats_df['PERCENT_COV_TOT'][0]    # reg pop cov percent
        reg_male_pop_cov = gen_stats_df['TOT_MALE_COV'][0]          # male pop covered
        reg_female_pop_cov = gen_stats_df['TOT_FEMALE_COV'][0]      # female pop covered

        reg_male_pop_cov_percent = '{:.1f}'.format((reg_male_pop_cov / reg_pop_cov) * 100)
        reg_female_pop_cov_percent = '{:.1f}'.format((reg_female_pop_cov / reg_pop_cov) * 100)

        #district, covered
        dist_stats_df = df_bg_xtics_3C8a_all[(df_bg_xtics_3C8a_all['REGION'] == region) & (df_bg_xtics_3C8a_all['DISTRICT'] == district) & (df_bg_xtics_3C8a_all['IS_DISTRICT'] == 1)]
        dist_stats_df = dist_stats_df.reset_index(drop=True)
        dist_pop = dist_stats_df['TOT_POP'][0]
        dist_tot_cov = dist_stats_df['TOT_COV'][0]
        dist_male_cov = dist_stats_df['TOT_MALE_COV'][0]
        dist_female_cov = dist_stats_df['TOT_FEMALE_COV'][0]

        dist_tot_cov_percent = '{:.1f}'.format((dist_tot_cov / dist_pop ) * 100)
        dist_male_cov_percent = '{:.1f}'.format((dist_male_cov / dist_tot_cov) * 100)
        dist_female_cov_percent = '{:.1f}'.format((dist_female_cov / dist_tot_cov) * 100)

        # district, not covered
        dist_tot_not_cov = dist_stats_df['TOT_NOT_COV'][0]
        dist_male_not_cov = dist_stats_df['TOT_MALE_NOT_COV'][0]
        dist_female_not_cov = dist_stats_df['TOT_FEMALE_NOT_COV'][0]

        dist_tot_not_cov_percent = '{:.1f}'.format((dist_tot_not_cov / dist_pop) * 100)
        dist_male_not_cov_percent = '{:.1f}'.format((dist_male_not_cov / dist_tot_not_cov) * 100)
        dist_female_not_cov_percent = '{:.1f}'.format((dist_female_not_cov / dist_tot_not_cov) * 100)

        #urban
        urban_pop = dist_stats_df['URBAN_TOT'][0]
        urban_pop_cov = dist_stats_df['URBAN_TOT_COV'][0]
        urban_pop_not_cov = dist_stats_df['URBAN_TOT_NOT_COV'][0]

        #print(urban_pop_cov, urban_pop)
        urban_pop_cov_percent = '{:.1f}'.format((urban_pop_cov / urban_pop) * 100)
        urban_pop_not_cov_percent = '{:.1f}'.format((urban_pop_not_cov / urban_pop) * 100)

        # rural
        rural_pop = dist_stats_df['RURAL_TOT'][0]
        rural_pop_cov = dist_stats_df['RURAL_TOT_COV'][0]
        rural_pop_not_cov = dist_stats_df['RURAL_TOT_NOT_COV'][0]

        rural_pop_cov_percent = '{:.1f}'.format((rural_pop_cov / rural_pop) * 100)
        rural_pop_not_cov_percent = '{:.1f}'.format((rural_pop_not_cov / rural_pop) * 100)

        # formatting
        reg_pop_cov = '{:,}'.format(reg_pop_cov)
        reg_male_pop_cov = '{:,}'.format(reg_male_pop_cov)
        reg_female_pop_cov = '{:,}'.format(reg_female_pop_cov)

        dist_pop = '{:,}'.format(dist_pop)
        dist_tot_cov = '{:,}'.format(dist_tot_cov)
        dist_male_cov = '{:,}'.format(dist_male_cov)
        dist_female_cov = '{:,}'.format(dist_female_cov)

        urban_pop = '{:,}'.format(urban_pop)
        urban_pop_cov = '{:,}'.format(urban_pop_cov)
        urban_pop_not_cov = '{:,}'.format(urban_pop_not_cov)
        rural_pop = '{:,}'.format(rural_pop)
        rural_pop_cov = '{:,}'.format(rural_pop_cov)
        rural_pop_not_cov = '{:,}'.format(rural_pop_not_cov)

        return reg_pop, reg_pop_cov, reg_pop_cov_percent, reg_male_pop_cov, reg_male_pop_cov_percent, reg_female_pop_cov, reg_female_pop_cov_percent, \
                dist_pop, dist_tot_cov, dist_tot_cov_percent, dist_male_cov, dist_male_cov_percent, dist_female_cov, dist_female_cov_percent, \
                dist_pop, dist_tot_not_cov, dist_tot_not_cov_percent, dist_male_not_cov, dist_male_not_cov_percent, dist_female_not_cov, dist_female_not_cov_percent, \
                urban_pop, urban_pop_cov, urban_pop_cov_percent, urban_pop_not_cov, urban_pop_not_cov_percent, \
                rural_pop, rural_pop_cov, rural_pop_cov_percent, rural_pop_not_cov, rural_pop_not_cov_percent
    else:
        return None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, \
               None, None, None

#***************************
#LITERACY & EDUCATION - 3D3a
#***************************
@app.callback(
    Output('lit_edu_all_lit', 'children'),
    Output('lit_edu_all_male_lit', 'children'),
    Output('lit_edu_all_female_lit', 'children'),
    Output('lit_edu_urban_male_lit', 'children'),
    Output('lit_edu_urban_female_lit', 'children'),
    Output('lit_edu_rural_male_lit', 'children'),
    Output('lit_edu_rural_female_lit', 'children'),
    Output('lit_edu_urban_both_lit', 'children'),
    Output('lit_edu_rural_both_lit', 'children'),
    Output('district_label', 'children'),
    Input('lit_edu_region_dd', 'value'),
    Input('lit_edu_district_dd', 'value')
)
def get_lit_edu_data(region, district):

    df_lit_edu_data = lit_edu_region_3D3a[region]

    lit_all_percent = None
    lit_all_male = None
    lit_all_female = None
    lit_urban_male = None
    lit_urban_female = None
    lit_rural_male = None
    lit_rural_female = None
    lit_urban_both = None

    if (region != None) & (district != None):

        #*******
        #ALL
        #*******
        df_data = df_lit_edu_data.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        total_all_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'All')][[district]]
        value_all_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'All')][[district]]

        total_all_df = total_all_df.reset_index(drop=True)
        value_all_df = value_all_df.reset_index(drop=True)

        total_all = total_all_df[district][0]
        value_all = value_all_df[district][0]

        if total_all > 0:
            lit_all = '{:.1f}'.format((value_all / total_all) * 100)
        else:
            lit_all = '{:.1f}'.format(0)

        #*********
        #ALL MALE
        #*********
        df_data = df_lit_edu_data.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        total_male_all_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'All Male')][[district]]
        value_male_all_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'All Male')][[district]]

        total_male_all_df = total_male_all_df.reset_index(drop=True)
        value_male_all_df = value_male_all_df.reset_index(drop=True)

        total_male_all = total_male_all_df[district][0]
        value_male_all = value_male_all_df[district][0]

        if total_male_all > 0:
            lit_male_all = '{:.1f}'.format((value_male_all / total_male_all) * 100)
        else:
            lit_male_all = '{:.1f}'.format(0)

        #************
        # ALL FEMALE
        #************
        df_data = df_lit_edu_data.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        total_female_all_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'All Female')][[district]]
        value_female_all_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'All Female')][[district]]

        total_female_all_df = total_female_all_df.reset_index(drop=True)
        value_female_all_df = value_female_all_df.reset_index(drop=True)

        total_female_all = total_female_all_df[district][0]
        value_female_all = value_female_all_df[district][0]

        if total_female_all > 0:
            lit_female_all = '{:.1f}'.format((value_female_all / total_female_all) * 100)
        else:
            lit_female_all = '{:.1f}'.format(0)

        # ************
        # URBAN MALE
        # ************
        df_data = df_lit_edu_data.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        total_urban_male_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'Urban Male')][[district]]
        value_urban_male_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'Urban Male')][[district]]

        total_urban_male_df = total_urban_male_df.reset_index(drop=True)
        value_urban_male_df = value_urban_male_df.reset_index(drop=True)

        total_urban_male = total_urban_male_df[district][0]
        value_urban_male = value_urban_male_df[district][0]

        if total_urban_male > 0:
            lit_urban_male = '{:.1f}'.format((value_urban_male / total_urban_male) * 100)
        else:
            lit_urban_male = '{:.1f}'.format(0)

        # ************
        # URBAN FEMALE
        # ************
        df_data = df_lit_edu_data.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        total_urban_female_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'Urban Female')][[district]]
        value_urban_female_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'Urban Female')][[district]]

        total_urban_female_df = total_urban_female_df.reset_index(drop=True)
        value_urban_female_df = value_urban_female_df.reset_index(drop=True)

        total_urban_female = total_urban_female_df[district][0]
        value_urban_female = value_urban_female_df[district][0]

        if total_urban_female > 0:
            lit_urban_female = '{:.1f}'.format((value_urban_female / total_urban_female) * 100)
        else:
            lit_urban_female = '{:.1f}'.format(0)

        # ************
        # RURAL MALE
        # ************
        df_data = df_lit_edu_data.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        total_rural_male_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'Rural Male')][[district]]
        value_rural_male_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'Rural Male')][[district]]

        total_rural_male_df = total_rural_male_df.reset_index(drop=True)
        value_rural_male_df = value_rural_male_df.reset_index(drop=True)

        total_rural_male = total_rural_male_df[district][0]
        value_rural_male = value_rural_male_df[district][0]

        if total_rural_male > 0:
            lit_rural_male = '{:.1f}'.format((value_rural_male / total_rural_male) * 100)
        else:
            lit_rural_male = '{:.1f}'.format(0)

        # ************
        # RURAL FEMALE
        # ************
        df_data = df_lit_edu_data.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        total_rural_female_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'Rural Female')][[district]]
        value_rural_female_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'Rural Female')][[district]]

        total_rural_female_df = total_rural_female_df.reset_index(drop=True)
        value_rural_female_df = value_rural_female_df.reset_index(drop=True)

        total_rural_female = total_rural_female_df[district][0]
        value_rural_female = value_rural_female_df[district][0]

        if total_rural_female > 0:
            lit_rural_female = '{:.1f}'.format((value_rural_female / total_rural_female) * 100)
        else:
            lit_rural_female = '{:.1f}'.format(0)

        # ****************
        # URBAN MALE, BOTH
        # ****************
        df_data = df_lit_edu_data.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        total_urban_both_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'Urban Both')][[district]]
        value_urban_both_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'Urban Both')][[district]]

        total_urban_both_df = total_urban_both_df.reset_index(drop=True)
        value_urban_both_df = value_urban_both_df.reset_index(drop=True)

        total_urban_both = total_urban_both_df[district][0]
        value_urban_both = value_urban_both_df[district][0]

        if total_urban_both > 0:
            lit_urban_both = '{:.1f}'.format((value_urban_both / total_urban_both) * 100)
        else:
            lit_urban_both = '{:.1f}'.format(0)


        # ******************
        # URBAN FEMALE, BOTH
        # ******************
        df_data = df_data.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        total_rural_both_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'Rural Both')][[district]]
        value_rural_both_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'Rural Both')][[district]]

        total_rural_both_df = total_rural_both_df.reset_index(drop=True)
        value_rural_both_df = value_rural_both_df.reset_index(drop=True)

        total_rural_both = total_rural_both_df[district][0]
        value_rural_both = value_rural_both_df[district][0]

        if total_rural_both > 0:
            lit_rural_both = '{:.1f}'.format((value_rural_both / total_rural_both) * 100)
        else:
            lit_rural_both = '{:.1f}'.format(0)

    if (region != None) & (district != None):
        return lit_all, lit_male_all, lit_female_all, lit_urban_male, lit_urban_female, lit_rural_male, lit_rural_female, lit_urban_both, lit_rural_both, district
    else:
        return None, None, None, None, None, None, None, None, None, None


#***************************
#LITERACY & EDUCATION - 3D6a
#***************************
@app.callback(

    #all
    Output('lit_edu_att_all_now', 'children'),
    Output('lit_edu_att_all_past', 'children'),
    Output('lit_edu_att_all_never', 'children'),

    #all, male
    Output('lit_edu_att_all_male_now', 'children'),
    Output('lit_edu_att_all_male_past', 'children'),
    Output('lit_edu_att_all_male_never', 'children'),

    #all, female
    Output('lit_edu_att_all_female_now', 'children'),
    Output('lit_edu_att_all_female_past', 'children'),
    Output('lit_edu_att_all_female_never', 'children'),

    #all, urban
    Output('lit_edu_att_all_urban_now', 'children'),
    Output('lit_edu_att_all_urban_past', 'children'),
    Output('lit_edu_att_all_urban_never', 'children'),

    #urban, male
    Output('lit_edu_att_urban_male_now', 'children'),
    Output('lit_edu_att_urban_male_past', 'children'),
    Output('lit_edu_att_urban_male_never', 'children'),

    #urban, female
    Output('lit_edu_att_urban_female_now', 'children'),
    Output('lit_edu_att_urban_female_past', 'children'),
    Output('lit_edu_att_urban_female_never', 'children'),

    #rural, all
    Output('lit_edu_att_all_rural_now', 'children'),
    Output('lit_edu_att_all_rural_past', 'children'),
    Output('lit_edu_att_all_rural_never', 'children'),

    #rural, male
    Output('lit_edu_att_rural_male_now', 'children'),
    Output('lit_edu_att_rural_male_past', 'children'),
    Output('lit_edu_att_rural_male_never', 'children'),

    #rural, female
    Output('lit_edu_att_rural_female_now', 'children'),
    Output('lit_edu_att_rural_female_past', 'children'),
    Output('lit_edu_att_rural_female_never', 'children'),

    Input('lit_edu_region_dd', 'value'),
    Input('lit_edu_district_dd', 'value')
)
def get_lit_edu_data(region, district):

    df_lit_edu_data = lit_edu_region_3D6a[region]

    value_all_att_df = None
    value_all_nvr_att_df = None

    if (region != None) & (district != None):

        #*****
        # ALL
        #*****
        df_data = df_lit_edu_data.loc[:, ['Status_Code', 'Number', 'Type', 'Percent', district]]
        total_all_df = df_data[(df_data['Status_Code'] == 0) & (df_data['Type'] == 'All')][[district]]
        val_all_never_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'All')][[district]]
        val_all_now_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'All')][[district]]
        val_all_past_df = df_data[(df_data['Status_Code'] == 3) & (df_data['Type'] == 'All')][[district]]

        total_all_df = total_all_df.reset_index(drop=True)
        val_all_never_df = val_all_never_df.reset_index(drop=True)
        val_all_now_df = val_all_now_df.reset_index(drop=True)
        val_all_past_df = val_all_past_df.reset_index(drop=True)

        total_all = total_all_df[district][0]
        val_all_never = val_all_never_df[district][0]
        val_all_now = val_all_now_df[district][0]
        val_all_past = val_all_past_df[district][0]

        if total_all > 0:
            percent_all_never = '{:.1f}'.format((val_all_never / total_all) * 100)
            percent_all_now = '{:.1f}'.format((val_all_now / total_all) * 100)
            percent_all_past = '{:.1f}'.format((val_all_past / total_all) * 100)
        else:
            percent_all_now = '{:.1f}'.format(0)
            percent_all_past = '{:.1f}'.format(0)

        #**********
        # ALL MALE
        #**********
        total_all_male_df = df_data[(df_data['Status_Code'] == 0) & (df_data['Type'] == 'All Male')][[district]]
        val_all_male_never_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'All Male')][[district]]
        val_all_male_now_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'All Male')][[district]]
        val_all_male_past_df = df_data[(df_data['Status_Code'] == 3) & (df_data['Type'] == 'All Male')][[district]]

        total_all_male_df = total_all_male_df.reset_index(drop=True)
        val_all_male_never_df = val_all_male_never_df.reset_index(drop=True)
        val_all_male_now_df = val_all_male_now_df.reset_index(drop=True)
        val_all_male_past_df = val_all_male_past_df.reset_index(drop=True)

        total_all_male = total_all_male_df[district][0]
        val_all_male_never = val_all_male_never_df[district][0]
        val_all_male_now = val_all_male_now_df[district][0]
        val_all_male_past = val_all_male_past_df[district][0]

        if total_all_male > 0:
            percent_all_male_never = '{:.1f}'.format((val_all_male_never / total_all_male) * 100)
            percent_all_male_now = '{:.1f}'.format((val_all_male_now / total_all_male) * 100)
            percent_all_male_past = '{:.1f}'.format((val_all_male_past / total_all_male) * 100)
        else:
            percent_all_male_never = '{:.1f}'.format(0)
            percent_all_male_now = '{:.1f}'.format(0)
            percent_all_male_past = '{:.1f}'.format(0)

        #************
        # ALL FEMALE
        #************
        total_all_female_df = df_data[(df_data['Status_Code'] == 0) & (df_data['Type'] == 'All Female')][[district]]
        val_all_female_never_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'All Female')][[district]]
        val_all_female_now_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'All Female')][[district]]
        val_all_female_past_df = df_data[(df_data['Status_Code'] == 3) & (df_data['Type'] == 'All Female')][[district]]

        total_all_female_df = total_all_female_df.reset_index(drop=True)
        val_all_female_never_df = val_all_female_never_df.reset_index(drop=True)
        val_all_female_now_df = val_all_female_now_df.reset_index(drop=True)
        val_all_female_past_df = val_all_female_past_df.reset_index(drop=True)

        total_all_female = total_all_female_df[district][0]
        val_all_female_never = val_all_female_never_df[district][0]
        val_all_female_now = val_all_female_now_df[district][0]
        val_all_female_past = val_all_female_past_df[district][0]

        if total_all_female > 0:
            percent_all_female_never = '{:.1f}'.format((val_all_female_now / total_all_female) * 100)
            percent_all_female_now = '{:.1f}'.format((val_all_female_now / total_all_female) * 100)
            percent_all_female_past = '{:.1f}'.format((val_all_female_past / total_all_female) * 100)
        else:
            percent_all_female_never = '{:.1f}'.format(0)
            percent_all_female_now = '{:.1f}'.format(0)
            percent_all_female_past = '{:.1f}'.format(0)

        # ************
        # ALL, URBAN
        # ************
        total_all_urban_df = df_data[(df_data['Status_Code'] == 0) & (df_data['Type'] == 'All Urban')][[district]]
        val_all_urban_never_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'All Urban')][[district]]
        val_all_urban_now_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'All Urban')][[district]]
        val_all_urban_past_df = df_data[(df_data['Status_Code'] == 3) & (df_data['Type'] == 'All Urban')][[district]]

        total_all_urban_df = total_all_urban_df.reset_index(drop=True)
        val_all_urban_never_df = val_all_urban_never_df.reset_index(drop=True)
        val_all_urban_now_df = val_all_urban_now_df.reset_index(drop=True)
        val_all_urban_past_df = val_all_urban_past_df.reset_index(drop=True)

        total_all_urban = total_all_urban_df[district][0]
        val_all_urban_never = val_all_urban_never_df[district][0]
        val_all_urban_now = val_all_urban_now_df[district][0]
        val_all_urban_past = val_all_urban_past_df[district][0]

        if total_all_urban > 0:
            percent_all_urban_never = '{:.1f}'.format((val_all_urban_never / total_all_urban) * 100)
            percent_all_urban_now = '{:.1f}'.format((val_all_urban_now / total_all_urban) * 100)
            percent_all_urban_past = '{:.1f}'.format((val_all_urban_past / total_all_urban) * 100)
        else:
            percent_all_urban_never = '{:.1f}'.format(0)
            percent_all_urban_now = '{:.1f}'.format(0)
            percent_all_urban_past = '{:.1f}'.format(0)

        # ************
        # URBAN, MALE
        # ************
        total_urban_male_df = df_data[(df_data['Status_Code'] == 0) & (df_data['Type'] == 'Urban Male')][[district]]
        val_urban_male_never_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'Urban Male')][[district]]
        val_urban_male_now_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'Urban Male')][[district]]
        val_urban_male_past_df = df_data[(df_data['Status_Code'] == 3) & (df_data['Type'] == 'Urban Male')][[district]]

        total_urban_male_df = total_urban_male_df.reset_index(drop=True)
        val_urban_male_never_df = val_urban_male_never_df.reset_index(drop=True)
        val_urban_male_now_df = val_urban_male_now_df.reset_index(drop=True)
        val_urban_male_past_df = val_urban_male_past_df.reset_index(drop=True)

        total_urban_male = total_urban_male_df[district][0]
        val_urban_male_never = val_urban_male_never_df[district][0]
        val_urban_male_now = val_urban_male_now_df[district][0]
        val_urban_male_past = val_urban_male_past_df[district][0]

        if total_urban_male > 0:
            percent_urban_male_never = '{:.1f}'.format((val_urban_male_never / total_urban_male) * 100)
            percent_urban_male_now = '{:.1f}'.format((val_urban_male_now / total_urban_male) * 100)
            percent_urban_male_past = '{:.1f}'.format((val_urban_male_past / total_urban_male) * 100)
        else:
            percent_urban_male_never = '{:.1f}'.format(0)
            percent_urban_male_now = '{:.1f}'.format(0)
            percent_urban_male_past = '{:.1f}'.format(0)

        # ************
        # URBAN, MALE
        # ************
        total_urban_female_df = df_data[(df_data['Status_Code'] == 0) & (df_data['Type'] == 'Urban Female')][[district]]
        val_urban_female_never_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'Urban Female')][[district]]
        val_urban_female_now_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'Urban Female')][[district]]
        val_urban_female_past_df = df_data[(df_data['Status_Code'] == 3) & (df_data['Type'] == 'Urban Male')][[district]]

        total_urban_female_df = total_urban_female_df.reset_index(drop=True)
        val_urban_female_never_df = val_urban_female_never_df.reset_index(drop=True)
        val_urban_female_now_df = val_urban_female_now_df.reset_index(drop=True)
        val_urban_female_past_df = val_urban_female_past_df.reset_index(drop=True)

        total_urban_female = total_urban_female_df[district][0]
        val_urban_female_never = val_urban_female_never_df[district][0]
        val_urban_female_now = val_urban_female_now_df[district][0]
        val_urban_female_past = val_urban_female_past_df[district][0]

        if total_urban_female > 0:
            percent_urban_female_never = '{:.1f}'.format((val_urban_female_never / total_urban_female) * 100)
            percent_urban_female_now = '{:.1f}'.format((val_urban_female_now / total_urban_female) * 100)
            percent_urban_female_past = '{:.1f}'.format((val_urban_female_past / total_urban_female) * 100)
        else:
            percent_urban_female_never = '{:.1f}'.format(0)
            percent_urban_female_now = '{:.1f}'.format(0)
            percent_urban_female_past = '{:.1f}'.format(0)

        # ************
        # ALL, RURAL
        # ************
        total_all_rural_df = df_data[(df_data['Status_Code'] == 0) & (df_data['Type'] == 'Rural Male')][[district]]
        val_all_rural_never_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'Rural Male')][[district]]
        val_all_rural_now_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'Rural Male')][[district]]
        val_all_rural_past_df = df_data[(df_data['Status_Code'] == 3) & (df_data['Type'] == 'Rural Male')][[district]]

        total_all_rural_df = total_all_rural_df.reset_index(drop=True)
        val_all_rural_never_df = val_all_rural_never_df.reset_index(drop=True)
        val_all_rural_now_df = val_all_rural_now_df.reset_index(drop=True)
        val_all_rural_past_df = val_all_rural_past_df.reset_index(drop=True)

        total_all_rural = total_all_rural_df[district][0]
        val_all_rural_never = val_all_rural_never_df[district][0]
        val_all_rural_now = val_all_rural_now_df[district][0]
        val_all_rural_past = val_all_rural_past_df[district][0]

        if total_all_rural > 0:
            percent_all_rural_never = '{:.1f}'.format((val_all_rural_never / total_all_rural) * 100)
            percent_all_rural_now = '{:.1f}'.format((val_all_rural_now / total_all_rural) * 100)
            percent_all_rural_past = '{:.1f}'.format((val_all_rural_past / total_all_rural) * 100)
        else:
            percent_all_rural_never = '{:.1f}'.format(0)
            percent_all_rural_now = '{:.1f}'.format(0)
            percent_all_rural_past = '{:.1f}'.format(0)

        # ************
        # RURAL, MALE
        # ************
        total_rural_male_df = df_data[(df_data['Status_Code'] == 0) & (df_data['Type'] == 'All Rural')][[district]]
        val_rural_male_never_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'All Rural')][[district]]
        val_rural_male_now_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'All Rural')][[district]]
        val_rural_male_past_df = df_data[(df_data['Status_Code'] == 3) & (df_data['Type'] == 'All Rural')][[district]]

        total_rural_male_df = total_rural_male_df.reset_index(drop=True)
        val_rural_male_never_df = val_rural_male_never_df.reset_index(drop=True)
        val_rural_male_now_df = val_rural_male_now_df.reset_index(drop=True)
        val_rural_male_past_df = val_rural_male_past_df.reset_index(drop=True)

        total_rural_male = total_rural_male_df[district][0]
        val_rural_male_never = val_rural_male_never_df[district][0]
        val_rural_male_now = val_rural_male_now_df[district][0]
        val_rural_male_past = val_rural_male_past_df[district][0]

        if total_rural_male > 0:
            percent_rural_male_never = '{:.1f}'.format((val_rural_male_never / total_rural_male) * 100)
            percent_rural_male_now = '{:.1f}'.format((val_rural_male_now / total_rural_male) * 100)
            percent_rural_male_past = '{:.1f}'.format((val_rural_male_past / total_rural_male) * 100)
        else:
            percent_rural_male_never = '{:.1f}'.format(0)
            percent_rural_male_now = '{:.1f}'.format(0)
            percent_rural_male_past = '{:.1f}'.format(0)

        # ************
        # RURAL, MALE
        # ************
        total_rural_female_df = df_data[(df_data['Status_Code'] == 0) & (df_data['Type'] == 'Rural Female')][[district]]
        val_rural_female_never_df = df_data[(df_data['Status_Code'] == 1) & (df_data['Type'] == 'Rural Female')][[district]]
        val_rural_female_now_df = df_data[(df_data['Status_Code'] == 2) & (df_data['Type'] == 'Rural Female')][[district]]
        val_rural_female_past_df = df_data[(df_data['Status_Code'] == 3) & (df_data['Type'] == 'Rural Female')][[district]]

        total_rural_female_df = total_rural_female_df.reset_index(drop=True)
        val_rural_female_never_df = val_rural_female_never_df.reset_index(drop=True)
        val_rural_female_now_df = val_rural_female_now_df.reset_index(drop=True)
        val_rural_female_past_df = val_rural_female_past_df.reset_index(drop=True)

        total_rural_female = total_rural_female_df[district][0]
        val_rural_female_never = val_rural_female_never_df[district][0]
        val_rural_female_now = val_rural_female_now_df[district][0]
        val_rural_female_past = val_rural_female_past_df[district][0]

        if total_rural_female > 0:
            percent_rural_female_never = '{:.1f}'.format((val_rural_female_never / total_rural_female) * 100)
            percent_rural_female_now = '{:.1f}'.format((val_rural_female_now / total_rural_female) * 100)
            percent_rural_female_past = '{:.1f}'.format((val_rural_female_past / total_rural_female) * 100)
        else:
            percent_rural_female_never = '{:.1f}'.format(0)
            percent_rural_female_now = '{:.1f}'.format(0)
            percent_rural_female_past = '{:.1f}'.format(0)

        return percent_all_now, percent_all_past, percent_all_never, \
               percent_all_male_now, percent_all_male_past, percent_all_male_never, \
               percent_all_female_now, percent_all_female_past, percent_all_female_never, \
               percent_all_urban_now, percent_all_urban_past, percent_all_urban_never, \
               percent_urban_male_now, percent_urban_male_past, percent_urban_male_never, \
               percent_urban_female_now, percent_urban_female_past, percent_urban_female_never, \
               percent_all_rural_now, percent_all_rural_past, percent_all_rural_never, \
               percent_rural_male_now, percent_rural_male_past, percent_rural_male_never, \
               percent_rural_female_now, percent_rural_female_past, percent_rural_female_never
    else:
        return None, None, None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, None, None, \
               None, None, None, None, None, None, None, None, None

#***********************************
# DIFFICULTY IN PERFORMING ACTIVITES
#***********************************
#categories
@app.callback(

    #all
    Output('dpa_all_total_val', 'children'),
    Output('dpa_all_no_diff_val', 'children'),
    Output('dpa_all_some_diff_val', 'children'),
    Output('dpa_all_lot_diff_val', 'children'),
    Output('dpa_all_cannot_do_at_all_val', 'children'),

    Output('dpa_all_percent', 'children'),
    Output('dpa_all_no_diff_percent', 'children'),
    Output('dpa_all_some_diff_percent', 'children'),
    Output('dpa_all_lot_diff_percent', 'children'),
    Output('dpa_all_cannot_do_at_all_percent', 'children'),

    #male
    Output('dpa_male_total_val', 'children'),
    Output('dpa_male_no_diff_val', 'children'),
    Output('dpa_male_some_diff_val', 'children'),
    Output('dpa_male_lot_diff_val', 'children'),
    Output('dpa_male_cannot_do_at_all_val', 'children'),

    Output('dpa_male_percent', 'children'),
    Output('dpa_male_no_diff_percent', 'children'),
    Output('dpa_male_some_diff_percent', 'children'),
    Output('dpa_male_lot_diff_percent', 'children'),
    Output('dpa_male_cannot_do_at_all_percent', 'children'),

    # female
    Output('dpa_female_total_val', 'children'),
    Output('dpa_female_no_diff_val', 'children'),
    Output('dpa_female_some_diff_val', 'children'),
    Output('dpa_female_lot_diff_val', 'children'),
    Output('dpa_female_cannot_do_at_all_val', 'children'),

    Output('dpa_female_percent', 'children'),
    Output('dpa_female_no_diff_percent', 'children'),
    Output('dpa_female_some_diff_percent', 'children'),
    Output('dpa_female_lot_diff_percent', 'children'),
    Output('dpa_female_cannot_do_at_all_percent', 'children'),

    # urban
    Output('dpa_urban_total_val', 'children'),
    Output('dpa_urban_no_diff_val', 'children'),
    Output('dpa_urban_some_diff_val', 'children'),
    Output('dpa_urban_lot_diff_val', 'children'),
    Output('dpa_urban_cannot_do_at_all_val', 'children'),

    Output('dpa_urban_percent', 'children'),
    Output('dpa_urban_no_diff_percent', 'children'),
    Output('dpa_urban_some_diff_percent', 'children'),
    Output('dpa_urban_lot_diff_percent', 'children'),
    Output('dpa_urban_cannot_do_at_all_percent', 'children'),

    # rural
    Output('dpa_rural_total_val', 'children'),
    Output('dpa_rural_no_diff_val', 'children'),
    Output('dpa_rural_some_diff_val', 'children'),
    Output('dpa_rural_lot_diff_val', 'children'),
    Output('dpa_rural_cannot_do_at_all_val', 'children'),

    Output('dpa_rural_percent', 'children'),
    Output('dpa_rural_no_diff_percent', 'children'),
    Output('dpa_rural_some_diff_percent', 'children'),
    Output('dpa_rural_lot_diff_percent', 'children'),
    Output('dpa_rural_cannot_do_at_all_percent', 'children'),

    # urban male
    Output('dpa_urban_male_total_val', 'children'),
    Output('dpa_urban_male_no_diff_val', 'children'),
    Output('dpa_urban_male_some_diff_val', 'children'),
    Output('dpa_urban_male_lot_diff_val', 'children'),
    Output('dpa_urban_male_cannot_do_at_all_val', 'children'),

    Output('dpa_urban_male_percent', 'children'),
    Output('dpa_urban_male_no_diff_percent', 'children'),
    Output('dpa_urban_male_some_diff_percent', 'children'),
    Output('dpa_urban_male_lot_diff_percent', 'children'),
    Output('dpa_urban_male_cannot_do_at_all_percent', 'children'),

    # urban female
    Output('dpa_urban_female_total_val', 'children'),
    Output('dpa_urban_female_no_diff_val', 'children'),
    Output('dpa_urban_female_some_diff_val', 'children'),
    Output('dpa_urban_female_lot_diff_val', 'children'),
    Output('dpa_urban_female_cannot_do_at_all_val', 'children'),

    Output('dpa_urban_female_percent', 'children'),
    Output('dpa_urban_female_no_diff_percent', 'children'),
    Output('dpa_urban_female_some_diff_percent', 'children'),
    Output('dpa_urban_female_lot_diff_percent', 'children'),
    Output('dpa_urban_female_cannot_do_at_all_percent', 'children'),

    # rural male
    Output('dpa_rural_male_total_val', 'children'),
    Output('dpa_rural_male_no_diff_val', 'children'),
    Output('dpa_rural_male_some_diff_val', 'children'),
    Output('dpa_rural_male_lot_diff_val', 'children'),
    Output('dpa_rural_male_cannot_do_at_all_val', 'children'),

    Output('dpa_rural_male_percent', 'children'),
    Output('dpa_rural_male_no_diff_percent', 'children'),
    Output('dpa_rural_male_some_diff_percent', 'children'),
    Output('dpa_rural_male_lot_diff_percent', 'children'),
    Output('dpa_rural_male_cannot_do_at_all_percent', 'children'),

    # rural female
    Output('dpa_rural_female_total_val', 'children'),
    Output('dpa_rural_female_no_diff_val', 'children'),
    Output('dpa_rural_female_some_diff_val', 'children'),
    Output('dpa_rural_female_lot_diff_val', 'children'),
    Output('dpa_rural_female_cannot_do_at_all_val', 'children'),

    Output('dpa_rural_female_percent', 'children'),
    Output('dpa_rural_female_no_diff_percent', 'children'),
    Output('dpa_rural_female_some_diff_percent', 'children'),
    Output('dpa_rural_female_lot_diff_percent', 'children'),
    Output('dpa_rural_female_cannot_do_at_all_percent', 'children'),

    # INPUT
    Input('dpa_region_dd', 'value'),
    Input('dpa_district_dd', 'value'),
    Input('dpa_category_dd', 'value')
)
def get_diff_perf_act_data(region, district, category):

    #all
    total_seeing = None
    no_diff_seeing = None
    some_diff_seeing = None
    lot_diff_seeing = None
    cannot_do_seeing = None
    total_seeing_percent = None
    no_diff_seeing_percent = None
    some_diff_seeing_percent = None
    lot_diff_seeing_percent = None
    cannot_do_seeing_percent = None

    #male
    total_seeing_male = None
    no_diff_seeing_male = None
    some_diff_seeing_male = None
    lot_diff_seeing_male = None
    cannot_do_seeing_male = None
    total_seeing_male_percent = None
    no_diff_seeing_male_percent = None
    some_diff_seeing_male_percent = None
    lot_diff_seeing_male_percent = None
    cannot_do_seeing_male_percent = None

    #female
    total_seeing_female = None
    no_diff_seeing_female = None
    some_diff_seeing_female = None
    lot_diff_seeing_female = None
    cannot_do_seeing_female = None
    total_seeing_female_percent = None
    no_diff_seeing_female_percent = None
    some_diff_seeing_female_percent = None
    lot_diff_seeing_female_percent = None
    cannot_do_seeing_female_percent = None

    #urban
    total_seeing_urban = None
    no_diff_seeing_urban = None
    some_diff_seeing_urban = None
    lot_diff_seeing_urban = None
    cannot_do_seeing_urban = None
    total_seeing_urban_percent = None
    no_diff_seeing_urban_percent = None
    some_diff_seeing_urban_percent = None
    lot_diff_seeing_urban_percent = None
    cannot_do_seeing_urban_percent = None

    #rural
    total_seeing_rural = None
    no_diff_seeing_rural = None
    some_diff_seeing_rural = None
    lot_diff_seeing_rural = None
    cannot_do_seeing_rural = None
    total_seeing_rural_percent = None
    no_diff_seeing_rural_percent = None
    some_diff_seeing_rural_percent = None
    lot_diff_seeing_rural_percent = None
    cannot_do_seeing_rural_percent = None

    # urban male
    total_seeing_urban_male = None
    no_diff_seeing_urban_male = None
    some_diff_seeing_urban_male = None
    lot_diff_seeing_urban_male = None
    cannot_do_seeing_urban_male = None
    total_seeing_urban_male_percent = None
    no_diff_seeing_urban_male_percent = None
    some_diff_seeing_urban_male_percent = None
    lot_diff_seeing_urban_male_percent = None
    cannot_do_seeing_urban_male_percent = None

    #urban female
    total_seeing_urban_female = None
    no_diff_seeing_urban_female = None
    some_diff_seeing_urban_female = None
    lot_diff_seeing_urban_female = None
    cannot_do_seeing_urban_female = None
    total_seeing_urban_female_percent = None
    no_diff_seeing_urban_female_percent = None
    some_diff_seeing_urban_female_percent = None
    lot_diff_seeing_urban_female_percent = None
    cannot_do_seeing_urban_female_percent = None

    # rural male
    total_seeing_rural_male = None
    no_diff_seeing_rural_male = None
    some_diff_seeing_rural_male = None
    lot_diff_seeing_rural_male = None
    cannot_do_seeing_rural_male = None
    total_seeing_rural_male_percent = None
    no_diff_seeing_rural_male_percent = None
    some_diff_seeing_rural_male_percent = None
    lot_diff_seeing_rural_male_percent = None
    cannot_do_seeing_rural_male_percent = None

    # rural female
    total_seeing_rural_female = None
    no_diff_seeing_rural_female = None
    some_diff_seeing_rural_female = None
    lot_diff_seeing_rural_female = None
    cannot_do_seeing_rural_female = None
    total_seeing_rural_female_percent = None
    no_diff_seeing_rural_female_percent = None
    some_diff_seeing_rural_female_percent = None
    lot_diff_seeing_rural_female_percent = None
    cannot_do_seeing_rural_female_percent = None

    if (region != None) & (district != None) & (district != None):

        if region == 'Western':
            df_dpa_data = df_diff_perf_act_3F2a_western
            df_dpa_data_all_domain = df_diff_perf_act_3F5a_western
        if region == 'Central':
            df_dpa_data = df_diff_perf_act_3F2a_central

        #Seeing
        if category == 'Seeing':

            df_data = df_dpa_data[(df_dpa_data['Category'] == 10) & (
                df_dpa_data['Status_Code'].isin(['S', '1', '2', '3', '4']))] \
                [['Status', 'Category', 'Status_Code', 'Type', district]]

            # all - both sexes
            all_stats_df = df_data[df_data['Type'] == 'All']
            all_stats_df = all_stats_df.reset_index(drop=True)

            total_seeing_df = all_stats_df[all_stats_df['Category'] == 10][
                ['Status', 'Category', 'Status_Code', district]]
            total_seeing_df = total_seeing_df.reset_index(drop=True)
            total_seeing = total_seeing_df[total_seeing_df['Status'] == 'Seeing'][district][0]

            no_diff_seeing = total_seeing_df[total_seeing_df['Status_Code'] == '1'][district][1]
            some_diff_seeing = total_seeing_df[total_seeing_df['Status_Code'] == '2'][district][2]
            lot_diff_seeing = total_seeing_df[total_seeing_df['Status_Code'] == '3'][district][3]
            cannot_do_seeing = total_seeing_df[total_seeing_df['Status_Code'] == '4'][district][4]

            no_diff_seeing_percent = '{:.1f}'.format((no_diff_seeing / total_seeing) * 100)
            some_diff_seeing_percent = '{:.1f}'.format((some_diff_seeing / total_seeing) * 100)
            lot_diff_seeing_percent = '{:.1f}'.format((lot_diff_seeing / total_seeing) * 100)
            cannot_do_seeing_percent = '{:.1f}'.format((cannot_do_seeing / total_seeing) * 100)

            total_seeing = '{:,}'.format(total_seeing)
            total_seeing_percent = 100
            no_diff_seeing = '{:,}'.format(no_diff_seeing)
            some_diff_seeing = '{:,}'.format(some_diff_seeing)
            lot_diff_seeing = '{:,}'.format(lot_diff_seeing)
            cannot_do_seeing = '{:,}'.format(cannot_do_seeing)

            #males
            # *********
            male_stats_df = df_dpa_data[df_dpa_data['Type'] == 'Male']
            male_stats_df = male_stats_df.reset_index(drop=True)

            total_seeing_male_df = male_stats_df[male_stats_df['Category'] == 10][
                ['Status', 'Category', 'Status_Code', district]]
            total_seeing_male_df = total_seeing_male_df.reset_index(drop=True)
            total_seeing_male = total_seeing_male_df[total_seeing_male_df['Status'] == 'Seeing'][district][0]

            no_diff_seeing_male = total_seeing_male_df[total_seeing_male_df['Status_Code'] == '1'][district][1]
            some_diff_seeing_male = total_seeing_male_df[total_seeing_male_df['Status_Code'] == '2'][district][2]
            lot_diff_seeing_male = total_seeing_male_df[total_seeing_male_df['Status_Code'] == '3'][district][3]
            cannot_do_seeing_male = total_seeing_male_df[total_seeing_male_df['Status_Code'] == '4'][district][4]

            no_diff_seeing__male_percent = '{:.1f}'.format((no_diff_seeing_male / total_seeing_male) * 100)
            some_diff_seeing_male_percent = '{:.1f}'.format((some_diff_seeing_male / total_seeing_male) * 100)
            lot_diff_seeing_male_percent = '{:.1f}'.format((lot_diff_seeing_male / total_seeing_male) * 100)
            cannot_do_seeing_male_percent = '{:.1f}'.format((cannot_do_seeing_male / total_seeing_male) * 100)

            total_seeing_male = '{:,}'.format(total_seeing_male)
            total_seeing_male_percent = 100
            no_diff_seeing_male = '{:,}'.format(no_diff_seeing_male)
            some_diff_seeing_male = '{:,}'.format(some_diff_seeing_male)
            lot_diff_seeing_male = '{:,}'.format(lot_diff_seeing_male)
            cannot_do_seeing_male = '{:,}'.format(cannot_do_seeing_male)

            # females
            # *********
            female_stats_df = df_dpa_data[df_dpa_data['Type'] == 'Female']
            female_stats_df = female_stats_df.reset_index(drop=True)

            total_seeing_female_df = female_stats_df[female_stats_df['Category'] == 10][
                ['Status', 'Category', 'Status_Code', district]]
            total_seeing_female_df = total_seeing_female_df.reset_index(drop=True)
            total_seeing_female = total_seeing_female_df[total_seeing_female_df['Status'] == 'Seeing'][district][0]

            no_diff_seeing_female = total_seeing_female_df[total_seeing_female_df['Status_Code'] == '1'][district][1]
            some_diff_seeing_female = total_seeing_female_df[total_seeing_female_df['Status_Code'] == '2'][district][2]
            lot_diff_seeing_female = total_seeing_female_df[total_seeing_female_df['Status_Code'] == '3'][district][3]
            cannot_do_seeing_female = total_seeing_female_df[total_seeing_female_df['Status_Code'] == '4'][district][4]

            no_diff_seeing__female_percent = '{:.1f}'.format((no_diff_seeing_female / total_seeing_female) * 100)
            some_diff_seeing_female_percent = '{:.1f}'.format((some_diff_seeing_female / total_seeing_female) * 100)
            lot_diff_seeing_female_percent = '{:.1f}'.format((lot_diff_seeing_female / total_seeing_female) * 100)
            cannot_do_seeing_female_percent = '{:.1f}'.format((cannot_do_seeing_female / total_seeing_female) * 100)

            total_seeing_female = '{:,}'.format(total_seeing_female)
            total_seeing_female_percent = 100
            no_diff_seeing_female = '{:,}'.format(no_diff_seeing_female)
            some_diff_seeing_female = '{:,}'.format(some_diff_seeing_female)
            lot_diff_seeing_female = '{:,}'.format(lot_diff_seeing_female)
            cannot_do_seeing_female = '{:,}'.format(cannot_do_seeing_female)

            # Urban
            # *********
            urban_stats_df = df_dpa_data[df_dpa_data['Type'] == 'Urban All']
            urban_stats_df = urban_stats_df.reset_index(drop=True)

            total_seeing_urban_df = urban_stats_df[urban_stats_df['Category'] == 10][
                ['Status', 'Category', 'Status_Code', district]]
            total_seeing_urban_df = total_seeing_urban_df.reset_index(drop=True)
            total_seeing_urban = total_seeing_urban_df[total_seeing_urban_df['Status'] == 'Seeing'][district][0]

            no_diff_seeing_urban = total_seeing_urban_df[total_seeing_urban_df['Status_Code'] == '1'][district][1]
            some_diff_seeing_urban = total_seeing_urban_df[total_seeing_urban_df['Status_Code'] == '2'][district][2]
            lot_diff_seeing_urban = total_seeing_urban_df[total_seeing_urban_df['Status_Code'] == '3'][district][3]
            cannot_do_seeing_urban = total_seeing_urban_df[total_seeing_urban_df['Status_Code'] == '4'][district][4]

            no_diff_seeing_urban_percent = '{:.1f}'.format((no_diff_seeing_urban / total_seeing_urban) * 100)
            some_diff_seeing_urban_percent = '{:.1f}'.format((some_diff_seeing_urban / total_seeing_urban) * 100)
            lot_diff_seeing_urban_percent = '{:.1f}'.format((lot_diff_seeing_urban / total_seeing_urban) * 100)
            cannot_do_seeing_urban_percent = '{:.1f}'.format((cannot_do_seeing_urban / total_seeing_urban) * 100)

            total_seeing_urban = '{:,}'.format(total_seeing_urban)
            total_seeing_urban_percent = 100
            no_diff_seeing_urban = '{:,}'.format(no_diff_seeing_urban)
            some_diff_seeing_urban = '{:,}'.format(some_diff_seeing_urban)
            lot_diff_seeing_urban = '{:,}'.format(lot_diff_seeing_urban)
            cannot_do_seeing_urban = '{:,}'.format(cannot_do_seeing_urban)

            # Rural
            # *********
            rural_stats_df = df_dpa_data[df_dpa_data['Type'] == 'Rural All']
            rural_stats_df = rural_stats_df.reset_index(drop=True)

            total_seeing_rural_df = rural_stats_df[rural_stats_df['Category'] == 10][
                ['Status', 'Category', 'Status_Code', district]]
            total_seeing_rural_df = total_seeing_rural_df.reset_index(drop=True)
            total_seeing_rural = total_seeing_rural_df[total_seeing_rural_df['Status'] == 'Seeing'][district][0]

            no_diff_seeing_rural = total_seeing_rural_df[total_seeing_rural_df['Status_Code'] == '1'][district][1]
            some_diff_seeing_rural = total_seeing_rural_df[total_seeing_rural_df['Status_Code'] == '2'][district][2]
            lot_diff_seeing_rural = total_seeing_rural_df[total_seeing_rural_df['Status_Code'] == '3'][district][3]
            cannot_do_seeing_rural = total_seeing_rural_df[total_seeing_rural_df['Status_Code'] == '4'][district][4]

            no_diff_seeing_rural_percent = '{:.1f}'.format((no_diff_seeing_rural / total_seeing_rural) * 100)
            some_diff_seeing_rural_percent = '{:.1f}'.format((some_diff_seeing_rural / total_seeing_rural) * 100)
            lot_diff_seeing_rural_percent = '{:.1f}'.format((lot_diff_seeing_rural / total_seeing_rural) * 100)
            cannot_do_seeing_rural_percent = '{:.1f}'.format((cannot_do_seeing_rural / total_seeing_rural) * 100)

            total_seeing_rural = '{:,}'.format(total_seeing_rural)
            total_seeing_rural_percent = 100
            no_diff_seeing_rural = '{:,}'.format(no_diff_seeing_rural)
            some_diff_seeing_rural = '{:,}'.format(some_diff_seeing_rural)
            lot_diff_seeing_rural = '{:,}'.format(lot_diff_seeing_rural)
            cannot_do_seeing_rural = '{:,}'.format(cannot_do_seeing_rural)

            # Urban Male
            # *********
            urban_male_stats_df = df_dpa_data[df_dpa_data['Type'] == 'Urban Male']
            urban_male_stats_df = urban_male_stats_df.reset_index(drop=True)

            total_seeing_urban_male_df = urban_male_stats_df[urban_male_stats_df['Category'] == 10][
                ['Status', 'Category', 'Status_Code', district]]
            total_seeing_urban_male_df = total_seeing_urban_male_df.reset_index(drop=True)
            total_seeing_urban_male = total_seeing_urban_male_df[total_seeing_urban_male_df['Status'] == 'Seeing'][district][0]

            no_diff_seeing_urban_male = total_seeing_urban_male_df[total_seeing_urban_male_df['Status_Code'] == '1'][district][1]
            some_diff_seeing_urban_male = total_seeing_urban_male_df[total_seeing_urban_male_df['Status_Code'] == '2'][district][2]
            lot_diff_seeing_urban_male = total_seeing_urban_male_df[total_seeing_urban_male_df['Status_Code'] == '3'][district][3]
            cannot_do_seeing_urban_male = total_seeing_urban_male_df[total_seeing_urban_male_df['Status_Code'] == '4'][district][4]

            no_diff_seeing_urban_male_percent = '{:.1f}'.format((no_diff_seeing_urban_male / total_seeing_urban_male) * 100)
            some_diff_seeing_urban_male_percent = '{:.1f}'.format((some_diff_seeing_urban_male / total_seeing_urban_male) * 100)
            lot_diff_seeing_urban_male_percent = '{:.1f}'.format((lot_diff_seeing_urban_male / total_seeing_urban_male) * 100)
            cannot_do_seeing_urban_male_percent = '{:.1f}'.format((cannot_do_seeing_urban_male / total_seeing_urban_male) * 100)

            total_seeing_urban_male = '{:,}'.format(total_seeing_urban_male)
            total_seeing_urban_male_percent = 100
            no_diff_seeing_urban_male = '{:,}'.format(no_diff_seeing_urban_male)
            some_diff_seeing_urban_male = '{:,}'.format(some_diff_seeing_urban_male)
            lot_diff_seeing_urban_male = '{:,}'.format(lot_diff_seeing_urban_male)
            cannot_do_seeing_urban_male = '{:,}'.format(cannot_do_seeing_urban_male)

            # Urban Female
            # *********
            urban_female_stats_df = df_dpa_data[df_dpa_data['Type'] == 'Urban Female']
            urban_female_stats_df = urban_female_stats_df.reset_index(drop=True)

            total_seeing_urban_female_df = urban_female_stats_df[urban_female_stats_df['Category'] == 10][['Status', 'Category', 'Status_Code', district]]
            total_seeing_urban_female_df = total_seeing_urban_female_df.reset_index(drop=True)
            total_seeing_urban_female = total_seeing_urban_female_df[total_seeing_urban_female_df['Status'] == 'Seeing'][district][0]

            no_diff_seeing_urban_female = total_seeing_urban_female_df[total_seeing_urban_female_df['Status_Code'] == '1'][district][1]
            some_diff_seeing_urban_female = total_seeing_urban_female_df[total_seeing_urban_female_df['Status_Code'] == '2'][district][2]
            lot_diff_seeing_urban_female = total_seeing_urban_female_df[total_seeing_urban_female_df['Status_Code'] == '3'][district][3]
            cannot_do_seeing_urban_female = total_seeing_urban_female_df[total_seeing_urban_female_df['Status_Code'] == '4'][district][4]

            no_diff_seeing_urban_female_percent = '{:.1f}'.format((no_diff_seeing_urban_female / total_seeing_urban_female) * 100)
            some_diff_seeing_urban_female_percent = '{:.1f}'.format((some_diff_seeing_urban_female / total_seeing_urban_female) * 100)
            lot_diff_seeing_urban_female_percent = '{:.1f}'.format((lot_diff_seeing_urban_female / total_seeing_urban_female) * 100)
            cannot_do_seeing_urban_female_percent = '{:.1f}'.format((cannot_do_seeing_urban_female / total_seeing_urban_female) * 100)

            total_seeing_urban_female = '{:,}'.format(total_seeing_urban_female)
            total_seeing_urban_female_percent = 100
            no_diff_seeing_urban_female = '{:,}'.format(no_diff_seeing_urban_female)
            some_diff_seeing_urban_female = '{:,}'.format(some_diff_seeing_urban_female)
            lot_diff_seeing_urban_female = '{:,}'.format(lot_diff_seeing_urban_female)
            cannot_do_seeing_urban_female = '{:,}'.format(cannot_do_seeing_urban_female)

            # Rural Male
            # *********
            rural_male_stats_df = df_dpa_data[df_dpa_data['Type'] == 'Rural Male']
            rural_male_stats_df = rural_male_stats_df.reset_index(drop=True)

            total_seeing_rural_male_df = rural_male_stats_df[rural_male_stats_df['Category'] == 10][
                ['Status', 'Category', 'Status_Code', district]]
            total_seeing_rural_male_df = total_seeing_rural_male_df.reset_index(drop=True)
            total_seeing_rural_male = total_seeing_rural_male_df[total_seeing_rural_male_df['Status'] == 'Seeing'][district][0]

            no_diff_seeing_rural_male = total_seeing_rural_male_df[total_seeing_rural_male_df['Status_Code'] == '1'][district][1]
            some_diff_seeing_rural_male = total_seeing_rural_male_df[total_seeing_rural_male_df['Status_Code'] == '2'][district][2]
            lot_diff_seeing_rural_male = total_seeing_rural_male_df[total_seeing_rural_male_df['Status_Code'] == '3'][district][3]
            cannot_do_seeing_rural_male = total_seeing_rural_male_df[total_seeing_rural_male_df['Status_Code'] == '4'][district][4]

            no_diff_seeing_rural_male_percent = '{:.1f}'.format((no_diff_seeing_rural_male / total_seeing_rural_male) * 100)
            some_diff_seeing_rural_male_percent = '{:.1f}'.format((some_diff_seeing_rural_male / total_seeing_rural_male) * 100)
            lot_diff_seeing_rural_male_percent = '{:.1f}'.format((lot_diff_seeing_rural_male / total_seeing_rural_male) * 100)
            cannot_do_seeing_rural_male_percent = '{:.1f}'.format((cannot_do_seeing_rural_male / total_seeing_rural_male) * 100)

            total_seeing_rural_male = '{:,}'.format(total_seeing_rural_male)
            total_seeing_rural_male_percent = 100
            no_diff_seeing_rural_male = '{:,}'.format(no_diff_seeing_rural_male)
            some_diff_seeing_rural_male = '{:,}'.format(some_diff_seeing_rural_male)
            lot_diff_seeing_rural_male = '{:,}'.format(lot_diff_seeing_rural_male)
            cannot_do_seeing_rural_male = '{:,}'.format(cannot_do_seeing_rural_male)

            # Rural Female
            # *********
            rural_female_stats_df = df_dpa_data[df_dpa_data['Type'] == 'Rural Female']
            rural_female_stats_df = rural_female_stats_df.reset_index(drop=True)

            total_seeing_rural_female_df = rural_female_stats_df[rural_female_stats_df['Category'] == 10][['Status', 'Category', 'Status_Code', district]]
            total_seeing_rural_female_df = total_seeing_rural_female_df.reset_index(drop=True)
            total_seeing_rural_female = total_seeing_rural_female_df[total_seeing_rural_female_df['Status'] == 'Seeing'][district][0]

            no_diff_seeing_rural_female = total_seeing_rural_female_df[total_seeing_rural_female_df['Status_Code'] == '1'][district][1]
            some_diff_seeing_rural_female = total_seeing_rural_female_df[total_seeing_rural_female_df['Status_Code'] == '2'][district][2]
            lot_diff_seeing_rural_female = total_seeing_rural_female_df[total_seeing_rural_female_df['Status_Code'] == '3'][district][3]
            cannot_do_seeing_rural_female = total_seeing_rural_female_df[total_seeing_rural_female_df['Status_Code'] == '4'][district][4]

            no_diff_seeing_rural_female_percent = '{:.1f}'.format((no_diff_seeing_rural_female / total_seeing_rural_female) * 100)
            some_diff_seeing_rural_female_percent = '{:.1f}'.format((some_diff_seeing_rural_female / total_seeing_rural_female) * 100)
            lot_diff_seeing_rural_female_percent = '{:.1f}'.format((lot_diff_seeing_rural_female / total_seeing_rural_female) * 100)
            cannot_do_seeing_rural_female_percent = '{:.1f}'.format((cannot_do_seeing_rural_female / total_seeing_rural_female) * 100)

            total_seeing_rural_female = '{:,}'.format(total_seeing_rural_female)
            total_seeing_rural_female_percent = 100
            no_diff_seeing_rural_female = '{:,}'.format(no_diff_seeing_rural_female)
            some_diff_seeing_rural_female = '{:,}'.format(some_diff_seeing_rural_female)
            lot_diff_seeing_rural_female = '{:,}'.format(lot_diff_seeing_rural_female)
            cannot_do_seeing_rural_female = '{:,}'.format(cannot_do_seeing_rural_female)

            return total_seeing, no_diff_seeing, some_diff_seeing, lot_diff_seeing, cannot_do_seeing, \
                    total_seeing_percent, no_diff_seeing_percent, some_diff_seeing_percent, lot_diff_seeing_percent, cannot_do_seeing_percent, \
                    total_seeing_male, no_diff_seeing_male, some_diff_seeing_male, lot_diff_seeing_male, cannot_do_seeing_male, \
                    total_seeing_male_percent, no_diff_seeing__male_percent, some_diff_seeing_male_percent, lot_diff_seeing_male_percent, cannot_do_seeing_male_percent, \
                    total_seeing_female, no_diff_seeing_female, some_diff_seeing_female, lot_diff_seeing_female, cannot_do_seeing_female, \
                    total_seeing_female_percent, no_diff_seeing__female_percent, some_diff_seeing_female_percent, lot_diff_seeing_female_percent, cannot_do_seeing_female_percent, \
                    total_seeing_urban, no_diff_seeing_urban, some_diff_seeing_urban, lot_diff_seeing_urban, cannot_do_seeing_urban, \
                    total_seeing_urban_percent, no_diff_seeing_urban_percent, some_diff_seeing_urban_percent, lot_diff_seeing_urban_percent, cannot_do_seeing_urban_percent, \
                    total_seeing_rural, no_diff_seeing_rural, some_diff_seeing_rural, lot_diff_seeing_rural, cannot_do_seeing_rural, \
                    total_seeing_rural_percent, no_diff_seeing_rural_percent, some_diff_seeing_rural_percent, lot_diff_seeing_rural_percent, cannot_do_seeing_rural_percent, \
                    total_seeing_urban_male, no_diff_seeing_urban_male, some_diff_seeing_urban_male, lot_diff_seeing_urban_male, cannot_do_seeing_urban_male, \
                    total_seeing_urban_male_percent, no_diff_seeing_urban_male_percent, some_diff_seeing_urban_male_percent, lot_diff_seeing_urban_male_percent, cannot_do_seeing_urban_male_percent, \
                    total_seeing_urban_female, no_diff_seeing_urban_female, some_diff_seeing_urban_female, lot_diff_seeing_urban_female, cannot_do_seeing_urban_female, \
                    total_seeing_urban_female_percent, no_diff_seeing_urban_female_percent, some_diff_seeing_urban_female_percent, lot_diff_seeing_urban_female_percent, cannot_do_seeing_urban_female_percent, \
                    total_seeing_rural_male, no_diff_seeing_rural_male, some_diff_seeing_rural_male, lot_diff_seeing_rural_male, cannot_do_seeing_rural_male, \
                    total_seeing_rural_male_percent, no_diff_seeing_rural_male_percent, some_diff_seeing_rural_male_percent, lot_diff_seeing_rural_male_percent, cannot_do_seeing_rural_male_percent, \
                    total_seeing_rural_female, no_diff_seeing_rural_female, some_diff_seeing_rural_female, lot_diff_seeing_rural_female, cannot_do_seeing_rural_female, \
                    total_seeing_rural_female_percent, no_diff_seeing_rural_female_percent, some_diff_seeing_rural_female_percent, lot_diff_seeing_rural_female_percent, cannot_do_seeing_rural_female_percent

        return  total_seeing, no_diff_seeing, some_diff_seeing, lot_diff_seeing, cannot_do_seeing, \
                total_seeing_percent, no_diff_seeing_percent, some_diff_seeing_percent, lot_diff_seeing_percent, cannot_do_seeing_percent, \
                total_seeing_male, no_diff_seeing_male, some_diff_seeing_male, lot_diff_seeing_male, cannot_do_seeing_male, \
                total_seeing_male_percent, no_diff_seeing_male_percent, some_diff_seeing_male_percent, lot_diff_seeing_male_percent, cannot_do_seeing_male_percent, \
                total_seeing_female, no_diff_seeing_female, some_diff_seeing_female, lot_diff_seeing_female, cannot_do_seeing_female, \
                total_seeing_female_percent, no_diff_seeing_female_percent, some_diff_seeing_female_percent, lot_diff_seeing_female_percent, cannot_do_seeing_female_percent, \
                total_seeing_urban, no_diff_seeing_urban, some_diff_seeing_urban, lot_diff_seeing_urban, cannot_do_seeing_urban, \
                total_seeing_urban_percent, no_diff_seeing_urban_percent, some_diff_seeing_urban_percent, lot_diff_seeing_urban_percent, cannot_do_seeing_urban_percent, \
                total_seeing_rural, no_diff_seeing_rural, some_diff_seeing_rural, lot_diff_seeing_rural, cannot_do_seeing_rural, \
                total_seeing_rural_percent, no_diff_seeing_rural_percent, some_diff_seeing_rural_percent, lot_diff_seeing_rural_percent, cannot_do_seeing_rural_percent, \
                total_seeing_urban_male, no_diff_seeing_urban_male, some_diff_seeing_urban_male, lot_diff_seeing_urban_male, cannot_do_seeing_urban_male, \
                total_seeing_urban_male_percent, no_diff_seeing_urban_male_percent, some_diff_seeing_urban_male_percent, lot_diff_seeing_urban_male_percent, cannot_do_seeing_urban_male_percent, \
                total_seeing_urban_female, no_diff_seeing_urban_female, some_diff_seeing_urban_female, lot_diff_seeing_urban_female, cannot_do_seeing_urban_female, \
                total_seeing_urban_female_percent, no_diff_seeing_urban_female_percent, some_diff_seeing_urban_female_percent, lot_diff_seeing_urban_female_percent, cannot_do_seeing_urban_female_percent, \
                total_seeing_rural_male, no_diff_seeing_rural_male, some_diff_seeing_rural_male, lot_diff_seeing_rural_male, cannot_do_seeing_rural_male, \
                total_seeing_rural_male_percent, no_diff_seeing_rural_male_percent, some_diff_seeing_rural_male_percent, lot_diff_seeing_rural_male_percent, cannot_do_seeing_rural_male_percent, \
                total_seeing_rural_female, no_diff_seeing_rural_female, some_diff_seeing_rural_female, lot_diff_seeing_rural_female, cannot_do_seeing_rural_female, \
                total_seeing_rural_female_percent, no_diff_seeing_rural_female_percent, some_diff_seeing_rural_female_percent, lot_diff_seeing_rural_female_percent, cannot_do_seeing_rural_female_percent

    return  total_seeing, no_diff_seeing, some_diff_seeing, lot_diff_seeing, cannot_do_seeing, \
            total_seeing_percent, no_diff_seeing_percent, some_diff_seeing_percent, lot_diff_seeing_percent, cannot_do_seeing_percent, \
            total_seeing_male, no_diff_seeing_male, some_diff_seeing_male, lot_diff_seeing_male, cannot_do_seeing_male, \
            total_seeing_male_percent, no_diff_seeing_male_percent, some_diff_seeing_male_percent, lot_diff_seeing_male_percent, cannot_do_seeing_male_percent, \
            total_seeing_female, no_diff_seeing_female, some_diff_seeing_female, lot_diff_seeing_female, cannot_do_seeing_female, \
            total_seeing_female_percent, no_diff_seeing_female_percent, some_diff_seeing_female_percent, lot_diff_seeing_female_percent, cannot_do_seeing_female_percent, \
            total_seeing_urban, no_diff_seeing_urban, some_diff_seeing_urban, lot_diff_seeing_urban, cannot_do_seeing_urban, \
            total_seeing_urban_percent, no_diff_seeing_urban_percent, some_diff_seeing_urban_percent, lot_diff_seeing_urban_percent, cannot_do_seeing_urban_percent, \
            total_seeing_rural, no_diff_seeing_rural, some_diff_seeing_rural, lot_diff_seeing_rural, cannot_do_seeing_rural, \
            total_seeing_rural_percent, no_diff_seeing_rural_percent, some_diff_seeing_rural_percent, lot_diff_seeing_rural_percent, cannot_do_seeing_rural_percent, \
            total_seeing_urban_male, no_diff_seeing_urban_male, some_diff_seeing_urban_male, lot_diff_seeing_urban_male, cannot_do_seeing_urban_male, \
            total_seeing_urban_male_percent, no_diff_seeing_urban_male_percent, some_diff_seeing_urban_male_percent, lot_diff_seeing_urban_male_percent, cannot_do_seeing_urban_male_percent, \
            total_seeing_urban_female, no_diff_seeing_urban_female, some_diff_seeing_urban_female, lot_diff_seeing_urban_female, cannot_do_seeing_urban_female, \
            total_seeing_urban_female_percent, no_diff_seeing_urban_female_percent, some_diff_seeing_urban_female_percent, lot_diff_seeing_urban_female_percent, cannot_do_seeing_urban_female_percent, \
            total_seeing_rural_male, no_diff_seeing_rural_male, some_diff_seeing_rural_male, lot_diff_seeing_rural_male, cannot_do_seeing_rural_male, \
            total_seeing_rural_male_percent, no_diff_seeing_rural_male_percent, some_diff_seeing_rural_male_percent, lot_diff_seeing_rural_male_percent, cannot_do_seeing_rural_male_percent, \
            total_seeing_rural_female, no_diff_seeing_rural_female, some_diff_seeing_rural_female, lot_diff_seeing_rural_female, cannot_do_seeing_rural_female, \
            total_seeing_rural_female_percent, no_diff_seeing_rural_female_percent, some_diff_seeing_rural_female_percent, lot_diff_seeing_rural_female_percent, cannot_do_seeing_rural_female_percent

#all domains
@app.callback(

    #OUTPUT
    # all
    Output('dpa_domain_all_total_val', 'children'),
    Output('dpa_domain_all_no_diff_val', 'children'),
    Output('dpa_domain_all_some_diff_val', 'children'),
    Output('dpa_domain_all_lot_diff_val', 'children'),
    Output('dpa_domain_all_cannot_do_at_all_val', 'children'),

    Output('dpa_domain_all_total_percent', 'children'),
    Output('dpa_domain_all_no_diff_percent', 'children'),
    Output('dpa_domain_all_some_diff_percent', 'children'),
    Output('dpa_domain_all_lot_diff_percent', 'children'),
    Output('dpa_domain_all_cannot_do_at_all_percent', 'children'),

    # all male
    Output('dpa_domain_all_male_total_val', 'children'),
    Output('dpa_domain_all_male_no_diff_val', 'children'),
    Output('dpa_domain_all_male_some_diff_val', 'children'),
    Output('dpa_domain_all_male_lot_diff_val', 'children'),
    Output('dpa_domain_all_male_cannot_do_at_all_val', 'children'),

    Output('dpa_domain_all_male_percent', 'children'),
    Output('dpa_domain_all_male_no_diff_percent', 'children'),
    Output('dpa_domain_all_male_some_diff_percent', 'children'),
    Output('dpa_domain_all_male_lot_diff_percent', 'children'),
    Output('dpa_domain_all_male_cannot_do_at_all_percent', 'children'),

    # all female
    Output('dpa_domain_all_female_total_val', 'children'),
    Output('dpa_domain_all_female_no_diff_val', 'children'),
    Output('dpa_domain_all_female_some_diff_val', 'children'),
    Output('dpa_domain_all_female_lot_diff_val', 'children'),
    Output('dpa_domain_all_female_cannot_do_at_all_val', 'children'),

    Output('dpa_domain_all_female_percent', 'children'),
    Output('dpa_domain_all_female_no_diff_percent', 'children'),
    Output('dpa_domain_all_female_some_diff_percent', 'children'),
    Output('dpa_domain_all_female_lot_diff_percent', 'children'),
    Output('dpa_domain_all_female_cannot_do_at_all_percent', 'children'),

    # urban both
    Output('dpa_domain_urban_both_total_val', 'children'),
    Output('dpa_domain_urban_both_no_diff_val', 'children'),
    Output('dpa_domain_urban_both_some_diff_val', 'children'),
    Output('dpa_domain_urban_both_lot_diff_val', 'children'),
    Output('dpa_domain_urban_both_cannot_do_at_all_val', 'children'),

    Output('dpa_domain_urban_both_percent', 'children'),
    Output('dpa_domain_urban_both_no_diff_percent', 'children'),
    Output('dpa_domain_urban_both_some_diff_percent', 'children'),
    Output('dpa_domain_urban_both_lot_diff_percent', 'children'),
    Output('dpa_domain_urban_both_cannot_do_at_all_percent', 'children'),

    # urban both
    Output('dpa_domain_urban_male_total_val', 'children'),
    Output('dpa_domain_urban_male_no_diff_val', 'children'),
    Output('dpa_domain_urban_male_some_diff_val', 'children'),
    Output('dpa_domain_urban_male_lot_diff_val', 'children'),
    Output('dpa_domain_urban_male_cannot_do_at_all_val', 'children'),

    Output('dpa_domain_urban_male_percent', 'children'),
    Output('dpa_domain_urban_male_no_diff_percent', 'children'),
    Output('dpa_domain_urban_male_some_diff_percent', 'children'),
    Output('dpa_domain_urban_male_lot_diff_percent', 'children'),
    Output('dpa_domain_urban_male_cannot_do_at_all_percent', 'children'),

    # urban female
    Output('dpa_domain_urban_female_total_val', 'children'),
    Output('dpa_domain_urban_female_no_diff_val', 'children'),
    Output('dpa_domain_urban_female_some_diff_val', 'children'),
    Output('dpa_domain_urban_female_lot_diff_val', 'children'),
    Output('dpa_domain_urban_female_cannot_do_at_all_val', 'children'),

    Output('dpa_domain_urban_female_percent', 'children'),
    Output('dpa_domain_urban_female_no_diff_percent', 'children'),
    Output('dpa_domain_urban_female_some_diff_percent', 'children'),
    Output('dpa_domain_urban_female_lot_diff_percent', 'children'),
    Output('dpa_domain_urban_female_cannot_do_at_all_percent', 'children'),

    # rural both
    Output('dpa_domain_rural_both_total_val', 'children'),
    Output('dpa_domain_rural_both_no_diff_val', 'children'),
    Output('dpa_domain_rural_both_some_diff_val', 'children'),
    Output('dpa_domain_rural_both_lot_diff_val', 'children'),
    Output('dpa_domain_rural_both_cannot_do_at_all_val', 'children'),

    Output('dpa_domain_rural_both_percent', 'children'),
    Output('dpa_domain_rural_both_no_diff_percent', 'children'),
    Output('dpa_domain_rural_both_some_diff_percent', 'children'),
    Output('dpa_domain_rural_both_lot_diff_percent', 'children'),
    Output('dpa_domain_rural_both_cannot_do_at_all_percent', 'children'),

    # rural male
    Output('dpa_domain_rural_male_total_val', 'children'),
    Output('dpa_domain_rural_male_no_diff_val', 'children'),
    Output('dpa_domain_rural_male_some_diff_val', 'children'),
    Output('dpa_domain_rural_male_lot_diff_val', 'children'),
    Output('dpa_domain_rural_male_cannot_do_at_all_val', 'children'),

    Output('dpa_domain_rural_male_percent', 'children'),
    Output('dpa_domain_rural_male_no_diff_percent', 'children'),
    Output('dpa_domain_rural_male_some_diff_percent', 'children'),
    Output('dpa_domain_rural_male_lot_diff_percent', 'children'),
    Output('dpa_domain_rural_male_cannot_do_at_all_percent', 'children'),

    # rural female
    Output('dpa_domain_rural_female_total_val', 'children'),
    Output('dpa_domain_rural_female_no_diff_val', 'children'),
    Output('dpa_domain_rural_female_some_diff_val', 'children'),
    Output('dpa_domain_rural_female_lot_diff_val', 'children'),
    Output('dpa_domain_rural_female_cannot_do_at_all_val', 'children'),

    Output('dpa_domain_rural_female_percent', 'children'),
    Output('dpa_domain_rural_female_no_diff_percent', 'children'),
    Output('dpa_domain_rural_female_some_diff_percent', 'children'),
    Output('dpa_domain_rural_female_lot_diff_percent', 'children'),
    Output('dpa_domain_rural_female_cannot_do_at_all_percent', 'children'),

    # INPUT
    Input('dpa_region_dd', 'value'),
    Input('dpa_district_dd', 'value'),
    Input('dpa_category_dd', 'value')
)
def get_diff_perf_act_all_domain(region, district, category):

    # all
    all_total = None
    no_diff = None
    some_diff_in_at_least_one_dom = None
    a_lot_diff_in_at_least_one_dom = None
    cannot_all_in_at_least_one_dom = None

    all_total_percent = None
    no_diff_percent = None
    some_diff_in_at_least_one_dom_percent = None
    a_lot_diff_in_at_least_one_dom_percent = None
    cannot_all_in_at_least_one_dom_percent = None

    # all male
    all_male_total = None
    all_male_no_diff = None
    all_male_some_diff_in_at_least_one_dom = None
    all_male_a_lot_diff_in_at_least_one_dom = None
    all_male_cannot_all_in_at_least_one_dom = None

    all_male_total_percent = None
    all_male_no_diff_percent = None
    all_male_some_diff_in_at_least_one_dom_percent = None
    all_male_a_lot_diff_in_at_least_one_dom_percent = None
    all_male_cannot_all_in_at_least_one_dom_percent = None

    # all female
    all_female_total = None
    all_female_no_diff = None
    all_female_some_diff_in_at_least_one_dom = None
    all_female_a_lot_diff_in_at_least_one_dom = None
    all_female_cannot_all_in_at_least_one_dom = None

    all_female_total_percent = None
    all_female_no_diff_percent = None
    all_female_some_diff_in_at_least_one_dom_percent = None
    all_female_a_lot_diff_in_at_least_one_dom_percent = None
    all_female_cannot_all_in_at_least_one_dom_percent = None

    # urban both
    urban_both_total = None
    urban_both_no_diff = None
    urban_both_some_diff_in_at_least_one_dom = None
    urban_both_a_lot_diff_in_at_least_one_dom = None
    urban_both_cannot_all_in_at_least_one_dom = None

    urban_both_total_percent = None
    urban_both_no_diff_percent = None
    urban_both_some_diff_in_at_least_one_dom_percent = None
    urban_both_a_lot_diff_in_at_least_one_dom_percent = None
    urban_both_cannot_all_in_at_least_one_dom_percent = None

    # urban male
    urban_male_total = None
    urban_male_no_diff = None
    urban_male_some_diff_in_at_least_one_dom = None
    urban_male_a_lot_diff_in_at_least_one_dom = None
    urban_male_cannot_all_in_at_least_one_dom = None

    urban_male_total_percent = None
    urban_male_no_diff_percent = None
    urban_male_some_diff_in_at_least_one_dom_percent = None
    urban_male_a_lot_diff_in_at_least_one_dom_percent = None
    urban_male_cannot_all_in_at_least_one_dom_percent = None

    # urban female
    urban_female_total = None
    urban_female_no_diff = None
    urban_female_some_diff_in_at_least_one_dom = None
    urban_female_a_lot_diff_in_at_least_one_dom = None
    urban_female_cannot_all_in_at_least_one_dom = None

    urban_female_total_percent = None
    urban_female_no_diff_percent = None
    urban_female_some_diff_in_at_least_one_dom_percent = None
    urban_female_a_lot_diff_in_at_least_one_dom_percent = None
    urban_female_cannot_all_in_at_least_one_dom_percent = None

    # rural both
    rural_both_total = None
    rural_both_no_diff = None
    rural_both_some_diff_in_at_least_one_dom = None
    rural_both_a_lot_diff_in_at_least_one_dom = None
    rural_both_cannot_all_in_at_least_one_dom = None

    rural_both_total_percent = None
    rural_both_no_diff_percent = None
    rural_both_some_diff_in_at_least_one_dom_percent = None
    rural_both_a_lot_diff_in_at_least_one_dom_percent = None
    rural_both_cannot_all_in_at_least_one_dom_percent = None

    # rural male
    rural_male_total = None
    rural_male_no_diff = None
    rural_male_some_diff_in_at_least_one_dom = None
    rural_male_a_lot_diff_in_at_least_one_dom = None
    rural_male_cannot_all_in_at_least_one_dom = None

    rural_male_total_percent = None
    rural_male_no_diff_percent = None
    rural_male_some_diff_in_at_least_one_dom_percent = None
    rural_male_a_lot_diff_in_at_least_one_dom_percent = None
    rural_male_cannot_all_in_at_least_one_dom_percent = None

    # rural female
    rural_female_total = None
    rural_female_no_diff = None
    rural_female_some_diff_in_at_least_one_dom = None
    rural_female_a_lot_diff_in_at_least_one_dom = None
    rural_female_cannot_all_in_at_least_one_dom = None

    rural_female_total_percent = None
    rural_female_no_diff_percent = None
    rural_female_some_diff_in_at_least_one_dom_percent = None
    rural_female_a_lot_diff_in_at_least_one_dom_percent = None
    rural_female_cannot_all_in_at_least_one_dom_percent = None

    if (region != None) & (district != None) & (category != None):

        if region == 'Western':
            df_dpa_data_all_dom = df_diff_perf_act_3F5a_western

            # ALL
            #*****
            df_data = df_dpa_data_all_dom[df_dpa_data_all_dom['Type'] == 'All'] \
                [['Status', 'Status_Code', 'Type', district]]

            all_stats_df = df_data[df_data['Type'] == 'All']
            all_stats_df = all_stats_df.reset_index(drop=True)

            #total
            all_total_df = all_stats_df[all_stats_df['Status_Code'] == 0][[district]]
            all_total_df = all_total_df.reset_index(drop=True)
            all_total = all_total_df[district][0]

            #no_diff
            no_diff_df  = all_stats_df[all_stats_df['Status_Code'] == 1][[district]]
            no_diff_df = no_diff_df.reset_index(drop=True)
            no_diff = no_diff_df[district][0]

            #some diff in at least one dom
            some_diff_in_at_least_one_dom_df = all_stats_df[all_stats_df['Status_Code'] == 2][[district]]
            some_diff_in_at_least_one_dom_df = some_diff_in_at_least_one_dom_df.reset_index(drop=True)
            some_diff_in_at_least_one_dom = some_diff_in_at_least_one_dom_df[district][0]

            # a lot of diff in at least one dom
            a_lot_diff_in_at_least_one_dom_df = all_stats_df[all_stats_df['Status_Code'] == 3][[district]]
            a_lot_diff_in_at_least_one_dom_df = a_lot_diff_in_at_least_one_dom_df.reset_index(drop=True)
            a_lot_diff_in_at_least_one_dom = a_lot_diff_in_at_least_one_dom_df[district][0]

            ##cannot do at all in at least one dom
            cannot_all_in_at_least_one_dom_df = all_stats_df[all_stats_df['Status_Code'] == 4][[district]]
            cannot_all_in_at_least_one_dom_df = cannot_all_in_at_least_one_dom_df.reset_index(drop=True)
            cannot_all_in_at_least_one_dom = cannot_all_in_at_least_one_dom_df[district][0]

            #percentages
            no_diff_percent = (no_diff / all_total) * 100
            some_diff_in_at_least_one_dom_percent = (some_diff_in_at_least_one_dom / all_total) * 100
            a_lot_diff_in_at_least_one_dom_percent = (a_lot_diff_in_at_least_one_dom / all_total) * 100
            cannot_all_in_at_least_one_dom_percent = (cannot_all_in_at_least_one_dom / all_total) * 100

            #format
            all_total = '{:,}'.format(all_total)
            no_diff = '{:,}'.format(no_diff)
            some_diff_in_at_least_one_dom = '{:,}'.format(some_diff_in_at_least_one_dom)
            a_lot_diff_in_at_least_one_dom = '{:,}'.format(a_lot_diff_in_at_least_one_dom)
            cannot_all_in_at_least_one_dom = '{:,}'.format(cannot_all_in_at_least_one_dom)

            all_total_percent = 100
            no_diff_percent = '{:.1f}'.format(no_diff_percent)
            some_diff_in_at_least_one_dom_percent = '{:.1f}'.format(some_diff_in_at_least_one_dom_percent)
            a_lot_diff_in_at_least_one_dom_percent = '{:.1f}'.format(a_lot_diff_in_at_least_one_dom_percent)
            cannot_all_in_at_least_one_dom_percent = '{:.1f}'.format(cannot_all_in_at_least_one_dom_percent)

            # ALL MALE
            #*********
            all_male_stats_df = df_dpa_data_all_dom[df_dpa_data_all_dom['Type'] == 'All Male'] \
                [['Status', 'Status_Code', 'Type', district]]

            # total
            all_male_total_df = all_male_stats_df[all_male_stats_df['Status_Code'] == 0][[district]]
            all_male_total_df = all_male_total_df.reset_index(drop=True)
            all_male_total = all_male_total_df[district][0]

            # no_diff
            all_male_no_diff_df = all_male_stats_df[all_male_stats_df['Status_Code'] == 1][[district]]
            all_male_no_diff_df = all_male_no_diff_df.reset_index(drop=True)
            all_male_no_diff = all_male_no_diff_df[district][0]

            # some diff in at least one dom
            all_male_some_diff_in_at_least_one_dom_df = all_male_stats_df[all_male_stats_df['Status_Code'] == 2][[district]]
            all_male_some_diff_in_at_least_one_dom_df = all_male_some_diff_in_at_least_one_dom_df.reset_index(drop=True)
            all_male_some_diff_in_at_least_one_dom = all_male_some_diff_in_at_least_one_dom_df[district][0]

            # a lot of diff in at least one dom
            all_male_a_lot_diff_in_at_least_one_dom_df = all_male_stats_df[all_male_stats_df['Status_Code'] == 3][[district]]
            all_male_a_lot_diff_in_at_least_one_dom_df = all_male_a_lot_diff_in_at_least_one_dom_df.reset_index(drop=True)
            all_male_a_lot_diff_in_at_least_one_dom = all_male_a_lot_diff_in_at_least_one_dom_df[district][0]

            ##cannot do at all in at least one dom
            all_male_cannot_all_in_at_least_one_dom_df = all_male_stats_df[all_male_stats_df['Status_Code'] == 4][[district]]
            all_male_cannot_all_in_at_least_one_dom_df = all_male_cannot_all_in_at_least_one_dom_df.reset_index(drop=True)
            all_male_cannot_all_in_at_least_one_dom = all_male_cannot_all_in_at_least_one_dom_df[district][0]

            # percentages
            all_male_no_diff_percent = (all_male_no_diff / all_male_total) * 100
            all_male_some_diff_in_at_least_one_dom_percent = (all_male_some_diff_in_at_least_one_dom / all_male_total) * 100
            all_male_a_lot_diff_in_at_least_one_dom_percent = (all_male_a_lot_diff_in_at_least_one_dom / all_male_total) * 100
            all_male_cannot_all_in_at_least_one_dom_percent = (all_male_cannot_all_in_at_least_one_dom / all_male_total) * 100

            # format
            all_male_total = '{:,}'.format(all_male_total)
            all_male_no_diff = '{:,}'.format(all_male_no_diff)
            all_male_some_diff_in_at_least_one_dom = '{:,}'.format(all_male_some_diff_in_at_least_one_dom)
            all_male_a_lot_diff_in_at_least_one_dom = '{:,}'.format(all_male_a_lot_diff_in_at_least_one_dom)
            all_male_cannot_all_in_at_least_one_dom = '{:,}'.format(all_male_cannot_all_in_at_least_one_dom)

            all_male_total_percent = 100
            all_male_no_diff_percent = '{:.1f}'.format(all_male_no_diff_percent)
            all_male_some_diff_in_at_least_one_dom_percent = '{:.1f}'.format(all_male_some_diff_in_at_least_one_dom_percent)
            all_male_a_lot_diff_in_at_least_one_dom_percent = '{:.1f}'.format(all_male_a_lot_diff_in_at_least_one_dom_percent)
            all_male_cannot_all_in_at_least_one_dom_percent = '{:.1f}'.format(all_male_cannot_all_in_at_least_one_dom_percent)

            # ALL FEMALE
            #***********
            all_female_stats_df = df_dpa_data_all_dom[df_dpa_data_all_dom['Type'] == 'All Female'][['Status', 'Status_Code', 'Type', district]]

            # total
            all_female_total_df = all_female_stats_df[all_female_stats_df['Status_Code'] == 0][[district]]
            all_female_total_df = all_female_total_df.reset_index(drop=True)
            all_female_total = all_female_total_df[district][0]

            # no_diff
            all_female_no_diff_df = all_female_stats_df[all_female_stats_df['Status_Code'] == 1][[district]]
            all_female_no_diff_df = all_female_no_diff_df.reset_index(drop=True)
            all_female_no_diff = all_female_no_diff_df[district][0]

            # some diff in at least one dom
            all_female_some_diff_in_at_least_one_dom_df = all_female_stats_df[all_female_stats_df['Status_Code'] == 2][
                [district]]
            all_female_some_diff_in_at_least_one_dom_df = all_female_some_diff_in_at_least_one_dom_df.reset_index(drop=True)
            all_female_some_diff_in_at_least_one_dom = all_female_some_diff_in_at_least_one_dom_df[district][0]

            # a lot of diff in at least one dom
            all_female_a_lot_diff_in_at_least_one_dom_df = all_female_stats_df[all_female_stats_df['Status_Code'] == 3][[district]]
            all_female_a_lot_diff_in_at_least_one_dom_df = all_female_a_lot_diff_in_at_least_one_dom_df.reset_index(drop=True)
            all_female_a_lot_diff_in_at_least_one_dom = all_female_a_lot_diff_in_at_least_one_dom_df[district][0]

            ##cannot do at all in at least one dom
            all_female_cannot_all_in_at_least_one_dom_df = all_female_stats_df[all_female_stats_df['Status_Code'] == 4][[district]]
            all_female_cannot_all_in_at_least_one_dom_df = all_female_cannot_all_in_at_least_one_dom_df.reset_index(drop=True)
            all_female_cannot_all_in_at_least_one_dom = all_female_cannot_all_in_at_least_one_dom_df[district][0]

            # percentages
            all_female_no_diff_percent = (all_female_no_diff / all_female_total) * 100
            all_female_some_diff_in_at_least_one_dom_percent = (all_female_some_diff_in_at_least_one_dom / all_female_total) * 100
            all_female_a_lot_diff_in_at_least_one_dom_percent = (all_female_a_lot_diff_in_at_least_one_dom / all_female_total) * 100
            all_female_cannot_all_in_at_least_one_dom_percent = (all_female_cannot_all_in_at_least_one_dom / all_female_total) * 100

            # format
            all_female_total = '{:,}'.format(all_female_total)
            all_female_no_diff = '{:,}'.format(all_female_no_diff)
            all_female_some_diff_in_at_least_one_dom = '{:,}'.format(all_female_some_diff_in_at_least_one_dom)
            all_female_a_lot_diff_in_at_least_one_dom = '{:,}'.format(all_female_a_lot_diff_in_at_least_one_dom)
            all_female_cannot_all_in_at_least_one_dom = '{:,}'.format(all_female_cannot_all_in_at_least_one_dom)

            all_female_total_percent = 100
            all_female_no_diff_percent = '{:.1f}'.format(all_female_no_diff_percent)
            all_female_some_diff_in_at_least_one_dom_percent = '{:.1f}'.format(all_female_some_diff_in_at_least_one_dom_percent)
            all_female_a_lot_diff_in_at_least_one_dom_percent = '{:.1f}'.format(all_female_a_lot_diff_in_at_least_one_dom_percent)
            all_female_cannot_all_in_at_least_one_dom_percent = '{:.1f}'.format(all_female_cannot_all_in_at_least_one_dom_percent)


            # URBAN BOTH
            #***********
            urban_both_stats_df = df_dpa_data_all_dom[df_dpa_data_all_dom['Type'] == 'Urban All'][['Status', 'Status_Code', 'Type', district]]

            # total
            urban_both_total_df = urban_both_stats_df[urban_both_stats_df['Status_Code'] == 0][[district]]
            urban_both_total_df = urban_both_total_df.reset_index(drop=True)
            urban_both_total = urban_both_total_df[district][0]

            # no_diff
            urban_both_no_diff_df = urban_both_stats_df[urban_both_stats_df['Status_Code'] == 1][[district]]
            urban_both_no_diff_df = urban_both_no_diff_df.reset_index(drop=True)
            urban_both_no_diff = urban_both_no_diff_df[district][0]

            # some diff in at least one dom
            urban_both_some_diff_in_at_least_one_dom_df = urban_both_stats_df[urban_both_stats_df['Status_Code'] == 2][[district]]
            urban_both_some_diff_in_at_least_one_dom_df = urban_both_some_diff_in_at_least_one_dom_df.reset_index(drop=True)
            urban_both_some_diff_in_at_least_one_dom = urban_both_some_diff_in_at_least_one_dom_df[district][0]

            # a lot of diff in at least one dom
            urban_both_a_lot_diff_in_at_least_one_dom_df = urban_both_stats_df[urban_both_stats_df['Status_Code'] == 3][[district]]
            urban_both_a_lot_diff_in_at_least_one_dom_df = urban_both_a_lot_diff_in_at_least_one_dom_df.reset_index(drop=True)
            urban_both_a_lot_diff_in_at_least_one_dom = urban_both_a_lot_diff_in_at_least_one_dom_df[district][0]

            ##cannot do at all in at least one dom
            urban_both_cannot_all_in_at_least_one_dom_df = urban_both_stats_df[urban_both_stats_df['Status_Code'] == 4][[district]]
            urban_both_cannot_all_in_at_least_one_dom_df = urban_both_cannot_all_in_at_least_one_dom_df.reset_index(drop=True)
            urban_both_cannot_all_in_at_least_one_dom = urban_both_cannot_all_in_at_least_one_dom_df[district][0]

            # percentages
            urban_both_no_diff_percent = (urban_both_no_diff / urban_both_total) * 100
            urban_both_some_diff_in_at_least_one_dom_percent = (urban_both_some_diff_in_at_least_one_dom / urban_both_total) * 100
            urban_both_a_lot_diff_in_at_least_one_dom_percent = (urban_both_a_lot_diff_in_at_least_one_dom / urban_both_total) * 100
            urban_both_cannot_all_in_at_least_one_dom_percent = (urban_both_cannot_all_in_at_least_one_dom / urban_both_total) * 100

            # format
            urban_both_total = '{:,}'.format(urban_both_total)
            urban_both_no_diff = '{:,}'.format(urban_both_no_diff)
            urban_both_some_diff_in_at_least_one_dom = '{:,}'.format(urban_both_some_diff_in_at_least_one_dom)
            urban_both_a_lot_diff_in_at_least_one_dom = '{:,}'.format(urban_both_a_lot_diff_in_at_least_one_dom)
            urban_both_cannot_all_in_at_least_one_dom = '{:,}'.format(urban_both_cannot_all_in_at_least_one_dom)

            urban_both_total_percent = 100
            urban_both_no_diff_percent = '{:.1f}'.format(urban_both_no_diff_percent)
            urban_both_some_diff_in_at_least_one_dom_percent = '{:.1f}'.format(urban_both_some_diff_in_at_least_one_dom_percent)
            urban_both_a_lot_diff_in_at_least_one_dom_percent = '{:.1f}'.format(urban_both_a_lot_diff_in_at_least_one_dom_percent)
            urban_both_cannot_all_in_at_least_one_dom_percent = '{:.1f}'.format(urban_both_cannot_all_in_at_least_one_dom_percent)

            # URBAN MALE
            #************
            urban_male_stats_df = df_dpa_data_all_dom[df_dpa_data_all_dom['Type'] == 'Urban Male'][['Status', 'Status_Code', 'Type', district]]

            # total
            urban_male_total_df = urban_male_stats_df[urban_male_stats_df['Status_Code'] == 0][[district]]
            urban_male_total_df = urban_male_total_df.reset_index(drop=True)
            urban_male_total = urban_male_total_df[district][0]

            # no_diff
            urban_male_no_diff_df = urban_male_stats_df[urban_male_stats_df['Status_Code'] == 1][[district]]
            urban_male_no_diff_df = urban_male_no_diff_df.reset_index(drop=True)
            urban_male_no_diff = urban_male_no_diff_df[district][0]

            # some diff in at least one dom
            urban_male_some_diff_in_at_least_one_dom_df = urban_male_stats_df[urban_male_stats_df['Status_Code'] == 2][[district]]
            urban_male_some_diff_in_at_least_one_dom_df = urban_male_some_diff_in_at_least_one_dom_df.reset_index(drop=True)
            urban_male_some_diff_in_at_least_one_dom = urban_male_some_diff_in_at_least_one_dom_df[district][0]

            # a lot of diff in at least one dom
            urban_male_a_lot_diff_in_at_least_one_dom_df = urban_male_stats_df[urban_male_stats_df['Status_Code'] == 3][[district]]
            urban_male_a_lot_diff_in_at_least_one_dom_df = urban_male_a_lot_diff_in_at_least_one_dom_df.reset_index(drop=True)
            urban_male_a_lot_diff_in_at_least_one_dom = urban_male_a_lot_diff_in_at_least_one_dom_df[district][0]

            ##cannot do at all in at least one dom
            urban_male_cannot_all_in_at_least_one_dom_df = urban_male_stats_df[urban_male_stats_df['Status_Code'] == 4][[district]]
            urban_male_cannot_all_in_at_least_one_dom_df = urban_male_cannot_all_in_at_least_one_dom_df.reset_index(drop=True)
            urban_male_cannot_all_in_at_least_one_dom = urban_male_cannot_all_in_at_least_one_dom_df[district][0]

            # percentages
            urban_male_no_diff_percent = (urban_male_no_diff / urban_male_total) * 100
            urban_male_some_diff_in_at_least_one_dom_percent = (urban_male_some_diff_in_at_least_one_dom / urban_male_total) * 100
            urban_male_a_lot_diff_in_at_least_one_dom_percent = (urban_male_a_lot_diff_in_at_least_one_dom / urban_male_total) * 100
            urban_male_cannot_all_in_at_least_one_dom_percent = (urban_male_cannot_all_in_at_least_one_dom / urban_male_total) * 100

            # format
            urban_male_total = '{:,}'.format(urban_male_total)
            urban_male_no_diff = '{:,}'.format(urban_male_no_diff)
            urban_male_some_diff_in_at_least_one_dom = '{:,}'.format(urban_male_some_diff_in_at_least_one_dom)
            urban_male_a_lot_diff_in_at_least_one_dom = '{:,}'.format(urban_male_a_lot_diff_in_at_least_one_dom)
            urban_male_cannot_all_in_at_least_one_dom = '{:,}'.format(urban_male_cannot_all_in_at_least_one_dom)

            urban_male_total_percent = 100
            urban_male_no_diff_percent = '{:.1f}'.format(urban_male_no_diff_percent)
            urban_male_some_diff_in_at_least_one_dom_percent = '{:.1f}'.format(urban_male_some_diff_in_at_least_one_dom_percent)
            urban_male_a_lot_diff_in_at_least_one_dom_percent = '{:.1f}'.format(urban_male_a_lot_diff_in_at_least_one_dom_percent)
            urban_male_cannot_all_in_at_least_one_dom_percent = '{:.1f}'.format(urban_male_cannot_all_in_at_least_one_dom_percent)

            # URBAN FEMALE
            # ************
            urban_female_stats_df = df_dpa_data_all_dom[df_dpa_data_all_dom['Type'] == 'Urban Female'][['Status', 'Status_Code', 'Type', district]]

            # total
            urban_female_total_df = urban_female_stats_df[urban_female_stats_df['Status_Code'] == 0][[district]]
            urban_female_total_df = urban_female_total_df.reset_index(drop=True)
            urban_female_total = urban_female_total_df[district][0]

            # no_diff
            urban_female_no_diff_df = urban_female_stats_df[urban_female_stats_df['Status_Code'] == 1][[district]]
            urban_female_no_diff_df = urban_female_no_diff_df.reset_index(drop=True)
            urban_female_no_diff = urban_female_no_diff_df[district][0]

            # some diff in at least one dom
            urban_female_some_diff_in_at_least_one_dom_df = urban_female_stats_df[urban_female_stats_df['Status_Code'] == 2][[district]]
            urban_female_some_diff_in_at_least_one_dom_df = urban_female_some_diff_in_at_least_one_dom_df.reset_index(drop=True)
            urban_female_some_diff_in_at_least_one_dom = urban_female_some_diff_in_at_least_one_dom_df[district][0]

            # a lot of diff in at least one dom
            urban_female_a_lot_diff_in_at_least_one_dom_df = urban_female_stats_df[urban_female_stats_df['Status_Code'] == 3][[district]]
            urban_female_a_lot_diff_in_at_least_one_dom_df = urban_female_a_lot_diff_in_at_least_one_dom_df.reset_index(drop=True)
            urban_female_a_lot_diff_in_at_least_one_dom = urban_female_a_lot_diff_in_at_least_one_dom_df[district][0]

            ##cannot do at all in at least one dom
            urban_female_cannot_all_in_at_least_one_dom_df = urban_female_stats_df[urban_female_stats_df['Status_Code'] == 4][[district]]
            urban_female_cannot_all_in_at_least_one_dom_df = urban_female_cannot_all_in_at_least_one_dom_df.reset_index(drop=True)
            urban_female_cannot_all_in_at_least_one_dom = urban_female_cannot_all_in_at_least_one_dom_df[district][0]

            # percentages
            urban_female_no_diff_percent = (urban_female_no_diff / urban_female_total) * 100
            urban_female_some_diff_in_at_least_one_dom_percent = (urban_female_some_diff_in_at_least_one_dom / urban_female_total) * 100
            urban_female_a_lot_diff_in_at_least_one_dom_percent = (urban_female_a_lot_diff_in_at_least_one_dom / urban_female_total) * 100
            urban_female_cannot_all_in_at_least_one_dom_percent = (urban_female_cannot_all_in_at_least_one_dom / urban_female_total) * 100

            # format
            urban_female_total = '{:,}'.format(urban_female_total)
            urban_female_no_diff = '{:,}'.format(urban_female_no_diff)
            urban_female_some_diff_in_at_least_one_dom = '{:,}'.format(urban_female_some_diff_in_at_least_one_dom)
            urban_female_a_lot_diff_in_at_least_one_dom = '{:,}'.format(urban_female_a_lot_diff_in_at_least_one_dom)
            urban_female_cannot_all_in_at_least_one_dom = '{:,}'.format(urban_female_cannot_all_in_at_least_one_dom)

            urban_female_total_percent = 100
            urban_female_no_diff_percent = '{:.1f}'.format(urban_female_no_diff_percent)
            urban_female_some_diff_in_at_least_one_dom_percent = '{:.1f}'.format(urban_female_some_diff_in_at_least_one_dom_percent)
            urban_female_a_lot_diff_in_at_least_one_dom_percent = '{:.1f}'.format(urban_female_a_lot_diff_in_at_least_one_dom_percent)
            urban_female_cannot_all_in_at_least_one_dom_percent = '{:.1f}'.format(urban_female_cannot_all_in_at_least_one_dom_percent)

            # RURAL BOTH
            # ************
            rural_both_stats_df = df_dpa_data_all_dom[df_dpa_data_all_dom['Type'] == 'Rural All'][['Status', 'Status_Code', 'Type', district]]

            # total
            rural_both_total_df = rural_both_stats_df[rural_both_stats_df['Status_Code'] == 0][[district]]
            rural_both_total_df = rural_both_total_df.reset_index(drop=True)
            rural_both_total = rural_both_total_df[district][0]

            # no_diff
            rural_both_no_diff_df = rural_both_stats_df[rural_both_stats_df['Status_Code'] == 1][[district]]
            rural_both_no_diff_df = rural_both_no_diff_df.reset_index(drop=True)
            rural_both_no_diff = rural_both_no_diff_df[district][0]

            # some diff in at least one dom
            rural_both_some_diff_in_at_least_one_dom_df = \
            rural_both_stats_df[rural_both_stats_df['Status_Code'] == 2][[district]]
            rural_both_some_diff_in_at_least_one_dom_df = rural_both_some_diff_in_at_least_one_dom_df.reset_index(
                drop=True)
            rural_both_some_diff_in_at_least_one_dom = rural_both_some_diff_in_at_least_one_dom_df[district][0]

            # a lot of diff in at least one dom
            rural_both_a_lot_diff_in_at_least_one_dom_df = \
            rural_both_stats_df[rural_both_stats_df['Status_Code'] == 3][[district]]
            rural_both_a_lot_diff_in_at_least_one_dom_df = rural_both_a_lot_diff_in_at_least_one_dom_df.reset_index(
                drop=True)
            rural_both_a_lot_diff_in_at_least_one_dom = rural_both_a_lot_diff_in_at_least_one_dom_df[district][0]

            ##cannot do at all in at least one dom
            rural_both_cannot_all_in_at_least_one_dom_df = \
            rural_both_stats_df[rural_both_stats_df['Status_Code'] == 4][[district]]
            rural_both_cannot_all_in_at_least_one_dom_df = rural_both_cannot_all_in_at_least_one_dom_df.reset_index(
                drop=True)
            rural_both_cannot_all_in_at_least_one_dom = rural_both_cannot_all_in_at_least_one_dom_df[district][0]

            # percentages
            rural_both_no_diff_percent = (rural_both_no_diff / rural_both_total) * 100
            rural_both_some_diff_in_at_least_one_dom_percent = (rural_both_some_diff_in_at_least_one_dom / rural_both_total) * 100
            rural_both_a_lot_diff_in_at_least_one_dom_percent = (rural_both_a_lot_diff_in_at_least_one_dom / rural_both_total) * 100
            rural_both_cannot_all_in_at_least_one_dom_percent = (rural_both_cannot_all_in_at_least_one_dom / rural_both_total) * 100

            # format
            rural_both_total = '{:,}'.format(rural_both_total)
            rural_both_no_diff = '{:,}'.format(rural_both_no_diff)
            rural_both_some_diff_in_at_least_one_dom = '{:,}'.format(rural_both_some_diff_in_at_least_one_dom)
            rural_both_a_lot_diff_in_at_least_one_dom = '{:,}'.format(rural_both_a_lot_diff_in_at_least_one_dom)
            rural_both_cannot_all_in_at_least_one_dom = '{:,}'.format(rural_both_cannot_all_in_at_least_one_dom)

            rural_both_total_percent = 100
            rural_both_no_diff_percent = '{:.1f}'.format(rural_both_no_diff_percent)
            rural_both_some_diff_in_at_least_one_dom_percent = '{:.1f}'.format(rural_both_some_diff_in_at_least_one_dom_percent)
            rural_both_a_lot_diff_in_at_least_one_dom_percent = '{:.1f}'.format(rural_both_a_lot_diff_in_at_least_one_dom_percent)
            rural_both_cannot_all_in_at_least_one_dom_percent = '{:.1f}'.format(rural_both_cannot_all_in_at_least_one_dom_percent)

            # RURAL MALE
            # ************
            rural_male_stats_df = df_dpa_data_all_dom[df_dpa_data_all_dom['Type'] == 'Rural Male'][['Status', 'Status_Code', 'Type', district]]

            # total
            rural_male_total_df = rural_male_stats_df[rural_male_stats_df['Status_Code'] == 0][[district]]
            rural_male_total_df = rural_male_total_df.reset_index(drop=True)
            rural_male_total = rural_male_total_df[district][0]

            # no_diff
            rural_male_no_diff_df = rural_male_stats_df[rural_male_stats_df['Status_Code'] == 1][[district]]
            rural_male_no_diff_df = rural_male_no_diff_df.reset_index(drop=True)
            rural_male_no_diff = rural_male_no_diff_df[district][0]

            # some diff in at least one dom
            rural_male_some_diff_in_at_least_one_dom_df = rural_male_stats_df[rural_male_stats_df['Status_Code'] == 2][[district]]
            rural_male_some_diff_in_at_least_one_dom_df = rural_male_some_diff_in_at_least_one_dom_df.reset_index(drop=True)
            rural_male_some_diff_in_at_least_one_dom = rural_male_some_diff_in_at_least_one_dom_df[district][0]

            # a lot of diff in at least one dom
            rural_male_a_lot_diff_in_at_least_one_dom_df = rural_male_stats_df[rural_male_stats_df['Status_Code'] == 3][[district]]
            rural_male_a_lot_diff_in_at_least_one_dom_df = rural_male_a_lot_diff_in_at_least_one_dom_df.reset_index(drop=True)
            rural_male_a_lot_diff_in_at_least_one_dom = rural_male_a_lot_diff_in_at_least_one_dom_df[district][0]

            ##cannot do at all in at least one dom
            rural_male_cannot_all_in_at_least_one_dom_df = rural_male_stats_df[rural_male_stats_df['Status_Code'] == 4][[district]]
            rural_male_cannot_all_in_at_least_one_dom_df = rural_male_cannot_all_in_at_least_one_dom_df.reset_index(drop=True)
            rural_male_cannot_all_in_at_least_one_dom = rural_male_cannot_all_in_at_least_one_dom_df[district][0]

            # percentages
            rural_male_no_diff_percent = (rural_male_no_diff / rural_male_total) * 100
            rural_male_some_diff_in_at_least_one_dom_percent = (rural_male_some_diff_in_at_least_one_dom / rural_male_total) * 100
            rural_male_a_lot_diff_in_at_least_one_dom_percent = (rural_male_a_lot_diff_in_at_least_one_dom / rural_male_total) * 100
            rural_male_cannot_all_in_at_least_one_dom_percent = (rural_male_cannot_all_in_at_least_one_dom / rural_male_total) * 100

            # format
            rural_male_total = '{:,}'.format(rural_male_total)
            rural_male_no_diff = '{:,}'.format(rural_male_no_diff)
            rural_male_some_diff_in_at_least_one_dom = '{:,}'.format(rural_male_some_diff_in_at_least_one_dom)
            rural_male_a_lot_diff_in_at_least_one_dom = '{:,}'.format(rural_male_a_lot_diff_in_at_least_one_dom)
            rural_male_cannot_all_in_at_least_one_dom = '{:,}'.format(rural_male_cannot_all_in_at_least_one_dom)

            rural_male_total_percent = 100
            rural_male_no_diff_percent = '{:.1f}'.format(rural_male_no_diff_percent)
            rural_male_some_diff_in_at_least_one_dom_percent = '{:.1f}'.format(rural_male_some_diff_in_at_least_one_dom_percent)
            rural_male_a_lot_diff_in_at_least_one_dom_percent = '{:.1f}'.format(rural_male_a_lot_diff_in_at_least_one_dom_percent)
            rural_male_cannot_all_in_at_least_one_dom_percent = '{:.1f}'.format(rural_male_cannot_all_in_at_least_one_dom_percent)

            # RURAL FEMALE
            # ************
            rural_female_stats_df = df_dpa_data_all_dom[df_dpa_data_all_dom['Type'] == 'Rural Female'][['Status', 'Status_Code', 'Type', district]]

            # total
            rural_female_total_df = rural_female_stats_df[rural_female_stats_df['Status_Code'] == 0][[district]]
            rural_female_total_df = rural_female_total_df.reset_index(drop=True)
            rural_female_total = rural_female_total_df[district][0]

            # no_diff
            rural_female_no_diff_df = rural_female_stats_df[rural_female_stats_df['Status_Code'] == 1][[district]]
            rural_female_no_diff_df = rural_female_no_diff_df.reset_index(drop=True)
            rural_female_no_diff = rural_female_no_diff_df[district][0]

            # some diff in at least one dom
            rural_female_some_diff_in_at_least_one_dom_df = rural_female_stats_df[rural_female_stats_df['Status_Code'] == 2][[district]]
            rural_female_some_diff_in_at_least_one_dom_df = rural_female_some_diff_in_at_least_one_dom_df.reset_index(drop=True)
            rural_female_some_diff_in_at_least_one_dom = rural_female_some_diff_in_at_least_one_dom_df[district][0]

            # a lot of diff in at least one dom
            rural_female_a_lot_diff_in_at_least_one_dom_df = rural_female_stats_df[rural_female_stats_df['Status_Code'] == 3][[district]]
            rural_female_a_lot_diff_in_at_least_one_dom_df = rural_female_a_lot_diff_in_at_least_one_dom_df.reset_index(drop=True)
            rural_female_a_lot_diff_in_at_least_one_dom = rural_female_a_lot_diff_in_at_least_one_dom_df[district][0]

            ##cannot do at all in at least one dom
            rural_female_cannot_all_in_at_least_one_dom_df = rural_female_stats_df[rural_female_stats_df['Status_Code'] == 4][[district]]
            rural_female_cannot_all_in_at_least_one_dom_df = rural_female_cannot_all_in_at_least_one_dom_df.reset_index(drop=True)
            rural_female_cannot_all_in_at_least_one_dom = rural_female_cannot_all_in_at_least_one_dom_df[district][0]

            # percentages
            rural_female_no_diff_percent = (rural_female_no_diff / rural_female_total) * 100
            rural_female_some_diff_in_at_least_one_dom_percent = (rural_female_some_diff_in_at_least_one_dom / rural_female_total) * 100
            rural_female_a_lot_diff_in_at_least_one_dom_percent = (rural_female_a_lot_diff_in_at_least_one_dom / rural_female_total) * 100
            rural_female_cannot_all_in_at_least_one_dom_percent = (rural_female_cannot_all_in_at_least_one_dom / rural_female_total) * 100

            # format
            rural_female_total = '{:,}'.format(rural_female_total)
            rural_female_no_diff = '{:,}'.format(rural_female_no_diff)
            rural_female_some_diff_in_at_least_one_dom = '{:,}'.format(rural_female_some_diff_in_at_least_one_dom)
            rural_female_a_lot_diff_in_at_least_one_dom = '{:,}'.format(rural_female_a_lot_diff_in_at_least_one_dom)
            rural_female_cannot_all_in_at_least_one_dom = '{:,}'.format(rural_female_cannot_all_in_at_least_one_dom)

            rural_female_total_percent = 100
            rural_female_no_diff_percent = '{:.1f}'.format(rural_female_no_diff_percent)
            rural_female_some_diff_in_at_least_one_dom_percent = '{:.1f}'.format(rural_female_some_diff_in_at_least_one_dom_percent)
            rural_female_a_lot_diff_in_at_least_one_dom_percent = '{:.1f}'.format(rural_female_a_lot_diff_in_at_least_one_dom_percent)
            rural_female_cannot_all_in_at_least_one_dom_percent = '{:.1f}'.format(rural_female_cannot_all_in_at_least_one_dom_percent)

        #RETURN VALUES
        return all_total, no_diff, some_diff_in_at_least_one_dom, a_lot_diff_in_at_least_one_dom, cannot_all_in_at_least_one_dom, \
               all_total_percent, no_diff_percent, some_diff_in_at_least_one_dom_percent, a_lot_diff_in_at_least_one_dom_percent, cannot_all_in_at_least_one_dom_percent, \
               all_male_total, all_male_no_diff, all_male_some_diff_in_at_least_one_dom, all_male_a_lot_diff_in_at_least_one_dom, all_male_cannot_all_in_at_least_one_dom, \
               all_male_total_percent, all_male_no_diff_percent, all_male_some_diff_in_at_least_one_dom_percent, all_male_a_lot_diff_in_at_least_one_dom_percent, all_male_cannot_all_in_at_least_one_dom_percent, \
               all_female_total, all_female_no_diff, all_female_some_diff_in_at_least_one_dom, all_female_a_lot_diff_in_at_least_one_dom, all_female_cannot_all_in_at_least_one_dom, \
               all_female_total_percent, all_female_no_diff_percent, all_female_some_diff_in_at_least_one_dom_percent, all_female_a_lot_diff_in_at_least_one_dom_percent, all_female_cannot_all_in_at_least_one_dom_percent, \
               urban_both_total, urban_both_no_diff, urban_both_some_diff_in_at_least_one_dom, urban_both_a_lot_diff_in_at_least_one_dom, urban_both_cannot_all_in_at_least_one_dom, \
               urban_both_total_percent, urban_both_no_diff_percent, urban_both_some_diff_in_at_least_one_dom_percent, urban_both_a_lot_diff_in_at_least_one_dom_percent, urban_both_cannot_all_in_at_least_one_dom_percent, \
               urban_male_total, urban_male_no_diff, urban_male_some_diff_in_at_least_one_dom, urban_male_a_lot_diff_in_at_least_one_dom, urban_male_cannot_all_in_at_least_one_dom, \
               urban_male_total_percent, urban_male_no_diff_percent, urban_male_some_diff_in_at_least_one_dom_percent, urban_male_a_lot_diff_in_at_least_one_dom_percent, urban_male_cannot_all_in_at_least_one_dom_percent, \
               urban_female_total, urban_female_no_diff, urban_female_some_diff_in_at_least_one_dom, urban_female_a_lot_diff_in_at_least_one_dom, urban_female_cannot_all_in_at_least_one_dom, \
               urban_female_total_percent, urban_female_no_diff_percent, urban_female_some_diff_in_at_least_one_dom_percent, urban_female_a_lot_diff_in_at_least_one_dom_percent, urban_female_cannot_all_in_at_least_one_dom_percent, \
               rural_both_total, rural_both_no_diff, rural_both_some_diff_in_at_least_one_dom, rural_both_a_lot_diff_in_at_least_one_dom, rural_both_cannot_all_in_at_least_one_dom, \
               rural_both_total_percent, rural_both_no_diff_percent, rural_both_some_diff_in_at_least_one_dom_percent, rural_both_a_lot_diff_in_at_least_one_dom_percent, rural_both_cannot_all_in_at_least_one_dom_percent, \
               rural_male_total, rural_male_no_diff, rural_male_some_diff_in_at_least_one_dom, rural_male_a_lot_diff_in_at_least_one_dom, rural_male_cannot_all_in_at_least_one_dom, \
               rural_male_total_percent, rural_male_no_diff_percent, rural_male_some_diff_in_at_least_one_dom_percent, rural_male_a_lot_diff_in_at_least_one_dom_percent, rural_male_cannot_all_in_at_least_one_dom_percent, \
               rural_female_total, rural_female_no_diff, rural_female_some_diff_in_at_least_one_dom, rural_female_a_lot_diff_in_at_least_one_dom, rural_female_cannot_all_in_at_least_one_dom, \
               rural_female_total_percent, rural_female_no_diff_percent, rural_female_some_diff_in_at_least_one_dom_percent, rural_female_a_lot_diff_in_at_least_one_dom_percent, rural_female_cannot_all_in_at_least_one_dom_percent

    return all_total, no_diff, some_diff_in_at_least_one_dom, a_lot_diff_in_at_least_one_dom, cannot_all_in_at_least_one_dom, \
           all_total_percent, no_diff_percent, some_diff_in_at_least_one_dom, a_lot_diff_in_at_least_one_dom, cannot_all_in_at_least_one_dom, \
           all_male_total, all_male_no_diff, all_male_some_diff_in_at_least_one_dom, all_male_a_lot_diff_in_at_least_one_dom, all_male_cannot_all_in_at_least_one_dom, \
           all_male_total_percent, all_male_no_diff_percent, all_male_some_diff_in_at_least_one_dom_percent, all_male_a_lot_diff_in_at_least_one_dom_percent, all_male_cannot_all_in_at_least_one_dom_percent, \
           all_female_total, all_female_no_diff, all_female_some_diff_in_at_least_one_dom, all_female_a_lot_diff_in_at_least_one_dom, all_female_cannot_all_in_at_least_one_dom, \
           all_female_total_percent, all_female_no_diff_percent, all_female_some_diff_in_at_least_one_dom_percent, all_female_a_lot_diff_in_at_least_one_dom_percent, all_female_cannot_all_in_at_least_one_dom_percent, \
           urban_both_total, urban_both_no_diff, urban_both_some_diff_in_at_least_one_dom, urban_both_a_lot_diff_in_at_least_one_dom, urban_both_cannot_all_in_at_least_one_dom, \
           urban_both_total_percent, urban_both_no_diff_percent, urban_both_some_diff_in_at_least_one_dom_percent, urban_both_a_lot_diff_in_at_least_one_dom_percent, urban_both_cannot_all_in_at_least_one_dom_percent, \
           urban_male_total, urban_male_no_diff, urban_male_some_diff_in_at_least_one_dom, urban_male_a_lot_diff_in_at_least_one_dom, urban_male_cannot_all_in_at_least_one_dom, \
           urban_male_total_percent, urban_male_no_diff_percent, urban_male_some_diff_in_at_least_one_dom_percent, urban_male_a_lot_diff_in_at_least_one_dom_percent, urban_male_cannot_all_in_at_least_one_dom_percent, \
           urban_female_total, urban_female_no_diff, urban_female_some_diff_in_at_least_one_dom, urban_female_a_lot_diff_in_at_least_one_dom, urban_female_cannot_all_in_at_least_one_dom, \
           urban_female_total_percent, urban_female_no_diff_percent, urban_female_some_diff_in_at_least_one_dom_percent, urban_female_a_lot_diff_in_at_least_one_dom_percent, urban_female_cannot_all_in_at_least_one_dom_percent, \
           rural_both_total, rural_both_no_diff, rural_both_some_diff_in_at_least_one_dom, rural_both_a_lot_diff_in_at_least_one_dom, rural_both_cannot_all_in_at_least_one_dom, \
           rural_both_total_percent, rural_both_no_diff_percent, rural_both_some_diff_in_at_least_one_dom_percent, rural_both_a_lot_diff_in_at_least_one_dom_percent, rural_both_cannot_all_in_at_least_one_dom_percent, \
           rural_male_total, rural_male_no_diff, rural_male_some_diff_in_at_least_one_dom, rural_male_a_lot_diff_in_at_least_one_dom, rural_male_cannot_all_in_at_least_one_dom, \
           rural_male_total_percent, rural_male_no_diff_percent, rural_male_some_diff_in_at_least_one_dom_percent, rural_male_a_lot_diff_in_at_least_one_dom_percent, rural_male_cannot_all_in_at_least_one_dom_percent, \
           rural_female_total, rural_female_no_diff, rural_female_some_diff_in_at_least_one_dom, rural_female_a_lot_diff_in_at_least_one_dom, rural_female_cannot_all_in_at_least_one_dom, \
           rural_female_total_percent, rural_female_no_diff_percent, rural_female_some_diff_in_at_least_one_dom_percent, rural_female_a_lot_diff_in_at_least_one_dom_percent, rural_female_cannot_all_in_at_least_one_dom_percent

#********************************************************
# FERTILITY & MORTALITY
#********************************************************
@app.callback(

    #total
    Output('fert_mort_chd_ever_born_tot', 'children'),
    Output('fert_mort_chd_surv_tot', 'children'),
    Output('fert_mort_mean_chd_surv_tot', 'children'),

    #district
    Output('fert_mort_chd_ever_born', 'children'),
    Output('fert_mort_chd_surv', 'children'),
    Output('fert_mort_mean_chd_surv', 'children'),

    [Input('fert_mort_region_dd', 'value')],
    [Input('fert_mort_district_dd', 'value')],
    [Input('fert_mort_search_btn', 'n_clicks')]
)
def get_fert_mort(region, district, n_clicks):

    chld_ever_born_total = None
    chld_surviving_total = None
    mean_chld_surviving_total = None

    chld_ever_born_dist = None
    chld_surviving_dist = None
    mean_chld_surviving_dist = None

    if (region != None) & (district != None) & (n_clicks > 0):

        #regional
        reg_df = df_fert_mort[(df_fert_mort['REGION'] == region) & (df_fert_mort['DISTRICT'] == 'Total') & (df_fert_mort['IS_DISTRICT'] == 0)]
        reg_df = reg_df.reset_index(drop=True)

        chld_ever_born_total = reg_df['CHILDREN_EVER_BORN'][0]
        chld_surviving_total = reg_df['CHILDREN_SURVIVING'][0]
        mean_chld_surviving_total = reg_df['MEAN_CHILDREN_SURVIVING'][0]

        #district
        dist_df = df_fert_mort[(df_fert_mort['REGION'] == region) & (df_fert_mort['DISTRICT'] == district) & (df_fert_mort['IS_DISTRICT'] == 1)]
        dist_df = dist_df.reset_index(drop=True)
        chd_ever_bn_dist = dist_df['CHILDREN_EVER_BORN'][0]
        chd_surv_dist = dist_df['CHILDREN_SURVIVING'][0]
        mn_chd_surv_dist = dist_df['MEAN_CHILDREN_SURVIVING'][0]

        #format
        chld_ever_born_total = '{:,}'.format(chld_ever_born_total)
        chld_surviving_total = '{:,}'.format(chld_surviving_total)
        mean_chld_surviving_total = '{:,}'.format(mean_chld_surviving_total)

        chld_ever_born_dist = '{:,}'.format(chd_ever_bn_dist)
        chld_surviving_dist = '{:,}'.format(chd_surv_dist)
        mean_chld_surviving_dist = '{:,}'.format(mn_chd_surv_dist)

    return chld_ever_born_total, chld_surviving_total, mean_chld_surviving_total, \
           chld_ever_born_dist, chld_surviving_dist, mean_chld_surviving_dist


#********************************************************
# HOUSING
#********************************************************
@app.callback(

    #total
    Output('housing_tot_pop', 'children'),
    Output('housing_tot_hh_pop', 'children'),
    Output('housing_tot_hh', 'children'),
    Output('housing_avg_hh_size', 'children'),

    #district
    Output('housing_tot_resi_struct', 'children'),
    Output('housing_tot_resi_struct_urban', 'children'),
    Output('housing_tot_resi_struct_rural', 'children'),
    Output('housing_resi_struct_urban_share', 'children'),
    Output('housing_resi_distrib_percent', 'children'),

    [Input('housing_region_dd', 'value')],
    [Input('housing_district_dd', 'value')],
    [Input('housing_search_btn', 'n_clicks')]
)
def get_housing(region, district, n_clicks):

    tot_pop = None
    tot_hh_pop = None
    no_of_hh = None
    avg_hh_size = None
    tot_resi_struct = None
    tot_resi_urban = None
    tot_resi_rural = None
    urban_resi_share = None
    dist_resi_struct_percent = None

    if (region != None) & (district != None) & (n_clicks > 0):

        df_total = df_housing[(df_housing['REGION'] == region) & (df_housing['DISTRICT'] == 'Total') & (df_housing['IS_DISTRICT'] == 0)]
        df_total = df_total.reset_index(drop=True)

        # regional
        tot_pop = df_total['TOT_POP'][0]
        tot_hh_pop = df_total['TOT_HH_POP'][0]
        no_of_hh = df_total['NO_HH_TOT'][0]
        avg_hh_size = df_total['AVG_HH_SIZE'][0]

        df_dist = df_housing[(df_housing['REGION'] == region) & (df_housing['DISTRICT'] == district) & (df_housing['IS_DISTRICT'] == 1)]
        df_dist = df_dist.reset_index(drop=True)

        # structures
        tot_resi_struct = df_dist['RES__STRUCT_TOT'][0]
        tot_resi_urban = df_dist['RES_STRUCT_URBAN'][0]
        tot_resi_rural = df_dist['RES_STRUCT_RURAL'][0]

        urban_resi_share = df_dist['URBAN_SHARE_RES_STRUCT'][0]
        dist_resi_struct_percent = df_dist['PERCENT_DIST_RES_STRUCT'][0]

        #tot_resi_struct_2010 = df_dist['NO_OF_RES_STRUCT_2010'][0]
        #percent_resi_struct_2010 = df_dist['PERCENT_OF_RES_STRUCT_2010'][0]

        # format
        tot_pop = '{:,}'.format(tot_pop)
        tot_hh_pop = '{:,}'.format(tot_hh_pop)
        no_of_hh = '{:,}'.format(no_of_hh)
        #avg_hh_size = '{:,}'.format(avg_hh_size)

        tot_resi_struct = '{:,}'.format(tot_resi_struct)
        tot_resi_urban = '{:,}'.format(tot_resi_urban)
        tot_resi_rural = '{:,}'.format(tot_resi_rural)

        #tot_resi_struct_2010 = '{:,}'.format(tot_resi_struct_2010)

    return tot_pop, tot_hh_pop, no_of_hh, avg_hh_size, \
           tot_resi_struct, tot_resi_urban, tot_resi_rural, urban_resi_share, dist_resi_struct_percent


#********************************************************
# WATER & SANITATION
#********************************************************

@app.callback(

    #***********
    #HEADER DATA
    #***********

    #Summary (main)
    Output('ws_reg_total', 'children'),
    Output('ws_reg_percent', 'children'),
    Output('ws_impr_water_src_all_total', 'children'),
    Output('ws_impr_water_src_all_percent', 'children'),
    Output('ws_unimpr_water_src_all_total', 'children'),
    Output('ws_unimpr_water_src_all_percent', 'children'),

    # Urban
    Output('ws_reg_total_urban', 'children'),
    Output('ws_reg_urban_percent', 'children'),
    Output('ws_impr_water_src_urban', 'children'),
    Output('ws_impr_water_src_urban_percent', 'children'),
    Output('ws_unimpr_water_src_urban', 'children'),
    Output('ws_unimpr_water_src_urban_percent', 'children'),

    # Rural
    Output('ws_reg_total_rural', 'children'),
    Output('ws_reg_rural_percent', 'children'),
    Output('ws_impr_water_src_rural', 'children'),
    Output('ws_impr_water_src_rural_percent', 'children'),
    Output('ws_unimpr_water_src_rural', 'children'),
    Output('ws_unimpr_water_src_rural_percent', 'children'),




    Input('ws_region_dd', 'value'),
    Input('ws_district_dd', 'value')
)
def get_water_sanitation_main(region, district):

    # WATER SOURCES - Header

    # ALL LOCALITIES
    all_reg_total = None
    all_reg_percent = None
    impr_water_src_all_main = None
    impr_water_src_all_main_percent = None
    unimpr_water_src_all_main = None
    unimpr_water_src_all_main_percent = None

    # URBAN - Header
    urban_reg_total = None
    urban_reg_percent = None
    impr_water_src_urban_main = None
    impr_water_src_urban_main_percent = None
    unimpr_water_src_urban_main = None
    unimpr_water_src_urban_main_percent = None

    # RURAL - Header
    rural_reg_total = None
    rural_reg_percent = None
    impr_water_src_rural_main = None
    impr_water_src_rural_main_percent = None
    unimpr_water_src_rural_main = None
    unimpr_water_src_rural_main_percent = None


    if (region != None) & (district != None):

        df_data = df_water_sanitation_dic[region]

        #***************
        #ALL LOCALITIES
        #***************

        #Header Data
        df_all = \
        df_data[(df_data['Water_Source'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'All')][
            ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]
        df_all = df_all.reset_index(drop=True)

        # ALL
        all_reg_total = df_all['Number'][0]
        all_reg_percent = 100.0
        all_dist_total = df_all[district][0]

        # water sources - all main regional totals
        df_all_water_src_main = df_data[
            (df_data['Type'] == 'All') &
            (df_data['Status_Code']).isin(['1', '2'])][
            ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]

        #improved main
        df_impr_water_src_all_main = df_all_water_src_main[df_all_water_src_main['Category'] == 'A1']
        df_impr_water_src_all_main = df_impr_water_src_all_main.reset_index(drop=True)

        impr_water_src_all_main = df_impr_water_src_all_main['Number'][0]
        impr_water_src_all_main_percent = df_impr_water_src_all_main['Percent'][0]

        #unimproved main
        df_unimpr_water_src_all_main = df_all_water_src_main[df_all_water_src_main['Category'] == 'A2']
        df_unimpr_water_src_all_main = df_unimpr_water_src_all_main.reset_index(drop=True)

        unimpr_water_src_all_main = df_unimpr_water_src_all_main['Number'][0]
        unimpr_water_src_all_main_percent = df_unimpr_water_src_all_main['Percent'][0]

        # Formatting
        all_reg_total = '{:,}'.format(all_reg_total)
        all_reg_percent = '{:.1f}'.format(all_reg_percent)


        all_dist_total = '{:,}'.format(all_dist_total)

        # ***********
        # URBAN
        # ***********

        #regional summary
        df_urban = \
        df_data[(df_data['Water_Source'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'Urban')][
            ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]
        df_urban = df_urban.reset_index(drop=True)

        urban_reg_total = df_urban['Number'][0]
        urban_reg_percent = 100.0

        # water sources - main
        df_all_water_src_urban = df_data[
            (df_data['Type'] == 'Urban') &
            (df_data['Status_Code']).isin(['1', '2'])][
            ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]

        df_all_water_src_urban_impr = df_all_water_src_urban[df_all_water_src_urban['Category'] == 'A1']
        df_all_water_src_urban_impr = df_all_water_src_urban_impr.reset_index(drop=True)
        impr_water_src_urban_main = df_all_water_src_urban_impr['Number'][0]
        impr_water_src_urban_main_percent = df_all_water_src_urban_impr['Percent'][0]

        df_all_water_src_urban_unimpr = df_all_water_src_urban[df_all_water_src_urban['Category'] == 'A2']
        df_all_water_src_urban_unimpr = df_all_water_src_urban_unimpr.reset_index(drop=True)
        unimpr_water_src_urban_main = df_all_water_src_urban_unimpr['Number'][0]
        unimpr_water_src_urban_main_percent = df_all_water_src_urban_unimpr['Percent'][0]

        impr_water_src_urban_main = '{:,}'.format(impr_water_src_urban_main)
        unimpr_water_src_urban_main = '{:,}'.format(unimpr_water_src_urban_main)

        impr_water_src_urban_main_percent = '{:.1f}'.format(impr_water_src_urban_main_percent)
        unimpr_water_src_urban_main_percent = '{:.1f}'.format(unimpr_water_src_urban_main_percent)

        # ***********
        # RURAL
        # ***********

        # regional summary
        df_rural = \
            df_data[
                (df_data['Water_Source'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'Rural')][
                ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]
        df_rural = df_rural.reset_index(drop=True)

        rural_reg_total = df_rural['Number'][0]
        rural_reg_percent = 100.0

        # water sources - main
        df_all_water_src_rural = df_data[
            (df_data['Type'] == 'Rural') &
            (df_data['Status_Code']).isin(['1', '2'])][
            ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]

        df_all_water_src_rural_impr = df_all_water_src_rural[df_all_water_src_rural['Category'] == 'A1']
        df_all_water_src_rural_impr = df_all_water_src_rural_impr.reset_index(drop=True)
        impr_water_src_rural_main = df_all_water_src_rural_impr['Number'][0]
        impr_water_src_rural_main_percent = df_all_water_src_rural_impr['Percent'][0]

        df_all_water_src_rural_unimpr = df_all_water_src_rural[df_all_water_src_rural['Category'] == 'A2']
        df_all_water_src_rural_unimpr = df_all_water_src_rural_unimpr.reset_index(drop=True)
        unimpr_water_src_rural_main = df_all_water_src_rural_unimpr['Number'][0]
        unimpr_water_src_rural_main_percent = df_all_water_src_rural_unimpr['Percent'][0]

        # format
        # ALL
        impr_water_src_all_main = '{:,}'.format(impr_water_src_all_main)
        unimpr_water_src_all_main = '{:,}'.format(unimpr_water_src_all_main)

        rural_reg_total = '{:,}'.format(rural_reg_total)
        rural_reg_percent = '{:.1f}'.format(rural_reg_percent)
        impr_water_src_rural_main = '{:,}'.format(impr_water_src_rural_main)
        unimpr_water_src_rural_main = '{:,}'.format(unimpr_water_src_rural_main)

        impr_water_src_rural_main_percent = '{:.1f}'.format(impr_water_src_rural_main_percent)
        unimpr_water_src_rural_main_percent = '{:.1f}'.format(unimpr_water_src_rural_main_percent)


    return all_reg_total, all_reg_percent, impr_water_src_all_main, impr_water_src_all_main_percent, unimpr_water_src_all_main, unimpr_water_src_all_main_percent, \
           urban_reg_total, urban_reg_percent, impr_water_src_urban_main, impr_water_src_urban_main_percent, unimpr_water_src_urban_main, unimpr_water_src_urban_main_percent, \
           rural_reg_total, rural_reg_percent, impr_water_src_rural_main, impr_water_src_rural_main_percent, unimpr_water_src_rural_main, unimpr_water_src_rural_main_percent, \


#****************************************
# ALL LOCALITIES, IMPROVED WATER SOURCES
#****************************************
@app.callback(

    Output('ws_impr_water_src_reg_all_total', 'children'),
    Output('ws_impr_water_src_reg_all_percent', 'children'),
    Output('ws_impr_water_src_dist_all_total', 'children'),
    Output('ws_impr_water_src_dist_all_percent', 'children'),

    #Pipe-borne inside dwelling (district)
    Output('ws_pipe_in_dw_reg_all_total', 'children'),
    Output('ws_pipe_in_dw_reg_all_percent', 'children'),
    Output('ws_pipe_in_dw_all_total', 'children'),
    Output('ws_pipe_in_dw_all_percent', 'children'),

    #Pipe-borne outside dwelling but on compound (district)
    Output('ws_pipe_out_dw_on_cmd_reg_all_total', 'children'),
    Output('ws_pipe_out_dw_on_cmd_reg_all_percent', 'children'),
    Output('ws_pipe_out_dw_on_cmd_all_total', 'children'),
    Output('ws_pipe_out_dw_on_cmd_all_percent', 'children'),

    #Pipe-borne outside dwelling but on neighbor's compound (district)
    Output('ws_pipe_out_dw_on_neb_cmd_reg_all_total', 'children'),
    Output('ws_pipe_out_dw_on_neb_cmd_reg_all_percent', 'children'),
    Output('ws_pipe_out_dw_on_neb_cmd_all_total', 'children'),
    Output('ws_pipe_out_dw_on_neb_cmd_all_percent', 'children'),

    #Pipe-tap/Stand pipe (district)
    Output('ws_pipe_tap_stand_pipe_reg_all_total', 'children'),
    Output('ws_pipe_tap_stand_pipe_reg_all_percent', 'children'),
    Output('ws_pipe_tap_stand_pipe_all_total', 'children'),
    Output('ws_pipe_tap_stand_pipe_all_percent', 'children'),

    #Borehole/Tube well (district)
    Output('ws_bore_hole_tube_well_reg_all_total', 'children'),
    Output('ws_bore_hole_tube_well_reg_all_percent', 'children'),
    Output('ws_bore_hole_tube_well_all_total', 'children'),
    Output('ws_bore_hole_tube_well_all_percent', 'children'),

    #Protected well (district)
    Output('ws_protected_well_reg_all_total', 'children'),
    Output('ws_protected_well_reg_all_percent', 'children'),
    Output('ws_protected_well_all_total', 'children'),
    Output('ws_protected_well_all_percent', 'children'),

    #Rain water (district)
    Output('ws_rain_water_reg_all_total', 'children'),
    Output('ws_rain_water_reg_all_percent', 'children'),
    Output('ws_rain_water_all_total', 'children'),
    Output('ws_rain_water_all_percent', 'children'),

    #Protected spring (district)
    Output('ws_protected_spring_reg_all_total', 'children'),
    Output('ws_protected_spring_reg_all_percent', 'children'),
    Output('ws_protected_spring_all_total', 'children'),
    Output('ws_protected_spring_all_percent', 'children'),

    #Bottled Water (district)
    Output('ws_bottled_water_reg_all_total', 'children'),
    Output('ws_bottled_water_reg_all_percent', 'children'),
    Output('ws_bottled_water_all_total', 'children'),
    Output('ws_bottled_water_all_percent', 'children'),

    #Sachet Water (district)
    Output('ws_sachet_water_reg_all_total', 'children'),
    Output('ws_sachet_water_reg_all_percent', 'children'),
    Output('ws_sachet_water_all_total', 'children'),
    Output('ws_sachet_water_all_percent', 'children'),

    Input('ws_region_dd', 'value'),
    Input('ws_district_dd', 'value')
)

def get_water_sanitation_impr_water_sources_all(region, district):

    #***********************************
    # ALL LOCALITIES - DISTRICT DETAILS
    # **********************************

    # Improved Water Sources
    impr_water_src_reg_all_total = None
    impr_water_src_reg_all_percent = None
    impr_water_src_dist_all_total = None
    impr_water_src_dist_all_percent = None

    pipe_in_dw_reg_all_total = None
    pipe_in_dw_reg_all_percent = None
    pipe_in_dw_all_total = None
    pipe_in_dw_all_percent = None

    pipe_out_dw_on_cmp_reg_all_total = None
    pipe_out_dw_on_cmp_reg_all_percent = None
    pipe_out_dw_on_cmp_all_total = None
    pipe_out_dw_on_cmp_all_percent = None

    pipe_out_dw_on_neb_cmp_reg_all_total = None
    pipe_out_dw_on_neb_cmp_reg_all_percent = None
    pipe_out_dw_on_neb_cmp_all_total = None
    pipe_out_dw_on_neb_cmp_all_percent = None

    pipe_tap_stand_pipe_reg_all_total = None
    pipe_tap_stand_pipe_reg_all_percent = None
    pipe_tap_stand_pipe_all_total = None
    pipe_tap_stand_pipe_all_percent = None

    bore_hole_tube_well_reg_all_total = None
    bore_hole_tube_well_reg_all_percent = None
    bore_hole_tube_well_all_total = None
    bore_hole_tube_well_all_percent = None

    protected_well_reg_all_total = None
    protected_well_reg_all_percent = None
    protected_well_all_total = None
    protected_well_all_percent = None

    rain_water_reg_all_total = None
    rain_water_reg_all_percent = None
    rain_water_all_total = None
    rain_water_all_percent = None

    protected_spring_reg_all_total = None
    protected_spring_reg_all_percent = None
    protected_spring_all_total = None
    protected_spring_all_percent = None

    bottled_water_reg_all_total = None
    bottled_water_reg_all_percent = None
    bottled_water_all_total = None
    bottled_water_all_percent = None

    sachet_water_reg_all_total = None
    sachet_water_reg_all_percent = None
    sachet_water_all_total = None
    sachet_water_all_percent = None

    if (region != None) & (district != None):

        # GET DATA
        df_data = df_water_sanitation_dic[region]

        df_all = \
            df_data[(df_data['Water_Source'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'All')][
                ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]
        df_all = df_all.reset_index(drop=True)

        # ALL
        #all_reg_total = df_all['Number'][0]
        #all_reg_percent = 100.0
        all_dist_total = df_all[district][0]

        # Improved Water Resources - District Data, all
        # **********************************************
        df_impr_water_src_dist_all = df_data[(df_data['Category'] == 'A1') & (df_data['Type'] == 'All')][
            ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]

        # District Total
        df_impr_water_src_dist_all_total = df_impr_water_src_dist_all[df_impr_water_src_dist_all['Status_Code'] == '1']
        df_impr_water_src_dist_all_total = df_impr_water_src_dist_all_total.reset_index(drop=True)

        impr_water_src_reg_all_total = df_impr_water_src_dist_all_total['Number'][0]
        impr_water_src_reg_all_percent = df_impr_water_src_dist_all_total['Percent'][0]
        impr_water_src_dist_all_total = df_impr_water_src_dist_all_total[district][0]
        impr_water_src_dist_all_percent = (impr_water_src_dist_all_total / all_dist_total) * 100

        # Pipe-borne inside dwelling
        df_pipe_in_dw_all_total = df_impr_water_src_dist_all[df_impr_water_src_dist_all['Status_Code'] == '1-1']
        df_pipe_in_dw_all_total = df_pipe_in_dw_all_total.reset_index(drop=True)

        pipe_in_dw_reg_all_total = df_pipe_in_dw_all_total['Number'][0]
        pipe_in_dw_all_total = df_pipe_in_dw_all_total[district][0]
        pipe_in_dw_reg_all_percent = df_pipe_in_dw_all_total['Percent'][0]
        pipe_in_dw_all_percent = (pipe_in_dw_all_total / impr_water_src_dist_all_total) * 100

        # Pipe-borne outside dwelling but on compound
        df_pipe_out_dw_on_cmp_all_total = df_impr_water_src_dist_all[df_impr_water_src_dist_all['Status_Code'] == '1-2']
        df_pipe_out_dw_on_cmp_all_total = df_pipe_out_dw_on_cmp_all_total.reset_index(drop=True)

        pipe_out_dw_on_cmp_reg_all_total = df_pipe_out_dw_on_cmp_all_total['Number'][0]
        pipe_out_dw_on_cmp_all_total = df_pipe_out_dw_on_cmp_all_total[district][0]
        pipe_out_dw_on_cmp_reg_all_percent = df_pipe_out_dw_on_cmp_all_total['Percent'][0]
        pipe_out_dw_on_cmp_all_percent = (pipe_out_dw_on_cmp_all_total / impr_water_src_dist_all_total) * 100

        # Pipe-borne outside dwelling but on neighbor's compound
        df_pipe_out_dw_on_neb_cmp_all_total = df_impr_water_src_dist_all[df_impr_water_src_dist_all['Status_Code'] == '1-3']
        df_pipe_out_dw_on_neb_cmp_all_total = df_pipe_out_dw_on_neb_cmp_all_total.reset_index(drop=True)

        pipe_out_dw_on_neb_cmp_reg_all_total = df_pipe_out_dw_on_neb_cmp_all_total['Number'][0]
        pipe_out_dw_on_neb_cmp_all_total = df_pipe_out_dw_on_neb_cmp_all_total[district][0]
        pipe_out_dw_on_neb_cmp_reg_all_percent = df_pipe_out_dw_on_neb_cmp_all_total['Percent'][0]
        pipe_out_dw_on_neb_cmp_all_percent = (pipe_out_dw_on_neb_cmp_all_total / impr_water_src_dist_all_total) * 100

        # Pipe tap / Stand Pipe
        df_pipe_tap_stand_pipe_all_total = df_impr_water_src_dist_all[df_impr_water_src_dist_all['Status_Code'] == '1-4']
        df_pipe_tap_stand_pipe_all_total = df_pipe_tap_stand_pipe_all_total.reset_index(drop=True)

        pipe_tap_stand_pipe_reg_all_total = df_pipe_tap_stand_pipe_all_total['Number'][0]
        pipe_tap_stand_pipe_all_total = df_pipe_tap_stand_pipe_all_total[district][0]
        pipe_tap_stand_pipe_reg_all_percent = df_pipe_tap_stand_pipe_all_total['Percent'][0]
        pipe_tap_stand_pipe_all_percent = (pipe_tap_stand_pipe_all_total / impr_water_src_dist_all_total) * 100

        # Borehole / Tube well
        df_bore_hole_tube_well_all_total = df_impr_water_src_dist_all[df_impr_water_src_dist_all['Status_Code'] == '1-5']
        df_bore_hole_tube_well_all_total = df_bore_hole_tube_well_all_total.reset_index(drop=True)

        bore_hole_tube_well_reg_all_total = df_bore_hole_tube_well_all_total['Number'][0]
        bore_hole_tube_well_all_total = df_bore_hole_tube_well_all_total[district][0]
        bore_hole_tube_well_reg_all_percent = df_bore_hole_tube_well_all_total['Percent'][0]
        bore_hole_tube_well_all_percent = (bore_hole_tube_well_all_total / impr_water_src_dist_all_total) * 100

        # Protected well
        df_protected_well_all_total = df_impr_water_src_dist_all[df_impr_water_src_dist_all['Status_Code'] == '1-6']
        df_protected_well_all_total = df_protected_well_all_total.reset_index(drop=True)

        protected_well_reg_all_total = df_protected_well_all_total['Number'][0]
        protected_well_all_total = df_protected_well_all_total[district][0]
        protected_well_reg_all_percent = df_protected_well_all_total['Percent'][0]
        protected_well_all_percent = (protected_well_all_total / impr_water_src_dist_all_total) * 100

        # Rain water
        df_rain_water_all_total = df_impr_water_src_dist_all[df_impr_water_src_dist_all['Status_Code'] == '1-7']
        df_rain_water_all_total = df_rain_water_all_total.reset_index(drop=True)

        rain_water_reg_all_total = df_rain_water_all_total['Number'][0]
        rain_water_all_total = df_rain_water_all_total[district][0]
        rain_water_reg_all_percent = df_rain_water_all_total['Percent'][0]
        rain_water_all_percent = (rain_water_all_total / impr_water_src_dist_all_total) * 100

        # Protected spring
        df_protected_spring_all_total = df_impr_water_src_dist_all[df_impr_water_src_dist_all['Status_Code'] == '1-8']
        df_protected_spring_all_total = df_protected_spring_all_total.reset_index(drop=True)

        protected_spring_reg_all_total = df_protected_spring_all_total['Number'][0]
        protected_spring_all_total = df_protected_spring_all_total[district][0]
        protected_spring_reg_all_percent = df_protected_spring_all_total['Percent'][0]
        protected_spring_all_percent = (protected_spring_all_total / impr_water_src_dist_all_total) * 100

        # Bottled water
        df_bottled_water_all_total = df_impr_water_src_dist_all[df_impr_water_src_dist_all['Status_Code'] == '1-9']
        df_bottled_water_all_total = df_bottled_water_all_total.reset_index(drop=True)

        bottled_water_reg_all_total = df_bottled_water_all_total['Number'][0]
        bottled_water_all_total = df_bottled_water_all_total[district][0]
        bottled_water_reg_all_percent = df_bottled_water_all_total['Percent'][0]
        bottled_water_all_percent = (bottled_water_all_total / impr_water_src_dist_all_total) * 100

        # Sachet water
        df_sachet_water_all_total = df_impr_water_src_dist_all[df_impr_water_src_dist_all['Status_Code'] == '1-10']
        df_sachet_water_all_total = df_sachet_water_all_total.reset_index(drop=True)

        sachet_water_reg_all_total = df_sachet_water_all_total['Number'][0]
        sachet_water_all_total = df_sachet_water_all_total[district][0]
        sachet_water_reg_all_percent = df_sachet_water_all_total['Percent'][0]
        sachet_water_all_percent = (sachet_water_all_total / impr_water_src_dist_all_total) * 100


        impr_water_src_reg_all_total = '{:,}'.format(impr_water_src_reg_all_total)
        impr_water_src_reg_all_percent = '{:.1f}'.format(impr_water_src_reg_all_percent)
        impr_water_src_dist_all_total = '{:,}'.format(impr_water_src_dist_all_total)
        impr_water_src_dist_all_percent = '{:,.1f}'.format(impr_water_src_dist_all_percent)

        pipe_in_dw_reg_all_total = '{:,}'.format(pipe_in_dw_reg_all_total)
        pipe_in_dw_all_total = '{:,}'.format(pipe_in_dw_all_total)
        pipe_in_dw_all_percent = '{:,.1f}'.format(pipe_in_dw_all_percent)

        pipe_out_dw_on_cmp_reg_all_total = '{:,}'.format(pipe_out_dw_on_cmp_reg_all_total)
        pipe_out_dw_on_cmp_all_total = '{:,}'.format(pipe_out_dw_on_cmp_all_total)
        pipe_out_dw_on_cmp_all_percent = '{:,.1f}'.format(pipe_out_dw_on_cmp_all_percent)

        pipe_out_dw_on_neb_cmp_reg_all_total = '{:,}'.format(pipe_out_dw_on_neb_cmp_reg_all_total)
        pipe_out_dw_on_neb_cmp_all_total = '{:,}'.format(pipe_out_dw_on_neb_cmp_all_total)
        pipe_out_dw_on_neb_cmp_reg_all_percent = '{:,.1f}'.format(pipe_out_dw_on_neb_cmp_reg_all_percent)
        pipe_out_dw_on_neb_cmp_all_percent = '{:,.1f}'.format(pipe_out_dw_on_neb_cmp_all_percent)

        pipe_tap_stand_pipe_reg_all_total = '{:,}'.format(pipe_tap_stand_pipe_reg_all_total)
        pipe_tap_stand_pipe_all_total = '{:,}'.format(pipe_tap_stand_pipe_all_total)
        pipe_tap_stand_pipe_reg_all_percent = '{:,.1f}'.format(pipe_tap_stand_pipe_reg_all_percent)
        pipe_tap_stand_pipe_all_percent = '{:,.1f}'.format(pipe_tap_stand_pipe_all_percent)

        bore_hole_tube_well_reg_all_total = '{:,}'.format(bore_hole_tube_well_reg_all_total)
        bore_hole_tube_well_all_total = '{:,}'.format(bore_hole_tube_well_all_total)
        bore_hole_tube_well_reg_all_percent = '{:,.1f}'.format(bore_hole_tube_well_reg_all_percent)
        bore_hole_tube_well_all_percent = '{:,.1f}'.format(bore_hole_tube_well_all_percent)

        protected_well_reg_all_total = '{:,}'.format(protected_well_reg_all_total)
        protected_well_all_total = '{:,}'.format(protected_well_all_total)
        protected_well_reg_all_percent = '{:,.1f}'.format(protected_well_reg_all_percent)
        protected_well_all_percent = '{:,.1f}'.format(protected_well_all_percent)

        rain_water_reg_all_total = '{:,}'.format(rain_water_reg_all_total)
        rain_water_all_total = '{:,}'.format(rain_water_all_total)
        rain_water_reg_all_percent = '{:,.1f}'.format(rain_water_reg_all_percent)
        rain_water_all_percent = '{:,.1f}'.format(rain_water_all_percent)

        protected_spring_reg_all_total = '{:,}'.format(protected_spring_reg_all_total)
        protected_spring_all_total = '{:,}'.format(protected_spring_all_total)
        protected_spring_reg_all_percent = '{:,.1f}'.format(protected_spring_reg_all_percent)
        protected_spring_all_percent = '{:,.1f}'.format(protected_spring_all_percent)

        bottled_water_reg_all_total = '{:,}'.format(bottled_water_reg_all_total)
        bottled_water_all_total = '{:,}'.format(bottled_water_all_total)
        bottled_water_reg_all_percent = '{:,.1f}'.format(bottled_water_reg_all_percent)
        bottled_water_all_percent = '{:,.1f}'.format(bottled_water_all_percent)

        sachet_water_reg_all_total = '{:,}'.format(sachet_water_reg_all_total)
        sachet_water_all_total = '{:,}'.format(sachet_water_all_total)
        sachet_water_reg_all_percent = '{:,.1f}'.format(sachet_water_reg_all_percent)
        sachet_water_all_percent = '{:,.1f}'.format(sachet_water_all_percent)

    return impr_water_src_reg_all_total, impr_water_src_reg_all_percent, \
           impr_water_src_dist_all_total, impr_water_src_dist_all_percent, \
           pipe_in_dw_reg_all_total, pipe_in_dw_reg_all_percent, pipe_in_dw_all_total, pipe_in_dw_all_percent, \
           pipe_out_dw_on_cmp_reg_all_total, pipe_out_dw_on_cmp_reg_all_percent, pipe_out_dw_on_cmp_all_total, pipe_out_dw_on_cmp_all_percent, \
           pipe_out_dw_on_neb_cmp_reg_all_total, pipe_out_dw_on_neb_cmp_reg_all_percent, pipe_out_dw_on_neb_cmp_all_total, pipe_out_dw_on_neb_cmp_all_percent, \
           pipe_tap_stand_pipe_reg_all_total, pipe_tap_stand_pipe_reg_all_percent, pipe_tap_stand_pipe_all_total, pipe_tap_stand_pipe_all_percent, \
           bore_hole_tube_well_reg_all_total, bore_hole_tube_well_reg_all_percent, bore_hole_tube_well_all_total, bore_hole_tube_well_all_percent, \
           protected_well_reg_all_total, protected_well_reg_all_percent, protected_well_all_total, protected_well_all_percent, \
           rain_water_reg_all_total, rain_water_reg_all_percent, rain_water_all_total, rain_water_all_percent, \
           protected_spring_reg_all_total, protected_spring_reg_all_percent, protected_spring_all_total, protected_spring_all_percent, \
           bottled_water_reg_all_total, bottled_water_reg_all_percent, bottled_water_all_total, bottled_water_all_total, \
           sachet_water_reg_all_total, sachet_water_reg_all_percent, sachet_water_all_total, sachet_water_all_total

#***************************************
# ALL, UNIMPROVED WATER SOURCES
#***************************************

@app.callback(

    Output('ws_unimpr_water_src_reg_all_total', 'children'),
    Output('ws_unimpr_water_src_reg_all_percent', 'children'),
    Output('ws_unimpr_water_src_dist_all_total', 'children'),
    Output('ws_unimpr_water_src_dist_all_percent', 'children'),

    # tanker
    Output('ws_tanker_vendor_reg_all_total', 'children'),
    Output('ws_tanker_vendor_reg_all_percent', 'children'),
    Output('ws_tanker_vendor_all_total', 'children'),
    Output('ws_tanker_vendor_all_percent', 'children'),

    # unprotected well
    Output('ws_unprotec_well_reg_all_total', 'children'),
    Output('ws_unprotec_well_reg_all_percent', 'children'),
    Output('ws_unprotec_well_all_total','children'),
    Output('ws_unprotec_well_all_percent', 'children'),

    # unprotected spring
    Output('unprotec_spring_reg_all_total', 'children'),
    Output('unprotec_spring_reg_all_percent', 'children'),
    Output('unprotec_spring_all_total', 'children'),
    Output('unprotec_spring_all_percent', 'children'),

    # river stream
    Output('river_stream_reg_all_total', 'children'),
    Output('river_stream_reg_all_percent', 'children'),
    Output('river_stream_all_total', 'children'),
    Output('river_stream_all_percent', 'children'),

    # Dugout/Pond/Lake/Dam/Canal
    Output('dugout_pond_lake_dam_canal_reg_all_total', 'children'),
    Output('dugout_pond_lake_dam_canal_reg_all_percent', 'children'),
    Output('dugout_pond_lake_dam_canal_all_total', 'children'),
    Output('dugout_pond_lake_dam_canal_all_percent', 'children'),

    Output('other_reg_all_total', 'children'),
    Output('other_reg_all_percent', 'children'),
    Output('other_all_total', 'children'),
    Output('other_all_percent', 'children'),

    Input('ws_region_dd', 'value'),
    Input('ws_district_dd', 'value')
)

def get_water_sanitation_unimpr_water_sources_all(region, district):

    # ***********************************
    # ALL LOCALITIES - DISTRICT DETAILS
    # **********************************

    # Unimproved Water Sources
    unimpr_water_src_reg_all_total = None
    unimpr_water_src_reg_all_percent = None
    unimpr_water_src_dist_all_total = None
    unimpr_water_src_dist_all_percent = None

    tanker_vendor_reg_all_total = None
    tanker_vendor_reg_all_percent = None
    tanker_vendor_all_total = None
    tanker_vendor_all_percent = None

    unprotected_well_reg_all_total = None
    unprotected_well_reg_all_percent = None
    unprotected_well_all_total = None
    unprotected_well_all_percent = None

    unprotected_spring_reg_all_total = None
    unprotected_spring_reg_all_percent = None
    unprotected_spring_all_total = None
    unprotected_spring_all_percent = None

    river_stream_reg_all_total = None
    river_stream_reg_all_percent = None
    river_stream_all_total = None
    river_stream_all_percent = None

    dugout_pond_lake_dam_canal_reg_all_total = None
    dugout_pond_lake_dam_canal_reg_all_percent = None
    dugout_pond_lake_dam_canal_all_total = None
    dugout_pond_lake_dam_canal_all_percent = None

    other_reg_all_total = None
    other_reg_all_percent = None
    other_all_total = None
    other_all_percent = None

    if (region != None) & (district != None):

        # GET DATA
        df_data = df_water_sanitation_dic[region]

        df_all = \
            df_data[
                (df_data['Water_Source'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'All')][
                ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]
        df_all = df_all.reset_index(drop=True)

        # District Total - ALL
        all_dist_total = df_all[district][0]

        # Unimproved Water Resources - District Data, all
        # **********************************************

        df_unimpr_water_src_dist_all = df_data[(df_data['Category'] == 'A2') & (df_data['Type'] == 'All')][
            ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]

        # District Total
        df_unimpr_water_src_dist_all_total = df_unimpr_water_src_dist_all[df_unimpr_water_src_dist_all['Status_Code'] == '2']
        df_unimpr_water_src_dist_all_total = df_unimpr_water_src_dist_all_total.reset_index(drop=True)

        unimpr_water_src_reg_all_total = df_unimpr_water_src_dist_all_total['Number'][0]
        unimpr_water_src_reg_all_percent = df_unimpr_water_src_dist_all_total['Percent'][0]
        unimpr_water_src_dist_all_total = df_unimpr_water_src_dist_all_total[district][0]
        unimpr_water_src_dist_all_percent = (unimpr_water_src_dist_all_total / all_dist_total) * 100

        # Tanker supplied/Vendor provided
        df_tanker_vendor_reg_all_total = df_unimpr_water_src_dist_all[df_unimpr_water_src_dist_all['Status_Code'] == '2-1']
        df_tanker_vendor_reg_all_total = df_tanker_vendor_reg_all_total.reset_index(drop=True)

        tanker_vendor_reg_all_total = df_tanker_vendor_reg_all_total['Number'][0]
        tanker_vendor_reg_all_percent = df_tanker_vendor_reg_all_total['Percent'][0]
        tanker_vendor_all_total = df_tanker_vendor_reg_all_total[district][0]
        tanker_vendor_all_percent = (tanker_vendor_all_total / unimpr_water_src_reg_all_total) * 100

        # Unprotected well
        df_unprotected_well_reg_all_total = df_unimpr_water_src_dist_all[
            df_unimpr_water_src_dist_all['Status_Code'] == '2-1']
        df_unprotected_well_reg_all_total = df_unprotected_well_reg_all_total.reset_index(drop=True)

        unprotected_well_reg_all_total = df_unprotected_well_reg_all_total['Number'][0]
        unprotected_well_reg_all_percent = df_unprotected_well_reg_all_total['Percent'][0]
        unprotected_well_all_total = df_unprotected_well_reg_all_total[district][0]
        unprotected_well_all_percent = (unprotected_well_all_total / unimpr_water_src_reg_all_total) * 100

        # Unprotected spring
        df_unprotected_spring_reg_all_total = df_unimpr_water_src_dist_all[
            df_unimpr_water_src_dist_all['Status_Code'] == '2-2']
        df_unprotected_spring_reg_all_total = df_unprotected_spring_reg_all_total.reset_index(drop=True)

        unprotected_spring_reg_all_total = df_unprotected_spring_reg_all_total['Number'][0]
        unprotected_spring_reg_all_percent = df_unprotected_spring_reg_all_total['Percent'][0]
        unprotected_spring_all_total = df_unprotected_spring_reg_all_total[district][0]
        unprotected_spring_all_percent = (unprotected_spring_all_total / unimpr_water_src_reg_all_total) * 100

        # river stream
        df_river_stream_reg_all_total = df_unimpr_water_src_dist_all[
            df_unimpr_water_src_dist_all['Status_Code'] == '2-3']
        df_river_stream_reg_all_total = df_tanker_vendor_reg_all_total.reset_index(drop=True)

        river_stream_reg_all_total = df_river_stream_reg_all_total['Number'][0]
        river_stream_reg_all_percent = df_river_stream_reg_all_total['Percent'][0]
        river_stream_all_total = df_river_stream_reg_all_total[district][0]
        river_stream_all_percent = (river_stream_all_total / unimpr_water_src_reg_all_total) * 100

        # dugout, pond, lake, dam, canal
        df_dpld_canal_reg_all_total = df_unimpr_water_src_dist_all[
            df_unimpr_water_src_dist_all['Status_Code'] == '2-3']
        df_dpld_canal_reg_all_total = df_dpld_canal_reg_all_total.reset_index(drop=True)

        dpld_canal_reg_all_total = df_dpld_canal_reg_all_total['Number'][0]
        dpld_canal_reg_all_percent = df_dpld_canal_reg_all_total['Percent'][0]
        dpld_canal_all_total = df_dpld_canal_reg_all_total[district][0]
        dpld_canal_all_percent = (dpld_canal_all_total / unimpr_water_src_reg_all_total) * 100

        # other
        df_other_reg_all_total = df_unimpr_water_src_dist_all[
            df_unimpr_water_src_dist_all['Status_Code'] == '2-4']
        df_other_reg_all_total = df_other_reg_all_total.reset_index(drop=True)

        other_reg_all_total = df_other_reg_all_total['Number'][0]
        other_reg_all_percent = df_other_reg_all_total['Percent'][0]
        other_all_total = df_other_reg_all_total[district][0]
        other_all_percent = (other_all_total / unimpr_water_src_reg_all_total) * 100

        # Formatting
        unimpr_water_src_reg_all_total = '{:,}'.format(unimpr_water_src_reg_all_total)
        unimpr_water_src_reg_all_percent = '{:,.1f}'.format(unimpr_water_src_reg_all_percent)
        unimpr_water_src_dist_all_total = '{:,}'.format(unimpr_water_src_dist_all_total)
        unimpr_water_src_dist_all_percent = '{:,.1f}'.format(unimpr_water_src_dist_all_percent)

        tanker_vendor_reg_all_total = '{:,}'.format(tanker_vendor_reg_all_total)
        tanker_vendor_reg_all_percent = '{:,.1f}'.format(tanker_vendor_reg_all_percent)
        tanker_vendor_all_total = '{:,}'.format(tanker_vendor_all_total)
        tanker_vendor_all_percent = '{:,.1f}'.format(tanker_vendor_all_percent)

        unprotected_well_reg_all_total = '{:,}'.format(unprotected_well_reg_all_total)
        unprotected_well_reg_all_percent = '{:,.1f}'.format(unprotected_well_reg_all_percent)
        unprotected_well_all_total = '{:,}'.format(unprotected_well_all_total)
        unprotected_well_all_percent = '{:,.1f}'.format(unprotected_well_all_percent)

        unprotected_spring_reg_all_total = '{:,}'.format(unprotected_spring_reg_all_total)
        unprotected_spring_reg_all_percent = '{:,.1f}'.format(unprotected_spring_reg_all_percent)
        unprotected_spring_all_total = '{:,}'.format(unprotected_spring_all_total)
        unprotected_spring_all_percent = '{:,.1f}'.format(unprotected_spring_all_percent)

        river_stream_reg_all_total = '{:,}'.format(river_stream_reg_all_total)
        river_stream_reg_all_percent = '{:,.1f}'.format(river_stream_reg_all_percent)
        river_stream_all_total = '{:,}'.format(river_stream_all_total)
        river_stream_all_percent = '{:,.1f}'.format(river_stream_all_percent)

        dpld_canal_reg_all_total = '{:,}'.format(dpld_canal_reg_all_total)
        dpld_canal_reg_all_percent = '{:,.1f}'.format(dpld_canal_reg_all_percent)
        dpld_canal_all_total = '{:,}'.format(dpld_canal_all_total)
        dpld_canal_all_percent = '{:,.1f}'.format(dpld_canal_all_percent)

        other_reg_all_total = '{:,}'.format(other_reg_all_total)
        other_reg_all_percent = '{:,.1f}'.format(other_reg_all_percent)
        other_all_total = '{:,}'.format(other_all_total)
        other_all_percent = '{:,.1f}'.format(other_all_percent)

    return unimpr_water_src_reg_all_total, unimpr_water_src_reg_all_percent, \
           unimpr_water_src_dist_all_total, unimpr_water_src_dist_all_percent, \
           tanker_vendor_reg_all_total, tanker_vendor_reg_all_percent, tanker_vendor_all_total, tanker_vendor_all_percent, \
           unprotected_well_reg_all_total, unprotected_well_reg_all_percent, unprotected_well_all_total, unprotected_well_all_percent, \
           unprotected_spring_reg_all_total, unprotected_spring_reg_all_percent, unprotected_spring_all_total, unprotected_spring_all_percent, \
           river_stream_reg_all_total, river_stream_reg_all_percent, river_stream_all_total, river_stream_all_percent, \
           dpld_canal_reg_all_total, dpld_canal_reg_all_percent, dpld_canal_all_total, dpld_canal_all_percent, \
           other_reg_all_total, other_reg_all_percent, other_all_total, other_all_percent


#**************************************
# Water & Sanitation - URBAN
#**************************************
@app.callback(

    #*******
    # URBAN
    #*******

    # #ALL, IMPROVED WATER SOURCES
    #*****************************
    Output('ws_impr_water_src_reg_urban_total', 'children'),
    Output('ws_impr_water_src_reg_urban_percent', 'children'),
    Output('ws_impr_water_src_dist_urban_total', 'children'),
    Output('ws_impr_water_src_dist_urban_percent', 'children'),

    #Pipe-borne inside dwelling (district)
    Output('ws_pipe_in_dw_reg_urban_total', 'children'),
    Output('ws_pipe_in_dw_reg_urban_percent', 'children'),
    Output('ws_pipe_in_dw_urban_total', 'children'),
    Output('ws_pipe_in_dw_urban_percent', 'children'),

    #Pipe-borne outside dwelling but on compound (district)
    Output('ws_pipe_out_dw_on_cmd_reg_urban_total', 'children'),
    Output('ws_pipe_out_dw_on_cmd_reg_urban_percent', 'children'),
    Output('ws_pipe_out_dw_on_cmd_urban_total', 'children'),
    Output('ws_pipe_out_dw_on_cmd_urban_percent', 'children'),

    #Pipe-borne outside dwelling but on neighbor's compound (district)
    Output('ws_pipe_out_dw_on_neb_cmd_reg_urban_total', 'children'),
    Output('ws_pipe_out_dw_on_neb_cmd_reg_urban_percent', 'children'),
    Output('ws_pipe_out_dw_on_neb_cmd_urban_total', 'children'),
    Output('ws_pipe_out_dw_on_neb_cmd_urban_percent', 'children'),

    #Pipe-tap/Stand pipe (district)
    Output('ws_pipe_tap_stand_pipe_reg_urban_total', 'children'),
    Output('ws_pipe_tap_stand_pipe_reg_urban_percent', 'children'),
    Output('ws_pipe_tap_stand_pipe_urban_total', 'children'),
    Output('ws_pipe_tap_stand_pipe_urban_percent', 'children'),

    #Borehole/Tube well (district)
    Output('ws_bore_hole_tube_well_reg_urban_total', 'children'),
    Output('ws_bore_hole_tube_well_reg_urban_percent', 'children'),
    Output('ws_bore_hole_tube_well_urban_total', 'children'),
    Output('ws_bore_hole_tube_well_urban_percent', 'children'),

    #Protected well (district)
    Output('ws_protected_well_reg_urban_total', 'children'),
    Output('ws_protected_well_reg_urban_percent', 'children'),
    Output('ws_protected_well_urban_total', 'children'),
    Output('ws_protected_well_urban_percent', 'children'),

    #Rain water (district)
    Output('ws_rain_water_reg_urban_total', 'children'),
    Output('ws_rain_water_reg_urban_percent', 'children'),
    Output('ws_rain_water_urban_total', 'children'),
    Output('ws_rain_water_urban_percent', 'children'),

    #Protected spring (district)
    Output('ws_protected_spring_reg_urban_total', 'children'),
    Output('ws_protected_spring_reg_urban_percent', 'children'),
    Output('ws_protected_spring_urban_total', 'children'),
    Output('ws_protected_spring_urban_percent', 'children'),

    #Bottled Water (district)
    Output('ws_bottled_water_reg_urban_total', 'children'),
    Output('ws_bottled_water_reg_urban_percent', 'children'),
    Output('ws_bottled_water_urban_total', 'children'),
    Output('ws_bottled_water_urban_percent', 'children'),

    #Sachet Water (district)
    Output('ws_sachet_water_reg_urban_total', 'children'),
    Output('ws_sachet_water_reg_urban_percent', 'children'),
    Output('ws_sachet_water_urban_total', 'children'),
    Output('ws_sachet_water_urban_percent', 'children'),

    Input('ws_region_dd', 'value'),
    Input('ws_district_dd', 'value')

)
def get_water_sanitation_impr_water_sources_urban(region, district):

    # Improved Water Resources - District Data, Urban
    # **********************************************

    impr_water_src_reg_urban_total = None
    impr_water_src_reg_urban_percent = None
    impr_water_src_dist_urban_total = None
    impr_water_src_dist_urban_percent = None

    pipe_in_dw_reg_urban_total = None
    pipe_in_dw_urban_total = None
    pipe_in_dw_reg_urban_percent = None
    pipe_in_dw_urban_percent = None

    pipe_out_dw_on_cmp_reg_urban_total = None
    pipe_out_dw_on_cmp_urban_total = None
    pipe_out_dw_on_cmp_reg_urban_percent = None
    pipe_out_dw_on_cmp_urban_percent = None

    pipe_out_dw_on_neb_cmp_reg_urban_total = None
    pipe_out_dw_on_neb_cmp_urban_total = None
    pipe_out_dw_on_neb_cmp_reg_urban_percent = None
    pipe_out_dw_on_neb_cmp_urban_percent = None

    pipe_tap_stand_pipe_reg_urban_total = None
    pipe_tap_stand_pipe_urban_total = None
    pipe_tap_stand_pipe_reg_urban_percent = None
    pipe_tap_stand_pipe_urban_percent = None

    bore_hole_tube_well_reg_urban_total = None
    bore_hole_tube_well_urban_total = None
    bore_hole_tube_well_reg_urban_percent = None
    bore_hole_tube_well_urban_percent = None

    protected_well_reg_urban_total = None
    protected_well_urban_total = None
    protected_well_reg_urban_percent = None
    protected_well_urban_percent = None

    rain_water_reg_urban_total = None
    rain_water_urban_total = None
    rain_water_reg_urban_percent = None
    rain_water_urban_percent = None

    protected_spring_reg_urban_total = None
    protected_spring_urban_total = None
    protected_spring_reg_urban_percent = None
    protected_spring_urban_percent = None

    bottled_water_reg_urban_total = None
    bottled_water_urban_total = None
    bottled_water_reg_urban_percent = None
    bottled_water_urban_percent = None

    sachet_water_reg_urban_total = None
    sachet_water_urban_total = None
    sachet_water_reg_urban_percent = None
    sachet_water_urban_percent = None

    if (region != None) & (district != None):

        # GET DATA
        df_data = df_water_sanitation_dic[region]

        df_urban = df_data[(df_data['Water_Source'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'Urban')][
                     ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]
        df_urban = df_urban.reset_index(drop=True)

        # format
        urban_reg_total = df_urban['Number'][0]
        urban_reg_percent = 100.0
        urban_dist_total = df_urban[district][0]


        df_impr_water_src_dist_urban = df_data[(df_data['Category'] == 'A1') & (df_data['Type'] == 'Urban')][
            ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]

        # District Total
        df_impr_water_src_dist_urban_total = df_impr_water_src_dist_urban[
            df_impr_water_src_dist_urban['Status_Code'] == '1']
        df_impr_water_src_dist_urban_total = df_impr_water_src_dist_urban_total.reset_index(drop=True)

        impr_water_src_reg_urban_total = df_impr_water_src_dist_urban_total['Number'][0]
        impr_water_src_reg_urban_percent = df_impr_water_src_dist_urban_total['Percent'][0]
        impr_water_src_dist_urban_total = df_impr_water_src_dist_urban_total[district][0]
        impr_water_src_dist_urban_percent = (impr_water_src_dist_urban_total / urban_dist_total) * 100

        # Pipe-borne inside dwelling
        df_pipe_in_dw_urban_total = df_impr_water_src_dist_urban[df_impr_water_src_dist_urban['Status_Code'] == '1-1']
        df_pipe_in_dw_urban_total = df_pipe_in_dw_urban_total.reset_index(drop=True)

        pipe_in_dw_reg_urban_total = df_pipe_in_dw_urban_total['Number'][0]
        pipe_in_dw_urban_total = df_pipe_in_dw_urban_total[district][0]
        pipe_in_dw_reg_urban_percent = df_pipe_in_dw_urban_total['Percent'][0]
        pipe_in_dw_urban_percent = (pipe_in_dw_urban_total / impr_water_src_dist_urban_total) * 100

        # Pipe-borne outside dwelling but on compound
        df_pipe_out_dw_on_cmp_urban_total = df_impr_water_src_dist_urban[
            df_impr_water_src_dist_urban['Status_Code'] == '1-2']
        df_pipe_out_dw_on_cmp_urban_total = df_pipe_out_dw_on_cmp_urban_total.reset_index(drop=True)

        pipe_out_dw_on_cmp_reg_urban_total = df_pipe_out_dw_on_cmp_urban_total['Number'][0]
        pipe_out_dw_on_cmp_urban_total = df_pipe_out_dw_on_cmp_urban_total[district][0]
        pipe_out_dw_on_cmp_reg_urban_percent = df_pipe_out_dw_on_cmp_urban_total['Percent'][0]
        pipe_out_dw_on_cmp_urban_percent = (pipe_out_dw_on_cmp_urban_total / impr_water_src_dist_urban_total) * 100

        # Pipe-borne outside dwelling but on neighbor's compound
        df_pipe_out_dw_on_neb_cmp_urban_total = df_impr_water_src_dist_urban[
            df_impr_water_src_dist_urban['Status_Code'] == '1-3']
        df_pipe_out_dw_on_neb_cmp_urban_total = df_pipe_out_dw_on_neb_cmp_urban_total.reset_index(drop=True)

        pipe_out_dw_on_neb_cmp_reg_urban_total = df_pipe_out_dw_on_neb_cmp_urban_total['Number'][0]
        pipe_out_dw_on_neb_cmp_urban_total = df_pipe_out_dw_on_neb_cmp_urban_total[district][0]
        pipe_out_dw_on_neb_cmp_reg_urban_percent = df_pipe_out_dw_on_neb_cmp_urban_total['Percent'][0]
        pipe_out_dw_on_neb_cmp_urban_percent = (pipe_out_dw_on_neb_cmp_urban_total / impr_water_src_dist_urban_total) * 100

        # Pipe tap / Stand Pipe
        df_pipe_tap_stand_pipe_urban_total = df_impr_water_src_dist_urban[
            df_impr_water_src_dist_urban['Status_Code'] == '1-4']
        df_pipe_tap_stand_pipe_urban_total = df_pipe_tap_stand_pipe_urban_total.reset_index(drop=True)

        pipe_tap_stand_pipe_reg_urban_total = df_pipe_tap_stand_pipe_urban_total['Number'][0]
        pipe_tap_stand_pipe_urban_total = df_pipe_tap_stand_pipe_urban_total[district][0]
        pipe_tap_stand_pipe_reg_urban_percent = df_pipe_tap_stand_pipe_urban_total['Percent'][0]
        pipe_tap_stand_pipe_urban_percent = (pipe_tap_stand_pipe_urban_total / impr_water_src_dist_urban_total) * 100

        # Borehole / Tube well
        df_bore_hole_tube_well_urban_total = df_impr_water_src_dist_urban[
            df_impr_water_src_dist_urban['Status_Code'] == '1-5']
        df_bore_hole_tube_well_urban_total = df_bore_hole_tube_well_urban_total.reset_index(drop=True)

        bore_hole_tube_well_reg_urban_total = df_bore_hole_tube_well_urban_total['Number'][0]
        bore_hole_tube_well_urban_total = df_bore_hole_tube_well_urban_total[district][0]
        bore_hole_tube_well_reg_urban_percent = df_bore_hole_tube_well_urban_total['Percent'][0]
        bore_hole_tube_well_urban_percent = (bore_hole_tube_well_urban_total / impr_water_src_dist_urban_total) * 100

        # Protected well
        df_protected_well_urban_total = df_impr_water_src_dist_urban[df_impr_water_src_dist_urban['Status_Code'] == '1-6']
        df_protected_well_urban_total = df_protected_well_urban_total.reset_index(drop=True)

        protected_well_reg_urban_total = df_protected_well_urban_total['Number'][0]
        protected_well_urban_total = df_protected_well_urban_total[district][0]
        protected_well_reg_urban_percent = df_protected_well_urban_total['Percent'][0]
        protected_well_urban_percent = (protected_well_urban_total / impr_water_src_dist_urban_total) * 100

        # Rain water
        df_rain_water_urban_total = df_impr_water_src_dist_urban[df_impr_water_src_dist_urban['Status_Code'] == '1-7']
        df_rain_water_urban_total = df_rain_water_urban_total.reset_index(drop=True)

        rain_water_reg_urban_total = df_rain_water_urban_total['Number'][0]
        rain_water_urban_total = df_rain_water_urban_total[district][0]
        rain_water_reg_urban_percent = df_rain_water_urban_total['Percent'][0]
        rain_water_urban_percent = (rain_water_urban_total / impr_water_src_dist_urban_total) * 100

        # Protected spring
        df_protected_spring_urban_total = df_impr_water_src_dist_urban[df_impr_water_src_dist_urban['Status_Code'] == '1-8']
        df_protected_spring_urban_total = df_protected_spring_urban_total.reset_index(drop=True)

        protected_spring_reg_urban_total = df_protected_spring_urban_total['Number'][0]
        protected_spring_urban_total = df_protected_spring_urban_total[district][0]
        protected_spring_reg_urban_percent = df_protected_spring_urban_total['Percent'][0]
        protected_spring_urban_percent = (protected_spring_urban_total / impr_water_src_dist_urban_total) * 100

        # Bottled water
        df_bottled_water_urban_total = df_impr_water_src_dist_urban[df_impr_water_src_dist_urban['Status_Code'] == '1-9']
        df_bottled_water_urban_total = df_bottled_water_urban_total.reset_index(drop=True)

        bottled_water_reg_urban_total = df_bottled_water_urban_total['Number'][0]
        bottled_water_urban_total = df_bottled_water_urban_total[district][0]
        bottled_water_reg_urban_percent = df_bottled_water_urban_total['Percent'][0]
        bottled_water_urban_percent = (bottled_water_urban_total / impr_water_src_dist_urban_total) * 100

        # Sachet water
        df_sachet_water_urban_total = df_impr_water_src_dist_urban[df_impr_water_src_dist_urban['Status_Code'] == '1-10']
        df_sachet_water_urban_total = df_sachet_water_urban_total.reset_index(drop=True)

        sachet_water_reg_urban_total = df_sachet_water_urban_total['Number'][0]
        sachet_water_urban_total = df_sachet_water_urban_total[district][0]
        sachet_water_reg_urban_percent = df_sachet_water_urban_total['Percent'][0]
        sachet_water_urban_percent = (sachet_water_urban_total / impr_water_src_dist_urban_total) * 100

        impr_water_src_reg_urban_total = '{:,}'.format(impr_water_src_reg_urban_total)
        impr_water_src_reg_urban_percent = '{:.1f}'.format(impr_water_src_reg_urban_percent)
        impr_water_src_dist_urban_total = '{:,}'.format(impr_water_src_dist_urban_total)
        impr_water_src_dist_urban_percent = '{:,.1f}'.format(impr_water_src_dist_urban_percent)

        pipe_in_dw_reg_urban_total = '{:,}'.format(pipe_in_dw_reg_urban_total)
        pipe_in_dw_urban_total = '{:,}'.format(pipe_in_dw_urban_total)
        pipe_in_dw_urban_percent = '{:,.1f}'.format(pipe_in_dw_urban_percent)

        pipe_out_dw_on_cmp_reg_urban_total = '{:,}'.format(pipe_out_dw_on_cmp_reg_urban_total)
        pipe_out_dw_on_cmp_urban_total = '{:,}'.format(pipe_out_dw_on_cmp_urban_total)
        pipe_out_dw_on_cmp_urban_percent = '{:,.1f}'.format(pipe_out_dw_on_cmp_urban_percent)

        pipe_out_dw_on_neb_cmp_reg_urban_total = '{:,}'.format(pipe_out_dw_on_neb_cmp_reg_urban_total)
        pipe_out_dw_on_neb_cmp_urban_total = '{:,}'.format(pipe_out_dw_on_neb_cmp_urban_total)
        pipe_out_dw_on_neb_cmp_reg_urban_percent = '{:,.1f}'.format(pipe_out_dw_on_neb_cmp_reg_urban_percent)
        pipe_out_dw_on_neb_cmp_urban_percent = '{:,.1f}'.format(pipe_out_dw_on_neb_cmp_urban_percent)

        pipe_tap_stand_pipe_reg_urban_total = '{:,}'.format(pipe_tap_stand_pipe_reg_urban_total)
        pipe_tap_stand_pipe_urban_total = '{:,}'.format(pipe_tap_stand_pipe_urban_total)
        pipe_tap_stand_pipe_reg_urban_percent = '{:,.1f}'.format(pipe_tap_stand_pipe_reg_urban_percent)
        pipe_tap_stand_pipe_urban_percent = '{:,.1f}'.format(pipe_tap_stand_pipe_urban_percent)

        bore_hole_tube_well_reg_urban_total = '{:,}'.format(bore_hole_tube_well_reg_urban_total)
        bore_hole_tube_well_urban_total = '{:,}'.format(bore_hole_tube_well_urban_total)
        bore_hole_tube_well_reg_urban_percent = '{:,.1f}'.format(bore_hole_tube_well_reg_urban_percent)
        bore_hole_tube_well_urban_percent = '{:,.1f}'.format(bore_hole_tube_well_urban_percent)

        protected_well_reg_urban_total = '{:,}'.format(protected_well_reg_urban_total)
        protected_well_urban_total = '{:,}'.format(protected_well_urban_total)
        protected_well_reg_urban_percent = '{:,.1f}'.format(protected_well_reg_urban_percent)
        protected_well_urban_percent = '{:,.1f}'.format(protected_well_urban_percent)

        rain_water_reg_urban_total = '{:,}'.format(rain_water_reg_urban_total)
        rain_water_urban_total = '{:,}'.format(rain_water_urban_total)
        rain_water_reg_urban_percent = '{:,.1f}'.format(rain_water_reg_urban_percent)
        rain_water_urban_percent = '{:,.1f}'.format(rain_water_urban_percent)

        protected_spring_reg_urban_total = '{:,}'.format(protected_spring_reg_urban_total)
        protected_spring_urban_total = '{:,}'.format(protected_spring_urban_total)
        protected_spring_reg_urban_percent = '{:,.1f}'.format(protected_spring_reg_urban_percent)
        protected_spring_urban_percent = '{:,.1f}'.format(protected_spring_urban_percent)

        bottled_water_reg_urban_total = '{:,}'.format(bottled_water_reg_urban_total)
        bottled_water_urban_total = '{:,}'.format(bottled_water_urban_total)
        bottled_water_reg_urban_percent = '{:,.1f}'.format(bottled_water_reg_urban_percent)
        bottled_water_urban_percent = '{:,.1f}'.format(bottled_water_urban_percent)

        sachet_water_reg_urban_total = '{:,}'.format(sachet_water_reg_urban_total)
        sachet_water_urban_total = '{:,}'.format(sachet_water_urban_total)
        sachet_water_reg_urban_percent = '{:,.1f}'.format(sachet_water_reg_urban_percent)
        sachet_water_urban_percent = '{:,.1f}'.format(sachet_water_urban_percent)

    return impr_water_src_reg_urban_total, impr_water_src_reg_urban_percent, \
           impr_water_src_dist_urban_total, impr_water_src_dist_urban_percent, \
           pipe_in_dw_reg_urban_total, pipe_in_dw_reg_urban_percent, pipe_in_dw_urban_total, pipe_in_dw_urban_percent, \
           pipe_out_dw_on_cmp_reg_urban_total, pipe_out_dw_on_cmp_reg_urban_percent, pipe_out_dw_on_cmp_urban_total, pipe_out_dw_on_cmp_urban_percent, \
           pipe_out_dw_on_neb_cmp_reg_urban_total, pipe_out_dw_on_neb_cmp_reg_urban_percent, pipe_out_dw_on_neb_cmp_urban_total, pipe_out_dw_on_neb_cmp_urban_percent, \
           pipe_tap_stand_pipe_reg_urban_total, pipe_tap_stand_pipe_reg_urban_percent, pipe_tap_stand_pipe_urban_total, pipe_tap_stand_pipe_urban_percent, \
           bore_hole_tube_well_reg_urban_total, bore_hole_tube_well_reg_urban_percent, bore_hole_tube_well_urban_total, bore_hole_tube_well_urban_percent, \
           protected_well_reg_urban_total, protected_well_reg_urban_percent, protected_well_urban_total, protected_well_urban_percent, \
           rain_water_reg_urban_total, rain_water_reg_urban_percent, rain_water_urban_total, rain_water_urban_percent, \
           protected_spring_reg_urban_total, protected_spring_reg_urban_percent, protected_spring_urban_total, protected_spring_urban_percent, \
           bottled_water_reg_urban_total, bottled_water_reg_urban_percent, bottled_water_urban_total, bottled_water_urban_percent, \
           sachet_water_reg_urban_total, sachet_water_reg_urban_percent, sachet_water_urban_total, sachet_water_urban_percent

# Unimproved Water Sources - Urban
#*********************************

@app.callback(

Output('ws_unimpr_water_src_reg_urban_total', 'children'),
    Output('ws_unimpr_water_src_reg_urban_percent', 'children'),
    Output('ws_unimpr_water_src_dist_urban_total', 'children'),
    Output('ws_unimpr_water_src_dist_urban_percent', 'children'),

    # tanker
    Output('ws_tanker_vendor_reg_urban_total', 'children'),
    Output('ws_tanker_vendor_reg_urban_percent', 'children'),
    Output('ws_tanker_vendor_urban_total', 'children'),
    Output('ws_tanker_vendor_urban_percent', 'children'),

    # unprotected well
    Output('ws_unprotec_well_reg_urban_total', 'children'),
    Output('ws_unprotec_well_reg_urban_percent', 'children'),
    Output('ws_unprotec_well_urban_total','children'),
    Output('ws_unprotec_well_urban_percent', 'children'),

    # unprotected spring
    Output('unprotec_spring_reg_urban_total', 'children'),
    Output('unprotec_spring_reg_urban_percent', 'children'),
    Output('unprotec_spring_urban_total', 'children'),
    Output('unprotec_spring_urban_percent', 'children'),

    # river stream
    Output('river_stream_reg_urban_total', 'children'),
    Output('river_stream_reg_urban_percent', 'children'),
    Output('river_stream_urban_total', 'children'),
    Output('river_stream_urban_percent', 'children'),

    # Dugout/Pond/Lake/Dam/Canal
    Output('dugout_pond_lake_dam_canal_reg_urban_total', 'children'),
    Output('dugout_pond_lake_dam_canal_reg_urban_percent', 'children'),
    Output('dugout_pond_lake_dam_canal_urban_total', 'children'),
    Output('dugout_pond_lake_dam_canal_urban_percent', 'children'),

    Output('other_reg_urban_total', 'children'),
    Output('other_reg_urban_percent', 'children'),
    Output('other_urban_total', 'children'),
    Output('other_urban_percent', 'children'),

    Input('ws_region_dd', 'value'),
    Input('ws_district_dd', 'value')

)

def get_water_sanitation_unimpr_water_sources_urban(region, district):

    # ***********************************
    # ALL LOCALITIES - DISTRICT DETAILS
    # **********************************

    # Unimproved Water Sources
    unimpr_water_src_reg_urban_total = None
    unimpr_water_src_reg_urban_percent = None
    unimpr_water_src_dist_urban_total = None
    unimpr_water_src_dist_urban_percent = None

    tanker_vendor_reg_urban_total = None
    tanker_vendor_reg_urban_percent = None
    tanker_vendor_urban_total = None
    tanker_vendor_urban_percent = None

    unprotected_well_reg_urban_total = None
    unprotected_well_reg_urban_percent = None
    unprotected_well_urban_total = None
    unprotected_well_urban_percent = None

    unprotected_spring_reg_urban_total = None
    unprotected_spring_reg_urban_percent = None
    unprotected_spring_urban_total = None
    unprotected_spring_urban_percent = None

    river_stream_reg_urban_total = None
    river_stream_reg_urban_percent = None
    river_stream_urban_total = None
    river_stream_urban_percent = None

    dpld_canal_reg_urban_total = None
    dpld_canal_reg_urban_percent = None
    dpld_canal_urban_total = None
    dpld_canal_urban_percent = None

    other_reg_urban_total = None
    other_reg_urban_percent = None
    other_urban_total = None
    other_urban_percent = None

    if (region != None) & (district != None):

        # GET DATA
        df_data = df_water_sanitation_dic[region]

        df_urban = \
            df_data[
                (df_data['Water_Source'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'Urban')][
                ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]
        df_urban = df_urban.reset_index(drop=True)

        # District Total - URBAN
        urban_dist_total = df_urban[district][0]

        # Unimproved Water Resources - District Data, urban
        # **********************************************

        df_unimpr_water_src_dist_urban = df_data[(df_data['Category'] == 'A2') & (df_data['Type'] == 'Urban')][
            ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]

        # District Total
        df_unimpr_water_src_dist_urban_total = df_unimpr_water_src_dist_urban[
            df_unimpr_water_src_dist_urban['Status_Code'] == '2']
        df_unimpr_water_src_dist_urban_total = df_unimpr_water_src_dist_urban_total.reset_index(drop=True)

        unimpr_water_src_reg_urban_total = df_unimpr_water_src_dist_urban_total['Number'][0]
        unimpr_water_src_reg_urban_percent = df_unimpr_water_src_dist_urban_total['Percent'][0]
        unimpr_water_src_dist_urban_total = df_unimpr_water_src_dist_urban_total[district][0]
        unimpr_water_src_dist_urban_percent = (unimpr_water_src_dist_urban_total / urban_dist_total) * 100

        # Tanker supplied/Vendor provided
        df_tanker_vendor_reg_urban_total = df_unimpr_water_src_dist_urban[
            df_unimpr_water_src_dist_urban['Status_Code'] == '2-1']
        df_tanker_vendor_reg_urban_total = df_tanker_vendor_reg_urban_total.reset_index(drop=True)

        tanker_vendor_reg_urban_total = df_tanker_vendor_reg_urban_total['Number'][0]
        tanker_vendor_reg_urban_percent = df_tanker_vendor_reg_urban_total['Percent'][0]
        tanker_vendor_urban_total = df_tanker_vendor_reg_urban_total[district][0]
        tanker_vendor_urban_percent = (tanker_vendor_urban_total / unimpr_water_src_reg_urban_total) * 100

        # Unprotected well
        df_unprotected_well_reg_urban_total = df_unimpr_water_src_dist_urban[
            df_unimpr_water_src_dist_urban['Status_Code'] == '2-1']
        df_unprotected_well_reg_urban_total = df_unprotected_well_reg_urban_total.reset_index(drop=True)

        unprotected_well_reg_urban_total = df_unprotected_well_reg_urban_total['Number'][0]
        unprotected_well_reg_urban_percent = df_unprotected_well_reg_urban_total['Percent'][0]
        unprotected_well_urban_total = df_unprotected_well_reg_urban_total[district][0]
        unprotected_well_urban_percent = (unprotected_well_urban_total / unimpr_water_src_reg_urban_total) * 100

        # Unprotected spring
        df_unprotected_spring_reg_urban_total = df_unimpr_water_src_dist_urban[
            df_unimpr_water_src_dist_urban['Status_Code'] == '2-2']
        df_unprotected_spring_reg_urban_total = df_unprotected_spring_reg_urban_total.reset_index(drop=True)

        unprotected_spring_reg_urban_total = df_unprotected_spring_reg_urban_total['Number'][0]
        unprotected_spring_reg_urban_percent = df_unprotected_spring_reg_urban_total['Percent'][0]
        unprotected_spring_urban_total = df_unprotected_spring_reg_urban_total[district][0]
        unprotected_spring_urban_percent = (unprotected_spring_urban_total / unimpr_water_src_reg_urban_total) * 100

        # river stream
        df_river_stream_reg_urban_total = df_unimpr_water_src_dist_urban[
            df_unimpr_water_src_dist_urban['Status_Code'] == '2-3']
        df_river_stream_reg_urban_total = df_tanker_vendor_reg_urban_total.reset_index(drop=True)

        river_stream_reg_urban_total = df_river_stream_reg_urban_total['Number'][0]
        river_stream_reg_urban_percent = df_river_stream_reg_urban_total['Percent'][0]
        river_stream_urban_total = df_river_stream_reg_urban_total[district][0]
        river_stream_urban_percent = (river_stream_urban_total / unimpr_water_src_reg_urban_total) * 100

        # dugout, pond, lake, dam, canal
        df_dpld_canal_reg_urban_total = df_unimpr_water_src_dist_urban[
            df_unimpr_water_src_dist_urban['Status_Code'] == '2-3']
        df_dpld_canal_reg_urban_total = df_dpld_canal_reg_urban_total.reset_index(drop=True)

        dpld_canal_reg_urban_total = df_dpld_canal_reg_urban_total['Number'][0]
        dpld_canal_reg_urban_percent = df_dpld_canal_reg_urban_total['Percent'][0]
        dpld_canal_urban_total = df_dpld_canal_reg_urban_total[district][0]
        dpld_canal_urban_percent = (dpld_canal_urban_total / unimpr_water_src_reg_urban_total) * 100

        # other
        df_other_reg_urban_total = df_unimpr_water_src_dist_urban[
            df_unimpr_water_src_dist_urban['Status_Code'] == '2-4']
        df_other_reg_urban_total = df_other_reg_urban_total.reset_index(drop=True)

        other_reg_urban_total = df_other_reg_urban_total['Number'][0]
        other_reg_urban_percent = df_other_reg_urban_total['Percent'][0]
        other_urban_total = df_other_reg_urban_total[district][0]
        other_urban_percent = (other_urban_total / unimpr_water_src_reg_urban_total) * 100

        # Formatting
        unimpr_water_src_reg_urban_total = '{:,}'.format(unimpr_water_src_reg_urban_total)
        unimpr_water_src_reg_urban_percent = '{:,.1f}'.format(unimpr_water_src_reg_urban_percent)
        unimpr_water_src_dist_urban_total = '{:,}'.format(unimpr_water_src_dist_urban_total)
        unimpr_water_src_dist_urban_percent = '{:,.1f}'.format(unimpr_water_src_dist_urban_percent)

        tanker_vendor_reg_urban_total = '{:,}'.format(tanker_vendor_reg_urban_total)
        tanker_vendor_reg_urban_percent = '{:,.1f}'.format(tanker_vendor_reg_urban_percent)
        tanker_vendor_urban_total = '{:,}'.format(tanker_vendor_urban_total)
        tanker_vendor_urban_percent = '{:,.1f}'.format(tanker_vendor_urban_percent)

        unprotected_well_reg_urban_total = '{:,}'.format(unprotected_well_reg_urban_total)
        unprotected_well_reg_urban_percent = '{:,.1f}'.format(unprotected_well_reg_urban_percent)
        unprotected_well_urban_total = '{:,}'.format(unprotected_well_urban_total)
        unprotected_well_urban_percent = '{:,.1f}'.format(unprotected_well_urban_percent)

        unprotected_spring_reg_urban_total = '{:,}'.format(unprotected_spring_reg_urban_total)
        unprotected_spring_reg_urban_percent = '{:,.1f}'.format(unprotected_spring_reg_urban_percent)
        unprotected_spring_urban_total = '{:,}'.format(unprotected_spring_urban_total)
        unprotected_spring_urban_percent = '{:,.1f}'.format(unprotected_spring_urban_percent)

        river_stream_reg_urban_total = '{:,}'.format(river_stream_reg_urban_total)
        river_stream_reg_urban_percent = '{:,.1f}'.format(river_stream_reg_urban_percent)
        river_stream_urban_total = '{:,}'.format(river_stream_urban_total)
        river_stream_urban_percent = '{:,.1f}'.format(river_stream_urban_percent)

        dpld_canal_reg_urban_total = '{:,}'.format(dpld_canal_reg_urban_total)
        dpld_canal_reg_urban_percent = '{:,.1f}'.format(dpld_canal_reg_urban_percent)
        dpld_canal_urban_total = '{:,}'.format(dpld_canal_urban_total)
        dpld_canal_urban_percent = '{:,.1f}'.format(dpld_canal_urban_percent)

        other_reg_urban_total = '{:,}'.format(other_reg_urban_total)
        other_reg_urban_percent = '{:,.1f}'.format(other_reg_urban_percent)
        other_urban_total = '{:,}'.format(other_urban_total)
        other_urban_percent = '{:,.1f}'.format(other_urban_percent)

    return unimpr_water_src_reg_urban_total, unimpr_water_src_reg_urban_percent, \
           unimpr_water_src_dist_urban_total, unimpr_water_src_dist_urban_percent, \
           tanker_vendor_reg_urban_total, tanker_vendor_reg_urban_percent, tanker_vendor_urban_total, tanker_vendor_urban_percent, \
           unprotected_well_reg_urban_total, unprotected_well_reg_urban_percent, unprotected_well_urban_total, unprotected_well_urban_percent, \
           unprotected_spring_reg_urban_total, unprotected_spring_reg_urban_percent, unprotected_spring_urban_total, unprotected_spring_urban_percent, \
           river_stream_reg_urban_total, river_stream_reg_urban_percent, river_stream_urban_total, river_stream_urban_percent, \
           dpld_canal_reg_urban_total, dpld_canal_reg_urban_percent, dpld_canal_urban_total, dpld_canal_urban_percent, \
           other_reg_urban_total, other_reg_urban_percent, other_urban_total, other_urban_percent


#**************************************
# Water & Sanitation - RURAL
#**************************************
@app.callback(

    #*******
    # RURAL
    #*******

    # #ALL, IMPROVED WATER SOURCES
    #*****************************
    Output('ws_impr_water_src_reg_rural_total', 'children'),
    Output('ws_impr_water_src_reg_rural_percent', 'children'),
    Output('ws_impr_water_src_dist_rural_total', 'children'),
    Output('ws_impr_water_src_dist_rural_percent', 'children'),

    #Pipe-borne inside dwelling (district)
    Output('ws_pipe_in_dw_reg_rural_total', 'children'),
    Output('ws_pipe_in_dw_reg_rural_percent', 'children'),
    Output('ws_pipe_in_dw_rural_total', 'children'),
    Output('ws_pipe_in_dw_rural_percent', 'children'),

    #Pipe-borne outside dwelling but on compound (district)
    Output('ws_pipe_out_dw_on_cmd_reg_rural_total', 'children'),
    Output('ws_pipe_out_dw_on_cmd_reg_rural_percent', 'children'),
    Output('ws_pipe_out_dw_on_cmd_rural_total', 'children'),
    Output('ws_pipe_out_dw_on_cmd_rural_percent', 'children'),

    #Pipe-borne outside dwelling but on neighbor's compound (district)
    Output('ws_pipe_out_dw_on_neb_cmd_reg_rural_total', 'children'),
    Output('ws_pipe_out_dw_on_neb_cmd_reg_rural_percent', 'children'),
    Output('ws_pipe_out_dw_on_neb_cmd_rural_total', 'children'),
    Output('ws_pipe_out_dw_on_neb_cmd_rural_percent', 'children'),

    #Pipe-tap/Stand pipe (district)
    Output('ws_pipe_tap_stand_pipe_reg_rural_total', 'children'),
    Output('ws_pipe_tap_stand_pipe_reg_rural_percent', 'children'),
    Output('ws_pipe_tap_stand_pipe_rural_total', 'children'),
    Output('ws_pipe_tap_stand_pipe_rural_percent', 'children'),

    #Borehole/Tube well (district)
    Output('ws_bore_hole_tube_well_reg_rural_total', 'children'),
    Output('ws_bore_hole_tube_well_reg_rural_percent', 'children'),
    Output('ws_bore_hole_tube_well_rural_total', 'children'),
    Output('ws_bore_hole_tube_well_rural_percent', 'children'),

    #Protected well (district)
    Output('ws_protected_well_reg_rural_total', 'children'),
    Output('ws_protected_well_reg_rural_percent', 'children'),
    Output('ws_protected_well_rural_total', 'children'),
    Output('ws_protected_well_rural_percent', 'children'),

    #Rain water (district)
    Output('ws_rain_water_reg_rural_total', 'children'),
    Output('ws_rain_water_reg_rural_percent', 'children'),
    Output('ws_rain_water_rural_total', 'children'),
    Output('ws_rain_water_rural_percent', 'children'),

    #Protected spring (district)
    Output('ws_protected_spring_reg_rural_total', 'children'),
    Output('ws_protected_spring_reg_rural_percent', 'children'),
    Output('ws_protected_spring_rural_total', 'children'),
    Output('ws_protected_spring_rural_percent', 'children'),

    #Bottled Water (district)
    Output('ws_bottled_water_reg_rural_total', 'children'),
    Output('ws_bottled_water_reg_rural_percent', 'children'),
    Output('ws_bottled_water_rural_total', 'children'),
    Output('ws_bottled_water_rural_percent', 'children'),

    #Sachet Water (district)
    Output('ws_sachet_water_reg_rural_total', 'children'),
    Output('ws_sachet_water_reg_rural_percent', 'children'),
    Output('ws_sachet_water_rural_total', 'children'),
    Output('ws_sachet_water_rural_percent', 'children'),

    Input('ws_region_dd', 'value'),
    Input('ws_district_dd', 'value')

)
def get_water_sanitation_impr_water_sources_rural(region, district):

    # Improved Water Resources - District Data, Rural
    # **********************************************

    impr_water_src_reg_rural_total = None
    impr_water_src_reg_rural_percent = None
    impr_water_src_dist_rural_total = None
    impr_water_src_dist_rural_percent = None

    pipe_in_dw_reg_rural_total = None
    pipe_in_dw_rural_total = None
    pipe_in_dw_reg_rural_percent = None
    pipe_in_dw_rural_percent = None

    pipe_out_dw_on_cmp_reg_rural_total = None
    pipe_out_dw_on_cmp_rural_total = None
    pipe_out_dw_on_cmp_reg_rural_percent = None
    pipe_out_dw_on_cmp_rural_percent = None

    pipe_out_dw_on_neb_cmp_reg_rural_total = None
    pipe_out_dw_on_neb_cmp_rural_total = None
    pipe_out_dw_on_neb_cmp_reg_rural_percent = None
    pipe_out_dw_on_neb_cmp_rural_percent = None

    pipe_tap_stand_pipe_reg_rural_total = None
    pipe_tap_stand_pipe_rural_total = None
    pipe_tap_stand_pipe_reg_rural_percent = None
    pipe_tap_stand_pipe_rural_percent = None

    bore_hole_tube_well_reg_rural_total = None
    bore_hole_tube_well_rural_total = None
    bore_hole_tube_well_reg_rural_percent = None
    bore_hole_tube_well_rural_percent = None

    protected_well_reg_rural_total = None
    protected_well_rural_total = None
    protected_well_reg_rural_percent = None
    protected_well_rural_percent = None

    rain_water_reg_rural_total = None
    rain_water_rural_total = None
    rain_water_reg_rural_percent = None
    rain_water_rural_percent = None

    protected_spring_reg_rural_total = None
    protected_spring_rural_total = None
    protected_spring_reg_rural_percent = None
    protected_spring_rural_percent = None

    bottled_water_reg_rural_total = None
    bottled_water_rural_total = None
    bottled_water_reg_rural_percent = None
    bottled_water_rural_percent = None

    sachet_water_reg_rural_total = None
    sachet_water_rural_total = None
    sachet_water_reg_rural_percent = None
    sachet_water_rural_percent = None

    if (region != None) & (district != None):

        # GET DATA
        df_data = df_water_sanitation_dic[region]

        df_rural = df_data[(df_data['Water_Source'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'Rural')][
                     ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]
        df_rural = df_rural.reset_index(drop=True)

        # format
        rural_reg_total = df_rural['Number'][0]
        rural_reg_percent = 100.0
        rural_dist_total = df_rural[district][0]


        df_impr_water_src_dist_rural = df_data[(df_data['Category'] == 'A1') & (df_data['Type'] == 'Rural')][
            ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]

        # District Total
        df_impr_water_src_dist_rural_total = df_impr_water_src_dist_rural[
            df_impr_water_src_dist_rural['Status_Code'] == '1']
        df_impr_water_src_dist_rural_total = df_impr_water_src_dist_rural_total.reset_index(drop=True)

        impr_water_src_reg_rural_total = df_impr_water_src_dist_rural_total['Number'][0]
        impr_water_src_reg_rural_percent = df_impr_water_src_dist_rural_total['Percent'][0]
        impr_water_src_dist_rural_total = df_impr_water_src_dist_rural_total[district][0]
        impr_water_src_dist_rural_percent = (impr_water_src_dist_rural_total / rural_dist_total) * 100

        # Pipe-borne inside dwelling
        df_pipe_in_dw_rural_total = df_impr_water_src_dist_rural[df_impr_water_src_dist_rural['Status_Code'] == '1-1']
        df_pipe_in_dw_rural_total = df_pipe_in_dw_rural_total.reset_index(drop=True)

        pipe_in_dw_reg_rural_total = df_pipe_in_dw_rural_total['Number'][0]
        pipe_in_dw_rural_total = df_pipe_in_dw_rural_total[district][0]
        pipe_in_dw_reg_rural_percent = df_pipe_in_dw_rural_total['Percent'][0]
        pipe_in_dw_rural_percent = (pipe_in_dw_rural_total / impr_water_src_dist_rural_total) * 100

        # Pipe-borne outside dwelling but on compound
        df_pipe_out_dw_on_cmp_rural_total = df_impr_water_src_dist_rural[
            df_impr_water_src_dist_rural['Status_Code'] == '1-2']
        df_pipe_out_dw_on_cmp_rural_total = df_pipe_out_dw_on_cmp_rural_total.reset_index(drop=True)

        pipe_out_dw_on_cmp_reg_rural_total = df_pipe_out_dw_on_cmp_rural_total['Number'][0]
        pipe_out_dw_on_cmp_rural_total = df_pipe_out_dw_on_cmp_rural_total[district][0]
        pipe_out_dw_on_cmp_reg_rural_percent = df_pipe_out_dw_on_cmp_rural_total['Percent'][0]
        pipe_out_dw_on_cmp_rural_percent = (pipe_out_dw_on_cmp_rural_total / impr_water_src_dist_rural_total) * 100

        # Pipe-borne outside dwelling but on neighbor's compound
        df_pipe_out_dw_on_neb_cmp_rural_total = df_impr_water_src_dist_rural[
            df_impr_water_src_dist_rural['Status_Code'] == '1-3']
        df_pipe_out_dw_on_neb_cmp_rural_total = df_pipe_out_dw_on_neb_cmp_rural_total.reset_index(drop=True)

        pipe_out_dw_on_neb_cmp_reg_rural_total = df_pipe_out_dw_on_neb_cmp_rural_total['Number'][0]
        pipe_out_dw_on_neb_cmp_rural_total = df_pipe_out_dw_on_neb_cmp_rural_total[district][0]
        pipe_out_dw_on_neb_cmp_reg_rural_percent = df_pipe_out_dw_on_neb_cmp_rural_total['Percent'][0]
        pipe_out_dw_on_neb_cmp_rural_percent = (pipe_out_dw_on_neb_cmp_rural_total / impr_water_src_dist_rural_total) * 100

        # Pipe tap / Stand Pipe
        df_pipe_tap_stand_pipe_rural_total = df_impr_water_src_dist_rural[
            df_impr_water_src_dist_rural['Status_Code'] == '1-4']
        df_pipe_tap_stand_pipe_rural_total = df_pipe_tap_stand_pipe_rural_total.reset_index(drop=True)

        pipe_tap_stand_pipe_reg_rural_total = df_pipe_tap_stand_pipe_rural_total['Number'][0]
        pipe_tap_stand_pipe_rural_total = df_pipe_tap_stand_pipe_rural_total[district][0]
        pipe_tap_stand_pipe_reg_rural_percent = df_pipe_tap_stand_pipe_rural_total['Percent'][0]
        pipe_tap_stand_pipe_rural_percent = (pipe_tap_stand_pipe_rural_total / impr_water_src_dist_rural_total) * 100

        # Borehole / Tube well
        df_bore_hole_tube_well_rural_total = df_impr_water_src_dist_rural[
            df_impr_water_src_dist_rural['Status_Code'] == '1-5']
        df_bore_hole_tube_well_rural_total = df_bore_hole_tube_well_rural_total.reset_index(drop=True)

        bore_hole_tube_well_reg_rural_total = df_bore_hole_tube_well_rural_total['Number'][0]
        bore_hole_tube_well_rural_total = df_bore_hole_tube_well_rural_total[district][0]
        bore_hole_tube_well_reg_rural_percent = df_bore_hole_tube_well_rural_total['Percent'][0]
        bore_hole_tube_well_rural_percent = (bore_hole_tube_well_rural_total / impr_water_src_dist_rural_total) * 100

        # Protected well
        df_protected_well_rural_total = df_impr_water_src_dist_rural[df_impr_water_src_dist_rural['Status_Code'] == '1-6']
        df_protected_well_rural_total = df_protected_well_rural_total.reset_index(drop=True)

        protected_well_reg_rural_total = df_protected_well_rural_total['Number'][0]
        protected_well_rural_total = df_protected_well_rural_total[district][0]
        protected_well_reg_rural_percent = df_protected_well_rural_total['Percent'][0]
        protected_well_rural_percent = (protected_well_rural_total / impr_water_src_dist_rural_total) * 100

        # Rain water
        df_rain_water_rural_total = df_impr_water_src_dist_rural[df_impr_water_src_dist_rural['Status_Code'] == '1-7']
        df_rain_water_rural_total = df_rain_water_rural_total.reset_index(drop=True)

        rain_water_reg_rural_total = df_rain_water_rural_total['Number'][0]
        rain_water_rural_total = df_rain_water_rural_total[district][0]
        rain_water_reg_rural_percent = df_rain_water_rural_total['Percent'][0]
        rain_water_rural_percent = (rain_water_rural_total / impr_water_src_dist_rural_total) * 100

        # Protected spring
        df_protected_spring_rural_total = df_impr_water_src_dist_rural[df_impr_water_src_dist_rural['Status_Code'] == '1-8']
        df_protected_spring_rural_total = df_protected_spring_rural_total.reset_index(drop=True)

        protected_spring_reg_rural_total = df_protected_spring_rural_total['Number'][0]
        protected_spring_rural_total = df_protected_spring_rural_total[district][0]
        protected_spring_reg_rural_percent = df_protected_spring_rural_total['Percent'][0]
        protected_spring_rural_percent = (protected_spring_rural_total / impr_water_src_dist_rural_total) * 100

        # Bottled water
        df_bottled_water_rural_total = df_impr_water_src_dist_rural[df_impr_water_src_dist_rural['Status_Code'] == '1-9']
        df_bottled_water_rural_total = df_bottled_water_rural_total.reset_index(drop=True)

        bottled_water_reg_rural_total = df_bottled_water_rural_total['Number'][0]
        bottled_water_rural_total = df_bottled_water_rural_total[district][0]
        bottled_water_reg_rural_percent = df_bottled_water_rural_total['Percent'][0]
        bottled_water_rural_percent = (bottled_water_rural_total / impr_water_src_dist_rural_total) * 100

        # Sachet water
        df_sachet_water_rural_total = df_impr_water_src_dist_rural[df_impr_water_src_dist_rural['Status_Code'] == '1-10']
        df_sachet_water_rural_total = df_sachet_water_rural_total.reset_index(drop=True)

        sachet_water_reg_rural_total = df_sachet_water_rural_total['Number'][0]
        sachet_water_rural_total = df_sachet_water_rural_total[district][0]
        sachet_water_reg_rural_percent = df_sachet_water_rural_total['Percent'][0]
        sachet_water_rural_percent = (sachet_water_rural_total / impr_water_src_dist_rural_total) * 100

        impr_water_src_reg_rural_total = '{:,}'.format(impr_water_src_reg_rural_total)
        impr_water_src_reg_rural_percent = '{:.1f}'.format(impr_water_src_reg_rural_percent)
        impr_water_src_dist_rural_total = '{:,}'.format(impr_water_src_dist_rural_total)
        impr_water_src_dist_rural_percent = '{:,.1f}'.format(impr_water_src_dist_rural_percent)

        pipe_in_dw_reg_rural_total = '{:,}'.format(pipe_in_dw_reg_rural_total)
        pipe_in_dw_rural_total = '{:,}'.format(pipe_in_dw_rural_total)
        pipe_in_dw_rural_percent = '{:,.1f}'.format(pipe_in_dw_rural_percent)

        pipe_out_dw_on_cmp_reg_rural_total = '{:,}'.format(pipe_out_dw_on_cmp_reg_rural_total)
        pipe_out_dw_on_cmp_rural_total = '{:,}'.format(pipe_out_dw_on_cmp_rural_total)
        pipe_out_dw_on_cmp_rural_percent = '{:,.1f}'.format(pipe_out_dw_on_cmp_rural_percent)

        pipe_out_dw_on_neb_cmp_reg_rural_total = '{:,}'.format(pipe_out_dw_on_neb_cmp_reg_rural_total)
        pipe_out_dw_on_neb_cmp_rural_total = '{:,}'.format(pipe_out_dw_on_neb_cmp_rural_total)
        pipe_out_dw_on_neb_cmp_reg_rural_percent = '{:,.1f}'.format(pipe_out_dw_on_neb_cmp_reg_rural_percent)
        pipe_out_dw_on_neb_cmp_rural_percent = '{:,.1f}'.format(pipe_out_dw_on_neb_cmp_rural_percent)

        pipe_tap_stand_pipe_reg_rural_total = '{:,}'.format(pipe_tap_stand_pipe_reg_rural_total)
        pipe_tap_stand_pipe_rural_total = '{:,}'.format(pipe_tap_stand_pipe_rural_total)
        pipe_tap_stand_pipe_reg_rural_percent = '{:,.1f}'.format(pipe_tap_stand_pipe_reg_rural_percent)
        pipe_tap_stand_pipe_rural_percent = '{:,.1f}'.format(pipe_tap_stand_pipe_rural_percent)

        bore_hole_tube_well_reg_rural_total = '{:,}'.format(bore_hole_tube_well_reg_rural_total)
        bore_hole_tube_well_rural_total = '{:,}'.format(bore_hole_tube_well_rural_total)
        bore_hole_tube_well_reg_rural_percent = '{:,.1f}'.format(bore_hole_tube_well_reg_rural_percent)
        bore_hole_tube_well_rural_percent = '{:,.1f}'.format(bore_hole_tube_well_rural_percent)

        protected_well_reg_rural_total = '{:,}'.format(protected_well_reg_rural_total)
        protected_well_rural_total = '{:,}'.format(protected_well_rural_total)
        protected_well_reg_rural_percent = '{:,.1f}'.format(protected_well_reg_rural_percent)
        protected_well_rural_percent = '{:,.1f}'.format(protected_well_rural_percent)

        rain_water_reg_rural_total = '{:,}'.format(rain_water_reg_rural_total)
        rain_water_rural_total = '{:,}'.format(rain_water_rural_total)
        rain_water_reg_rural_percent = '{:,.1f}'.format(rain_water_reg_rural_percent)
        rain_water_rural_percent = '{:,.1f}'.format(rain_water_rural_percent)

        protected_spring_reg_rural_total = '{:,}'.format(protected_spring_reg_rural_total)
        protected_spring_rural_total = '{:,}'.format(protected_spring_rural_total)
        protected_spring_reg_rural_percent = '{:,.1f}'.format(protected_spring_reg_rural_percent)
        protected_spring_rural_percent = '{:,.1f}'.format(protected_spring_rural_percent)

        bottled_water_reg_rural_total = '{:,}'.format(bottled_water_reg_rural_total)
        bottled_water_rural_total = '{:,}'.format(bottled_water_rural_total)
        bottled_water_reg_rural_percent = '{:,.1f}'.format(bottled_water_reg_rural_percent)
        bottled_water_rural_percent = '{:,.1f}'.format(bottled_water_rural_percent)

        sachet_water_reg_rural_total = '{:,}'.format(sachet_water_reg_rural_total)
        sachet_water_rural_total = '{:,}'.format(sachet_water_rural_total)
        sachet_water_reg_rural_percent = '{:,.1f}'.format(sachet_water_reg_rural_percent)
        sachet_water_rural_percent = '{:,.1f}'.format(sachet_water_rural_percent)

    return impr_water_src_reg_rural_total, impr_water_src_reg_rural_percent, \
           impr_water_src_dist_rural_total, impr_water_src_dist_rural_percent, \
           pipe_in_dw_reg_rural_total, pipe_in_dw_reg_rural_percent, pipe_in_dw_rural_total, pipe_in_dw_rural_percent, \
           pipe_out_dw_on_cmp_reg_rural_total, pipe_out_dw_on_cmp_reg_rural_percent, pipe_out_dw_on_cmp_rural_total, pipe_out_dw_on_cmp_rural_percent, \
           pipe_out_dw_on_neb_cmp_reg_rural_total, pipe_out_dw_on_neb_cmp_reg_rural_percent, pipe_out_dw_on_neb_cmp_rural_total, pipe_out_dw_on_neb_cmp_rural_percent, \
           pipe_tap_stand_pipe_reg_rural_total, pipe_tap_stand_pipe_reg_rural_percent, pipe_tap_stand_pipe_rural_total, pipe_tap_stand_pipe_rural_percent, \
           bore_hole_tube_well_reg_rural_total, bore_hole_tube_well_reg_rural_percent, bore_hole_tube_well_rural_total, bore_hole_tube_well_rural_percent, \
           protected_well_reg_rural_total, protected_well_reg_rural_percent, protected_well_rural_total, protected_well_rural_percent, \
           rain_water_reg_rural_total, rain_water_reg_rural_percent, rain_water_rural_total, rain_water_rural_percent, \
           protected_spring_reg_rural_total, protected_spring_reg_rural_percent, protected_spring_rural_total, protected_spring_rural_percent, \
           bottled_water_reg_rural_total, bottled_water_reg_rural_percent, bottled_water_rural_total, bottled_water_rural_percent, \
           sachet_water_reg_rural_total, sachet_water_reg_rural_percent, sachet_water_rural_total, sachet_water_rural_percent




# Unimproved Water Sources - Rural
#*********************************

@app.callback(

Output('ws_unimpr_water_src_reg_rural_total', 'children'),
    Output('ws_unimpr_water_src_reg_rural_percent', 'children'),
    Output('ws_unimpr_water_src_dist_rural_total', 'children'),
    Output('ws_unimpr_water_src_dist_rural_percent', 'children'),

    # tanker
    Output('ws_tanker_vendor_reg_rural_total', 'children'),
    Output('ws_tanker_vendor_reg_rural_percent', 'children'),
    Output('ws_tanker_vendor_rural_total', 'children'),
    Output('ws_tanker_vendor_rural_percent', 'children'),

    # unprotected well
    Output('ws_unprotec_well_reg_rural_total', 'children'),
    Output('ws_unprotec_well_reg_rural_percent', 'children'),
    Output('ws_unprotec_well_rural_total','children'),
    Output('ws_unprotec_well_rural_percent', 'children'),

    # unprotected spring
    Output('unprotec_spring_reg_rural_total', 'children'),
    Output('unprotec_spring_reg_rural_percent', 'children'),
    Output('unprotec_spring_rural_total', 'children'),
    Output('unprotec_spring_rural_percent', 'children'),

    # river stream
    Output('river_stream_reg_rural_total', 'children'),
    Output('river_stream_reg_rural_percent', 'children'),
    Output('river_stream_rural_total', 'children'),
    Output('river_stream_rural_percent', 'children'),

    # Dugout/Pond/Lake/Dam/Canal
    Output('dugout_pond_lake_dam_canal_reg_rural_total', 'children'),
    Output('dugout_pond_lake_dam_canal_reg_rural_percent', 'children'),
    Output('dugout_pond_lake_dam_canal_rural_total', 'children'),
    Output('dugout_pond_lake_dam_canal_rural_percent', 'children'),

    Output('other_reg_rural_total', 'children'),
    Output('other_reg_rural_percent', 'children'),
    Output('other_rural_total', 'children'),
    Output('other_rural_percent', 'children'),

    Input('ws_region_dd', 'value'),
    Input('ws_district_dd', 'value')
)
def get_water_sanitation_unimpr_water_sources_rural(region, district):

    # ***********************************
    # ALL LOCALITIES - DISTRICT DETAILS
    # **********************************

    # Unimproved Water Sources
    unimpr_water_src_reg_rural_total = None
    unimpr_water_src_reg_rural_percent = None
    unimpr_water_src_dist_rural_total = None
    unimpr_water_src_dist_rural_percent = None

    tanker_vendor_reg_rural_total = None
    tanker_vendor_reg_rural_percent = None
    tanker_vendor_rural_total = None
    tanker_vendor_rural_percent = None

    unprotected_well_reg_rural_total = None
    unprotected_well_reg_rural_percent = None
    unprotected_well_rural_total = None
    unprotected_well_rural_percent = None

    unprotected_spring_reg_rural_total = None
    unprotected_spring_reg_rural_percent = None
    unprotected_spring_rural_total = None
    unprotected_spring_rural_percent = None

    river_stream_reg_rural_total = None
    river_stream_reg_rural_percent = None
    river_stream_rural_total = None
    river_stream_rural_percent = None

    dpld_canal_reg_rural_total = None
    dpld_canal_reg_rural_percent = None
    dpld_canal_rural_total = None
    dpld_canal_rural_percent = None

    other_reg_rural_total = None
    other_reg_rural_percent = None
    other_rural_total = None
    other_rural_percent = None

    if (region != None) & (district != None):

        # GET DATA
        df_data = df_water_sanitation_dic[region]

        df_rural = \
            df_data[
                (df_data['Water_Source'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'Rural')][
                ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]
        df_rural = df_rural.reset_index(drop=True)

        # District Total - RURAL
        rural_dist_total = df_rural[district][0]

        # Unimproved Water Resources - District Data, rural
        # **********************************************

        df_unimpr_water_src_dist_rural = df_data[(df_data['Category'] == 'A2') & (df_data['Type'] == 'Rural')][
            ['Type', 'Status_Code', 'Category', 'Water_Source', 'Number', 'Percent', district]]

        # District Total
        df_unimpr_water_src_dist_rural_total = df_unimpr_water_src_dist_rural[
            df_unimpr_water_src_dist_rural['Status_Code'] == '2']
        df_unimpr_water_src_dist_rural_total = df_unimpr_water_src_dist_rural_total.reset_index(drop=True)

        unimpr_water_src_reg_rural_total = df_unimpr_water_src_dist_rural_total['Number'][0]
        unimpr_water_src_reg_rural_percent = df_unimpr_water_src_dist_rural_total['Percent'][0]
        unimpr_water_src_dist_rural_total = df_unimpr_water_src_dist_rural_total[district][0]
        unimpr_water_src_dist_rural_percent = (unimpr_water_src_dist_rural_total / rural_dist_total) * 100

        # Tanker supplied/Vendor provided
        df_tanker_vendor_reg_rural_total = df_unimpr_water_src_dist_rural[
            df_unimpr_water_src_dist_rural['Status_Code'] == '2-1']
        df_tanker_vendor_reg_rural_total = df_tanker_vendor_reg_rural_total.reset_index(drop=True)

        tanker_vendor_reg_rural_total = df_tanker_vendor_reg_rural_total['Number'][0]
        tanker_vendor_reg_rural_percent = df_tanker_vendor_reg_rural_total['Percent'][0]
        tanker_vendor_rural_total = df_tanker_vendor_reg_rural_total[district][0]
        tanker_vendor_rural_percent = (tanker_vendor_rural_total / unimpr_water_src_reg_rural_total) * 100

        # Unprotected well
        df_unprotected_well_reg_rural_total = df_unimpr_water_src_dist_rural[
            df_unimpr_water_src_dist_rural['Status_Code'] == '2-1']
        df_unprotected_well_reg_rural_total = df_unprotected_well_reg_rural_total.reset_index(drop=True)

        unprotected_well_reg_rural_total = df_unprotected_well_reg_rural_total['Number'][0]
        unprotected_well_reg_rural_percent = df_unprotected_well_reg_rural_total['Percent'][0]
        unprotected_well_rural_total = df_unprotected_well_reg_rural_total[district][0]
        unprotected_well_rural_percent = (unprotected_well_rural_total / unimpr_water_src_reg_rural_total) * 100

        # Unprotected spring
        df_unprotected_spring_reg_rural_total = df_unimpr_water_src_dist_rural[
            df_unimpr_water_src_dist_rural['Status_Code'] == '2-2']
        df_unprotected_spring_reg_rural_total = df_unprotected_spring_reg_rural_total.reset_index(drop=True)

        unprotected_spring_reg_rural_total = df_unprotected_spring_reg_rural_total['Number'][0]
        unprotected_spring_reg_rural_percent = df_unprotected_spring_reg_rural_total['Percent'][0]
        unprotected_spring_rural_total = df_unprotected_spring_reg_rural_total[district][0]
        unprotected_spring_rural_percent = (unprotected_spring_rural_total / unimpr_water_src_reg_rural_total) * 100

        # river stream
        df_river_stream_reg_rural_total = df_unimpr_water_src_dist_rural[
            df_unimpr_water_src_dist_rural['Status_Code'] == '2-3']
        df_river_stream_reg_rural_total = df_tanker_vendor_reg_rural_total.reset_index(drop=True)

        river_stream_reg_rural_total = df_river_stream_reg_rural_total['Number'][0]
        river_stream_reg_rural_percent = df_river_stream_reg_rural_total['Percent'][0]
        river_stream_rural_total = df_river_stream_reg_rural_total[district][0]
        river_stream_rural_percent = (river_stream_rural_total / unimpr_water_src_reg_rural_total) * 100

        # dugout, pond, lake, dam, canal
        df_dpld_canal_reg_rural_total = df_unimpr_water_src_dist_rural[
            df_unimpr_water_src_dist_rural['Status_Code'] == '2-3']
        df_dpld_canal_reg_rural_total = df_dpld_canal_reg_rural_total.reset_index(drop=True)

        dpld_canal_reg_rural_total = df_dpld_canal_reg_rural_total['Number'][0]
        dpld_canal_reg_rural_percent = df_dpld_canal_reg_rural_total['Percent'][0]
        dpld_canal_rural_total = df_dpld_canal_reg_rural_total[district][0]
        dpld_canal_rural_percent = (dpld_canal_rural_total / unimpr_water_src_reg_rural_total) * 100

        # other
        df_other_reg_rural_total = df_unimpr_water_src_dist_rural[
            df_unimpr_water_src_dist_rural['Status_Code'] == '2-4']
        df_other_reg_rural_total = df_other_reg_rural_total.reset_index(drop=True)

        other_reg_rural_total = df_other_reg_rural_total['Number'][0]
        other_reg_rural_percent = df_other_reg_rural_total['Percent'][0]
        other_rural_total = df_other_reg_rural_total[district][0]
        other_rural_percent = (other_rural_total / unimpr_water_src_reg_rural_total) * 100

        # Formatting
        unimpr_water_src_reg_rural_total = '{:,}'.format(unimpr_water_src_reg_rural_total)
        unimpr_water_src_reg_rural_percent = '{:,.1f}'.format(unimpr_water_src_reg_rural_percent)
        unimpr_water_src_dist_rural_total = '{:,}'.format(unimpr_water_src_dist_rural_total)
        unimpr_water_src_dist_rural_percent = '{:,.1f}'.format(unimpr_water_src_dist_rural_percent)

        tanker_vendor_reg_rural_total = '{:,}'.format(tanker_vendor_reg_rural_total)
        tanker_vendor_reg_rural_percent = '{:,.1f}'.format(tanker_vendor_reg_rural_percent)
        tanker_vendor_rural_total = '{:,}'.format(tanker_vendor_rural_total)
        tanker_vendor_rural_percent = '{:,.1f}'.format(tanker_vendor_rural_percent)

        unprotected_well_reg_rural_total = '{:,}'.format(unprotected_well_reg_rural_total)
        unprotected_well_reg_rural_percent = '{:,.1f}'.format(unprotected_well_reg_rural_percent)
        unprotected_well_rural_total = '{:,}'.format(unprotected_well_rural_total)
        unprotected_well_rural_percent = '{:,.1f}'.format(unprotected_well_rural_percent)

        unprotected_spring_reg_rural_total = '{:,}'.format(unprotected_spring_reg_rural_total)
        unprotected_spring_reg_rural_percent = '{:,.1f}'.format(unprotected_spring_reg_rural_percent)
        unprotected_spring_rural_total = '{:,}'.format(unprotected_spring_rural_total)
        unprotected_spring_rural_percent = '{:,.1f}'.format(unprotected_spring_rural_percent)

        river_stream_reg_rural_total = '{:,}'.format(river_stream_reg_rural_total)
        river_stream_reg_rural_percent = '{:,.1f}'.format(river_stream_reg_rural_percent)
        river_stream_rural_total = '{:,}'.format(river_stream_rural_total)
        river_stream_rural_percent = '{:,.1f}'.format(river_stream_rural_percent)

        dpld_canal_reg_rural_total = '{:,}'.format(dpld_canal_reg_rural_total)
        dpld_canal_reg_rural_percent = '{:,.1f}'.format(dpld_canal_reg_rural_percent)
        dpld_canal_rural_total = '{:,}'.format(dpld_canal_rural_total)
        dpld_canal_rural_percent = '{:,.1f}'.format(dpld_canal_rural_percent)

        other_reg_rural_total = '{:,}'.format(other_reg_rural_total)
        other_reg_rural_percent = '{:,.1f}'.format(other_reg_rural_percent)
        other_rural_total = '{:,}'.format(other_rural_total)
        other_rural_percent = '{:,.1f}'.format(other_rural_percent)

    return unimpr_water_src_reg_rural_total, unimpr_water_src_reg_rural_percent, \
           unimpr_water_src_dist_rural_total, unimpr_water_src_dist_rural_percent, \
           tanker_vendor_reg_rural_total, tanker_vendor_reg_rural_percent, tanker_vendor_rural_total, tanker_vendor_rural_percent, \
           unprotected_well_reg_rural_total, unprotected_well_reg_rural_percent, unprotected_well_rural_total, unprotected_well_rural_percent, \
           unprotected_spring_reg_rural_total, unprotected_spring_reg_rural_percent, unprotected_spring_rural_total, unprotected_spring_rural_percent, \
           river_stream_reg_rural_total, river_stream_reg_rural_percent, river_stream_rural_total, river_stream_rural_percent, \
           dpld_canal_reg_rural_total, dpld_canal_reg_rural_percent, dpld_canal_rural_total, dpld_canal_rural_percent, \
           other_reg_rural_total, other_reg_rural_percent, other_rural_total, other_rural_percent


#***************************************
# ALL, UNIMPROVED WATER SOURCES
#***************************************

@app.callback(

    #Total
    Output('struct_reg_all_total', 'children'),
    Output('struct_reg_all_percent', 'children'),
    Output('struct_all_total', 'children'),
    Output('struct_all_percent', 'children'),

    # #Fully completed:
    Output('struct_fully_compl_reg_all_val', 'children'),
    Output('struct_fully_compl_reg_all_percent', 'children'),
    Output('struct_fully_compl_all_val', 'children'),
    Output('struct_fully_compl_all_percent', 'children'),

    #
    #Completely roofed but uncompleted:
    Output('struct_compl_roofed_uncom_reg_all_val', 'children'),
    Output('struct_compl_roofed_uncom_reg_all_percent', 'children'),
    Output('struct_compl_roofed_uncom_all_val', 'children'),
    Output('struct_compl_roofed_uncom_all_percent', 'children'),

    #
    #Partially roofed:
    Output('struct_part_roofed_reg_all_val', 'children'),
    Output('struct_part_roofed_reg_all_percent', 'children'),
    Output('struct_part_roofed_all_val', 'children'),
    Output('struct_part_roofed_all_percent', 'children'),

    #
    # #Roofing level [with improvised roof
    Output('struct_roof_lvl_improv_reg_all_val', 'children'),
    Output('struct_roof_lvl_improv_reg_all_percent', 'children'),
    Output('struct_roof_lvl_improv_all_val', 'children'),
    Output('struct_roof_lvl_improv_all_percent', 'children'),
    #
    # #Lintel level [with improvised roof]
    Output('struct_lintel_improv_reg_all_val','children'),
    Output('struct_lintel_improv_reg_all_percent', 'children'),
    Output('struct_lintel_improv_all_val','children'),
    Output('struct_lintel_improv_all_percent', 'children'),
    #
    # #Roofing level [without roof]
    Output('struct_roof_lvl_wout_roof_reg_all_val', 'children'),
    Output('struct_roof_lvl_wout_roof_reg_all_percent', 'children'),
    Output('struct_roof_lvl_wout_roof_all_val', 'children'),
    Output('struct_roof_lvl_wout_roof_all_percent', 'children'),
    #
    # #Lintel level [without roof]
    Output('struct_lintel_wout_roof_reg_all_val', 'children'),
    Output('struct_lintel_wout_roof_reg_all_percent', 'children'),
    Output('struct_lintel_wout_roof_all_val', 'children'),
    Output('struct_lintel_wout_roof_all_percent', 'children'),

    #
    #Window level
    Output('struct_window_lvl_reg_all_val', 'children'),
    Output('struct_window_lvl_reg_all_percent', 'children'),
    Output('struct_window_lvl_all_val', 'children'),
    Output('struct_window_lvl_all_percent', 'children'),

    #Concrete/Metal Pillars level
    Output('struct_concr_metal_pill_lvl_reg_all_val', 'children'),
    Output('struct_concr_metal_pill_lvl_reg_all_percent', 'children'),
    Output('struct_concr_metal_pill_lvl_all_val', 'children'),
    Output('struct_concr_metal_pill_lvl_all_percent', 'children'),

    Input('struct_region_dd', 'value'),
    Input('struct_district_dd', 'value')
)

# ***********************************
    # STRUCTURES - All
# **********************************
def get_structures_all(region, district):

    #total
    struct_all_reg_total = None
    struct_all_reg_percent = None
    struct_all_total = None
    struct_all_percent = None

    #fully completed
    struct_fully_compl_reg_all_val = None
    struct_fully_compl_reg_all_percent = None
    struct_fully_compl_all_val = None
    struct_fully_compl_all_percent = None

    #completely roofed but uncompleted
    struct_compl_roofed_uncom_reg_all_val = None
    struct_compl_roofed_uncom_reg_all_percent = None
    struct_compl_roofed_uncom_all_val = None
    struct_compl_roofed_uncom_all_percent = None

    #partially roofed
    struct_part_roofed_reg_all_val = None
    struct_part_roofed_reg_all_percent = None
    struct_part_roofed_all_val = None
    struct_part_roofed_all_percent = None

    #***********************

    # roofing level with improvised roof
    struct_roof_lvl_with_improv_reg_all_val = None
    struct_roof_lvl_with_improv_reg_all_percent = None
    struct_roof_lvl_with_improv_all_val = None
    struct_roof_lvl_with_improv_all_percent = None

    # lintel level with improvised roof
    struct_lintel_lvl_with_improv_roof_reg_all_val = None
    struct_lintel_lvl_with_improv_roof_reg_all_percent = None
    struct_lintel_lvl_with_improv_roof_all_val = None
    struct_lintel_lvl_with_improv_roof_all_percent = None

    #roofing level without roof
    struct_roof_lvl_wout_roof_reg_all_val = None
    struct_roof_lvl_wout_roof_reg_all_percent = None
    struct_roof_lvl_wout_roof_all_val = None
    struct_roof_lvl_wout_roof_all_percent = None

    #lintel level without roof
    struct_lintel_lvl_wout_roof_reg_all_val = None
    struct_lintel_lvl_wout_roof_reg_all_percent = None
    struct_lintel_lvl_wout_roof_all_val = None
    struct_lintel_lvl_wout_roof_all_percent = None

    #window level
    struct_window_lvl_reg_all_val = None
    struct_window_lvl_reg_all_percent = None
    struct_window_lvl_all_val = None
    struct_window_lvl_all_percent = None

    #concrete/metallic pillars
    struct_conc_metal_pill_reg_all_val = None
    struct_conc_metal_pill_reg_all_percent = None
    struct_conc_metal_pill_all_val = None
    struct_conc_metal_pill_all_percent = None


    if (region != None) & (district != None):

        # GET DATA
        df_data = df_structures_dic[region]

        df_all = \
        df_data[(df_data['Structure_Type'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'All')][
            ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_all = df_all.reset_index(drop=True)

        # All
        # total
        struct_all_reg_total = df_all['Number'][0]
        struct_all_reg_percent = df_all['Percent'][0]
        struct_all_total = df_all[district][0]
        struct_all_percent = 100.0

        #District Details
        # **********************************************

        #Fully completed
        df_struct_fully_compl_all = df_all = df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '1-1')][
            ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_fully_compl_all = df_struct_fully_compl_all.reset_index(drop=True)

        struct_fully_compl_reg_all_val = df_struct_fully_compl_all['Number'][0]
        struct_fully_compl_reg_all_percent = df_struct_fully_compl_all['Percent'][0]
        struct_fully_compl_all_val = df_struct_fully_compl_all[district][0]
        struct_fully_compl_all_percent = (struct_fully_compl_all_val / struct_all_total) * 100

        # Completely roofed but uncompleted
        df_struct_compl_roofed_uncom_reg_all = df_all = df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '1-2')][
            ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_compl_roofed_uncom_reg_all = df_struct_compl_roofed_uncom_reg_all.reset_index(drop=True)

        struct_compl_roofed_uncom_reg_all_val = df_struct_compl_roofed_uncom_reg_all['Number'][0]
        struct_compl_roofed_uncom_reg_all_percent = df_struct_compl_roofed_uncom_reg_all['Percent'][0]
        struct_compl_roofed_uncom_all_val = df_struct_compl_roofed_uncom_reg_all[district][0]
        struct_compl_roofed_uncom_all_percent = (struct_compl_roofed_uncom_all_val / struct_all_total) * 100

        # Partially roofed
        df_struct_part_roofed_all = df_all = \
        df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '1-3')][
            ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_part_roofed_all = df_struct_part_roofed_all.reset_index(drop=True)

        struct_part_roofed_reg_all_val = df_struct_part_roofed_all['Number'][0]
        struct_part_roofed_reg_all_percent = df_struct_part_roofed_all['Percent'][0]
        struct_part_roofed_all_val = df_struct_part_roofed_all[district][0]
        struct_part_roofed_all_percent = (struct_part_roofed_reg_all_val / struct_all_total) * 100

        #***************************
        # Roofing Level with improvised roof
        df_struct_roof_with_lvl_improv_reg_all = df_all = \
            df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '1-4')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_roof_with_lvl_improv_reg_all = df_struct_roof_with_lvl_improv_reg_all.reset_index(drop=True)

        struct_roof_lvl_with_improv_reg_all_val = df_struct_roof_with_lvl_improv_reg_all['Number'][0]
        struct_roof_lvl_with_improv_reg_all_percent = df_struct_roof_with_lvl_improv_reg_all['Percent'][0]
        struct_roof_lvl_with_improv_all_val = df_struct_roof_with_lvl_improv_reg_all[district][0]
        struct_roof_lvl_with_improv_all_percent = (struct_roof_lvl_with_improv_all_val / struct_all_total) * 100

        # lintel Level with improvised roof
        df_struct_lintel_lvl_improv_reg_all = df_all = \
            df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '1-5')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_lintel_lvl_improv_reg_all = df_struct_lintel_lvl_improv_reg_all.reset_index(drop=True)

        struct_lintel_lvl_with_improv_roof_reg_all_val = df_struct_lintel_lvl_improv_reg_all['Number'][0]
        struct_lintel_lvl_with_improv_roof_reg_all_percent = df_struct_lintel_lvl_improv_reg_all['Percent'][0]
        struct_lintel_lvl_with_improv_roof_all_val = df_struct_lintel_lvl_improv_reg_all[district][0]
        struct_lintel_lvl_wth_improv_roof_all_percent = (struct_lintel_lvl_with_improv_roof_all_val / struct_all_total) * 100

        # roofing level without roof
        df_struct_roof_lvl_wout_roof_reg_all = df_all = \
            df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '1-6')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_roof_lvl_wout_roof_reg_all = df_struct_roof_lvl_wout_roof_reg_all.reset_index(drop=True)

        struct_roof_lvl_wout_roof_reg_all_val = df_struct_roof_lvl_wout_roof_reg_all['Number'][0]
        struct_roof_lvl_wout_roof_reg_all_percent = df_struct_roof_lvl_wout_roof_reg_all['Percent'][0]
        struct_roof_lvl_wout_roof_all_val = df_struct_roof_lvl_wout_roof_reg_all[district][0]
        struct_roof_lvl_wout_roof_all_percent = (struct_roof_lvl_wout_roof_all_val / struct_all_total) * 100

        # lintel Level without roof
        df_struct_lintel_lvl_wout_roof_all = df_all = \
            df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '1-7')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_lintel_lvl_wout_roof_all = df_struct_lintel_lvl_wout_roof_all.reset_index(drop=True)

        struct_lintel_lvl_wout_roof_reg_all_val = df_struct_lintel_lvl_wout_roof_all['Number'][0]
        struct_lintel_lvl_wout_roof_reg_all_percent = df_struct_lintel_lvl_wout_roof_all['Percent'][0]
        struct_lintel_lvl_wout_roof_all_val = df_struct_lintel_lvl_wout_roof_all[district][0]
        struct_lintel_lvl_wout_roof_all_percent = (struct_lintel_lvl_wout_roof_all_val / struct_all_total) * 100

        # window level
        df_struct_window_lvl_all = df_all = \
            df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '1-8')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_window_lvl_all = df_struct_window_lvl_all.reset_index(drop=True)

        struct_window_lvl_reg_all_val = df_struct_window_lvl_all['Number'][0]
        struct_window_lvl_reg_all_percent = df_struct_window_lvl_all['Percent'][0]
        struct_window_lvl_all_val = df_struct_window_lvl_all[district][0]
        struct_window_lvl_all_percent = (struct_window_lvl_all_val / struct_all_total) * 100

        # concrete/metal pillars
        df_struct_conc_metal_pill_all = df_all = \
            df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '1-9')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_conc_metal_pill_all = df_struct_conc_metal_pill_all.reset_index(drop=True)

        struct_conc_metal_pill_reg_all_val = df_struct_conc_metal_pill_all['Number'][0]
        struct_window_lvl_reg_reg_all_percent = df_struct_conc_metal_pill_all['Percent'][0]
        struct_conc_metal_pill_all_val = df_struct_conc_metal_pill_all[district][0]
        struct_conc_metal_pill_all_percent = struct_window_lvl_all_percent = (struct_conc_metal_pill_all_val / struct_all_total) * 100

        # Formatting
        #***********

        #total
        struct_all_reg_total = '{:,}'.format(struct_all_reg_total)
        struct_all_reg_percent = '{:,.1f}'.format(struct_all_reg_percent)
        struct_all_total = '{:,}'.format(struct_all_total)
        struct_all_percent = '{:,.1f}'.format(struct_all_percent)

        # fully completed
        struct_fully_compl_reg_all_val = '{:,}'.format(struct_fully_compl_reg_all_val)
        struct_fully_compl_reg_all_percent = '{:,.1f}'.format(struct_fully_compl_reg_all_percent)
        struct_fully_compl_all_val = '{:,}'.format(struct_fully_compl_all_val)
        struct_fully_compl_all_percent = '{:,.1f}'.format(struct_fully_compl_all_percent)

        #completely roofed but uncompleted
        struct_compl_roofed_uncom_reg_all_val = '{:,}'.format(struct_compl_roofed_uncom_reg_all_val)
        struct_compl_roofed_uncom_reg_all_percent = '{:,.1f}'.format(struct_compl_roofed_uncom_reg_all_percent)
        struct_compl_roofed_uncom_all_val = '{:,}'.format(struct_compl_roofed_uncom_all_val)
        struct_compl_roofed_uncom_all_percent = '{:,.1f}'.format(struct_compl_roofed_uncom_all_percent)

        #partially roofed
        struct_part_roofed_reg_all_val = '{:,}'.format(struct_part_roofed_reg_all_val)
        struct_part_roofed_reg_all_percent = '{:,.1f}'.format(struct_part_roofed_reg_all_percent)
        struct_part_roofed_all_val = '{:,}'.format(struct_part_roofed_all_val)
        struct_part_roofed_all_percent = '{:,.1f}'.format(struct_part_roofed_all_percent)

        #roofing level with improvised roof
        struct_roof_lvl_with_improv_reg_all_val = '{:,}'.format(struct_roof_lvl_with_improv_reg_all_val)
        struct_roof_lvl_with_improv_reg_all_percent = '{:,.1f}'.format(struct_roof_lvl_with_improv_reg_all_percent)
        struct_roof_lvl_with_improv_all_val = '{:,}'.format(struct_roof_lvl_with_improv_all_val)
        struct_roof_lvl_with_improv_all_percent = '{:,.1f}'.format(struct_roof_lvl_with_improv_all_percent)

        #lintel level with improvised roof
        struct_lintel_lvl_with_improv_roof_reg_all_val = '{:,}'.format(struct_lintel_lvl_with_improv_roof_reg_all_val)
        struct_lintel_lvl_with_improv_roof_reg_all_percent = '{:,.1f}'.format(struct_lintel_lvl_with_improv_roof_reg_all_percent)
        struct_lintel_lvl_with_improv_roof_all_val = '{:,}'.format(struct_lintel_lvl_with_improv_roof_all_val)
        struct_lintel_lvl_with_improv_roof_all_percent = '{:,.1f}'.format(struct_lintel_lvl_wth_improv_roof_all_percent)

        # roofing level without roof
        struct_roof_lvl_wout_roof_reg_all_val = '{:,}'.format(struct_roof_lvl_wout_roof_reg_all_val)
        struct_roof_lvl_wout_roof_reg_all_percent = '{:,.1f}'.format(struct_roof_lvl_wout_roof_reg_all_percent)
        struct_roof_lvl_wout_roof_all_val = '{:,}'.format(struct_roof_lvl_wout_roof_all_val)
        struct_roof_lvl_wout_roof_all_percent = '{:,.1f}'.format(struct_roof_lvl_wout_roof_all_percent)

        #lintel level without roof
        struct_lintel_lvl_wout_roof_reg_all_val = '{:,}'.format(struct_lintel_lvl_wout_roof_reg_all_val)
        struct_lintel_lvl_wout_roof_reg_all_percent = '{:,.1f}'.format(struct_lintel_lvl_wout_roof_reg_all_percent)
        struct_lintel_lvl_wout_roof_all_val = '{:,}'.format(struct_lintel_lvl_wout_roof_all_val)
        struct_lintel_lvl_wout_roof_all_percent = '{:,.1f}'.format(struct_lintel_lvl_wout_roof_all_percent)

        # windows level
        struct_window_lvl_reg_all_val = '{:,}'.format(struct_window_lvl_reg_all_val)
        struct_window_lvl_reg_all_percent = '{:,.1f}'.format(struct_window_lvl_reg_all_percent)
        struct_window_lvl_all_val = '{:,}'.format(struct_window_lvl_all_val)
        struct_window_lvl_all_percent = '{:,.1f}'.format(struct_window_lvl_all_percent)

        #concrete/metal pillars
        struct_conc_metal_pill_reg_all_val = '{:,}'.format(struct_conc_metal_pill_reg_all_val)
        struct_conc_metal_pill_reg_all_percent = '{:,.1f}'.format(struct_window_lvl_reg_reg_all_percent)
        struct_conc_metal_pill_all_val = '{:,}'.format(struct_conc_metal_pill_all_val)
        struct_conc_metal_pill_all_percent = '{:,.1f}'.format(struct_conc_metal_pill_all_percent)

    return struct_all_reg_total, struct_all_reg_percent, struct_all_total, struct_all_percent, \
           struct_fully_compl_reg_all_val, struct_fully_compl_reg_all_percent, struct_fully_compl_all_val, struct_fully_compl_all_percent, \
           struct_compl_roofed_uncom_reg_all_val, struct_compl_roofed_uncom_reg_all_percent, struct_compl_roofed_uncom_all_val, struct_compl_roofed_uncom_all_percent, \
           struct_part_roofed_reg_all_val, struct_part_roofed_reg_all_percent, struct_part_roofed_all_val, struct_part_roofed_all_percent, \
           struct_roof_lvl_with_improv_reg_all_val, struct_roof_lvl_with_improv_reg_all_percent, struct_roof_lvl_with_improv_all_val, struct_roof_lvl_with_improv_all_percent, \
           struct_lintel_lvl_with_improv_roof_reg_all_val, struct_lintel_lvl_with_improv_roof_reg_all_percent, struct_lintel_lvl_with_improv_roof_all_val, struct_lintel_lvl_with_improv_roof_all_percent, \
           struct_roof_lvl_wout_roof_reg_all_val, struct_roof_lvl_wout_roof_reg_all_percent, struct_roof_lvl_wout_roof_all_val, struct_roof_lvl_wout_roof_all_percent, \
           struct_lintel_lvl_wout_roof_reg_all_val, struct_lintel_lvl_wout_roof_reg_all_percent, struct_lintel_lvl_wout_roof_all_val, struct_lintel_lvl_wout_roof_all_percent, \
           struct_window_lvl_reg_all_val, struct_window_lvl_reg_all_percent, struct_window_lvl_all_val, struct_window_lvl_all_percent, \
           struct_conc_metal_pill_reg_all_val, struct_conc_metal_pill_reg_all_percent, struct_conc_metal_pill_all_val, struct_conc_metal_pill_all_percent


# ***********************************
    # STRUCTURES - URBAN
# **********************************
@app.callback(

    # Total
    Output('struct_reg_urban_total', 'children'),
    Output('struct_reg_urban_percent', 'children'),
    Output('struct_urban_total', 'children'),
    Output('struct_urban_percent', 'children'),

    # #Fully completed:
    Output('struct_fully_compl_reg_urban_val', 'children'),
    Output('struct_fully_compl_reg_urban_percent', 'children'),
    Output('struct_fully_compl_urban_val', 'children'),
    Output('struct_fully_compl_urban_percent', 'children'),

    #
    # Completely roofed but uncompleted:
    Output('struct_compl_roofed_uncom_reg_urban_val', 'children'),
    Output('struct_compl_roofed_uncom_reg_urban_percent', 'children'),
    Output('struct_compl_roofed_uncom_urban_val', 'children'),
    Output('struct_compl_roofed_uncom_urban_percent', 'children'),

    #
    # Partially roofed:
    Output('struct_part_roofed_reg_urban_val', 'children'),
    Output('struct_part_roofed_reg_urban_percent', 'children'),
    Output('struct_part_roofed_urban_val', 'children'),
    Output('struct_part_roofed_urban_percent', 'children'),

    #
    # #Roofing level [with improvised roof
    Output('struct_roof_lvl_improv_reg_urban_val', 'children'),
    Output('struct_roof_lvl_improv_reg_urban_percent', 'children'),
    Output('struct_roof_lvl_improv_urban_val', 'children'),
    Output('struct_roof_lvl_improv_urban_percent', 'children'),
    #
    # #Lintel level [with improvised roof]
    Output('struct_lintel_improv_reg_urban_val', 'children'),
    Output('struct_lintel_improv_reg_urban_percent', 'children'),
    Output('struct_lintel_improv_urban_val', 'children'),
    Output('struct_lintel_improv_urban_percent', 'children'),
    #
    # #Roofing level [without roof]
    Output('struct_roof_lvl_wout_roof_reg_urban_val', 'children'),
    Output('struct_roof_lvl_wout_roof_reg_urban_percent', 'children'),
    Output('struct_roof_lvl_wout_roof_urban_val', 'children'),
    Output('struct_roof_lvl_wout_roof_urban_percent', 'children'),
    #
    # #Lintel level [without roof]
    Output('struct_lintel_wout_roof_reg_urban_val', 'children'),
    Output('struct_lintel_wout_roof_reg_urban_percent', 'children'),
    Output('struct_lintel_wout_roof_urban_val', 'children'),
    Output('struct_lintel_wout_roof_urban_percent', 'children'),

    #
    # Window level
    Output('struct_window_lvl_reg_urban_val', 'children'),
    Output('struct_window_lvl_reg_urban_percent', 'children'),
    Output('struct_window_lvl_urban_val', 'children'),
    Output('struct_window_lvl_urban_percent', 'children'),

    # Concrete/Metal Pillars level
    Output('struct_concr_metal_pill_lvl_reg_urban_val', 'children'),
    Output('struct_concr_metal_pill_lvl_reg_urban_percent', 'children'),
    Output('struct_concr_metal_pill_lvl_urban_val', 'children'),
    Output('struct_concr_metal_pill_lvl_urban_percent', 'children'),

    Input('struct_region_dd', 'value'),
    Input('struct_district_dd', 'value')

)

def get_structures_urban(region, district):

    #total
    struct_urban_reg_total = None
    struct_urban_reg_percent = None
    struct_urban_total = None
    struct_urban_percent = None

    #fully completed
    struct_fully_compl_reg_urban_val = None
    struct_fully_compl_reg_urban_percent = None
    struct_fully_compl_urban_val = None
    struct_fully_compl_urban_percent = None

    #completely roofed but uncompleted
    struct_compl_roofed_uncom_reg_urban_val = None
    struct_compl_roofed_uncom_reg_urban_percent = None
    struct_compl_roofed_uncom_urban_val = None
    struct_compl_roofed_uncom_urban_percent = None

    #partially roofed
    struct_part_roofed_reg_urban_val = None
    struct_part_roofed_reg_urban_percent = None
    struct_part_roofed_urban_val = None
    struct_part_roofed_urban_percent = None

    # roofing level with improvised roof
    struct_roof_lvl_with_improv_reg_urban_val = None
    struct_roof_lvl_with_improv_reg_urban_percent = None
    struct_roof_lvl_with_improv_urban_val = None
    struct_roof_lvl_with_improv_urban_percent = None

    # lintel level with improvised roof
    struct_lintel_lvl_with_improv_roof_reg_urban_val = None
    struct_lintel_lvl_with_improv_roof_reg_urban_percent = None
    struct_lintel_lvl_with_improv_roof_urban_val = None
    struct_lintel_lvl_with_improv_roof_urban_percent = None

    #roofing level without roof
    struct_roof_lvl_wout_roof_reg_urban_val = None
    struct_roof_lvl_wout_roof_reg_urban_percent = None
    struct_roof_lvl_wout_roof_urban_val = None
    struct_roof_lvl_wout_roof_urban_percent = None

    #lintel level without roof
    struct_lintel_lvl_wout_roof_reg_urban_val = None
    struct_lintel_lvl_wout_roof_reg_urban_percent = None
    struct_lintel_lvl_wout_roof_urban_val = None
    struct_lintel_lvl_wout_roof_urban_percent = None

    #window level
    struct_window_lvl_reg_urban_val = None
    struct_window_lvl_reg_urban_percent = None
    struct_window_lvl_urban_val = None
    struct_window_lvl_urban_percent = None

    #concrete/meturbanic pillars
    struct_conc_metal_pill_reg_urban_val = None
    struct_conc_metal_pill_reg_urban_percent = None
    struct_conc_metal_pill_urban_val = None
    struct_conc_metal_pill_urban_percent = None


    if (region != None) & (district != None):

        # GET DATA
        df_data = df_structures_dic[region]

        df_urban = \
        df_data[(df_data['Structure_Type'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'Urban')][
            ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_urban = df_urban.reset_index(drop=True)

        # Urban total
        struct_urban_reg_total = df_urban['Number'][0]
        struct_urban_reg_percent = df_urban['Percent'][0]
        struct_urban_total = df_urban[district][0]
        struct_urban_percent = 100.0

        #District Details
        # **********************************************

        #Fully completed
        df_struct_fully_compl_urban = df_urban = df_data[((df_data['Type'] == 'Urban')) & (df_data['Status_Code'] == '1-1')][
            ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_fully_compl_urban = df_struct_fully_compl_urban.reset_index(drop=True)

        struct_fully_compl_reg_urban_val = df_struct_fully_compl_urban['Number'][0]
        struct_fully_compl_reg_urban_percent = df_struct_fully_compl_urban['Percent'][0]
        struct_fully_compl_urban_val = df_struct_fully_compl_urban[district][0]
        struct_fully_compl_urban_percent = (struct_fully_compl_urban_val / struct_urban_total) * 100

        # Completely roofed but uncompleted
        df_struct_compl_roofed_uncom_reg_urban = df_urban = df_data[((df_data['Type'] == 'Urban')) & (df_data['Status_Code'] == '1-2')][
            ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_compl_roofed_uncom_reg_urban = df_struct_compl_roofed_uncom_reg_urban.reset_index(drop=True)

        struct_compl_roofed_uncom_reg_urban_val = df_struct_compl_roofed_uncom_reg_urban['Number'][0]
        struct_compl_roofed_uncom_reg_urban_percent = df_struct_compl_roofed_uncom_reg_urban['Percent'][0]
        struct_compl_roofed_uncom_urban_val = df_struct_compl_roofed_uncom_reg_urban[district][0]
        struct_compl_roofed_uncom_urban_percent = (struct_compl_roofed_uncom_urban_val / struct_urban_total) * 100

        # Partially roofed
        df_struct_part_roofed_urban = df_urban = \
        df_data[((df_data['Type'] == 'Urban')) & (df_data['Status_Code'] == '1-3')][
            ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_part_roofed_urban = df_struct_part_roofed_urban.reset_index(drop=True)

        struct_part_roofed_reg_urban_val = df_struct_part_roofed_urban['Number'][0]
        struct_part_roofed_reg_urban_percent = df_struct_part_roofed_urban['Percent'][0]
        struct_part_roofed_urban_val = df_struct_part_roofed_urban[district][0]
        struct_part_roofed_urban_percent = (struct_part_roofed_reg_urban_val / struct_urban_total) * 100

        #***************************
        # Roofing Level with improvised roof
        df_struct_roof_with_lvl_improv_reg_urban = df_urban = \
            df_data[((df_data['Type'] == 'Urban')) & (df_data['Status_Code'] == '1-4')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_roof_with_lvl_improv_reg_urban = df_struct_roof_with_lvl_improv_reg_urban.reset_index(drop=True)

        struct_roof_lvl_with_improv_reg_urban_val = df_struct_roof_with_lvl_improv_reg_urban['Number'][0]
        struct_roof_lvl_with_improv_reg_urban_percent = df_struct_roof_with_lvl_improv_reg_urban['Percent'][0]
        struct_roof_lvl_with_improv_urban_val = df_struct_roof_with_lvl_improv_reg_urban[district][0]
        struct_roof_lvl_with_improv_urban_percent = (struct_roof_lvl_with_improv_urban_val / struct_urban_total) * 100

        # lintel Level with improvised roof
        df_struct_lintel_lvl_improv_reg_urban = df_urban = \
            df_data[((df_data['Type'] == 'Urban')) & (df_data['Status_Code'] == '1-5')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_lintel_lvl_improv_reg_urban = df_struct_lintel_lvl_improv_reg_urban.reset_index(drop=True)

        struct_lintel_lvl_with_improv_roof_reg_urban_val = df_struct_lintel_lvl_improv_reg_urban['Number'][0]
        struct_lintel_lvl_with_improv_roof_reg_urban_percent = df_struct_lintel_lvl_improv_reg_urban['Percent'][0]
        struct_lintel_lvl_with_improv_roof_urban_val = df_struct_lintel_lvl_improv_reg_urban[district][0]
        struct_lintel_lvl_wth_improv_roof_urban_percent = (struct_lintel_lvl_with_improv_roof_urban_val / struct_urban_total) * 100

        # roofing level without roof
        df_struct_roof_lvl_wout_roof_reg_urban = df_urban = \
            df_data[((df_data['Type'] == 'Urban')) & (df_data['Status_Code'] == '1-6')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_roof_lvl_wout_roof_reg_urban = df_struct_roof_lvl_wout_roof_reg_urban.reset_index(drop=True)

        struct_roof_lvl_wout_roof_reg_urban_val = df_struct_roof_lvl_wout_roof_reg_urban['Number'][0]
        struct_roof_lvl_wout_roof_reg_urban_percent = df_struct_roof_lvl_wout_roof_reg_urban['Percent'][0]
        struct_roof_lvl_wout_roof_urban_val = df_struct_roof_lvl_wout_roof_reg_urban[district][0]
        struct_roof_lvl_wout_roof_urban_percent = (struct_roof_lvl_wout_roof_urban_val / struct_urban_total) * 100

        # lintel Level without roof
        df_struct_lintel_lvl_wout_roof_urban = df_urban = \
            df_data[((df_data['Type'] == 'Urban')) & (df_data['Status_Code'] == '1-7')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_lintel_lvl_wout_roof_urban = df_struct_lintel_lvl_wout_roof_urban.reset_index(drop=True)

        struct_lintel_lvl_wout_roof_reg_urban_val = df_struct_lintel_lvl_wout_roof_urban['Number'][0]
        struct_lintel_lvl_wout_roof_reg_urban_percent = df_struct_lintel_lvl_wout_roof_urban['Percent'][0]
        struct_lintel_lvl_wout_roof_urban_val = df_struct_lintel_lvl_wout_roof_urban[district][0]
        struct_lintel_lvl_wout_roof_urban_percent = (struct_lintel_lvl_wout_roof_urban_val / struct_urban_total) * 100

        # window level
        df_struct_window_lvl_urban = df_urban = \
            df_data[((df_data['Type'] == 'Urban')) & (df_data['Status_Code'] == '1-8')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_window_lvl_urban = df_struct_window_lvl_urban.reset_index(drop=True)

        struct_window_lvl_reg_urban_val = df_struct_window_lvl_urban['Number'][0]
        struct_window_lvl_reg_urban_percent = df_struct_window_lvl_urban['Percent'][0]
        struct_window_lvl_urban_val = df_struct_window_lvl_urban[district][0]
        struct_window_lvl_urban_percent = (struct_window_lvl_urban_val / struct_urban_total) * 100

        # concrete/metal pillars
        df_struct_conc_metal_pill_urban = df_urban = \
            df_data[((df_data['Type'] == 'Urban')) & (df_data['Status_Code'] == '1-9')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_conc_metal_pill_urban = df_struct_conc_metal_pill_urban.reset_index(drop=True)

        struct_conc_metal_pill_reg_urban_val = df_struct_conc_metal_pill_urban['Number'][0]
        struct_window_lvl_reg_reg_urban_percent = df_struct_conc_metal_pill_urban['Percent'][0]
        struct_conc_metal_pill_urban_val = df_struct_conc_metal_pill_urban[district][0]
        struct_conc_metal_pill_urban_percent = struct_window_lvl_urban_percent = (struct_conc_metal_pill_urban_val / struct_urban_total) * 100

        # Formatting
        #***********

        #total
        struct_urban_reg_total = '{:,}'.format(struct_urban_reg_total)
        struct_urban_reg_percent = '{:,.1f}'.format(struct_urban_reg_percent)
        struct_urban_total = '{:,}'.format(struct_urban_total)
        struct_urban_percent = '{:,.1f}'.format(struct_urban_percent)

        # fully completed
        struct_fully_compl_reg_urban_val = '{:,}'.format(struct_fully_compl_reg_urban_val)
        struct_fully_compl_reg_urban_percent = '{:,.1f}'.format(struct_fully_compl_reg_urban_percent)
        struct_fully_compl_urban_val = '{:,}'.format(struct_fully_compl_urban_val)
        struct_fully_compl_urban_percent = '{:,.1f}'.format(struct_fully_compl_urban_percent)

        #completely roofed but uncompleted
        struct_compl_roofed_uncom_reg_urban_val = '{:,}'.format(struct_compl_roofed_uncom_reg_urban_val)
        struct_compl_roofed_uncom_reg_urban_percent = '{:,.1f}'.format(struct_compl_roofed_uncom_reg_urban_percent)
        struct_compl_roofed_uncom_urban_val = '{:,}'.format(struct_compl_roofed_uncom_urban_val)
        struct_compl_roofed_uncom_urban_percent = '{:,.1f}'.format(struct_compl_roofed_uncom_urban_percent)

        #partially roofed
        struct_part_roofed_reg_urban_val = '{:,}'.format(struct_part_roofed_reg_urban_val)
        struct_part_roofed_reg_urban_percent = '{:,.1f}'.format(struct_part_roofed_reg_urban_percent)
        struct_part_roofed_urban_val = '{:,}'.format(struct_part_roofed_urban_val)
        struct_part_roofed_urban_percent = '{:,.1f}'.format(struct_part_roofed_urban_percent)

        #roofing level with improvised roof
        struct_roof_lvl_with_improv_reg_urban_val = '{:,}'.format(struct_roof_lvl_with_improv_reg_urban_val)
        struct_roof_lvl_with_improv_reg_urban_percent = '{:,.1f}'.format(struct_roof_lvl_with_improv_reg_urban_percent)
        struct_roof_lvl_with_improv_urban_val = '{:,}'.format(struct_roof_lvl_with_improv_urban_val)
        struct_roof_lvl_with_improv_urban_percent = '{:,.1f}'.format(struct_roof_lvl_with_improv_urban_percent)

        #lintel level with improvised roof
        struct_lintel_lvl_with_improv_roof_reg_urban_val = '{:,}'.format(struct_lintel_lvl_with_improv_roof_reg_urban_val)
        struct_lintel_lvl_with_improv_roof_reg_urban_percent = '{:,.1f}'.format(struct_lintel_lvl_with_improv_roof_reg_urban_percent)
        struct_lintel_lvl_with_improv_roof_urban_val = '{:,}'.format(struct_lintel_lvl_with_improv_roof_urban_val)
        struct_lintel_lvl_with_improv_roof_urban_percent = '{:,.1f}'.format(struct_lintel_lvl_wth_improv_roof_urban_percent)

        # roofing level without roof
        struct_roof_lvl_wout_roof_reg_urban_val = '{:,}'.format(struct_roof_lvl_wout_roof_reg_urban_val)
        struct_roof_lvl_wout_roof_reg_urban_percent = '{:,.1f}'.format(struct_roof_lvl_wout_roof_reg_urban_percent)
        struct_roof_lvl_wout_roof_urban_val = '{:,}'.format(struct_roof_lvl_wout_roof_urban_val)
        struct_roof_lvl_wout_roof_urban_percent = '{:,.1f}'.format(struct_roof_lvl_wout_roof_urban_percent)

        #lintel level without roof
        struct_lintel_lvl_wout_roof_reg_urban_val = '{:,}'.format(struct_lintel_lvl_wout_roof_reg_urban_val)
        struct_lintel_lvl_wout_roof_reg_urban_percent = '{:,.1f}'.format(struct_lintel_lvl_wout_roof_reg_urban_percent)
        struct_lintel_lvl_wout_roof_urban_val = '{:,}'.format(struct_lintel_lvl_wout_roof_urban_val)
        struct_lintel_lvl_wout_roof_urban_percent = '{:,.1f}'.format(struct_lintel_lvl_wout_roof_urban_percent)

        # windows level
        struct_window_lvl_reg_urban_val = '{:,}'.format(struct_window_lvl_reg_urban_val)
        struct_window_lvl_reg_urban_percent = '{:,.1f}'.format(struct_window_lvl_reg_urban_percent)
        struct_window_lvl_urban_val = '{:,}'.format(struct_window_lvl_urban_val)
        struct_window_lvl_urban_percent = '{:,.1f}'.format(struct_window_lvl_urban_percent)

        #concrete/metal pillars
        struct_conc_metal_pill_reg_urban_val = '{:,}'.format(struct_conc_metal_pill_reg_urban_val)
        struct_conc_metal_pill_reg_urban_percent = '{:,.1f}'.format(struct_window_lvl_reg_reg_urban_percent)
        struct_conc_metal_pill_urban_val = '{:,}'.format(struct_conc_metal_pill_urban_val)
        struct_conc_metal_pill_urban_percent = '{:,.1f}'.format(struct_conc_metal_pill_urban_percent)

    return struct_urban_reg_total, struct_urban_reg_percent, struct_urban_total, struct_urban_percent, \
           struct_fully_compl_reg_urban_val, struct_fully_compl_reg_urban_percent, struct_fully_compl_urban_val, struct_fully_compl_urban_percent, \
           struct_compl_roofed_uncom_reg_urban_val, struct_compl_roofed_uncom_reg_urban_percent, struct_compl_roofed_uncom_urban_val, struct_compl_roofed_uncom_urban_percent, \
           struct_part_roofed_reg_urban_val, struct_part_roofed_reg_urban_percent, struct_part_roofed_urban_val, struct_part_roofed_urban_percent, \
           struct_roof_lvl_with_improv_reg_urban_val, struct_roof_lvl_with_improv_reg_urban_percent, struct_roof_lvl_with_improv_urban_val, struct_roof_lvl_with_improv_urban_percent, \
           struct_lintel_lvl_with_improv_roof_reg_urban_val, struct_lintel_lvl_with_improv_roof_reg_urban_percent, struct_lintel_lvl_with_improv_roof_urban_val, struct_lintel_lvl_with_improv_roof_urban_percent, \
           struct_roof_lvl_wout_roof_reg_urban_val, struct_roof_lvl_wout_roof_reg_urban_percent, struct_roof_lvl_wout_roof_urban_val, struct_roof_lvl_wout_roof_urban_percent, \
           struct_lintel_lvl_wout_roof_reg_urban_val, struct_lintel_lvl_wout_roof_reg_urban_percent, struct_lintel_lvl_wout_roof_urban_val, struct_lintel_lvl_wout_roof_urban_percent, \
           struct_window_lvl_reg_urban_val, struct_window_lvl_reg_urban_percent, struct_window_lvl_urban_val, struct_window_lvl_urban_percent, \
           struct_conc_metal_pill_reg_urban_val, struct_conc_metal_pill_reg_urban_percent, struct_conc_metal_pill_urban_val, struct_conc_metal_pill_urban_percent


# ***********************************
    # STRUCTURES - RURAL
# **********************************
@app.callback(

    # Total
    Output('struct_reg_rural_total', 'children'),
    Output('struct_reg_rural_percent', 'children'),
    Output('struct_rural_total', 'children'),
    Output('struct_rural_percent', 'children'),

    # #Fully completed:
    Output('struct_fully_compl_reg_rural_val', 'children'),
    Output('struct_fully_compl_reg_rural_percent', 'children'),
    Output('struct_fully_compl_rural_val', 'children'),
    Output('struct_fully_compl_rural_percent', 'children'),

    #
    # Completely roofed but uncompleted:
    Output('struct_compl_roofed_uncom_reg_rural_val', 'children'),
    Output('struct_compl_roofed_uncom_reg_rural_percent', 'children'),
    Output('struct_compl_roofed_uncom_rural_val', 'children'),
    Output('struct_compl_roofed_uncom_rural_percent', 'children'),

    #
    # Partially roofed:
    Output('struct_part_roofed_reg_rural_val', 'children'),
    Output('struct_part_roofed_reg_rural_percent', 'children'),
    Output('struct_part_roofed_rural_val', 'children'),
    Output('struct_part_roofed_rural_percent', 'children'),

    #
    # #Roofing level [with improvised roof
    Output('struct_roof_lvl_improv_reg_rural_val', 'children'),
    Output('struct_roof_lvl_improv_reg_rural_percent', 'children'),
    Output('struct_roof_lvl_improv_rural_val', 'children'),
    Output('struct_roof_lvl_improv_rural_percent', 'children'),
    #
    # #Lintel level [with improvised roof]
    Output('struct_lintel_improv_reg_rural_val', 'children'),
    Output('struct_lintel_improv_reg_rural_percent', 'children'),
    Output('struct_lintel_improv_rural_val', 'children'),
    Output('struct_lintel_improv_rural_percent', 'children'),
    #
    # #Roofing level [without roof]
    Output('struct_roof_lvl_wout_roof_reg_rural_val', 'children'),
    Output('struct_roof_lvl_wout_roof_reg_rural_percent', 'children'),
    Output('struct_roof_lvl_wout_roof_rural_val', 'children'),
    Output('struct_roof_lvl_wout_roof_rural_percent', 'children'),
    #
    # #Lintel level [without roof]
    Output('struct_lintel_wout_roof_reg_rural_val', 'children'),
    Output('struct_lintel_wout_roof_reg_rural_percent', 'children'),
    Output('struct_lintel_wout_roof_rural_val', 'children'),
    Output('struct_lintel_wout_roof_rural_percent', 'children'),

    #
    # Window level
    Output('struct_window_lvl_reg_rural_val', 'children'),
    Output('struct_window_lvl_reg_rural_percent', 'children'),
    Output('struct_window_lvl_rural_val', 'children'),
    Output('struct_window_lvl_rural_percent', 'children'),

    # Concrete/Metal Pillars level
    Output('struct_concr_metal_pill_lvl_reg_rural_val', 'children'),
    Output('struct_concr_metal_pill_lvl_reg_rural_percent', 'children'),
    Output('struct_concr_metal_pill_lvl_rural_val', 'children'),
    Output('struct_concr_metal_pill_lvl_rural_percent', 'children'),

    Input('struct_region_dd', 'value'),
    Input('struct_district_dd', 'value')

)

def get_structures_rural(region, district):

    #total
    struct_rural_reg_total = None
    struct_rural_reg_percent = None
    struct_rural_total = None
    struct_rural_percent = None

    #fully completed
    struct_fully_compl_reg_rural_val = None
    struct_fully_compl_reg_rural_percent = None
    struct_fully_compl_rural_val = None
    struct_fully_compl_rural_percent = None

    #completely roofed but uncompleted
    struct_compl_roofed_uncom_reg_rural_val = None
    struct_compl_roofed_uncom_reg_rural_percent = None
    struct_compl_roofed_uncom_rural_val = None
    struct_compl_roofed_uncom_rural_percent = None

    #partially roofed
    struct_part_roofed_reg_rural_val = None
    struct_part_roofed_reg_rural_percent = None
    struct_part_roofed_rural_val = None
    struct_part_roofed_rural_percent = None

    # roofing level with improvised roof
    struct_roof_lvl_with_improv_reg_rural_val = None
    struct_roof_lvl_with_improv_reg_rural_percent = None
    struct_roof_lvl_with_improv_rural_val = None
    struct_roof_lvl_with_improv_rural_percent = None

    # lintel level with improvised roof
    struct_lintel_lvl_with_improv_roof_reg_rural_val = None
    struct_lintel_lvl_with_improv_roof_reg_rural_percent = None
    struct_lintel_lvl_with_improv_roof_rural_val = None
    struct_lintel_lvl_with_improv_roof_rural_percent = None

    #roofing level without roof
    struct_roof_lvl_wout_roof_reg_rural_val = None
    struct_roof_lvl_wout_roof_reg_rural_percent = None
    struct_roof_lvl_wout_roof_rural_val = None
    struct_roof_lvl_wout_roof_rural_percent = None

    #lintel level without roof
    struct_lintel_lvl_wout_roof_reg_rural_val = None
    struct_lintel_lvl_wout_roof_reg_rural_percent = None
    struct_lintel_lvl_wout_roof_rural_val = None
    struct_lintel_lvl_wout_roof_rural_percent = None

    #window level
    struct_window_lvl_reg_rural_val = None
    struct_window_lvl_reg_rural_percent = None
    struct_window_lvl_rural_val = None
    struct_window_lvl_rural_percent = None

    #concrete/metruralic pillars
    struct_conc_metal_pill_reg_rural_val = None
    struct_conc_metal_pill_reg_rural_percent = None
    struct_conc_metal_pill_rural_val = None
    struct_conc_metal_pill_rural_percent = None


    if (region != None) & (district != None):

        # GET DATA
        df_data = df_structures_dic[region]

        df_rural = \
        df_data[(df_data['Structure_Type'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'Rural')][
            ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_rural = df_rural.reset_index(drop=True)

        # rural total
        struct_rural_reg_total = df_rural['Number'][0]
        struct_rural_reg_percent = df_rural['Percent'][0]
        struct_rural_total = df_rural[district][0]
        struct_rural_percent = 100.0

        #District Details
        # **********************************************

        #Fully completed
        df_struct_fully_compl_rural = df_rural = df_data[((df_data['Type'] == 'Rural')) & (df_data['Status_Code'] == '1-1')][
            ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_fully_compl_rural = df_struct_fully_compl_rural.reset_index(drop=True)

        struct_fully_compl_reg_rural_val = df_struct_fully_compl_rural['Number'][0]
        struct_fully_compl_reg_rural_percent = df_struct_fully_compl_rural['Percent'][0]
        struct_fully_compl_rural_val = df_struct_fully_compl_rural[district][0]
        struct_fully_compl_rural_percent = (struct_fully_compl_rural_val / struct_rural_total) * 100

        # Completely roofed but uncompleted
        df_struct_compl_roofed_uncom_reg_rural = df_rural = df_data[((df_data['Type'] == 'Rural')) & (df_data['Status_Code'] == '1-2')][
            ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_compl_roofed_uncom_reg_rural = df_struct_compl_roofed_uncom_reg_rural.reset_index(drop=True)

        struct_compl_roofed_uncom_reg_rural_val = df_struct_compl_roofed_uncom_reg_rural['Number'][0]
        struct_compl_roofed_uncom_reg_rural_percent = df_struct_compl_roofed_uncom_reg_rural['Percent'][0]
        struct_compl_roofed_uncom_rural_val = df_struct_compl_roofed_uncom_reg_rural[district][0]
        struct_compl_roofed_uncom_rural_percent = (struct_compl_roofed_uncom_rural_val / struct_rural_total) * 100

        # Partially roofed
        df_struct_part_roofed_rural = df_rural = \
        df_data[((df_data['Type'] == 'Rural')) & (df_data['Status_Code'] == '1-3')][
            ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_part_roofed_rural = df_struct_part_roofed_rural.reset_index(drop=True)

        struct_part_roofed_reg_rural_val = df_struct_part_roofed_rural['Number'][0]
        struct_part_roofed_reg_rural_percent = df_struct_part_roofed_rural['Percent'][0]
        struct_part_roofed_rural_val = df_struct_part_roofed_rural[district][0]
        struct_part_roofed_rural_percent = (struct_part_roofed_reg_rural_val / struct_rural_total) * 100

        #***************************
        # Roofing Level with improvised roof
        df_struct_roof_with_lvl_improv_reg_rural = df_rural = \
            df_data[((df_data['Type'] == 'Rural')) & (df_data['Status_Code'] == '1-4')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_roof_with_lvl_improv_reg_rural = df_struct_roof_with_lvl_improv_reg_rural.reset_index(drop=True)

        struct_roof_lvl_with_improv_reg_rural_val = df_struct_roof_with_lvl_improv_reg_rural['Number'][0]
        struct_roof_lvl_with_improv_reg_rural_percent = df_struct_roof_with_lvl_improv_reg_rural['Percent'][0]
        struct_roof_lvl_with_improv_rural_val = df_struct_roof_with_lvl_improv_reg_rural[district][0]
        struct_roof_lvl_with_improv_rural_percent = (struct_roof_lvl_with_improv_rural_val / struct_rural_total) * 100

        # lintel Level with improvised roof
        df_struct_lintel_lvl_improv_reg_rural = df_rural = \
            df_data[((df_data['Type'] == 'Rural')) & (df_data['Status_Code'] == '1-5')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_lintel_lvl_improv_reg_rural = df_struct_lintel_lvl_improv_reg_rural.reset_index(drop=True)

        struct_lintel_lvl_with_improv_roof_reg_rural_val = df_struct_lintel_lvl_improv_reg_rural['Number'][0]
        struct_lintel_lvl_with_improv_roof_reg_rural_percent = df_struct_lintel_lvl_improv_reg_rural['Percent'][0]
        struct_lintel_lvl_with_improv_roof_rural_val = df_struct_lintel_lvl_improv_reg_rural[district][0]
        struct_lintel_lvl_wth_improv_roof_rural_percent = (struct_lintel_lvl_with_improv_roof_rural_val / struct_rural_total) * 100

        # roofing level without roof
        df_struct_roof_lvl_wout_roof_reg_rural = df_rural = \
            df_data[((df_data['Type'] == 'Rural')) & (df_data['Status_Code'] == '1-6')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_roof_lvl_wout_roof_reg_rural = df_struct_roof_lvl_wout_roof_reg_rural.reset_index(drop=True)

        struct_roof_lvl_wout_roof_reg_rural_val = df_struct_roof_lvl_wout_roof_reg_rural['Number'][0]
        struct_roof_lvl_wout_roof_reg_rural_percent = df_struct_roof_lvl_wout_roof_reg_rural['Percent'][0]
        struct_roof_lvl_wout_roof_rural_val = df_struct_roof_lvl_wout_roof_reg_rural[district][0]
        struct_roof_lvl_wout_roof_rural_percent = (struct_roof_lvl_wout_roof_rural_val / struct_rural_total) * 100

        # lintel Level without roof
        df_struct_lintel_lvl_wout_roof_rural = df_rural = \
            df_data[((df_data['Type'] == 'Rural')) & (df_data['Status_Code'] == '1-7')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_lintel_lvl_wout_roof_rural = df_struct_lintel_lvl_wout_roof_rural.reset_index(drop=True)

        struct_lintel_lvl_wout_roof_reg_rural_val = df_struct_lintel_lvl_wout_roof_rural['Number'][0]
        struct_lintel_lvl_wout_roof_reg_rural_percent = df_struct_lintel_lvl_wout_roof_rural['Percent'][0]
        struct_lintel_lvl_wout_roof_rural_val = df_struct_lintel_lvl_wout_roof_rural[district][0]
        struct_lintel_lvl_wout_roof_rural_percent = (struct_lintel_lvl_wout_roof_rural_val / struct_rural_total) * 100

        # window level
        df_struct_window_lvl_rural = df_rural = \
            df_data[((df_data['Type'] == 'Rural')) & (df_data['Status_Code'] == '1-8')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_window_lvl_rural = df_struct_window_lvl_rural.reset_index(drop=True)

        struct_window_lvl_reg_rural_val = df_struct_window_lvl_rural['Number'][0]
        struct_window_lvl_reg_rural_percent = df_struct_window_lvl_rural['Percent'][0]
        struct_window_lvl_rural_val = df_struct_window_lvl_rural[district][0]
        struct_window_lvl_rural_percent = (struct_window_lvl_rural_val / struct_rural_total) * 100

        # concrete/metal pillars
        df_struct_conc_metal_pill_rural = df_rural = \
            df_data[((df_data['Type'] == 'Rural')) & (df_data['Status_Code'] == '1-9')][
                ['Structure_Type', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_struct_conc_metal_pill_rural = df_struct_conc_metal_pill_rural.reset_index(drop=True)

        struct_conc_metal_pill_reg_rural_val = df_struct_conc_metal_pill_rural['Number'][0]
        struct_window_lvl_reg_reg_rural_percent = df_struct_conc_metal_pill_rural['Percent'][0]
        struct_conc_metal_pill_rural_val = df_struct_conc_metal_pill_rural[district][0]
        struct_conc_metal_pill_rural_percent = struct_window_lvl_rural_percent = (struct_conc_metal_pill_rural_val / struct_rural_total) * 100

        # Formatting
        #***********

        #total
        struct_rural_reg_total = '{:,}'.format(struct_rural_reg_total)
        struct_rural_reg_percent = '{:,.1f}'.format(struct_rural_reg_percent)
        struct_rural_total = '{:,}'.format(struct_rural_total)
        struct_rural_percent = '{:,.1f}'.format(struct_rural_percent)

        # fully completed
        struct_fully_compl_reg_rural_val = '{:,}'.format(struct_fully_compl_reg_rural_val)
        struct_fully_compl_reg_rural_percent = '{:,.1f}'.format(struct_fully_compl_reg_rural_percent)
        struct_fully_compl_rural_val = '{:,}'.format(struct_fully_compl_rural_val)
        struct_fully_compl_rural_percent = '{:,.1f}'.format(struct_fully_compl_rural_percent)

        #completely roofed but uncompleted
        struct_compl_roofed_uncom_reg_rural_val = '{:,}'.format(struct_compl_roofed_uncom_reg_rural_val)
        struct_compl_roofed_uncom_reg_rural_percent = '{:,.1f}'.format(struct_compl_roofed_uncom_reg_rural_percent)
        struct_compl_roofed_uncom_rural_val = '{:,}'.format(struct_compl_roofed_uncom_rural_val)
        struct_compl_roofed_uncom_rural_percent = '{:,.1f}'.format(struct_compl_roofed_uncom_rural_percent)

        #partially roofed
        struct_part_roofed_reg_rural_val = '{:,}'.format(struct_part_roofed_reg_rural_val)
        struct_part_roofed_reg_rural_percent = '{:,.1f}'.format(struct_part_roofed_reg_rural_percent)
        struct_part_roofed_rural_val = '{:,}'.format(struct_part_roofed_rural_val)
        struct_part_roofed_rural_percent = '{:,.1f}'.format(struct_part_roofed_rural_percent)

        #roofing level with improvised roof
        struct_roof_lvl_with_improv_reg_rural_val = '{:,}'.format(struct_roof_lvl_with_improv_reg_rural_val)
        struct_roof_lvl_with_improv_reg_rural_percent = '{:,.1f}'.format(struct_roof_lvl_with_improv_reg_rural_percent)
        struct_roof_lvl_with_improv_rural_val = '{:,}'.format(struct_roof_lvl_with_improv_rural_val)
        struct_roof_lvl_with_improv_rural_percent = '{:,.1f}'.format(struct_roof_lvl_with_improv_rural_percent)

        #lintel level with improvised roof
        struct_lintel_lvl_with_improv_roof_reg_rural_val = '{:,}'.format(struct_lintel_lvl_with_improv_roof_reg_rural_val)
        struct_lintel_lvl_with_improv_roof_reg_rural_percent = '{:,.1f}'.format(struct_lintel_lvl_with_improv_roof_reg_rural_percent)
        struct_lintel_lvl_with_improv_roof_rural_val = '{:,}'.format(struct_lintel_lvl_with_improv_roof_rural_val)
        struct_lintel_lvl_with_improv_roof_rural_percent = '{:,.1f}'.format(struct_lintel_lvl_wth_improv_roof_rural_percent)

        # roofing level without roof
        struct_roof_lvl_wout_roof_reg_rural_val = '{:,}'.format(struct_roof_lvl_wout_roof_reg_rural_val)
        struct_roof_lvl_wout_roof_reg_rural_percent = '{:,.1f}'.format(struct_roof_lvl_wout_roof_reg_rural_percent)
        struct_roof_lvl_wout_roof_rural_val = '{:,}'.format(struct_roof_lvl_wout_roof_rural_val)
        struct_roof_lvl_wout_roof_rural_percent = '{:,.1f}'.format(struct_roof_lvl_wout_roof_rural_percent)

        #lintel level without roof
        struct_lintel_lvl_wout_roof_reg_rural_val = '{:,}'.format(struct_lintel_lvl_wout_roof_reg_rural_val)
        struct_lintel_lvl_wout_roof_reg_rural_percent = '{:,.1f}'.format(struct_lintel_lvl_wout_roof_reg_rural_percent)
        struct_lintel_lvl_wout_roof_rural_val = '{:,}'.format(struct_lintel_lvl_wout_roof_rural_val)
        struct_lintel_lvl_wout_roof_rural_percent = '{:,.1f}'.format(struct_lintel_lvl_wout_roof_rural_percent)

        # windows level
        struct_window_lvl_reg_rural_val = '{:,}'.format(struct_window_lvl_reg_rural_val)
        struct_window_lvl_reg_rural_percent = '{:,.1f}'.format(struct_window_lvl_reg_rural_percent)
        struct_window_lvl_rural_val = '{:,}'.format(struct_window_lvl_rural_val)
        struct_window_lvl_rural_percent = '{:,.1f}'.format(struct_window_lvl_rural_percent)

        #concrete/metal pillars
        struct_conc_metal_pill_reg_rural_val = '{:,}'.format(struct_conc_metal_pill_reg_rural_val)
        struct_conc_metal_pill_reg_rural_percent = '{:,.1f}'.format(struct_window_lvl_reg_reg_rural_percent)
        struct_conc_metal_pill_rural_val = '{:,}'.format(struct_conc_metal_pill_rural_val)
        struct_conc_metal_pill_rural_percent = '{:,.1f}'.format(struct_conc_metal_pill_rural_percent)

    return struct_rural_reg_total, struct_rural_reg_percent, struct_rural_total, struct_rural_percent, \
           struct_fully_compl_reg_rural_val, struct_fully_compl_reg_rural_percent, struct_fully_compl_rural_val, struct_fully_compl_rural_percent, \
           struct_compl_roofed_uncom_reg_rural_val, struct_compl_roofed_uncom_reg_rural_percent, struct_compl_roofed_uncom_rural_val, struct_compl_roofed_uncom_rural_percent, \
           struct_part_roofed_reg_rural_val, struct_part_roofed_reg_rural_percent, struct_part_roofed_rural_val, struct_part_roofed_rural_percent, \
           struct_roof_lvl_with_improv_reg_rural_val, struct_roof_lvl_with_improv_reg_rural_percent, struct_roof_lvl_with_improv_rural_val, struct_roof_lvl_with_improv_rural_percent, \
           struct_lintel_lvl_with_improv_roof_reg_rural_val, struct_lintel_lvl_with_improv_roof_reg_rural_percent, struct_lintel_lvl_with_improv_roof_rural_val, struct_lintel_lvl_with_improv_roof_rural_percent, \
           struct_roof_lvl_wout_roof_reg_rural_val, struct_roof_lvl_wout_roof_reg_rural_percent, struct_roof_lvl_wout_roof_rural_val, struct_roof_lvl_wout_roof_rural_percent, \
           struct_lintel_lvl_wout_roof_reg_rural_val, struct_lintel_lvl_wout_roof_reg_rural_percent, struct_lintel_lvl_wout_roof_rural_val, struct_lintel_lvl_wout_roof_rural_percent, \
           struct_window_lvl_reg_rural_val, struct_window_lvl_reg_rural_percent, struct_window_lvl_rural_val, struct_window_lvl_rural_percent, \
           struct_conc_metal_pill_reg_rural_val, struct_conc_metal_pill_reg_rural_percent, struct_conc_metal_pill_rural_val, struct_conc_metal_pill_rural_percent


# ***********************************
    # ECONOMIC ACTIVITIES - ALL
# **********************************
@app.callback(

    # All, Total
    Output('econ_act_reg_all_total', 'children'),
    Output('econ_act_reg_all_percent', 'children'),
    Output('econ_act_all_total', 'children'),
    #Output('econ_act_all_percent', 'children'),

    # All, Labor Force
    Output('econ_act_labor_fx_reg_all_val', 'children'),
    Output('econ_act_labor_fx_reg_all_percent', 'children'),
    Output('econ_act_labor_fx_all_val', 'children'),
    Output('econ_act_labor_fx_all_percent', 'children'),

    # All, Employed
    Output('econ_act_employ_reg_all_val', 'children'),
    Output('econ_act_employ_reg_all_percent', 'children'),
    Output('econ_act_employ_all_val', 'children'),
    Output('econ_act_employ_all_percent', 'children'),

    # All, Unemployed
    Output('econ_act_unemploy_reg_all_val', 'children'),
    Output('econ_act_unemploy_reg_all_percent', 'children'),
    Output('econ_act_unemploy_all_val', 'children'),
    Output('econ_act_unemploy_all_percent', 'children'),

    # All, Population outside labor force
    Output('econ_act_pop_outs_labor_fx_reg_all_val', 'children'),
    Output('econ_act_pop_outs_labor_fx_reg_all_percent', 'children'),
    Output('econ_act_pop_outs_labor_fx_all_val', 'children'),
    Output('econ_act_pop_outs_labor_fx_all_percent', 'children'),

    Input('econ_act_region_dd', 'value'),
    Input('econ_act_district_dd', 'value')
)

def get_econ_act_all(region, district):

    # all, total
    econ_act_reg_all_total = None
    econ_act_reg_all_percent = None
    econ_act_all_total = None
    econ_act_all_percent = None

    # all, labor force
    econ_act_labor_fx_reg_all_val = None
    econ_act_labor_fx_reg_all_percent = None
    econ_act_labor_fx_all_val = None
    econ_act_labor_fx_all_percent = None

    # all, employed
    econ_act_employ_reg_all_val = None
    econ_act_employ_reg_all_percent = None
    econ_act_employ_all_val = None
    econ_act_employ_all_percent = None

    # all, unemployed
    econ_act_unemploy_reg_all_val = None
    econ_act_unemploy_reg_all_percent = None
    econ_act_unemploy_all_val = None
    econ_act_unemploy_all_percent = None

    # all, population outside labor force
    econ_act_pop_outs_labor_fx_reg_all_val = None
    econ_act_pop_outs_labor_fx_reg_all_percent = None
    econ_act_pop_outs_labor_fx_all_val = None
    econ_act_pop_outs_labor_fx_all_percent = None

    if (region != None) & (district != None):

        # GET DATA
        df_data = df_econ_act_dic[region]

        # ALL
        df_total_all = \
        df_data[(df_data['Activity_Status'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'All')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_total_all = df_total_all.reset_index(drop=True)

        econ_act_reg_all_total = df_total_all['Number'][0]
        econ_act_reg_all_percent = df_total_all['Percent'][0]
        econ_act_all_total = df_total_all[district][0]
        #econ_act_all_percent = 100.0

        #ALL - District Details
        # **********************************************

        # All, Labor Force
        df_labor_fx_all = df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '1')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_labor_fx_all = df_labor_fx_all.reset_index(drop=True)

        econ_act_labor_fx_reg_all_val = df_labor_fx_all['Number'][0]
        econ_act_labor_fx_reg_all_percent = df_labor_fx_all['Percent'][0]
        econ_act_labor_fx_all_val = df_labor_fx_all[district][0]
        econ_act_labor_fx_all_percent = (econ_act_labor_fx_all_val / econ_act_reg_all_total) * 100

        # All, Employed
        df_all_employ = df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '1-1')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_all_employ = df_all_employ.reset_index(drop=True)

        econ_act_employ_reg_all_val = df_all_employ['Number'][0]
        econ_act_employ_reg_all_percent = df_all_employ['Percent'][0]
        econ_act_employ_all_val = df_all_employ[district][0]
        econ_act_employ_all_percent = (econ_act_employ_all_val / econ_act_reg_all_total) * 100

        # All, Unmployed
        df_all_unemploy = df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '1-2')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_all_unemploy = df_all_unemploy.reset_index(drop=True)

        econ_act_unemploy_reg_all_val = df_all_unemploy['Number'][0]
        econ_act_unemploy_reg_all_percent = df_all_unemploy['Percent'][0]
        econ_act_unemploy_all_val = df_all_unemploy[district][0]
        econ_act_unemploy_all_percent = (econ_act_unemploy_all_val / econ_act_reg_all_total) * 100

        # All, Population outside labor force
        df_all_pop_outs_labor_fx = df_data[((df_data['Type'] == 'All')) & (df_data['Status_Code'] == '2')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_all_pop_outs_labor_fx = df_all_pop_outs_labor_fx.reset_index(drop=True)

        econ_act_pop_outs_labor_fx_reg_all_val = df_all_pop_outs_labor_fx['Number'][0]
        econ_act_pop_outs_labor_fx_reg_all_percent = df_all_pop_outs_labor_fx['Percent'][0]
        econ_act_pop_outs_labor_fx_all_val = df_all_pop_outs_labor_fx[district][0]
        econ_act_pop_outs_labor_fx_all_percent = (econ_act_pop_outs_labor_fx_all_val / econ_act_reg_all_total) * 100

        # Formatting

        # all, total
        econ_act_reg_all_total = '{:,}'.format(econ_act_reg_all_total)
        econ_act_reg_all_percent = '{:.1f}'.format(econ_act_reg_all_percent)
        econ_act_all_total = '{:,}'.format(econ_act_all_total)
        #econ_act_all_percent = '{:.1f}'.format(econ_act_all_percent)

        # all, labor force
        econ_act_labor_fx_reg_all_val = '{:,}'.format(econ_act_labor_fx_reg_all_val)
        econ_act_labor_fx_reg_all_percent = '{:.1f}'.format(econ_act_labor_fx_reg_all_percent)
        econ_act_labor_fx_all_val = '{:,}'.format(econ_act_labor_fx_all_val)
        econ_act_labor_fx_all_percent = '{:.1f}'.format(econ_act_labor_fx_all_percent)

        # all, employed
        econ_act_employ_reg_all_val = '{:,}'.format(econ_act_employ_reg_all_val)
        econ_act_employ_reg_all_percent = '{:.1f}'.format(econ_act_employ_reg_all_percent)
        econ_act_employ_all_val = '{:,}'.format(econ_act_employ_all_val)
        econ_act_employ_all_percent = '{:.1f}'.format(econ_act_employ_all_percent)

        # all, unemployed
        econ_act_unemploy_reg_all_val = '{:,}'.format(econ_act_unemploy_reg_all_val)
        econ_act_unemploy_reg_all_percent = '{:.1f}'.format(econ_act_unemploy_reg_all_percent)
        econ_act_unemploy_all_val = '{:,}'.format(econ_act_unemploy_all_val)
        econ_act_unemploy_all_percent = '{:.1f}'.format(econ_act_unemploy_all_percent)

        # all, population outside labor force
        econ_act_pop_outs_labor_fx_reg_all_val = '{:,}'.format(econ_act_pop_outs_labor_fx_reg_all_val)
        econ_act_pop_outs_labor_fx_reg_all_percent = '{:.1f}'.format(econ_act_pop_outs_labor_fx_reg_all_percent)
        econ_act_pop_outs_labor_fx_all_val = '{:,}'.format(econ_act_pop_outs_labor_fx_all_val)
        econ_act_pop_outs_labor_fx_all_percent = '{:.1f}'.format(econ_act_pop_outs_labor_fx_all_percent)


    return econ_act_reg_all_total, econ_act_reg_all_percent, econ_act_all_total, \
           econ_act_labor_fx_reg_all_val, econ_act_labor_fx_reg_all_percent, econ_act_labor_fx_all_val, econ_act_labor_fx_all_percent, \
           econ_act_employ_reg_all_val, econ_act_employ_reg_all_percent, econ_act_employ_all_val, econ_act_employ_all_percent, \
           econ_act_unemploy_reg_all_val, econ_act_unemploy_reg_all_percent, econ_act_unemploy_all_val, econ_act_unemploy_all_percent, \
           econ_act_pop_outs_labor_fx_reg_all_val, econ_act_pop_outs_labor_fx_reg_all_percent, econ_act_pop_outs_labor_fx_all_val, econ_act_pop_outs_labor_fx_all_percent


#************************************************************
# ECONOMIC ACTIVITIES - MALE
# ***********************************************************

@app.callback(

    # Male, Total
    Output('econ_act_reg_male_total', 'children'),
    Output('econ_act_reg_male_percent', 'children'),
    Output('econ_act_male_total', 'children'),
    #Output('econ_act_male_percent', 'children'),

    # Male, Labor Force
    Output('econ_act_labor_fx_reg_male_val', 'children'),
    Output('econ_act_labor_fx_reg_male_percent', 'children'),
    Output('econ_act_labor_fx_male_val', 'children'),
    Output('econ_act_labor_fx_male_percent', 'children'),

    # Male, Employed
    Output('econ_act_employ_reg_male_val', 'children'),
    Output('econ_act_employ_reg_male_percent', 'children'),
    Output('econ_act_employ_male_val', 'children'),
    Output('econ_act_employ_male_percent', 'children'),

    # Male, Unemployed
    Output('econ_act_unemploy_reg_male_val', 'children'),
    Output('econ_act_unemploy_reg_male_percent', 'children'),
    Output('econ_act_unemploy_male_val', 'children'),
    Output('econ_act_unemploy_male_percent', 'children'),

    # Male, Population outside labor force
    Output('econ_act_pop_outs_labor_fx_reg_male_val', 'children'),
    Output('econ_act_pop_outs_labor_fx_reg_male_percent', 'children'),
    Output('econ_act_pop_outs_labor_fx_male_val', 'children'),
    Output('econ_act_pop_outs_labor_fx_male_percent', 'children'),

    Input('econ_act_region_dd', 'value'),
    Input('econ_act_district_dd', 'value')
)

def get_econ_act_male(region, district):

    # male, total
    econ_act_reg_male_total = None
    econ_act_reg_male_percent = None
    econ_act_male_total = None
    econ_act_male_percent = None

    # male, labor force
    econ_act_labor_fx_reg_male_val = None
    econ_act_labor_fx_reg_male_percent = None
    econ_act_labor_fx_male_val = None
    econ_act_labor_fx_male_percent = None

    # male, employed
    econ_act_employ_reg_male_val = None
    econ_act_employ_reg_male_percent = None
    econ_act_employ_male_val = None
    econ_act_employ_male_percent = None

    # male, unemployed
    econ_act_unemploy_reg_male_val = None
    econ_act_unemploy_reg_male_percent = None
    econ_act_unemploy_male_val = None
    econ_act_unemploy_male_percent = None

    # male, population outside labor force
    econ_act_pop_outs_labor_fx_reg_male_val = None
    econ_act_pop_outs_labor_fx_reg_male_percent = None
    econ_act_pop_outs_labor_fx_male_val = None
    econ_act_pop_outs_labor_fx_male_percent = None

    if (region != None) & (district != None):

        # GET DATA
        df_data = df_econ_act_dic[region]

        # male
        df_total_male = \
        df_data[(df_data['Activity_Status'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'Male')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_total_male = df_total_male.reset_index(drop=True)

        econ_act_reg_male_total = df_total_male['Number'][0]
        econ_act_reg_male_percent = df_total_male['Percent'][0]
        econ_act_male_total = df_total_male[district][0]
        #econ_act_male_percent = 100.0

        #male - District Details
        # **********************************************

        # male, Labor Force
        df_labor_fx_male = df_data[((df_data['Type'] == 'Male')) & (df_data['Status_Code'] == '1')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_labor_fx_male = df_labor_fx_male.reset_index(drop=True)

        econ_act_labor_fx_reg_male_val = df_labor_fx_male['Number'][0]
        econ_act_labor_fx_reg_male_percent = df_labor_fx_male['Percent'][0]
        econ_act_labor_fx_male_val = df_labor_fx_male[district][0]
        econ_act_labor_fx_male_percent = (econ_act_labor_fx_male_val / econ_act_reg_male_total) * 100

        # male, Employed
        df_male_employ = df_data[((df_data['Type'] == 'Male')) & (df_data['Status_Code'] == '1-1')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_male_employ = df_male_employ.reset_index(drop=True)

        econ_act_employ_reg_male_val = df_male_employ['Number'][0]
        econ_act_employ_reg_male_percent = df_male_employ['Percent'][0]
        econ_act_employ_male_val = df_male_employ[district][0]
        econ_act_employ_male_percent = (econ_act_employ_male_val / econ_act_reg_male_total) * 100

        # male, Unmployed
        df_male_unemploy = df_data[((df_data['Type'] == 'Male')) & (df_data['Status_Code'] == '1-2')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_male_unemploy = df_male_unemploy.reset_index(drop=True)

        econ_act_unemploy_reg_male_val = df_male_unemploy['Number'][0]
        econ_act_unemploy_reg_male_percent = df_male_unemploy['Percent'][0]
        econ_act_unemploy_male_val = df_male_unemploy[district][0]
        econ_act_unemploy_male_percent = (econ_act_unemploy_male_val / econ_act_reg_male_total) * 100

        # male, Population outside labor force
        df_male_pop_outs_labor_fx = df_data[((df_data['Type'] == 'Male')) & (df_data['Status_Code'] == '2')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_male_pop_outs_labor_fx = df_male_pop_outs_labor_fx.reset_index(drop=True)

        econ_act_pop_outs_labor_fx_reg_male_val = df_male_pop_outs_labor_fx['Number'][0]
        econ_act_pop_outs_labor_fx_reg_male_percent = df_male_pop_outs_labor_fx['Percent'][0]
        econ_act_pop_outs_labor_fx_male_val = df_male_pop_outs_labor_fx[district][0]
        econ_act_pop_outs_labor_fx_male_percent = (econ_act_pop_outs_labor_fx_male_val / econ_act_reg_male_total) * 100

        # Formatting
        # male, total
        econ_act_reg_male_total = '{:,}'.format(econ_act_reg_male_total)
        econ_act_reg_male_percent = '{:.1f}'.format(econ_act_reg_male_percent)
        econ_act_male_total = '{:,}'.format(econ_act_male_total)
        #econ_act_male_percent = '{:.1f}'.format(econ_act_male_percent)

        # male, labor force
        econ_act_labor_fx_reg_male_val = '{:,}'.format(econ_act_labor_fx_reg_male_val)
        econ_act_labor_fx_reg_male_percent = '{:.1f}'.format(econ_act_labor_fx_reg_male_percent)
        econ_act_labor_fx_male_val = '{:,}'.format(econ_act_labor_fx_male_val)
        econ_act_labor_fx_male_percent = '{:.1f}'.format(econ_act_labor_fx_male_percent)

        # male, employed
        econ_act_employ_reg_male_val = '{:,}'.format(econ_act_employ_reg_male_val)
        econ_act_employ_reg_male_percent = '{:.1f}'.format(econ_act_employ_reg_male_percent)
        econ_act_employ_male_val = '{:,}'.format(econ_act_employ_male_val)
        econ_act_employ_male_percent = '{:.1f}'.format(econ_act_employ_male_percent)

        # male, unemployed
        econ_act_unemploy_reg_male_val = '{:,}'.format(econ_act_unemploy_reg_male_val)
        econ_act_unemploy_reg_male_percent = '{:.1f}'.format(econ_act_unemploy_reg_male_percent)
        econ_act_unemploy_male_val = '{:,}'.format(econ_act_unemploy_male_val)
        econ_act_unemploy_male_percent = '{:.1f}'.format(econ_act_unemploy_male_percent)

        # male, population outside labor force
        econ_act_pop_outs_labor_fx_reg_male_val = '{:,}'.format(econ_act_pop_outs_labor_fx_reg_male_val)
        econ_act_pop_outs_labor_fx_reg_male_percent = '{:.1f}'.format(econ_act_pop_outs_labor_fx_reg_male_percent)
        econ_act_pop_outs_labor_fx_male_val = '{:,}'.format(econ_act_pop_outs_labor_fx_male_val)
        econ_act_pop_outs_labor_fx_male_percent = '{:.1f}'.format(econ_act_pop_outs_labor_fx_male_percent)

    return econ_act_reg_male_total, econ_act_reg_male_percent, econ_act_male_total, \
           econ_act_labor_fx_reg_male_val, econ_act_labor_fx_reg_male_percent, econ_act_labor_fx_male_val, econ_act_labor_fx_male_percent, \
           econ_act_employ_reg_male_val, econ_act_employ_reg_male_percent, econ_act_employ_male_val, econ_act_employ_male_percent, \
           econ_act_unemploy_reg_male_val, econ_act_unemploy_reg_male_percent, econ_act_unemploy_male_val, econ_act_unemploy_male_percent, \
           econ_act_pop_outs_labor_fx_reg_male_val, econ_act_pop_outs_labor_fx_reg_male_percent, econ_act_pop_outs_labor_fx_male_val, econ_act_pop_outs_labor_fx_male_percent


#************************************************************
# ECONOMIC ACTIVITIES - FEMALE
# ***********************************************************

@app.callback(

    # Female, Total
    Output('econ_act_reg_female_total', 'children'),
    Output('econ_act_reg_female_percent', 'children'),
    Output('econ_act_female_total', 'children'),
    #Output('econ_act_female_percent', 'children'),

    # Female, Labor Force
    Output('econ_act_labor_fx_reg_female_val', 'children'),
    Output('econ_act_labor_fx_reg_female_percent', 'children'),
    Output('econ_act_labor_fx_female_val', 'children'),
    Output('econ_act_labor_fx_female_percent', 'children'),

    # Female, Employed
    Output('econ_act_employ_reg_female_val', 'children'),
    Output('econ_act_employ_reg_female_percent', 'children'),
    Output('econ_act_employ_female_val', 'children'),
    Output('econ_act_employ_female_percent', 'children'),

    # Female, Unemployed
    Output('econ_act_unemploy_reg_female_val', 'children'),
    Output('econ_act_unemploy_reg_female_percent', 'children'),
    Output('econ_act_unemploy_female_val', 'children'),
    Output('econ_act_unemploy_female_percent', 'children'),

    # Female, Population outside labor force
    Output('econ_act_pop_outs_labor_fx_reg_female_val', 'children'),
    Output('econ_act_pop_outs_labor_fx_reg_female_percent', 'children'),
    Output('econ_act_pop_outs_labor_fx_female_val', 'children'),
    Output('econ_act_pop_outs_labor_fx_female_percent', 'children'),

    Input('econ_act_region_dd', 'value'),
    Input('econ_act_district_dd', 'value')
)

def get_econ_act_female(region, district):

    # female, total
    econ_act_reg_female_total = None
    econ_act_reg_female_percent = None
    econ_act_female_total = None
    econ_act_female_percent = None

    # female, labor force
    econ_act_labor_fx_reg_female_val = None
    econ_act_labor_fx_reg_female_percent = None
    econ_act_labor_fx_female_val = None
    econ_act_labor_fx_female_percent = None

    # female, employed
    econ_act_employ_reg_female_val = None
    econ_act_employ_reg_female_percent = None
    econ_act_employ_female_val = None
    econ_act_employ_female_percent = None

    # female, unemployed
    econ_act_unemploy_reg_female_val = None
    econ_act_unemploy_reg_female_percent = None
    econ_act_unemploy_female_val = None
    econ_act_unemploy_female_percent = None

    # female, population outside labor force
    econ_act_pop_outs_labor_fx_reg_female_val = None
    econ_act_pop_outs_labor_fx_reg_female_percent = None
    econ_act_pop_outs_labor_fx_female_val = None
    econ_act_pop_outs_labor_fx_female_percent = None

    if (region != None) & (district != None):

        # GET DATA
        df_data = df_econ_act_dic[region]

        # female
        df_total_female = \
        df_data[(df_data['Activity_Status'] == 'Total') & (df_data['Status_Code'] == '0') & (df_data['Type'] == 'Female')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_total_female = df_total_female.reset_index(drop=True)

        econ_act_reg_female_total = df_total_female['Number'][0]
        econ_act_reg_female_percent = df_total_female['Percent'][0]
        econ_act_female_total = df_total_female[district][0]
        #econ_act_female_percent = 100.0

        #female - District Details
        # **********************************************

        # female, Labor Force
        df_labor_fx_female = df_data[((df_data['Type'] == 'Female')) & (df_data['Status_Code'] == '1')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_labor_fx_female = df_labor_fx_female.reset_index(drop=True)

        econ_act_labor_fx_reg_female_val = df_labor_fx_female['Number'][0]
        econ_act_labor_fx_reg_female_percent = df_labor_fx_female['Percent'][0]
        econ_act_labor_fx_female_val = df_labor_fx_female[district][0]
        econ_act_labor_fx_female_percent = (econ_act_labor_fx_female_val / econ_act_reg_female_total) * 100

        # female, Employed
        df_female_employ = df_data[((df_data['Type'] == 'Female')) & (df_data['Status_Code'] == '1-1')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_female_employ = df_female_employ.reset_index(drop=True)

        econ_act_employ_reg_female_val = df_female_employ['Number'][0]
        econ_act_employ_reg_female_percent = df_female_employ['Percent'][0]
        econ_act_employ_female_val = df_female_employ[district][0]
        econ_act_employ_female_percent = (econ_act_employ_female_val / econ_act_reg_female_total) * 100

        # female, Unmployed
        df_female_unemploy = df_data[((df_data['Type'] == 'Female')) & (df_data['Status_Code'] == '1-2')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_female_unemploy = df_female_unemploy.reset_index(drop=True)

        econ_act_unemploy_reg_female_val = df_female_unemploy['Number'][0]
        econ_act_unemploy_reg_female_percent = df_female_unemploy['Percent'][0]
        econ_act_unemploy_female_val = df_female_unemploy[district][0]
        econ_act_unemploy_female_percent = (econ_act_unemploy_female_val / econ_act_reg_female_total) * 100

        # female, Population outside labor force
        df_female_pop_outs_labor_fx = df_data[((df_data['Type'] == 'Female')) & (df_data['Status_Code'] == '2')][
            ['Activity_Status', 'Type', 'Status_Code', 'Number', 'Percent', district]]
        df_female_pop_outs_labor_fx = df_female_pop_outs_labor_fx.reset_index(drop=True)

        econ_act_pop_outs_labor_fx_reg_female_val = df_female_pop_outs_labor_fx['Number'][0]
        econ_act_pop_outs_labor_fx_reg_female_percent = df_female_pop_outs_labor_fx['Percent'][0]
        econ_act_pop_outs_labor_fx_female_val = df_female_pop_outs_labor_fx[district][0]
        econ_act_pop_outs_labor_fx_female_percent = (econ_act_pop_outs_labor_fx_female_val / econ_act_reg_female_total) * 100

        # Formatting
        # female, total
        econ_act_reg_female_total = '{:,}'.format(econ_act_reg_female_total)
        econ_act_reg_female_percent = '{:.1f}'.format(econ_act_reg_female_percent)
        econ_act_female_total = '{:,}'.format(econ_act_female_total)
        #econ_act_female_percent = '{:.1f}'.format(econ_act_female_percent)

        # female, labor force
        econ_act_labor_fx_reg_female_val = '{:,}'.format(econ_act_labor_fx_reg_female_val)
        econ_act_labor_fx_reg_female_percent = '{:.1f}'.format(econ_act_labor_fx_reg_female_percent)
        econ_act_labor_fx_female_val = '{:,}'.format(econ_act_labor_fx_female_val)
        econ_act_labor_fx_female_percent = '{:.1f}'.format(econ_act_labor_fx_female_percent)

        # female, employed
        econ_act_employ_reg_female_val = '{:,}'.format(econ_act_employ_reg_female_val)
        econ_act_employ_reg_female_percent = '{:.1f}'.format(econ_act_employ_reg_female_percent)
        econ_act_employ_female_val = '{:,}'.format(econ_act_employ_female_val)
        econ_act_employ_female_percent = '{:.1f}'.format(econ_act_employ_female_percent)

        # female, unemployed
        econ_act_unemploy_reg_female_val = '{:,}'.format(econ_act_unemploy_reg_female_val)
        econ_act_unemploy_reg_female_percent = '{:.1f}'.format(econ_act_unemploy_reg_female_percent)
        econ_act_unemploy_female_val = '{:,}'.format(econ_act_unemploy_female_val)
        econ_act_unemploy_female_percent = '{:.1f}'.format(econ_act_unemploy_female_percent)

        # female, population outside labor force
        econ_act_pop_outs_labor_fx_reg_female_val = '{:,}'.format(econ_act_pop_outs_labor_fx_reg_female_val)
        econ_act_pop_outs_labor_fx_reg_female_percent = '{:.1f}'.format(econ_act_pop_outs_labor_fx_reg_female_percent)
        econ_act_pop_outs_labor_fx_female_val = '{:,}'.format(econ_act_pop_outs_labor_fx_female_val)
        econ_act_pop_outs_labor_fx_female_percent = '{:.1f}'.format(econ_act_pop_outs_labor_fx_female_percent)

    return econ_act_reg_female_total, econ_act_reg_female_percent, econ_act_female_total, \
           econ_act_labor_fx_reg_female_val, econ_act_labor_fx_reg_female_percent, econ_act_labor_fx_female_val, econ_act_labor_fx_female_percent, \
           econ_act_employ_reg_female_val, econ_act_employ_reg_female_percent, econ_act_employ_female_val, econ_act_employ_female_percent, \
           econ_act_unemploy_reg_female_val, econ_act_unemploy_reg_female_percent, econ_act_unemploy_female_val, econ_act_unemploy_female_percent, \
           econ_act_pop_outs_labor_fx_reg_female_val, econ_act_pop_outs_labor_fx_reg_female_percent, econ_act_pop_outs_labor_fx_female_val, econ_act_pop_outs_labor_fx_female_percent

#***********************************************************
#   ICT: All, Both Sexes
#***********************************************************
@app.callback(

    # all
    Output('ict_reg_all_total', 'children'),
    Output('ict_reg_all_percent', 'children'),
    Output('ict_all_total', 'children'),
    Output('ict_all_percent', 'children'),

    # all, mobile phone (smart)
    Output('ict_mob_phone_smart_reg_all_val', 'children'),
    Output('ict_mob_phone_smart_reg_all_percent', 'children'),
    Output('ict_mob_phone_smart_all_val', 'children'),
    Output('ict_mob_phone_smart_all_percent', 'children'),

    # all, mobile phone (non-smart)
    Output('ict_mob_phone_non_smart_reg_all_val', 'children'),
    Output('ict_mob_phone_non_smart_reg_all_percent', 'children'),
    Output('ict_mob_phone_non_smart_all_val', 'children'),
    Output('ict_mob_phone_non_smart_all_percent', 'children'),

    # all, tablet
    Output('ict_tablet_reg_all_val', 'children'),
    Output('ict_tablet_reg_all_percent', 'children'),
    Output('ict_tablet_all_val', 'children'),
    Output('ict_tablet_all_percent', 'children'),

    # all, laptop
    Output('ict_laptop_reg_all_val', 'children'),
    Output('ict_laptop_reg_all_percent', 'children'),
    Output('ict_laptop_all_val', 'children'),
    Output('ict_laptop_all_percent', 'children'),

    # all, none
    Output('ict_none_reg_all_val', 'children'),
    Output('ict_none_reg_all_percent', 'children'),
    Output('ict_none_all_val', 'children'),
    Output('ict_none_all_percent', 'children'),

    Input('ict_region_dd', 'value'),
    Input('ict_district_dd', 'value')
)
def get_ict_all_both_sexes(region, district):

    # All, Regional
    ict_reg_all_total = None
    ict_reg_all_percent = None
    ict_all_total = None
    ict_all_percent = None

    # All, Mobile Phone (Smart)
    ict_mob_phone_smart_reg_all_val = None
    ict_mob_phone_smart_reg_all_percent = None
    ict_mob_phone_smart_all_val = None
    ict_mob_phone_smart_all_percent = None

    # All, Mobile Phone (Non-Smart)
    ict_mob_phone_non_smart_reg_all_val = None
    ict_mob_phone_non_smart_reg_all_percent = None
    ict_mob_phone_non_smart_all_val = None
    ict_mob_phone_non_smart_all_percent = None

    # All, Tablet
    ict_tablet_reg_all_val = None
    ict_tablet_reg_all_percent = None
    ict_tablet_all_val = None
    ict_tablet_all_percent = None

    # All, Laptop
    ict_laptop_reg_all_val = None
    ict_laptop_reg_all_percent = None
    ict_laptop_all_val = None
    ict_laptop_all_percent = None

    # All, None
    ict_none_reg_all_val = None
    ict_none_reg_all_percent = None
    ict_none_all_val = None
    ict_none_all_percent = None

    if (region != None) & (district != None):

        # get data
        df_data = df_ict_dic[region]

        # All, Total
        df_all = df_data[(df_data['Type'] == 'All') & (df_data['Status_Code'] == 0) & (df_data['Device_Type'] == 'Total')][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_all = df_all.reset_index(drop=True)

        ict_reg_all_total = df_all['Number'][0]
        ict_reg_all_percent = df_all['Percent'][0]
        ict_all_total = df_all[district][0]
        ict_all_percent = (ict_all_total /  ict_reg_all_total) * 100

        # All, Mobile Phone (Smart)
        df_mobile_sm = df_data[(df_data['Type'] == 'All') & (df_data['Status_Code'] == 1)][['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_sm = df_mobile_sm.reset_index(drop=True)

        ict_mob_phone_smart_reg_all_val = df_mobile_sm['Number'][0]
        ict_mob_phone_smart_reg_all_percent = df_mobile_sm['Percent'][0]
        ict_mob_phone_smart_all_val = df_mobile_sm[district][0]
        ict_mob_phone_smart_all_percent = (ict_mob_phone_smart_all_val / ict_reg_all_total) * 100

        # All, Mobile Phone (Non Smart)
        df_mobile_non_sm = df_data[(df_data['Type'] == 'All') & (df_data['Status_Code'] == 2)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_non_sm = df_mobile_non_sm.reset_index(drop=True)

        ict_mob_phone_non_smart_reg_all_val = df_mobile_non_sm['Number'][0]
        ict_mob_phone_non_smart_reg_all_percent = df_mobile_non_sm['Percent'][0]
        ict_mob_phone_non_smart_all_val = df_mobile_non_sm[district][0]
        ict_mob_phone_non_smart_all_percent = (ict_mob_phone_non_smart_all_val / ict_reg_all_total) * 100

        # All, Tablet
        df_tablet = df_data[(df_data['Type'] == 'All') & (df_data['Status_Code'] == 3)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_tablet = df_tablet.reset_index(drop=True)

        ict_tablet_reg_all_val = df_tablet['Number'][0]
        ict_tablet_reg_all_percent = df_tablet['Percent'][0]
        ict_tablet_all_val = df_tablet[district][0]
        ict_tablet_all_percent = (ict_tablet_all_val / ict_reg_all_total) * 100

        # All, Laptop
        df_laptop = df_data[(df_data['Type'] == 'All') & (df_data['Status_Code'] == 4)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_laptop = df_laptop.reset_index(drop=True)

        ict_laptop_reg_all_val = df_laptop['Number'][0]
        ict_laptop_reg_all_percent = df_laptop['Percent'][0]
        ict_laptop_all_val = df_laptop[district][0]
        ict_laptop_all_percent = (ict_laptop_all_val / ict_reg_all_total) * 100

        # All, None
        df_none = df_data[(df_data['Type'] == 'All') & (df_data['Status_Code'] == 5)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_none = df_none.reset_index(drop=True)

        ict_none_reg_all_val = df_none['Number'][0]
        ict_none_reg_all_percent = df_none['Percent'][0]
        ict_none_all_val = df_none[district][0]
        ict_none_all_percent = (ict_laptop_all_val / ict_reg_all_total) * 100

        # Formatting

        #all, total
        ict_reg_all_total = '{:,}'.format(ict_reg_all_total)
        ict_reg_all_percent = '{:.1f}'.format(ict_reg_all_percent)
        ict_all_total = '{:,}'.format(ict_all_total)
        ict_all_percent = '{:.1f}'.format(ict_all_percent)

        #all, mobile phone (smart)
        ict_mob_phone_smart_reg_all_val = '{:,}'.format(ict_mob_phone_smart_reg_all_val)
        ict_mob_phone_smart_reg_all_percent = '{:.1f}'.format(ict_mob_phone_smart_reg_all_percent)
        ict_mob_phone_smart_all_val = '{:,}'.format(ict_mob_phone_smart_all_val)
        ict_mob_phone_smart_all_percent = '{:.1f}'.format(ict_mob_phone_smart_all_percent)

        # all, mobile phone (non smart)
        ict_mob_phone_non_smart_reg_all_val = '{:,}'.format(ict_mob_phone_non_smart_reg_all_val)
        ict_mob_phone_non_smart_reg_all_percent = '{:.1f}'.format(ict_mob_phone_non_smart_reg_all_percent)
        ict_mob_phone_non_smart_all_val = '{:,}'.format(ict_mob_phone_non_smart_all_val)
        ict_mob_phone_non_smart_all_percent = '{:.1f}'.format(ict_mob_phone_non_smart_all_percent)

        #all, tablet
        ict_tablet_reg_all_val = '{:,}'.format(ict_tablet_reg_all_val)
        ict_tablet_reg_all_percent = '{:.1f}'.format(ict_tablet_reg_all_percent)
        ict_tablet_all_val = '{:,}'.format(ict_tablet_all_val)
        ict_tablet_all_percent = '{:.1f}'.format(ict_tablet_all_percent)

        # all, laptop
        ict_laptop_reg_all_val = '{:,}'.format(ict_laptop_reg_all_val)
        ict_laptop_reg_all_percent = '{:.1f}'.format(ict_laptop_reg_all_percent)
        ict_laptop_all_val = '{:,}'.format(ict_laptop_all_val)
        ict_laptop_all_percent = '{:.1f}'.format(ict_laptop_all_percent)

        # all, none
        ict_none_reg_all_val = '{:,}'.format(ict_none_reg_all_val)
        ict_none_reg_all_percent = '{:.1f}'.format(ict_none_reg_all_percent)
        ict_none_all_val = '{:,}'.format(ict_none_all_val)
        ict_none_all_percent = '{:.1f}'.format(ict_none_all_percent)

    return ict_reg_all_total, ict_reg_all_percent, ict_all_total, ict_all_percent, \
           ict_mob_phone_smart_reg_all_val, ict_mob_phone_smart_reg_all_percent, ict_mob_phone_smart_all_val, ict_mob_phone_smart_all_percent, \
           ict_mob_phone_non_smart_reg_all_val, ict_mob_phone_non_smart_reg_all_percent, ict_mob_phone_non_smart_all_val, ict_mob_phone_non_smart_all_percent, \
           ict_tablet_reg_all_val, ict_tablet_reg_all_percent, ict_tablet_all_val, ict_tablet_all_percent, \
           ict_laptop_reg_all_val, ict_laptop_reg_all_percent, ict_laptop_all_val, ict_laptop_all_percent, \
           ict_none_reg_all_val, ict_none_reg_all_percent, ict_none_all_val, ict_none_all_percent


#********************************************************************
# ICT - All, Males
#********************************************************************
@app.callback(

    # all
    Output('ict_reg_all_male_total', 'children'),
    Output('ict_reg_all_male_percent', 'children'),
    Output('ict_all_male_total', 'children'),
    Output('ict_all_male_percent', 'children'),

    # all, male, mobile phone (smart)
    Output('ict_mob_phone_smart_reg_all_male_val', 'children'),
    Output('ict_mob_phone_smart_reg_all_male_percent', 'children'),
    Output('ict_mob_phone_smart_all_male_val', 'children'),
    Output('ict_mob_phone_smart_all_male_percent', 'children'),

    # all, mobile phone (non-smart)
    Output('ict_mob_phone_non_smart_reg_all_male_val', 'children'),
    Output('ict_mob_phone_non_smart_reg_all_male_percent', 'children'),
    Output('ict_mob_phone_non_smart_all_male_val', 'children'),
    Output('ict_mob_phone_non_smart_all_male_percent', 'children'),

    # all, tablet
    Output('ict_tablet_reg_all_male_val', 'children'),
    Output('ict_tablet_reg_all_male_percent', 'children'),
    Output('ict_tablet_all_male_val', 'children'),
    Output('ict_tablet_all_male_percent', 'children'),

    # all, laptop
    Output('ict_laptop_reg_all_male_val', 'children'),
    Output('ict_laptop_reg_all_male_percent', 'children'),
    Output('ict_laptop_all_male_val', 'children'),
    Output('ict_laptop_all_male_percent', 'children'),

    # all, none
    Output('ict_none_reg_all_male_val', 'children'),
    Output('ict_none_reg_all_male_percent', 'children'),
    Output('ict_none_all_male_val', 'children'),
    Output('ict_none_all_male_percent', 'children'),

    Input('ict_region_dd', 'value'),
    Input('ict_district_dd', 'value')
)
def get_ict_all_male(region, district):

    # All, Regional
    ict_reg_all_male_total = None
    ict_reg_all_male_percent = None
    ict_all_male_total = None
    ict_all_male_percent = None

    # All, Mobile Phone (Smart)
    ict_mob_phone_smart_reg_all_male_val = None
    ict_mob_phone_smart_reg_all_male_percent = None
    ict_mob_phone_smart_all_male_val = None
    ict_mob_phone_smart_all_male_percent = None

    # All, Mobile Phone (Non-Smart)
    ict_mob_phone_non_smart_reg_all_male_val = None
    ict_mob_phone_non_smart_reg_all_male_percent = None
    ict_mob_phone_non_smart_all_male_val = None
    ict_mob_phone_non_smart_all_male_percent = None

    # All, Tablet
    ict_tablet_reg_all_male_val = None
    ict_tablet_reg_all_male_percent = None
    ict_tablet_all_male_val = None
    ict_tablet_all_male_percent = None

    # All, Laptop
    ict_laptop_reg_all_male_val = None
    ict_laptop_reg_all_male_percent = None
    ict_laptop_all_male_val = None
    ict_laptop_all_male_percent = None

    # All, None
    ict_none_reg_all_male_val = None
    ict_none_reg_all_male_percent = None
    ict_none_all_male_val = None
    ict_none_all_male_percent = None

    if (region != None) & (district != None):

        # get data
        df_data = df_ict_dic[region]

        # All, Total
        df_all = df_data[(df_data['Type'] == 'Male') & (df_data['Status_Code'] == 0) & (df_data['Device_Type'] == 'Total')][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]  # pop in percent
        df_all = df_all.reset_index(drop=True)

        ict_reg_all_male_total = df_all['Number'][0]
        ict_reg_all_male_percent = df_all['Percent'][0]
        ict_all_male_total = df_all[district][0]
        ict_all_male_percent = (ict_all_male_total /  ict_reg_all_male_total) * 100

        # All, Mobile Phone (Smart)
        df_mobile_sm = df_data[(df_data['Type'] == 'Male') & (df_data['Status_Code'] == 1)][['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_sm = df_mobile_sm.reset_index(drop=True)

        ict_mob_phone_smart_reg_all_male_val = df_mobile_sm['Number'][0]
        ict_mob_phone_smart_reg_all_male_percent = df_mobile_sm['Percent'][0]
        ict_mob_phone_smart_all_male_val = df_mobile_sm[district][0]
        ict_mob_phone_smart_all_male_percent = (ict_mob_phone_smart_all_male_val / ict_reg_all_male_total) * 100

        # All, Mobile Phone (Non Smart)
        df_mobile_non_sm = df_data[(df_data['Type'] == 'Male') & (df_data['Status_Code'] == 2)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_non_sm = df_mobile_non_sm.reset_index(drop=True)

        ict_mob_phone_non_smart_reg_all_male_val = df_mobile_non_sm['Number'][0]
        ict_mob_phone_non_smart_reg_all_male_percent = df_mobile_non_sm['Percent'][0]
        ict_mob_phone_non_smart_all_male_val = df_mobile_non_sm[district][0]
        ict_mob_phone_non_smart_all_male_percent = (ict_mob_phone_non_smart_all_male_val / ict_reg_all_male_total) * 100

        # All, Tablet
        df_tablet = df_data[(df_data['Type'] == 'Male') & (df_data['Status_Code'] == 3)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_tablet = df_tablet.reset_index(drop=True)

        ict_tablet_reg_all_male_val = df_tablet['Number'][0]
        ict_tablet_reg_all_male_percent = df_tablet['Percent'][0]
        ict_tablet_all_male_val = df_tablet[district][0]
        ict_tablet_all_male_percent = (ict_tablet_all_male_val / ict_reg_all_male_total) * 100

        # All, Laptop
        df_laptop = df_data[(df_data['Type'] == 'Male') & (df_data['Status_Code'] == 4)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_laptop = df_laptop.reset_index(drop=True)

        ict_laptop_reg_all_male_val = df_laptop['Number'][0]
        ict_laptop_reg_all_male_percent = df_laptop['Percent'][0]
        ict_laptop_all_male_val = df_laptop[district][0]
        ict_laptop_all_male_percent = (ict_laptop_all_male_val / ict_reg_all_male_total) * 100

        # All, None
        df_none = df_data[(df_data['Type'] == 'Male') & (df_data['Status_Code'] == 5)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_none = df_none.reset_index(drop=True)

        ict_none_reg_all_male_val = df_none['Number'][0]
        ict_none_reg_all_male_percent = df_none['Percent'][0]
        ict_none_all_male_val = df_none[district][0]
        ict_none_all_male_percent = (ict_laptop_all_male_val / ict_reg_all_male_total) * 100

        # Formatting

        #all, total
        ict_reg_all_male_total = '{:,}'.format(ict_reg_all_male_total)
        ict_reg_all_male_percent = '{:.1f}'.format(ict_reg_all_male_percent)
        ict_all_male_total = '{:,}'.format(ict_all_male_total)
        ict_all_male_percent = '{:.1f}'.format(ict_all_male_percent)

        #all, mobile phone (smart)
        ict_mob_phone_smart_reg_all_male_val = '{:,}'.format(ict_mob_phone_smart_reg_all_male_val)
        ict_mob_phone_smart_reg_all_male_percent = '{:.1f}'.format(ict_mob_phone_smart_reg_all_male_percent)
        ict_mob_phone_smart_all_male_val = '{:,}'.format(ict_mob_phone_smart_all_male_val)
        ict_mob_phone_smart_all_male_percent = '{:.1f}'.format(ict_mob_phone_smart_all_male_percent)

        # all, mobile phone (non smart)
        ict_mob_phone_non_smart_reg_all_male_val = '{:,}'.format(ict_mob_phone_non_smart_reg_all_male_val)
        ict_mob_phone_non_smart_reg_all_male_percent = '{:.1f}'.format(ict_mob_phone_non_smart_reg_all_male_percent)
        ict_mob_phone_non_smart_all_male_val = '{:,}'.format(ict_mob_phone_non_smart_all_male_val)
        ict_mob_phone_non_smart_all_male_percent = '{:.1f}'.format(ict_mob_phone_non_smart_all_male_percent)

        #all, tablet
        ict_tablet_reg_all_male_val = '{:,}'.format(ict_tablet_reg_all_male_val)
        ict_tablet_reg_all_male_percent = '{:.1f}'.format(ict_tablet_reg_all_male_percent)
        ict_tablet_all_male_val = '{:,}'.format(ict_tablet_all_male_val)
        ict_tablet_all_male_percent = '{:.1f}'.format(ict_tablet_all_male_percent)

        # all, laptop
        ict_laptop_reg_all_male_val = '{:,}'.format(ict_laptop_reg_all_male_val)
        ict_laptop_reg_all_male_percent = '{:.1f}'.format(ict_laptop_reg_all_male_percent)
        ict_laptop_all_male_val = '{:,}'.format(ict_laptop_all_male_val)
        ict_laptop_all_male_percent = '{:.1f}'.format(ict_laptop_all_male_percent)

        # all, none
        ict_none_reg_all_male_val = '{:,}'.format(ict_none_reg_all_male_val)
        ict_none_reg_all_male_percent = '{:.1f}'.format(ict_none_reg_all_male_percent)
        ict_none_all_male_val = '{:,}'.format(ict_none_all_male_val)
        ict_none_all_male_percent = '{:.1f}'.format(ict_none_all_male_percent)

    return ict_reg_all_male_total, ict_reg_all_male_percent, ict_all_male_total, ict_all_male_percent, \
           ict_mob_phone_smart_reg_all_male_val, ict_mob_phone_smart_reg_all_male_percent, ict_mob_phone_smart_all_male_val, ict_mob_phone_smart_all_male_percent, \
           ict_mob_phone_non_smart_reg_all_male_val, ict_mob_phone_non_smart_reg_all_male_percent, ict_mob_phone_non_smart_all_male_val, ict_mob_phone_non_smart_all_male_percent, \
           ict_tablet_reg_all_male_val, ict_tablet_reg_all_male_percent, ict_tablet_all_male_val, ict_tablet_all_male_percent, \
           ict_laptop_reg_all_male_val, ict_laptop_reg_all_male_percent, ict_laptop_all_male_val, ict_laptop_all_male_percent, \
           ict_none_reg_all_male_val, ict_none_reg_all_male_percent, ict_none_all_male_val, ict_none_all_male_percent

#********************************************************************
# ICT - All, Females
#********************************************************************
@app.callback(

    # all
    Output('ict_reg_all_female_total', 'children'),
    Output('ict_reg_all_female_percent', 'children'),
    Output('ict_all_female_total', 'children'),
    Output('ict_all_female_percent', 'children'),

    # all, female, mobile phone (smart)
    Output('ict_mob_phone_smart_reg_all_female_val', 'children'),
    Output('ict_mob_phone_smart_reg_all_female_percent', 'children'),
    Output('ict_mob_phone_smart_all_female_val', 'children'),
    Output('ict_mob_phone_smart_all_female_percent', 'children'),

    # all, mobile phone (non-smart)
    Output('ict_mob_phone_non_smart_reg_all_female_val', 'children'),
    Output('ict_mob_phone_non_smart_reg_all_female_percent', 'children'),
    Output('ict_mob_phone_non_smart_all_female_val', 'children'),
    Output('ict_mob_phone_non_smart_all_female_percent', 'children'),

    # all, tablet
    Output('ict_tablet_reg_all_female_val', 'children'),
    Output('ict_tablet_reg_all_female_percent', 'children'),
    Output('ict_tablet_all_female_val', 'children'),
    Output('ict_tablet_all_female_percent', 'children'),

    # all, laptop
    Output('ict_laptop_reg_all_female_val', 'children'),
    Output('ict_laptop_reg_all_female_percent', 'children'),
    Output('ict_laptop_all_female_val', 'children'),
    Output('ict_laptop_all_female_percent', 'children'),

    # all, none
    Output('ict_none_reg_all_female_val', 'children'),
    Output('ict_none_reg_all_female_percent', 'children'),
    Output('ict_none_all_female_val', 'children'),
    Output('ict_none_all_female_percent', 'children'),

    Input('ict_region_dd', 'value'),
    Input('ict_district_dd', 'value')
)
def get_ict_all_female(region, district):

    # All, Regional
    ict_reg_all_female_total = None
    ict_reg_all_female_percent = None
    ict_all_female_total = None
    ict_all_female_percent = None

    # All, Mobile Phone (Smart)
    ict_mob_phone_smart_reg_all_female_val = None
    ict_mob_phone_smart_reg_all_female_percent = None
    ict_mob_phone_smart_all_female_val = None
    ict_mob_phone_smart_all_female_percent = None

    # All, Mobile Phone (Non-Smart)
    ict_mob_phone_non_smart_reg_all_female_val = None
    ict_mob_phone_non_smart_reg_all_female_percent = None
    ict_mob_phone_non_smart_all_female_val = None
    ict_mob_phone_non_smart_all_female_percent = None

    # All, Tablet
    ict_tablet_reg_all_female_val = None
    ict_tablet_reg_all_female_percent = None
    ict_tablet_all_female_val = None
    ict_tablet_all_female_percent = None

    # All, Laptop
    ict_laptop_reg_all_female_val = None
    ict_laptop_reg_all_female_percent = None
    ict_laptop_all_female_val = None
    ict_laptop_all_female_percent = None

    # All, None
    ict_none_reg_all_female_val = None
    ict_none_reg_all_female_percent = None
    ict_none_all_female_val = None
    ict_none_all_female_percent = None

    if (region != None) & (district != None):

        # get data
        df_data = df_ict_dic[region]

        # All, Total
        df_all = df_data[(df_data['Type'] == 'Female') & (df_data['Status_Code'] == 0) & (df_data['Device_Type'] == 'Total')][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]  # pop in percent
        df_all = df_all.reset_index(drop=True)

        ict_reg_all_female_total = df_all['Number'][0]
        ict_reg_all_female_percent = df_all['Percent'][0]
        ict_all_female_total = df_all[district][0]
        ict_all_female_percent = (ict_all_female_total /  ict_reg_all_female_total) * 100

        # All, Mobile Phone (Smart)
        df_mobile_sm = df_data[(df_data['Type'] == 'Female') & (df_data['Status_Code'] == 1)][['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_sm = df_mobile_sm.reset_index(drop=True)

        ict_mob_phone_smart_reg_all_female_val = df_mobile_sm['Number'][0]
        ict_mob_phone_smart_reg_all_female_percent = df_mobile_sm['Percent'][0]
        ict_mob_phone_smart_all_female_val = df_mobile_sm[district][0]
        ict_mob_phone_smart_all_female_percent = (ict_mob_phone_smart_all_female_val / ict_reg_all_female_total) * 100

        # All, Mobile Phone (Non Smart)
        df_mobile_non_sm = df_data[(df_data['Type'] == 'Female') & (df_data['Status_Code'] == 2)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_non_sm = df_mobile_non_sm.reset_index(drop=True)

        ict_mob_phone_non_smart_reg_all_female_val = df_mobile_non_sm['Number'][0]
        ict_mob_phone_non_smart_reg_all_female_percent = df_mobile_non_sm['Percent'][0]
        ict_mob_phone_non_smart_all_female_val = df_mobile_non_sm[district][0]
        ict_mob_phone_non_smart_all_female_percent = (ict_mob_phone_non_smart_all_female_val / ict_reg_all_female_total) * 100

        # All, Tablet
        df_tablet = df_data[(df_data['Type'] == 'Female') & (df_data['Status_Code'] == 3)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_tablet = df_tablet.reset_index(drop=True)

        ict_tablet_reg_all_female_val = df_tablet['Number'][0]
        ict_tablet_reg_all_female_percent = df_tablet['Percent'][0]
        ict_tablet_all_female_val = df_tablet[district][0]
        ict_tablet_all_female_percent = (ict_tablet_all_female_val / ict_reg_all_female_total) * 100

        # All, Laptop
        df_laptop = df_data[(df_data['Type'] == 'Female') & (df_data['Status_Code'] == 4)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_laptop = df_laptop.reset_index(drop=True)

        ict_laptop_reg_all_female_val = df_laptop['Number'][0]
        ict_laptop_reg_all_female_percent = df_laptop['Percent'][0]
        ict_laptop_all_female_val = df_laptop[district][0]
        ict_laptop_all_female_percent = (ict_laptop_all_female_val / ict_reg_all_female_total) * 100

        # All, None
        df_none = df_data[(df_data['Type'] == 'Female') & (df_data['Status_Code'] == 5)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_none = df_none.reset_index(drop=True)

        ict_none_reg_all_female_val = df_none['Number'][0]
        ict_none_reg_all_female_percent = df_none['Percent'][0]
        ict_none_all_female_val = df_none[district][0]
        ict_none_all_female_percent = (ict_none_all_female_val / ict_reg_all_female_total) * 100

        # Formatting

        #all, total
        ict_reg_all_female_total = '{:,}'.format(ict_reg_all_female_total)
        ict_reg_all_female_percent = '{:.1f}'.format(ict_reg_all_female_percent)
        ict_all_female_total = '{:,}'.format(ict_all_female_total)
        ict_all_female_percent = '{:.1f}'.format(ict_all_female_percent)

        #all, mobile phone (smart)
        ict_mob_phone_smart_reg_all_female_val = '{:,}'.format(ict_mob_phone_smart_reg_all_female_val)
        ict_mob_phone_smart_reg_all_female_percent = '{:.1f}'.format(ict_mob_phone_smart_reg_all_female_percent)
        ict_mob_phone_smart_all_female_val = '{:,}'.format(ict_mob_phone_smart_all_female_val)
        ict_mob_phone_smart_all_female_percent = '{:.1f}'.format(ict_mob_phone_smart_all_female_percent)

        # all, mobile phone (non smart)
        ict_mob_phone_non_smart_reg_all_female_val = '{:,}'.format(ict_mob_phone_non_smart_reg_all_female_val)
        ict_mob_phone_non_smart_reg_all_female_percent = '{:.1f}'.format(ict_mob_phone_non_smart_reg_all_female_percent)
        ict_mob_phone_non_smart_all_female_val = '{:,}'.format(ict_mob_phone_non_smart_all_female_val)
        ict_mob_phone_non_smart_all_female_percent = '{:.1f}'.format(ict_mob_phone_non_smart_all_female_percent)

        #all, tablet
        ict_tablet_reg_all_female_val = '{:,}'.format(ict_tablet_reg_all_female_val)
        ict_tablet_reg_all_female_percent = '{:.1f}'.format(ict_tablet_reg_all_female_percent)
        ict_tablet_all_female_val = '{:,}'.format(ict_tablet_all_female_val)
        ict_tablet_all_female_percent = '{:.1f}'.format(ict_tablet_all_female_percent)

        # all, laptop
        ict_laptop_reg_all_female_val = '{:,}'.format(ict_laptop_reg_all_female_val)
        ict_laptop_reg_all_female_percent = '{:.1f}'.format(ict_laptop_reg_all_female_percent)
        ict_laptop_all_female_val = '{:,}'.format(ict_laptop_all_female_val)
        ict_laptop_all_female_percent = '{:.1f}'.format(ict_laptop_all_female_percent)

        # all, none
        ict_none_reg_all_female_val = '{:,}'.format(ict_none_reg_all_female_val)
        ict_none_reg_all_female_percent = '{:.1f}'.format(ict_none_reg_all_female_percent)
        ict_none_all_female_val = '{:,}'.format(ict_none_all_female_val)
        ict_none_all_female_percent = '{:.1f}'.format(ict_none_all_female_percent)

    return ict_reg_all_female_total, ict_reg_all_female_percent, ict_all_female_total, ict_all_female_percent, \
           ict_mob_phone_smart_reg_all_female_val, ict_mob_phone_smart_reg_all_female_percent, ict_mob_phone_smart_all_female_val, ict_mob_phone_smart_all_female_percent, \
           ict_mob_phone_non_smart_reg_all_female_val, ict_mob_phone_non_smart_reg_all_female_percent, ict_mob_phone_non_smart_all_female_val, ict_mob_phone_non_smart_all_female_percent, \
           ict_tablet_reg_all_female_val, ict_tablet_reg_all_female_percent, ict_tablet_all_female_val, ict_tablet_all_female_percent, \
           ict_laptop_reg_all_female_val, ict_laptop_reg_all_female_percent, ict_laptop_all_female_val, ict_laptop_all_female_percent, \
           ict_none_reg_all_female_val, ict_none_reg_all_female_percent, ict_none_all_female_val, ict_none_all_female_percent


#********************************************************************
# ICT - Urban, Both Sexes
#********************************************************************
@app.callback(

    # all
    Output('ict_reg_urban_all_total', 'children'),
    Output('ict_reg_urban_all_percent', 'children'),
    Output('ict_urban_all_total', 'children'),
    Output('ict_urban_all_percent', 'children'),

    # urban, all, mobile phone (smart)
    Output('ict_mob_phone_smart_reg_urban_all_val', 'children'),
    Output('ict_mob_phone_smart_reg_urban_all_percent', 'children'),
    Output('ict_mob_phone_smart_urban_all_val', 'children'),
    Output('ict_mob_phone_smart_urban_all_percent', 'children'),

    # urban, mobile phone (non-smart)
    Output('ict_mob_phone_non_smart_reg_urban_all_val', 'children'),
    Output('ict_mob_phone_non_smart_reg_urban_all_percent', 'children'),
    Output('ict_mob_phone_non_smart_urban_all_val', 'children'),
    Output('ict_mob_phone_non_smart_urban_all_percent', 'children'),

    # urban, tablet
    Output('ict_tablet_reg_urban_all_val', 'children'),
    Output('ict_tablet_reg_urban_all_percent', 'children'),
    Output('ict_tablet_urban_all_val', 'children'),
    Output('ict_tablet_urban_all_percent', 'children'),

    # urban, laptop
    Output('ict_laptop_reg_urban_all_val', 'children'),
    Output('ict_laptop_reg_urban_all_percent', 'children'),
    Output('ict_laptop_urban_all_val', 'children'),
    Output('ict_laptop_urban_all_percent', 'children'),

    # urban, none
    Output('ict_none_reg_urban_all_val', 'children'),
    Output('ict_none_reg_urban_all_percent', 'children'),
    Output('ict_none_urban_all_val', 'children'),
    Output('ict_none_urban_all_percent', 'children'),

    Input('ict_region_dd', 'value'),
    Input('ict_district_dd', 'value')
)
def get_ict_urban_all(region, district):

    # urban, Regional
    ict_reg_urban_all_total = None
    ict_reg_urban_all_percent = None
    ict_urban_all_total = None
    ict_urban_all_percent = None

    # urban, Mobile Phone (Smart)
    ict_mob_phone_smart_reg_urban_all_val = None
    ict_mob_phone_smart_reg_urban_all_percent = None
    ict_mob_phone_smart_urban_all_val = None
    ict_mob_phone_smart_urban_all_percent = None

    # urban, Mobile Phone (Non-Smart)
    ict_mob_phone_non_smart_reg_urban_all_val = None
    ict_mob_phone_non_smart_reg_urban_all_percent = None
    ict_mob_phone_non_smart_urban_all_val = None
    ict_mob_phone_non_smart_urban_all_percent = None

    # urban, Tablet
    ict_tablet_reg_urban_all_val = None
    ict_tablet_reg_urban_all_percent = None
    ict_tablet_urban_all_val = None
    ict_tablet_urban_all_percent = None

    # urban, Laptop
    ict_laptop_reg_urban_all_val = None
    ict_laptop_reg_urban_all_percent = None
    ict_laptop_urban_all_val = None
    ict_laptop_urban_all_percent = None

    # urban, None
    ict_none_reg_urban_all_val = None
    ict_none_reg_urban_all_percent = None
    ict_none_urban_all_val = None
    ict_none_urban_all_percent = None

    if (region != None) & (district != None):

        # get data
        df_data = df_ict_dic[region]

        # urban, Total
        df_urban = df_data[(df_data['Type'] == 'Urban All') & (df_data['Status_Code'] == 0) & (df_data['Device_Type'] == 'Total')][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]  # pop in percent
        df_urban = df_urban.reset_index(drop=True)

        ict_reg_urban_all_total = df_urban['Number'][0]
        ict_reg_urban_all_percent = df_urban['Percent'][0]
        ict_urban_all_total = df_urban[district][0]
        ict_urban_all_percent = (ict_urban_all_total /  ict_reg_urban_all_total) * 100

        # urban, Mobile Phone (Smart)
        df_mobile_sm = df_data[(df_data['Type'] == 'Urban All') & (df_data['Status_Code'] == 1)][['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_sm = df_mobile_sm.reset_index(drop=True)

        ict_mob_phone_smart_reg_urban_all_val = df_mobile_sm['Number'][0]
        ict_mob_phone_smart_reg_urban_all_percent = df_mobile_sm['Percent'][0]
        ict_mob_phone_smart_urban_all_val = df_mobile_sm[district][0]
        ict_mob_phone_smart_urban_all_percent = (ict_mob_phone_smart_urban_all_val / ict_reg_urban_all_total) * 100

        # urban, Mobile Phone (Non Smart)
        df_mobile_non_sm = df_data[(df_data['Type'] == 'Urban All') & (df_data['Status_Code'] == 2)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_non_sm = df_mobile_non_sm.reset_index(drop=True)

        ict_mob_phone_non_smart_reg_urban_all_val = df_mobile_non_sm['Number'][0]
        ict_mob_phone_non_smart_reg_urban_all_percent = df_mobile_non_sm['Percent'][0]
        ict_mob_phone_non_smart_urban_all_val = df_mobile_non_sm[district][0]
        ict_mob_phone_non_smart_urban_all_percent = (ict_mob_phone_non_smart_urban_all_val / ict_reg_urban_all_total) * 100

        # urban, Tablet
        df_tablet = df_data[(df_data['Type'] == 'Urban All') & (df_data['Status_Code'] == 3)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_tablet = df_tablet.reset_index(drop=True)

        ict_tablet_reg_urban_all_val = df_tablet['Number'][0]
        ict_tablet_reg_urban_all_percent = df_tablet['Percent'][0]
        ict_tablet_urban_all_val = df_tablet[district][0]
        ict_tablet_urban_all_percent = (ict_tablet_urban_all_val / ict_reg_urban_all_total) * 100

        # urban, Laptop
        df_laptop = df_data[(df_data['Type'] == 'Urban All') & (df_data['Status_Code'] == 4)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_laptop = df_laptop.reset_index(drop=True)

        ict_laptop_reg_urban_all_val = df_laptop['Number'][0]
        ict_laptop_reg_urban_all_percent = df_laptop['Percent'][0]
        ict_laptop_urban_all_val = df_laptop[district][0]
        ict_laptop_urban_all_percent = (ict_laptop_urban_all_val / ict_reg_urban_all_total) * 100

        # urban, None
        df_none = df_data[(df_data['Type'] == 'Urban All') & (df_data['Status_Code'] == 5)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_none = df_none.reset_index(drop=True)

        ict_none_reg_urban_all_val = df_none['Number'][0]
        ict_none_reg_urban_all_percent = df_none['Percent'][0]
        ict_none_urban_all_val = df_none[district][0]
        ict_none_urban_all_percent = (ict_none_urban_all_val / ict_reg_urban_all_total) * 100

        # Formatting

        #urban, total
        ict_reg_urban_all_total = '{:,}'.format(ict_reg_urban_all_total)
        ict_reg_urban_all_percent = '{:.1f}'.format(ict_reg_urban_all_percent)
        ict_urban_all_total = '{:,}'.format(ict_urban_all_total)
        ict_urban_all_percent = '{:.1f}'.format(ict_urban_all_percent)

        #urban, mobile phone (smart)
        ict_mob_phone_smart_reg_urban_all_val = '{:,}'.format(ict_mob_phone_smart_reg_urban_all_val)
        ict_mob_phone_smart_reg_urban_all_percent = '{:.1f}'.format(ict_mob_phone_smart_reg_urban_all_percent)
        ict_mob_phone_smart_urban_all_val = '{:,}'.format(ict_mob_phone_smart_urban_all_val)
        ict_mob_phone_smart_urban_all_percent = '{:.1f}'.format(ict_mob_phone_smart_urban_all_percent)

        # urban, mobile phone (non smart)
        ict_mob_phone_non_smart_reg_urban_all_val = '{:,}'.format(ict_mob_phone_non_smart_reg_urban_all_val)
        ict_mob_phone_non_smart_reg_urban_all_percent = '{:.1f}'.format(ict_mob_phone_non_smart_reg_urban_all_percent)
        ict_mob_phone_non_smart_urban_all_val = '{:,}'.format(ict_mob_phone_non_smart_urban_all_val)
        ict_mob_phone_non_smart_urban_all_percent = '{:.1f}'.format(ict_mob_phone_non_smart_urban_all_percent)

        #urban, tablet
        ict_tablet_reg_urban_all_val = '{:,}'.format(ict_tablet_reg_urban_all_val)
        ict_tablet_reg_urban_all_percent = '{:.1f}'.format(ict_tablet_reg_urban_all_percent)
        ict_tablet_urban_all_val = '{:,}'.format(ict_tablet_urban_all_val)
        ict_tablet_urban_all_percent = '{:.1f}'.format(ict_tablet_urban_all_percent)

        # urban, laptop
        ict_laptop_reg_urban_all_val = '{:,}'.format(ict_laptop_reg_urban_all_val)
        ict_laptop_reg_urban_all_percent = '{:.1f}'.format(ict_laptop_reg_urban_all_percent)
        ict_laptop_urban_all_val = '{:,}'.format(ict_laptop_urban_all_val)
        ict_laptop_urban_all_percent = '{:.1f}'.format(ict_laptop_urban_all_percent)

        # urban, none
        ict_none_reg_urban_all_val = '{:,}'.format(ict_none_reg_urban_all_val)
        ict_none_reg_urban_all_percent = '{:.1f}'.format(ict_none_reg_urban_all_percent)
        ict_none_urban_all_val = '{:,}'.format(ict_none_urban_all_val)
        ict_none_urban_all_percent = '{:.1f}'.format(ict_none_urban_all_percent)

    return ict_reg_urban_all_total, ict_reg_urban_all_percent, ict_urban_all_total, ict_urban_all_percent, \
           ict_mob_phone_smart_reg_urban_all_val, ict_mob_phone_smart_reg_urban_all_percent, ict_mob_phone_smart_urban_all_val, ict_mob_phone_smart_urban_all_percent, \
           ict_mob_phone_non_smart_reg_urban_all_val, ict_mob_phone_non_smart_reg_urban_all_percent, ict_mob_phone_non_smart_urban_all_val, ict_mob_phone_non_smart_urban_all_percent, \
           ict_tablet_reg_urban_all_val, ict_tablet_reg_urban_all_percent, ict_tablet_urban_all_val, ict_tablet_urban_all_percent, \
           ict_laptop_reg_urban_all_val, ict_laptop_reg_urban_all_percent, ict_laptop_urban_all_val, ict_laptop_urban_all_percent, \
           ict_none_reg_urban_all_val, ict_none_reg_urban_all_percent, ict_none_urban_all_val, ict_none_urban_all_percent


#********************************************************************
# ICT - Urban, Male
#********************************************************************
@app.callback(

    # all
    Output('ict_reg_urban_male_total', 'children'),
    Output('ict_reg_urban_male_percent', 'children'),
    Output('ict_urban_male_total', 'children'),
    Output('ict_urban_male_percent', 'children'),

    # urban, male, mobile phone (smart)
    Output('ict_mob_phone_smart_reg_urban_male_val', 'children'),
    Output('ict_mob_phone_smart_reg_urban_male_percent', 'children'),
    Output('ict_mob_phone_smart_urban_male_val', 'children'),
    Output('ict_mob_phone_smart_urban_male_percent', 'children'),

    # urban, mobile phone (non-smart)
    Output('ict_mob_phone_non_smart_reg_urban_male_val', 'children'),
    Output('ict_mob_phone_non_smart_reg_urban_male_percent', 'children'),
    Output('ict_mob_phone_non_smart_urban_male_val', 'children'),
    Output('ict_mob_phone_non_smart_urban_male_percent', 'children'),

    # urban, tablet
    Output('ict_tablet_reg_urban_male_val', 'children'),
    Output('ict_tablet_reg_urban_male_percent', 'children'),
    Output('ict_tablet_urban_male_val', 'children'),
    Output('ict_tablet_urban_male_percent', 'children'),

    # urban, laptop
    Output('ict_laptop_reg_urban_male_val', 'children'),
    Output('ict_laptop_reg_urban_male_percent', 'children'),
    Output('ict_laptop_urban_male_val', 'children'),
    Output('ict_laptop_urban_male_percent', 'children'),

    # urban, none
    Output('ict_none_reg_urban_male_val', 'children'),
    Output('ict_none_reg_urban_male_percent', 'children'),
    Output('ict_none_urban_male_val', 'children'),
    Output('ict_none_urban_male_percent', 'children'),

    Input('ict_region_dd', 'value'),
    Input('ict_district_dd', 'value')
)
def get_ict_urban_male(region, district):

    # urban, Regional
    ict_reg_urban_male_total = None
    ict_reg_urban_male_percent = None
    ict_urban_male_total = None
    ict_urban_male_percent = None

    # urban, Mobile Phone (Smart)
    ict_mob_phone_smart_reg_urban_male_val = None
    ict_mob_phone_smart_reg_urban_male_percent = None
    ict_mob_phone_smart_urban_male_val = None
    ict_mob_phone_smart_urban_male_percent = None

    # urban, Mobile Phone (Non-Smart)
    ict_mob_phone_non_smart_reg_urban_male_val = None
    ict_mob_phone_non_smart_reg_urban_male_percent = None
    ict_mob_phone_non_smart_urban_male_val = None
    ict_mob_phone_non_smart_urban_male_percent = None

    # urban, Tablet
    ict_tablet_reg_urban_male_val = None
    ict_tablet_reg_urban_male_percent = None
    ict_tablet_urban_male_val = None
    ict_tablet_urban_male_percent = None

    # urban, Laptop
    ict_laptop_reg_urban_male_val = None
    ict_laptop_reg_urban_male_percent = None
    ict_laptop_urban_male_val = None
    ict_laptop_urban_male_percent = None

    # urban, None
    ict_none_reg_urban_male_val = None
    ict_none_reg_urban_male_percent = None
    ict_none_urban_male_val = None
    ict_none_urban_male_percent = None

    if (region != None) & (district != None):

        # get data
        df_data = df_ict_dic[region]

        # urban, Total
        df_urban = df_data[(df_data['Type'] == 'Urban Male') & (df_data['Status_Code'] == 0) & (df_data['Device_Type'] == 'Total')][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]  # pop in percent
        df_urban = df_urban.reset_index(drop=True)

        ict_reg_urban_male_total = df_urban['Number'][0]
        ict_reg_urban_male_percent = df_urban['Percent'][0]
        ict_urban_male_total = df_urban[district][0]
        ict_urban_male_percent = (ict_urban_male_total /  ict_reg_urban_male_total) * 100

        # urban, Mobile Phone (Smart)
        df_mobile_sm = df_data[(df_data['Type'] == 'Urban Male') & (df_data['Status_Code'] == 1)][['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_sm = df_mobile_sm.reset_index(drop=True)

        ict_mob_phone_smart_reg_urban_male_val = df_mobile_sm['Number'][0]
        ict_mob_phone_smart_reg_urban_male_percent = df_mobile_sm['Percent'][0]
        ict_mob_phone_smart_urban_male_val = df_mobile_sm[district][0]
        ict_mob_phone_smart_urban_male_percent = (ict_mob_phone_smart_urban_male_val / ict_reg_urban_male_total) * 100

        # urban, Mobile Phone (Non Smart)
        df_mobile_non_sm = df_data[(df_data['Type'] == 'Urban Male') & (df_data['Status_Code'] == 2)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_non_sm = df_mobile_non_sm.reset_index(drop=True)

        ict_mob_phone_non_smart_reg_urban_male_val = df_mobile_non_sm['Number'][0]
        ict_mob_phone_non_smart_reg_urban_male_percent = df_mobile_non_sm['Percent'][0]
        ict_mob_phone_non_smart_urban_male_val = df_mobile_non_sm[district][0]
        ict_mob_phone_non_smart_urban_male_percent = (ict_mob_phone_non_smart_urban_male_val / ict_reg_urban_male_total) * 100

        # urban, Tablet
        df_tablet = df_data[(df_data['Type'] == 'Urban Male') & (df_data['Status_Code'] == 3)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_tablet = df_tablet.reset_index(drop=True)

        ict_tablet_reg_urban_male_val = df_tablet['Number'][0]
        ict_tablet_reg_urban_male_percent = df_tablet['Percent'][0]
        ict_tablet_urban_male_val = df_tablet[district][0]
        ict_tablet_urban_male_percent = (ict_tablet_urban_male_val / ict_reg_urban_male_total) * 100

        # urban, Laptop
        df_laptop = df_data[(df_data['Type'] == 'Urban Male') & (df_data['Status_Code'] == 4)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_laptop = df_laptop.reset_index(drop=True)

        ict_laptop_reg_urban_male_val = df_laptop['Number'][0]
        ict_laptop_reg_urban_male_percent = df_laptop['Percent'][0]
        ict_laptop_urban_male_val = df_laptop[district][0]
        ict_laptop_urban_male_percent = (ict_laptop_urban_male_val / ict_reg_urban_male_total) * 100

        # urban, None
        df_none = df_data[(df_data['Type'] == 'Urban Male') & (df_data['Status_Code'] == 5)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_none = df_none.reset_index(drop=True)

        ict_none_reg_urban_male_val = df_none['Number'][0]
        ict_none_reg_urban_male_percent = df_none['Percent'][0]
        ict_none_urban_male_val = df_none[district][0]
        ict_none_urban_male_percent = (ict_none_urban_male_val / ict_reg_urban_male_total) * 100

        # Formatting

        #urban, total
        ict_reg_urban_male_total = '{:,}'.format(ict_reg_urban_male_total)
        ict_reg_urban_male_percent = '{:.1f}'.format(ict_reg_urban_male_percent)
        ict_urban_male_total = '{:,}'.format(ict_urban_male_total)
        ict_urban_male_percent = '{:.1f}'.format(ict_urban_male_percent)

        #urban, mobile phone (smart)
        ict_mob_phone_smart_reg_urban_male_val = '{:,}'.format(ict_mob_phone_smart_reg_urban_male_val)
        ict_mob_phone_smart_reg_urban_male_percent = '{:.1f}'.format(ict_mob_phone_smart_reg_urban_male_percent)
        ict_mob_phone_smart_urban_male_val = '{:,}'.format(ict_mob_phone_smart_urban_male_val)
        ict_mob_phone_smart_urban_male_percent = '{:.1f}'.format(ict_mob_phone_smart_urban_male_percent)

        # urban, mobile phone (non smart)
        ict_mob_phone_non_smart_reg_urban_male_val = '{:,}'.format(ict_mob_phone_non_smart_reg_urban_male_val)
        ict_mob_phone_non_smart_reg_urban_male_percent = '{:.1f}'.format(ict_mob_phone_non_smart_reg_urban_male_percent)
        ict_mob_phone_non_smart_urban_male_val = '{:,}'.format(ict_mob_phone_non_smart_urban_male_val)
        ict_mob_phone_non_smart_urban_male_percent = '{:.1f}'.format(ict_mob_phone_non_smart_urban_male_percent)

        #urban, tablet
        ict_tablet_reg_urban_male_val = '{:,}'.format(ict_tablet_reg_urban_male_val)
        ict_tablet_reg_urban_male_percent = '{:.1f}'.format(ict_tablet_reg_urban_male_percent)
        ict_tablet_urban_male_val = '{:,}'.format(ict_tablet_urban_male_val)
        ict_tablet_urban_male_percent = '{:.1f}'.format(ict_tablet_urban_male_percent)

        # urban, laptop
        ict_laptop_reg_urban_male_val = '{:,}'.format(ict_laptop_reg_urban_male_val)
        ict_laptop_reg_urban_male_percent = '{:.1f}'.format(ict_laptop_reg_urban_male_percent)
        ict_laptop_urban_male_val = '{:,}'.format(ict_laptop_urban_male_val)
        ict_laptop_urban_male_percent = '{:.1f}'.format(ict_laptop_urban_male_percent)

        # urban, none
        ict_none_reg_urban_male_val = '{:,}'.format(ict_none_reg_urban_male_val)
        ict_none_reg_urban_male_percent = '{:.1f}'.format(ict_none_reg_urban_male_percent)
        ict_none_urban_male_val = '{:,}'.format(ict_none_urban_male_val)
        ict_none_urban_male_percent = '{:.1f}'.format(ict_none_urban_male_percent)

    return ict_reg_urban_male_total, ict_reg_urban_male_percent, ict_urban_male_total, ict_urban_male_percent, \
           ict_mob_phone_smart_reg_urban_male_val, ict_mob_phone_smart_reg_urban_male_percent, ict_mob_phone_smart_urban_male_val, ict_mob_phone_smart_urban_male_percent, \
           ict_mob_phone_non_smart_reg_urban_male_val, ict_mob_phone_non_smart_reg_urban_male_percent, ict_mob_phone_non_smart_urban_male_val, ict_mob_phone_non_smart_urban_male_percent, \
           ict_tablet_reg_urban_male_val, ict_tablet_reg_urban_male_percent, ict_tablet_urban_male_val, ict_tablet_urban_male_percent, \
           ict_laptop_reg_urban_male_val, ict_laptop_reg_urban_male_percent, ict_laptop_urban_male_val, ict_laptop_urban_male_percent, \
           ict_none_reg_urban_male_val, ict_none_reg_urban_male_percent, ict_none_urban_male_val, ict_none_urban_male_percent


#********************************************************************
# ICT - Urban, Female
#********************************************************************
@app.callback(

    # all
    Output('ict_reg_urban_female_total', 'children'),
    Output('ict_reg_urban_female_percent', 'children'),
    Output('ict_urban_female_total', 'children'),
    Output('ict_urban_female_percent', 'children'),

    # urban, female, mobile phone (smart)
    Output('ict_mob_phone_smart_reg_urban_female_val', 'children'),
    Output('ict_mob_phone_smart_reg_urban_female_percent', 'children'),
    Output('ict_mob_phone_smart_urban_female_val', 'children'),
    Output('ict_mob_phone_smart_urban_female_percent', 'children'),

    # urban, mobile phone (non-smart)
    Output('ict_mob_phone_non_smart_reg_urban_female_val', 'children'),
    Output('ict_mob_phone_non_smart_reg_urban_female_percent', 'children'),
    Output('ict_mob_phone_non_smart_urban_female_val', 'children'),
    Output('ict_mob_phone_non_smart_urban_female_percent', 'children'),

    # urban, tablet
    Output('ict_tablet_reg_urban_female_val', 'children'),
    Output('ict_tablet_reg_urban_female_percent', 'children'),
    Output('ict_tablet_urban_female_val', 'children'),
    Output('ict_tablet_urban_female_percent', 'children'),

    # urban, laptop
    Output('ict_laptop_reg_urban_female_val', 'children'),
    Output('ict_laptop_reg_urban_female_percent', 'children'),
    Output('ict_laptop_urban_female_val', 'children'),
    Output('ict_laptop_urban_female_percent', 'children'),

    # urban, none
    Output('ict_none_reg_urban_female_val', 'children'),
    Output('ict_none_reg_urban_female_percent', 'children'),
    Output('ict_none_urban_female_val', 'children'),
    Output('ict_none_urban_female_percent', 'children'),

    Input('ict_region_dd', 'value'),
    Input('ict_district_dd', 'value')
)
def get_ict_urban_female(region, district):

    # urban, Regional
    ict_reg_urban_female_total = None
    ict_reg_urban_female_percent = None
    ict_urban_female_total = None
    ict_urban_female_percent = None

    # urban, Mobile Phone (Smart)
    ict_mob_phone_smart_reg_urban_female_val = None
    ict_mob_phone_smart_reg_urban_female_percent = None
    ict_mob_phone_smart_urban_female_val = None
    ict_mob_phone_smart_urban_female_percent = None

    # urban, Mobile Phone (Non-Smart)
    ict_mob_phone_non_smart_reg_urban_female_val = None
    ict_mob_phone_non_smart_reg_urban_female_percent = None
    ict_mob_phone_non_smart_urban_female_val = None
    ict_mob_phone_non_smart_urban_female_percent = None

    # urban, Tablet
    ict_tablet_reg_urban_female_val = None
    ict_tablet_reg_urban_female_percent = None
    ict_tablet_urban_female_val = None
    ict_tablet_urban_female_percent = None

    # urban, Laptop
    ict_laptop_reg_urban_female_val = None
    ict_laptop_reg_urban_female_percent = None
    ict_laptop_urban_female_val = None
    ict_laptop_urban_female_percent = None

    # urban, None
    ict_none_reg_urban_female_val = None
    ict_none_reg_urban_female_percent = None
    ict_none_urban_female_val = None
    ict_none_urban_female_percent = None

    if (region != None) & (district != None):

        # get data
        df_data = df_ict_dic[region]

        # urban, Total
        df_urban = df_data[(df_data['Type'] == 'Urban Female') & (df_data['Status_Code'] == 0) & (df_data['Device_Type'] == 'Total')][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]  # pop in percent
        df_urban = df_urban.reset_index(drop=True)

        ict_reg_urban_female_total = df_urban['Number'][0]
        ict_reg_urban_female_percent = df_urban['Percent'][0]
        ict_urban_female_total = df_urban[district][0]
        ict_urban_female_percent = (ict_urban_female_total /  ict_reg_urban_female_total) * 100

        # urban, Mobile Phone (Smart)
        df_mobile_sm = df_data[(df_data['Type'] == 'Urban Female') & (df_data['Status_Code'] == 1)][['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_sm = df_mobile_sm.reset_index(drop=True)

        ict_mob_phone_smart_reg_urban_female_val = df_mobile_sm['Number'][0]
        ict_mob_phone_smart_reg_urban_female_percent = df_mobile_sm['Percent'][0]
        ict_mob_phone_smart_urban_female_val = df_mobile_sm[district][0]
        ict_mob_phone_smart_urban_female_percent = (ict_mob_phone_smart_urban_female_val / ict_reg_urban_female_total) * 100

        # urban, Mobile Phone (Non Smart)
        df_mobile_non_sm = df_data[(df_data['Type'] == 'Urban Female') & (df_data['Status_Code'] == 2)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_non_sm = df_mobile_non_sm.reset_index(drop=True)

        ict_mob_phone_non_smart_reg_urban_female_val = df_mobile_non_sm['Number'][0]
        ict_mob_phone_non_smart_reg_urban_female_percent = df_mobile_non_sm['Percent'][0]
        ict_mob_phone_non_smart_urban_female_val = df_mobile_non_sm[district][0]
        ict_mob_phone_non_smart_urban_female_percent = (ict_mob_phone_non_smart_urban_female_val / ict_reg_urban_female_total) * 100

        # urban, Tablet
        df_tablet = df_data[(df_data['Type'] == 'Urban Female') & (df_data['Status_Code'] == 3)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_tablet = df_tablet.reset_index(drop=True)

        ict_tablet_reg_urban_female_val = df_tablet['Number'][0]
        ict_tablet_reg_urban_female_percent = df_tablet['Percent'][0]
        ict_tablet_urban_female_val = df_tablet[district][0]
        ict_tablet_urban_female_percent = (ict_tablet_urban_female_val / ict_reg_urban_female_total) * 100

        # urban, Laptop
        df_laptop = df_data[(df_data['Type'] == 'Urban Female') & (df_data['Status_Code'] == 4)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_laptop = df_laptop.reset_index(drop=True)

        ict_laptop_reg_urban_female_val = df_laptop['Number'][0]
        ict_laptop_reg_urban_female_percent = df_laptop['Percent'][0]
        ict_laptop_urban_female_val = df_laptop[district][0]
        ict_laptop_urban_female_percent = (ict_laptop_urban_female_val / ict_reg_urban_female_total) * 100

        # urban, None
        df_none = df_data[(df_data['Type'] == 'Urban Female') & (df_data['Status_Code'] == 5)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_none = df_none.reset_index(drop=True)

        ict_none_reg_urban_female_val = df_none['Number'][0]
        ict_none_reg_urban_female_percent = df_none['Percent'][0]
        ict_none_urban_female_val = df_none[district][0]
        ict_none_urban_female_percent = (ict_none_urban_female_val / ict_reg_urban_female_total) * 100

        # Formatting

        #urban, total
        ict_reg_urban_female_total = '{:,}'.format(ict_reg_urban_female_total)
        ict_reg_urban_female_percent = '{:.1f}'.format(ict_reg_urban_female_percent)
        ict_urban_female_total = '{:,}'.format(ict_urban_female_total)
        ict_urban_female_percent = '{:.1f}'.format(ict_urban_female_percent)

        #urban, mobile phone (smart)
        ict_mob_phone_smart_reg_urban_female_val = '{:,}'.format(ict_mob_phone_smart_reg_urban_female_val)
        ict_mob_phone_smart_reg_urban_female_percent = '{:.1f}'.format(ict_mob_phone_smart_reg_urban_female_percent)
        ict_mob_phone_smart_urban_female_val = '{:,}'.format(ict_mob_phone_smart_urban_female_val)
        ict_mob_phone_smart_urban_female_percent = '{:.1f}'.format(ict_mob_phone_smart_urban_female_percent)

        # urban, mobile phone (non smart)
        ict_mob_phone_non_smart_reg_urban_female_val = '{:,}'.format(ict_mob_phone_non_smart_reg_urban_female_val)
        ict_mob_phone_non_smart_reg_urban_female_percent = '{:.1f}'.format(ict_mob_phone_non_smart_reg_urban_female_percent)
        ict_mob_phone_non_smart_urban_female_val = '{:,}'.format(ict_mob_phone_non_smart_urban_female_val)
        ict_mob_phone_non_smart_urban_female_percent = '{:.1f}'.format(ict_mob_phone_non_smart_urban_female_percent)

        #urban, tablet
        ict_tablet_reg_urban_female_val = '{:,}'.format(ict_tablet_reg_urban_female_val)
        ict_tablet_reg_urban_female_percent = '{:.1f}'.format(ict_tablet_reg_urban_female_percent)
        ict_tablet_urban_female_val = '{:,}'.format(ict_tablet_urban_female_val)
        ict_tablet_urban_female_percent = '{:.1f}'.format(ict_tablet_urban_female_percent)

        # urban, laptop
        ict_laptop_reg_urban_female_val = '{:,}'.format(ict_laptop_reg_urban_female_val)
        ict_laptop_reg_urban_female_percent = '{:.1f}'.format(ict_laptop_reg_urban_female_percent)
        ict_laptop_urban_female_val = '{:,}'.format(ict_laptop_urban_female_val)
        ict_laptop_urban_female_percent = '{:.1f}'.format(ict_laptop_urban_female_percent)

        # urban, none
        ict_none_reg_urban_female_val = '{:,}'.format(ict_none_reg_urban_female_val)
        ict_none_reg_urban_female_percent = '{:.1f}'.format(ict_none_reg_urban_female_percent)
        ict_none_urban_female_val = '{:,}'.format(ict_none_urban_female_val)
        ict_none_urban_female_percent = '{:.1f}'.format(ict_none_urban_female_percent)

    return ict_reg_urban_female_total, ict_reg_urban_female_percent, ict_urban_female_total, ict_urban_female_percent, \
           ict_mob_phone_smart_reg_urban_female_val, ict_mob_phone_smart_reg_urban_female_percent, ict_mob_phone_smart_urban_female_val, ict_mob_phone_smart_urban_female_percent, \
           ict_mob_phone_non_smart_reg_urban_female_val, ict_mob_phone_non_smart_reg_urban_female_percent, ict_mob_phone_non_smart_urban_female_val, ict_mob_phone_non_smart_urban_female_percent, \
           ict_tablet_reg_urban_female_val, ict_tablet_reg_urban_female_percent, ict_tablet_urban_female_val, ict_tablet_urban_female_percent, \
           ict_laptop_reg_urban_female_val, ict_laptop_reg_urban_female_percent, ict_laptop_urban_female_val, ict_laptop_urban_female_percent, \
           ict_none_reg_urban_female_val, ict_none_reg_urban_female_percent, ict_none_urban_female_val, ict_none_urban_female_percent



#********************************************************************
# ICT - Rural, Both Sexes
#********************************************************************
@app.callback(

    # all
    Output('ict_reg_rural_all_total', 'children'),
    Output('ict_reg_rural_all_percent', 'children'),
    Output('ict_rural_all_total', 'children'),
    Output('ict_rural_all_percent', 'children'),

    # rural, all, mobile phone (smart)
    Output('ict_mob_phone_smart_reg_rural_all_val', 'children'),
    Output('ict_mob_phone_smart_reg_rural_all_percent', 'children'),
    Output('ict_mob_phone_smart_rural_all_val', 'children'),
    Output('ict_mob_phone_smart_rural_all_percent', 'children'),

    # rural, mobile phone (non-smart)
    Output('ict_mob_phone_non_smart_reg_rural_all_val', 'children'),
    Output('ict_mob_phone_non_smart_reg_rural_all_percent', 'children'),
    Output('ict_mob_phone_non_smart_rural_all_val', 'children'),
    Output('ict_mob_phone_non_smart_rural_all_percent', 'children'),

    # rural, tablet
    Output('ict_tablet_reg_rural_all_val', 'children'),
    Output('ict_tablet_reg_rural_all_percent', 'children'),
    Output('ict_tablet_rural_all_val', 'children'),
    Output('ict_tablet_rural_all_percent', 'children'),

    # rural, laptop
    Output('ict_laptop_reg_rural_all_val', 'children'),
    Output('ict_laptop_reg_rural_all_percent', 'children'),
    Output('ict_laptop_rural_all_val', 'children'),
    Output('ict_laptop_rural_all_percent', 'children'),

    # rural, none
    Output('ict_none_reg_rural_all_val', 'children'),
    Output('ict_none_reg_rural_all_percent', 'children'),
    Output('ict_none_rural_all_val', 'children'),
    Output('ict_none_rural_all_percent', 'children'),

    Input('ict_region_dd', 'value'),
    Input('ict_district_dd', 'value')
)
def get_ict_rural_all(region, district):

    # rural, Regional
    ict_reg_rural_all_total = None
    ict_reg_rural_all_percent = None
    ict_rural_all_total = None
    ict_rural_all_percent = None

    # rural, Mobile Phone (Smart)
    ict_mob_phone_smart_reg_rural_all_val = None
    ict_mob_phone_smart_reg_rural_all_percent = None
    ict_mob_phone_smart_rural_all_val = None
    ict_mob_phone_smart_rural_all_percent = None

    # rural, Mobile Phone (Non-Smart)
    ict_mob_phone_non_smart_reg_rural_all_val = None
    ict_mob_phone_non_smart_reg_rural_all_percent = None
    ict_mob_phone_non_smart_rural_all_val = None
    ict_mob_phone_non_smart_rural_all_percent = None

    # rural, Tablet
    ict_tablet_reg_rural_all_val = None
    ict_tablet_reg_rural_all_percent = None
    ict_tablet_rural_all_val = None
    ict_tablet_rural_all_percent = None

    # rural, Laptop
    ict_laptop_reg_rural_all_val = None
    ict_laptop_reg_rural_all_percent = None
    ict_laptop_rural_all_val = None
    ict_laptop_rural_all_percent = None

    # rural, None
    ict_none_reg_rural_all_val = None
    ict_none_reg_rural_all_percent = None
    ict_none_rural_all_val = None
    ict_none_rural_all_percent = None

    if (region != None) & (district != None):

        # get data
        df_data = df_ict_dic[region]

        # rural, Total
        df_rural = df_data[(df_data['Type'] == 'Rural All') & (df_data['Status_Code'] == 0) & (df_data['Device_Type'] == 'Total')][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]  # pop in percent
        df_rural = df_rural.reset_index(drop=True)

        ict_reg_rural_all_total = df_rural['Number'][0]
        ict_reg_rural_all_percent = df_rural['Percent'][0]
        ict_rural_all_total = df_rural[district][0]
        ict_rural_all_percent = (ict_rural_all_total /  ict_reg_rural_all_total) * 100

        # rural, Mobile Phone (Smart)
        df_mobile_sm = df_data[(df_data['Type'] == 'Rural All') & (df_data['Status_Code'] == 1)][['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_sm = df_mobile_sm.reset_index(drop=True)

        ict_mob_phone_smart_reg_rural_all_val = df_mobile_sm['Number'][0]
        ict_mob_phone_smart_reg_rural_all_percent = df_mobile_sm['Percent'][0]
        ict_mob_phone_smart_rural_all_val = df_mobile_sm[district][0]
        ict_mob_phone_smart_rural_all_percent = (ict_mob_phone_smart_rural_all_val / ict_reg_rural_all_total) * 100

        # rural, Mobile Phone (Non Smart)
        df_mobile_non_sm = df_data[(df_data['Type'] == 'Rural All') & (df_data['Status_Code'] == 2)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_non_sm = df_mobile_non_sm.reset_index(drop=True)

        ict_mob_phone_non_smart_reg_rural_all_val = df_mobile_non_sm['Number'][0]
        ict_mob_phone_non_smart_reg_rural_all_percent = df_mobile_non_sm['Percent'][0]
        ict_mob_phone_non_smart_rural_all_val = df_mobile_non_sm[district][0]
        ict_mob_phone_non_smart_rural_all_percent = (ict_mob_phone_non_smart_rural_all_val / ict_reg_rural_all_total) * 100

        # rural, Tablet
        df_tablet = df_data[(df_data['Type'] == 'Rural All') & (df_data['Status_Code'] == 3)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_tablet = df_tablet.reset_index(drop=True)

        ict_tablet_reg_rural_all_val = df_tablet['Number'][0]
        ict_tablet_reg_rural_all_percent = df_tablet['Percent'][0]
        ict_tablet_rural_all_val = df_tablet[district][0]
        ict_tablet_rural_all_percent = (ict_tablet_rural_all_val / ict_reg_rural_all_total) * 100

        # rural, Laptop
        df_laptop = df_data[(df_data['Type'] == 'Rural All') & (df_data['Status_Code'] == 4)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_laptop = df_laptop.reset_index(drop=True)

        ict_laptop_reg_rural_all_val = df_laptop['Number'][0]
        ict_laptop_reg_rural_all_percent = df_laptop['Percent'][0]
        ict_laptop_rural_all_val = df_laptop[district][0]
        ict_laptop_rural_all_percent = (ict_laptop_rural_all_val / ict_reg_rural_all_total) * 100

        # rural, None
        df_none = df_data[(df_data['Type'] == 'Rural All') & (df_data['Status_Code'] == 5)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_none = df_none.reset_index(drop=True)

        ict_none_reg_rural_all_val = df_none['Number'][0]
        ict_none_reg_rural_all_percent = df_none['Percent'][0]
        ict_none_rural_all_val = df_none[district][0]
        ict_none_rural_all_percent = (ict_none_rural_all_val / ict_reg_rural_all_total) * 100

        # Formatting

        #rural, total
        ict_reg_rural_all_total = '{:,}'.format(ict_reg_rural_all_total)
        ict_reg_rural_all_percent = '{:.1f}'.format(ict_reg_rural_all_percent)
        ict_rural_all_total = '{:,}'.format(ict_rural_all_total)
        ict_rural_all_percent = '{:.1f}'.format(ict_rural_all_percent)

        #rural, mobile phone (smart)
        ict_mob_phone_smart_reg_rural_all_val = '{:,}'.format(ict_mob_phone_smart_reg_rural_all_val)
        ict_mob_phone_smart_reg_rural_all_percent = '{:.1f}'.format(ict_mob_phone_smart_reg_rural_all_percent)
        ict_mob_phone_smart_rural_all_val = '{:,}'.format(ict_mob_phone_smart_rural_all_val)
        ict_mob_phone_smart_rural_all_percent = '{:.1f}'.format(ict_mob_phone_smart_rural_all_percent)

        # rural, mobile phone (non smart)
        ict_mob_phone_non_smart_reg_rural_all_val = '{:,}'.format(ict_mob_phone_non_smart_reg_rural_all_val)
        ict_mob_phone_non_smart_reg_rural_all_percent = '{:.1f}'.format(ict_mob_phone_non_smart_reg_rural_all_percent)
        ict_mob_phone_non_smart_rural_all_val = '{:,}'.format(ict_mob_phone_non_smart_rural_all_val)
        ict_mob_phone_non_smart_rural_all_percent = '{:.1f}'.format(ict_mob_phone_non_smart_rural_all_percent)

        #rural, tablet
        ict_tablet_reg_rural_all_val = '{:,}'.format(ict_tablet_reg_rural_all_val)
        ict_tablet_reg_rural_all_percent = '{:.1f}'.format(ict_tablet_reg_rural_all_percent)
        ict_tablet_rural_all_val = '{:,}'.format(ict_tablet_rural_all_val)
        ict_tablet_rural_all_percent = '{:.1f}'.format(ict_tablet_rural_all_percent)

        # rural, laptop
        ict_laptop_reg_rural_all_val = '{:,}'.format(ict_laptop_reg_rural_all_val)
        ict_laptop_reg_rural_all_percent = '{:.1f}'.format(ict_laptop_reg_rural_all_percent)
        ict_laptop_rural_all_val = '{:,}'.format(ict_laptop_rural_all_val)
        ict_laptop_rural_all_percent = '{:.1f}'.format(ict_laptop_rural_all_percent)

        # rural, none
        ict_none_reg_rural_all_val = '{:,}'.format(ict_none_reg_rural_all_val)
        ict_none_reg_rural_all_percent = '{:.1f}'.format(ict_none_reg_rural_all_percent)
        ict_none_rural_all_val = '{:,}'.format(ict_none_rural_all_val)
        ict_none_rural_all_percent = '{:.1f}'.format(ict_none_rural_all_percent)

    return ict_reg_rural_all_total, ict_reg_rural_all_percent, ict_rural_all_total, ict_rural_all_percent, \
           ict_mob_phone_smart_reg_rural_all_val, ict_mob_phone_smart_reg_rural_all_percent, ict_mob_phone_smart_rural_all_val, ict_mob_phone_smart_rural_all_percent, \
           ict_mob_phone_non_smart_reg_rural_all_val, ict_mob_phone_non_smart_reg_rural_all_percent, ict_mob_phone_non_smart_rural_all_val, ict_mob_phone_non_smart_rural_all_percent, \
           ict_tablet_reg_rural_all_val, ict_tablet_reg_rural_all_percent, ict_tablet_rural_all_val, ict_tablet_rural_all_percent, \
           ict_laptop_reg_rural_all_val, ict_laptop_reg_rural_all_percent, ict_laptop_rural_all_val, ict_laptop_rural_all_percent, \
           ict_none_reg_rural_all_val, ict_none_reg_rural_all_percent, ict_none_rural_all_val, ict_none_rural_all_percent


#********************************************************************
# ICT - Rural, Male
#********************************************************************
@app.callback(

    # all
    Output('ict_reg_rural_male_total', 'children'),
    Output('ict_reg_rural_male_percent', 'children'),
    Output('ict_rural_male_total', 'children'),
    Output('ict_rural_male_percent', 'children'),

    # rural, male, mobile phone (smart)
    Output('ict_mob_phone_smart_reg_rural_male_val', 'children'),
    Output('ict_mob_phone_smart_reg_rural_male_percent', 'children'),
    Output('ict_mob_phone_smart_rural_male_val', 'children'),
    Output('ict_mob_phone_smart_rural_male_percent', 'children'),

    # rural, mobile phone (non-smart)
    Output('ict_mob_phone_non_smart_reg_rural_male_val', 'children'),
    Output('ict_mob_phone_non_smart_reg_rural_male_percent', 'children'),
    Output('ict_mob_phone_non_smart_rural_male_val', 'children'),
    Output('ict_mob_phone_non_smart_rural_male_percent', 'children'),

    # rural, tablet
    Output('ict_tablet_reg_rural_male_val', 'children'),
    Output('ict_tablet_reg_rural_male_percent', 'children'),
    Output('ict_tablet_rural_male_val', 'children'),
    Output('ict_tablet_rural_male_percent', 'children'),

    # rural, laptop
    Output('ict_laptop_reg_rural_male_val', 'children'),
    Output('ict_laptop_reg_rural_male_percent', 'children'),
    Output('ict_laptop_rural_male_val', 'children'),
    Output('ict_laptop_rural_male_percent', 'children'),

    # rural, none
    Output('ict_none_reg_rural_male_val', 'children'),
    Output('ict_none_reg_rural_male_percent', 'children'),
    Output('ict_none_rural_male_val', 'children'),
    Output('ict_none_rural_male_percent', 'children'),

    Input('ict_region_dd', 'value'),
    Input('ict_district_dd', 'value')
)
def get_ict_rural_male(region, district):

    # rural, Regional
    ict_reg_rural_male_total = None
    ict_reg_rural_male_percent = None
    ict_rural_male_total = None
    ict_rural_male_percent = None

    # rural, Mobile Phone (Smart)
    ict_mob_phone_smart_reg_rural_male_val = None
    ict_mob_phone_smart_reg_rural_male_percent = None
    ict_mob_phone_smart_rural_male_val = None
    ict_mob_phone_smart_rural_male_percent = None

    # rural, Mobile Phone (Non-Smart)
    ict_mob_phone_non_smart_reg_rural_male_val = None
    ict_mob_phone_non_smart_reg_rural_male_percent = None
    ict_mob_phone_non_smart_rural_male_val = None
    ict_mob_phone_non_smart_rural_male_percent = None

    # rural, Tablet
    ict_tablet_reg_rural_male_val = None
    ict_tablet_reg_rural_male_percent = None
    ict_tablet_rural_male_val = None
    ict_tablet_rural_male_percent = None

    # rural, Laptop
    ict_laptop_reg_rural_male_val = None
    ict_laptop_reg_rural_male_percent = None
    ict_laptop_rural_male_val = None
    ict_laptop_rural_male_percent = None

    # rural, None
    ict_none_reg_rural_male_val = None
    ict_none_reg_rural_male_percent = None
    ict_none_rural_male_val = None
    ict_none_rural_male_percent = None

    if (region != None) & (district != None):

        # get data
        df_data = df_ict_dic[region]

        # rural, Total
        df_rural = df_data[(df_data['Type'] == 'Rural Male') & (df_data['Status_Code'] == 0) & (df_data['Device_Type'] == 'Total')][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]  # pop in percent
        df_rural = df_rural.reset_index(drop=True)

        ict_reg_rural_male_total = df_rural['Number'][0]
        ict_reg_rural_male_percent = df_rural['Percent'][0]
        ict_rural_male_total = df_rural[district][0]
        ict_rural_male_percent = (ict_rural_male_total /  ict_reg_rural_male_total) * 100

        # rural, Mobile Phone (Smart)
        df_mobile_sm = df_data[(df_data['Type'] == 'Rural Male') & (df_data['Status_Code'] == 1)][['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_sm = df_mobile_sm.reset_index(drop=True)

        ict_mob_phone_smart_reg_rural_male_val = df_mobile_sm['Number'][0]
        ict_mob_phone_smart_reg_rural_male_percent = df_mobile_sm['Percent'][0]
        ict_mob_phone_smart_rural_male_val = df_mobile_sm[district][0]
        ict_mob_phone_smart_rural_male_percent = (ict_mob_phone_smart_rural_male_val / ict_reg_rural_male_total) * 100

        # rural, Mobile Phone (Non Smart)
        df_mobile_non_sm = df_data[(df_data['Type'] == 'Rural Male') & (df_data['Status_Code'] == 2)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_non_sm = df_mobile_non_sm.reset_index(drop=True)

        ict_mob_phone_non_smart_reg_rural_male_val = df_mobile_non_sm['Number'][0]
        ict_mob_phone_non_smart_reg_rural_male_percent = df_mobile_non_sm['Percent'][0]
        ict_mob_phone_non_smart_rural_male_val = df_mobile_non_sm[district][0]
        ict_mob_phone_non_smart_rural_male_percent = (ict_mob_phone_non_smart_rural_male_val / ict_reg_rural_male_total) * 100

        # rural, Tablet
        df_tablet = df_data[(df_data['Type'] == 'Rural Male') & (df_data['Status_Code'] == 3)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_tablet = df_tablet.reset_index(drop=True)

        ict_tablet_reg_rural_male_val = df_tablet['Number'][0]
        ict_tablet_reg_rural_male_percent = df_tablet['Percent'][0]
        ict_tablet_rural_male_val = df_tablet[district][0]
        ict_tablet_rural_male_percent = (ict_tablet_rural_male_val / ict_reg_rural_male_total) * 100

        # rural, Laptop
        df_laptop = df_data[(df_data['Type'] == 'Rural Male') & (df_data['Status_Code'] == 4)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_laptop = df_laptop.reset_index(drop=True)

        ict_laptop_reg_rural_male_val = df_laptop['Number'][0]
        ict_laptop_reg_rural_male_percent = df_laptop['Percent'][0]
        ict_laptop_rural_male_val = df_laptop[district][0]
        ict_laptop_rural_male_percent = (ict_laptop_rural_male_val / ict_reg_rural_male_total) * 100

        # rural, None
        df_none = df_data[(df_data['Type'] == 'Rural Male') & (df_data['Status_Code'] == 5)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_none = df_none.reset_index(drop=True)

        ict_none_reg_rural_male_val = df_none['Number'][0]
        ict_none_reg_rural_male_percent = df_none['Percent'][0]
        ict_none_rural_male_val = df_none[district][0]
        ict_none_rural_male_percent = (ict_none_rural_male_val / ict_reg_rural_male_total) * 100

        # Formatting

        #rural, total
        ict_reg_rural_male_total = '{:,}'.format(ict_reg_rural_male_total)
        ict_reg_rural_male_percent = '{:.1f}'.format(ict_reg_rural_male_percent)
        ict_rural_male_total = '{:,}'.format(ict_rural_male_total)
        ict_rural_male_percent = '{:.1f}'.format(ict_rural_male_percent)

        #rural, mobile phone (smart)
        ict_mob_phone_smart_reg_rural_male_val = '{:,}'.format(ict_mob_phone_smart_reg_rural_male_val)
        ict_mob_phone_smart_reg_rural_male_percent = '{:.1f}'.format(ict_mob_phone_smart_reg_rural_male_percent)
        ict_mob_phone_smart_rural_male_val = '{:,}'.format(ict_mob_phone_smart_rural_male_val)
        ict_mob_phone_smart_rural_male_percent = '{:.1f}'.format(ict_mob_phone_smart_rural_male_percent)

        # rural, mobile phone (non smart)
        ict_mob_phone_non_smart_reg_rural_male_val = '{:,}'.format(ict_mob_phone_non_smart_reg_rural_male_val)
        ict_mob_phone_non_smart_reg_rural_male_percent = '{:.1f}'.format(ict_mob_phone_non_smart_reg_rural_male_percent)
        ict_mob_phone_non_smart_rural_male_val = '{:,}'.format(ict_mob_phone_non_smart_rural_male_val)
        ict_mob_phone_non_smart_rural_male_percent = '{:.1f}'.format(ict_mob_phone_non_smart_rural_male_percent)

        #rural, tablet
        ict_tablet_reg_rural_male_val = '{:,}'.format(ict_tablet_reg_rural_male_val)
        ict_tablet_reg_rural_male_percent = '{:.1f}'.format(ict_tablet_reg_rural_male_percent)
        ict_tablet_rural_male_val = '{:,}'.format(ict_tablet_rural_male_val)
        ict_tablet_rural_male_percent = '{:.1f}'.format(ict_tablet_rural_male_percent)

        # rural, laptop
        ict_laptop_reg_rural_male_val = '{:,}'.format(ict_laptop_reg_rural_male_val)
        ict_laptop_reg_rural_male_percent = '{:.1f}'.format(ict_laptop_reg_rural_male_percent)
        ict_laptop_rural_male_val = '{:,}'.format(ict_laptop_rural_male_val)
        ict_laptop_rural_male_percent = '{:.1f}'.format(ict_laptop_rural_male_percent)

        # rural, none
        ict_none_reg_rural_male_val = '{:,}'.format(ict_none_reg_rural_male_val)
        ict_none_reg_rural_male_percent = '{:.1f}'.format(ict_none_reg_rural_male_percent)
        ict_none_rural_male_val = '{:,}'.format(ict_none_rural_male_val)
        ict_none_rural_male_percent = '{:.1f}'.format(ict_none_rural_male_percent)

    return ict_reg_rural_male_total, ict_reg_rural_male_percent, ict_rural_male_total, ict_rural_male_percent, \
           ict_mob_phone_smart_reg_rural_male_val, ict_mob_phone_smart_reg_rural_male_percent, ict_mob_phone_smart_rural_male_val, ict_mob_phone_smart_rural_male_percent, \
           ict_mob_phone_non_smart_reg_rural_male_val, ict_mob_phone_non_smart_reg_rural_male_percent, ict_mob_phone_non_smart_rural_male_val, ict_mob_phone_non_smart_rural_male_percent, \
           ict_tablet_reg_rural_male_val, ict_tablet_reg_rural_male_percent, ict_tablet_rural_male_val, ict_tablet_rural_male_percent, \
           ict_laptop_reg_rural_male_val, ict_laptop_reg_rural_male_percent, ict_laptop_rural_male_val, ict_laptop_rural_male_percent, \
           ict_none_reg_rural_male_val, ict_none_reg_rural_male_percent, ict_none_rural_male_val, ict_none_rural_male_percent


#********************************************************************
# ICT - Rural, Female
#********************************************************************
@app.callback(

    # all
    Output('ict_reg_rural_female_total', 'children'),
    Output('ict_reg_rural_female_percent', 'children'),
    Output('ict_rural_female_total', 'children'),
    Output('ict_rural_female_percent', 'children'),

    # rural, female, mobile phone (smart)
    Output('ict_mob_phone_smart_reg_rural_female_val', 'children'),
    Output('ict_mob_phone_smart_reg_rural_female_percent', 'children'),
    Output('ict_mob_phone_smart_rural_female_val', 'children'),
    Output('ict_mob_phone_smart_rural_female_percent', 'children'),

    # rural, mobile phone (non-smart)
    Output('ict_mob_phone_non_smart_reg_rural_female_val', 'children'),
    Output('ict_mob_phone_non_smart_reg_rural_female_percent', 'children'),
    Output('ict_mob_phone_non_smart_rural_female_val', 'children'),
    Output('ict_mob_phone_non_smart_rural_female_percent', 'children'),

    # rural, tablet
    Output('ict_tablet_reg_rural_female_val', 'children'),
    Output('ict_tablet_reg_rural_female_percent', 'children'),
    Output('ict_tablet_rural_female_val', 'children'),
    Output('ict_tablet_rural_female_percent', 'children'),

    # rural, laptop
    Output('ict_laptop_reg_rural_female_val', 'children'),
    Output('ict_laptop_reg_rural_female_percent', 'children'),
    Output('ict_laptop_rural_female_val', 'children'),
    Output('ict_laptop_rural_female_percent', 'children'),

    # rural, none
    Output('ict_none_reg_rural_female_val', 'children'),
    Output('ict_none_reg_rural_female_percent', 'children'),
    Output('ict_none_rural_female_val', 'children'),
    Output('ict_none_rural_female_percent', 'children'),

    Input('ict_region_dd', 'value'),
    Input('ict_district_dd', 'value')
)
def get_ict_rural_female(region, district):

    # rural, Regional
    ict_reg_rural_female_total = None
    ict_reg_rural_female_percent = None
    ict_rural_female_total = None
    ict_rural_female_percent = None

    # rural, Mobile Phone (Smart)
    ict_mob_phone_smart_reg_rural_female_val = None
    ict_mob_phone_smart_reg_rural_female_percent = None
    ict_mob_phone_smart_rural_female_val = None
    ict_mob_phone_smart_rural_female_percent = None

    # rural, Mobile Phone (Non-Smart)
    ict_mob_phone_non_smart_reg_rural_female_val = None
    ict_mob_phone_non_smart_reg_rural_female_percent = None
    ict_mob_phone_non_smart_rural_female_val = None
    ict_mob_phone_non_smart_rural_female_percent = None

    # rural, Tablet
    ict_tablet_reg_rural_female_val = None
    ict_tablet_reg_rural_female_percent = None
    ict_tablet_rural_female_val = None
    ict_tablet_rural_female_percent = None

    # rural, Laptop
    ict_laptop_reg_rural_female_val = None
    ict_laptop_reg_rural_female_percent = None
    ict_laptop_rural_female_val = None
    ict_laptop_rural_female_percent = None

    # rural, None
    ict_none_reg_rural_female_val = None
    ict_none_reg_rural_female_percent = None
    ict_none_rural_female_val = None
    ict_none_rural_female_percent = None

    if (region != None) & (district != None):

        # get data
        df_data = df_ict_dic[region]

        # Rural, Total
        df_rural = df_data[(df_data['Type'] == 'Rural Female') & (df_data['Status_Code'] == 0) & (df_data['Device_Type'] == 'Total')][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]  # pop in percent
        df_rural = df_rural.reset_index(drop=True)

        ict_reg_rural_female_total = df_rural['Number'][0]
        ict_reg_rural_female_percent = df_rural['Percent'][0]
        ict_rural_female_total = df_rural[district][0]
        ict_rural_female_percent = (ict_rural_female_total /  ict_reg_rural_female_total) * 100

        # rural, Mobile Phone (Smart)
        df_mobile_sm = df_data[(df_data['Type'] == 'Rural Female') & (df_data['Status_Code'] == 1)][['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_sm = df_mobile_sm.reset_index(drop=True)

        ict_mob_phone_smart_reg_rural_female_val = df_mobile_sm['Number'][0]
        ict_mob_phone_smart_reg_rural_female_percent = df_mobile_sm['Percent'][0]
        ict_mob_phone_smart_rural_female_val = df_mobile_sm[district][0]
        ict_mob_phone_smart_rural_female_percent = (ict_mob_phone_smart_rural_female_val / ict_reg_rural_female_total) * 100

        # rural, Mobile Phone (Non Smart)
        df_mobile_non_sm = df_data[(df_data['Type'] == 'Rural Female') & (df_data['Status_Code'] == 2)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_mobile_non_sm = df_mobile_non_sm.reset_index(drop=True)

        ict_mob_phone_non_smart_reg_rural_female_val = df_mobile_non_sm['Number'][0]
        ict_mob_phone_non_smart_reg_rural_female_percent = df_mobile_non_sm['Percent'][0]
        ict_mob_phone_non_smart_rural_female_val = df_mobile_non_sm[district][0]
        ict_mob_phone_non_smart_rural_female_percent = (ict_mob_phone_non_smart_rural_female_val / ict_reg_rural_female_total) * 100

        # rural, Tablet
        df_tablet = df_data[(df_data['Type'] == 'Rural Female') & (df_data['Status_Code'] == 3)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_tablet = df_tablet.reset_index(drop=True)

        ict_tablet_reg_rural_female_val = df_tablet['Number'][0]
        ict_tablet_reg_rural_female_percent = df_tablet['Percent'][0]
        ict_tablet_rural_female_val = df_tablet[district][0]
        ict_tablet_rural_female_percent = (ict_tablet_rural_female_val / ict_reg_rural_female_total) * 100

        # rural, Laptop
        df_laptop = df_data[(df_data['Type'] == 'Rural Female') & (df_data['Status_Code'] == 4)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_laptop = df_laptop.reset_index(drop=True)

        ict_laptop_reg_rural_female_val = df_laptop['Number'][0]
        ict_laptop_reg_rural_female_percent = df_laptop['Percent'][0]
        ict_laptop_rural_female_val = df_laptop[district][0]
        ict_laptop_rural_female_percent = (ict_laptop_rural_female_val / ict_reg_rural_female_total) * 100

        # rural, None
        df_none = df_data[(df_data['Type'] == 'Rural Female') & (df_data['Status_Code'] == 5)][
            ['Device_Type', 'Status_Code', 'Type', 'Number', 'Percent', district]]
        df_none = df_none.reset_index(drop=True)

        ict_none_reg_rural_female_val = df_none['Number'][0]
        ict_none_reg_rural_female_percent = df_none['Percent'][0]
        ict_none_rural_female_val = df_none[district][0]
        ict_none_rural_female_percent = (ict_none_rural_female_val / ict_reg_rural_female_total) * 100

        # Formatting

        #rural, total
        ict_reg_rural_female_total = '{:,}'.format(ict_reg_rural_female_total)
        ict_reg_rural_female_percent = '{:.1f}'.format(ict_reg_rural_female_percent)
        ict_rural_female_total = '{:,}'.format(ict_rural_female_total)
        ict_rural_female_percent = '{:.1f}'.format(ict_rural_female_percent)

        #rural, mobile phone (smart)
        ict_mob_phone_smart_reg_rural_female_val = '{:,}'.format(ict_mob_phone_smart_reg_rural_female_val)
        ict_mob_phone_smart_reg_rural_female_percent = '{:.1f}'.format(ict_mob_phone_smart_reg_rural_female_percent)
        ict_mob_phone_smart_rural_female_val = '{:,}'.format(ict_mob_phone_smart_rural_female_val)
        ict_mob_phone_smart_rural_female_percent = '{:.1f}'.format(ict_mob_phone_smart_rural_female_percent)

        # rural, mobile phone (non smart)
        ict_mob_phone_non_smart_reg_rural_female_val = '{:,}'.format(ict_mob_phone_non_smart_reg_rural_female_val)
        ict_mob_phone_non_smart_reg_rural_female_percent = '{:.1f}'.format(ict_mob_phone_non_smart_reg_rural_female_percent)
        ict_mob_phone_non_smart_rural_female_val = '{:,}'.format(ict_mob_phone_non_smart_rural_female_val)
        ict_mob_phone_non_smart_rural_female_percent = '{:.1f}'.format(ict_mob_phone_non_smart_rural_female_percent)

        #rural, tablet
        ict_tablet_reg_rural_female_val = '{:,}'.format(ict_tablet_reg_rural_female_val)
        ict_tablet_reg_rural_female_percent = '{:.1f}'.format(ict_tablet_reg_rural_female_percent)
        ict_tablet_rural_female_val = '{:,}'.format(ict_tablet_rural_female_val)
        ict_tablet_rural_female_percent = '{:.1f}'.format(ict_tablet_rural_female_percent)

        # rural, laptop
        ict_laptop_reg_rural_female_val = '{:,}'.format(ict_laptop_reg_rural_female_val)
        ict_laptop_reg_rural_female_percent = '{:.1f}'.format(ict_laptop_reg_rural_female_percent)
        ict_laptop_rural_female_val = '{:,}'.format(ict_laptop_rural_female_val)
        ict_laptop_rural_female_percent = '{:.1f}'.format(ict_laptop_rural_female_percent)

        # rural, none
        ict_none_reg_rural_female_val = '{:,}'.format(ict_none_reg_rural_female_val)
        ict_none_reg_rural_female_percent = '{:.1f}'.format(ict_none_reg_rural_female_percent)
        ict_none_rural_female_val = '{:,}'.format(ict_none_rural_female_val)
        ict_none_rural_female_percent = '{:.1f}'.format(ict_none_rural_female_percent)

    return ict_reg_rural_female_total, ict_reg_rural_female_percent, ict_rural_female_total, ict_rural_female_percent, \
           ict_mob_phone_smart_reg_rural_female_val, ict_mob_phone_smart_reg_rural_female_percent, ict_mob_phone_smart_rural_female_val, ict_mob_phone_smart_rural_female_percent, \
           ict_mob_phone_non_smart_reg_rural_female_val, ict_mob_phone_non_smart_reg_rural_female_percent, ict_mob_phone_non_smart_rural_female_val, ict_mob_phone_non_smart_rural_female_percent, \
           ict_tablet_reg_rural_female_val, ict_tablet_reg_rural_female_percent, ict_tablet_rural_female_val, ict_tablet_rural_female_percent, \
           ict_laptop_reg_rural_female_val, ict_laptop_reg_rural_female_percent, ict_laptop_rural_female_val, ict_laptop_rural_female_percent, \
           ict_none_reg_rural_female_val, ict_none_reg_rural_female_percent, ict_none_rural_female_val, ict_none_rural_female_percent

#***********************************************************
#   POPULATION PYRAMID
#***********************************************************
@app.callback(

    Output('age_pyramid', 'children'),

    Input('pyramid_region_dd', 'value'),
    Input('pyramid_district_dd', 'value')
)
def get_population_pyramid(region, district):

    fig = None
    config = {}

    if (region != None) & (district != None):

        western = ['Jomoro', 'Ellembelle', 'Nzema East', 'Ahanta West', 'Effia Kwesimintsim',
                   'Stma-Takoradi', 'Stma-Sekondi', 'Stma-Essikado Ketan', 'Shama', 'Wassa East', 'Mpohor',
                   'Tarkwa Nsuaem', 'Prestea Huni Valley', 'Wassa Amenfi East', 'Wassa Amenfi Central',
                   'Wassa Amenfi West']

        central = ['Komenda Edina Eguafo Abirem', 'Ccma-Cape Coast South', 'Ccma-Cape Coast North',
                   'Abura Asebu Kwamankese', 'Gomoa West',
                   'Effutu', 'Gomoa Central',
                   'Gomoa East', 'Awutu Senya East', 'Awutu Senya', 'Agona East', 'Agona West',
                   'Asikuman / Odoben / Brakwa', 'Ajumako-Enyan-Esiam', 'Assin South', 'Twifo Heman Lower Denkyira',
                   'Twifo Ati Morkwa',
                   'Assin Fosu  Municipal', 'Assin North', 'Upper Denkyira East', 'Upper Denkyira West']

        volta = ['South Tongu', 'Anloga', 'Keta Municipal', 'Ketu South', 'Ketu North', 'Akatsi North', 'Akatsi South',
                 'Central Tongu',
                 'North Tongu', 'Ho-West', 'Adaklu', 'Agortime Ziope', 'Ho', 'South Dayi', 'Afadzato South',
                 'North Dayi', 'Kpando Municipal']

        eastern = ['Birim South', 'Birim Central', 'Achiase', 'Asene Manso Akroso', 'West Akim', 'Upper West Akim',
                   'Ayensuano',
                   'Nsawam Adoagyiri Municipal', 'Akwapim South', 'Akwapim North', 'Okere', 'New Juaben South',
                   'New Juaben North', 'Suhum Municipal',
                   'Abuakwa South', 'Abuakwa North', 'Denkyembour', 'Akyemansa', 'Kwaebibirem', 'Birim North',
                   'Atiwa West', 'Atiwa East',
                   'Fanteakwa South', 'Yilo Krobo Municipal', 'Lower Manya Krobo Municipal', 'Asuogyaman',
                   'Upper Manya Krobo',
                   'Fanteakwa North', 'Kwahu South Municipal', 'Kwahu West Municipal', 'Kwahu East',
                   'Kwahu Afram Plains South', 'Kwahu Afram Plains North']

        ashanti = ['Amansie South', 'Amansie Central', 'Akrofuom', 'Adansi South',
                   'Adansi Asokwa', 'Obuasi East', 'Obuasi Municipal', 'Adansi North',
                   'Bekwai Municipal', 'Amansie West', 'Atwima Kwanwoma', 'Bosomtwi',
                   'Bosome Freho', 'Asante Akim Central Municipal',
                   'Asante Akim South Municipal', 'Asante Akim North', 'Sekyere Kumawu',
                   'Sekyere East', 'Juaben Municipal', 'Ejisu Municipal', 'Oforikrom Municipal',
                   'Asokwa Municipal', 'Kma-Nhyiaeso', 'Kma-Subin', 'Kma-Manhyia South',
                   'Kma-Manhyia North', 'Kma-Bantama', 'Kwadaso Municipal',
                   'Suame Municipal', 'Old Tafo Municipal', 'Asokore Mampong Municipal',
                   'Kwabre East', 'Afigya Kwabre South', 'Atwima Nwabiagya North',
                   'Atwima Nwabiagya South Municipal', 'Atwima Mponua',
                   'Ahafo Ano South West', 'Ahafo Ano North Municipal', 'Ahafo Ano South East',
                   'Offinso North', 'Offinso Municipal', 'Afigya Kwabre North',
                   'Sekyere South', 'Mampong Municipal', 'Ejura Sekyedumase Municipal',
                   'Sekyere Central', 'Sekyere Afram Plains']

        western_north = ['Aowin Municipal', 'Sefwi Akontombra', 'Suaman', 'Bodi',
                     'Sefwi Wiawso', 'Bibiani Anhwiaso Bekwai', 'Juaboso', 'Bia West', 'Bia East']

        ahafo = ['Asunafo South', 'Asunafo North Municipal', 'Asutifi South',
                 'Asutifi  North', 'Tano North', 'Tano South Municipal']

        bono = ['Dormaa West', 'Dormaa Municipal', 'Dormaa East',
                'Sunyani Municipal', 'Sunyani West', 'Berekum East Municipal',
                'Berekum West', 'Jaman South Municipal', 'Jaman North', 'Tain',
                'Wenchi Municipal', 'Banda']

        lst = []
        img = None
        fig = None

        config = {
            'scrollZoom': False,
            'displayModeBar': True,
            'editable': True,
            'showLink': False,
            'displaylogo': False
        }

        if district != None:
            lst.append(re.split('[ -]+', district))
            for l in lst:
                lx = ''.join(l)
                lx = lx.lower()

            distr_img_name = lx

        #print(distr_img_name)
        if region == 'Western':
            if district in western:
                img = np.array(Image.open(f'assets/age_pyramid/western/{distr_img_name}.png'))

        if region == 'Central':
            if district in central:
                img = np.array(Image.open(f'assets/age_pyramid/central/{distr_img_name}.png'))

        if region == 'Volta':
            if district in volta:
                img = np.array(Image.open(f'assets/age_pyramid/volta/{distr_img_name}.png'))

        if region == 'Eastern':
            if district in eastern:
                img = np.array(Image.open(f'assets/age_pyramid/eastern/{distr_img_name}.png'))

        if region == 'Ashanti':
            if district in ashanti:
                img = np.array(Image.open(f'assets/age_pyramid/ashanti/{distr_img_name}.png'))

        if region == 'Western North':
            if district in western_north:
                img = np.array(Image.open(f'assets/age_pyramid/western_north/{distr_img_name}.png'))

        if region == 'Ahafo':
            if district in ahafo:
                img = np.array(Image.open(f'assets/age_pyramid/ahafo/{distr_img_name}.png'))

        if region == 'Bono':
            if district in bono:
                img = np.array(Image.open(f'assets/age_pyramid/bono/{distr_img_name}.png'))

        if len(img) > 0:
            fig = px.imshow(img, color_continuous_scale='gray')
            # fig.update_layout(coloraxis_showscale=False, width=1000, height=1000,  margin=dict(t=0, r=0, b=0, l=50,))
            fig.update_layout(width=1000, height=600, margin=dict(l=20, r=20, t=40, b=20), title=district,
                              modebar_remove=['logo', 'zoom', 'pan', 'zoomIn2d', 'zoomOut2d', 'autoScale2d',
                                              'resetScale2d', 'plotly-logomark'])
            fig.update_xaxes(showticklabels=False)
            fig.update_yaxes(showticklabels=False)
            fig.update_xaxes(title=None)
            fig.update_yaxes(title=None)

            #fig.show()

        return dcc.Graph(figure=fig, config=config)



#****************************************************************************************************************
# CLEAR BUTTONS CALLBACKS
#****************************************************************************************************************

#region & districts
@app.callback(
    Output('pop_reg_dist_region_dd', 'value'),
    Output('pop_reg_dist_district_dd', 'value'),

    Input('pop_dist_clear_btn', 'n_clicks')
)
def clear_search_pop_reg_dist(n_clicks):

    if (n_clicks > 0):
        return None, None
    else:
        return None, None

#Age and sex
@app.callback(
    Output('age_sex_region_dd', 'value'),
    Output('age_sex_district_dd', 'value'),
    Input('age_sex_clear_btn', 'n_clicks')
)
def clear_search_age_sex(n_clicks):

    if (n_clicks > 0):
        return None, None
    else:
        return None, None

#background & characteristics
@app.callback(
    Output('bg_xtics_region_dd', 'value'),
    Output('bg_xtics_district_dd', 'value'),

    Input('clear_all_btn_background', 'n_clicks')
)
def clear_bg_xtics(n_clicks):

    if (n_clicks > 0):
        return None, None
    else:
        return None, None

#literacy and education
@app.callback(
    Output('lit_edu_district_dd', 'value'),
    Output('lit_edu_region_dd', 'value'),

    Input('clear_lit_edu_btn', 'n_clicks')
)
def clear_lit_edu(n_clicks):

    if (n_clicks > 0):
        return None, None
    else:
        return None, None

#fertility & mortality
@app.callback(
    Output('fert_mort_region_dd', 'value'),
    Output('fert_mort_district_dd', 'value'),

    Input('fert_mort_clear_btn', 'n_clicks')
)
def clear_fert_mort(n_clicks):

    if (n_clicks > 0):
        return None, None
    else:
        return None, None

#housing
@app.callback(
    Output('housing_region_dd', 'value'),
    Output('housing_district_dd', 'value'),

    Input('housing_clear_btn', 'n_clicks')
)
def clear_housing(n_clicks):

    if (n_clicks > 0):
        return None, None
    else:
        return None, None


#population pyramid
@app.callback(
    Output('pyramid_region_dd', 'value'),
    Output('pyramid_district_dd', 'value'),

    Input('pyramid_clear_btn', 'n_clicks')
)
def clear_pyramid(n_clicks):

    if (n_clicks > 0):
        return None, None
    else:
        return None, None


#Serving local static files
@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)

#RUN APPLICATION
if __name__ == '__main__':
    app.run_server(debug=False)
