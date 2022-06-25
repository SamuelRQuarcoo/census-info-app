from dash import html
from navbar import create_navbar
import dash_bootstrap_components as dbc
import os
import base64
image_directory =  os.getcwd()
image_filename = image_directory + '/assets/people.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

#invoke methods to create layout of home
nav = create_navbar();
header = html.Div([
    dbc.Row([
        dbc.Col([
            html.Br(),
            html.H1('GHANA STATISTICAL SERVICE'),
        ], width=12),
        dbc.Col([
            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))
        ], width=12)
    ], className='text-center'),

])

def create_page_home():
    layout = html.Div([
        nav,
        header
    ])

    return layout