import dash_bootstrap_components as dbc

def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Population", # Label given to the dropdown menu
                children=[
                    dbc.DropdownMenuItem("National", href='/national'),
                    dbc.DropdownMenuItem("Regions & Districts", href='/region_district'),
                ],
            ),

            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Socio-Demographics",
                children=[
                    dbc.DropdownMenuItem("Age & Sex Profile", href='/age_sex'),
                    dbc.DropdownMenuItem("Background Characteristics", href='/bg_xtics'),
                    dbc.DropdownMenuItem("Difficulty in Performing Activities", href='/diff_perf_act'),
                    dbc.DropdownMenuItem("Fertlity & Mortality", href='/fert_mort'),
                    dbc.DropdownMenuItem("Literacy & Education", href='/lit_edu'),
                    dbc.DropdownMenuItem("Population Pyramid", href='/population_pyramid'),
                ],
            ),

            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Social",  # Label given to the dropdown menu
                children=[
                    dbc.DropdownMenuItem("Housing", href='/housing'),
                    dbc.DropdownMenuItem("Water & Sanitation", href='/water_sanitation'),
                    dbc.DropdownMenuItem("Structures", href='/structures'),

                ],
            ),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Economic",
                children=[
                    dbc.DropdownMenuItem("Economic Activities", href='/economic_activity'),
                    dbc.DropdownMenuItem("Information & Communication Technology", href='/ict'),

                ],
            ),

            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="GIS",  # Label given to the dropdown menu
                children=[
                    dbc.DropdownMenuItem("National", href='/'),  # Hyperlink item that appears in the dropdown menu
                    dbc.DropdownMenuItem("Regions and Districts", href='/'),  # Hyperlink item that appears in the dropdown menu

                ],
            ),
        ],
        brand="Home",  # Set the text on the left side of the Navbar
        brand_href="/",  # Set the URL where the user will be sent when they click the brand we just created "Home"
        sticky="top",  # Stick it to the top... like Spider Man crawling on the ceiling?
        color="navy",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for light text)
        links_left=True,
        className='navbar-nav nav-pills',
        style={'text-decoration':'none', 'color':'white', 'fontSize':'20px', 'fontWeight':'bold', 'margin': '5px'}

    )

    return navbar