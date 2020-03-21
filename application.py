# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import application, app
from pages import index, actions, bulletin, predictions
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output



# app = dash.Dash(__name__)

# app.layout = html.Div([
#     dcc.Tabs(id="tabs-styled-with-props", value='tab-1', children=[
#         dcc.Tab(label='1', value='tab-1'),
#         dcc.Tab(label='2', value='tab-2'),
#     ], colors={
#         "border": "white",
#         "primary": "gold",
#         "background": "cornsilk"
#     }),
#     html.Div(id='tabs-content-props')
# ])

# @app.callback(Output('tabs-content-props', 'children'),
#               [Input('tabs-styled-with-props', 'value')])
# def render_content(tab):
#     if tab == 'tab-1':
#         return html.Div([
#             html.H3('Tab content 1')
#         ])
#     elif tab == 'tab-2':
#         return html.Div([
#             html.H3('Tab content 2')
#         ])

# if __name__ == '__main__':
#     app.run_server(debug=True)




# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(

    brand='Covid-19 Cases NYC',
    brand_style={'fontSize':20, 'paddingLeft':0, 'paddingRight':0},
    brand_href='/', 
    children=[
        #dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), # Virtual Fitness
        dbc.NavItem(dcc.Link('This too shall pass', href='/actions', className='nav-link')), # Affirmations #follow therapists # new ideas to manage and engage with wellness, committing to best practices with what we can control
        # dbc.NavItem(dcc.Link('Bulletin Board', href='/bulletin', className='nav-link')), # changes that better reflect the humanity that we want to see in our systems
    ],
    sticky='top',
    color='light', 
    light=True, 
    dark=False,
    style={'marginLeft': 0, 'marginRight': 0, 'fontSize':14, 'height': 60}
)


# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                html.Center(
                    [
                        html.Br(),
                        html.Span(' Powered by Data Analytics NYC', className='mr-2'), 
                        html.Br(),
                        html.Span(' ', className='mr-1'), 
                        html.Br(),
                        html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/LilySu/Covid-19nyc'), 
                        html.Span(' Data Analytics by Lily Su', className='mr-1'), 
                        html.A(html.I(className='fab fa-github-square mr-1'), href='https://www.linkedin.com/in/lilyxsu/'), 
                        html.Br(),
                        html.Span(' ', className='mr-1'), 
                        html.Br(),
                        html.A(html.I(className='fa fa-id-card mr-1'), href='http://www.joshmongeau.com/'), 
                        html.Span(' Design by Josh Mongeau', className='mr-1'), 
                        html.A(html.I(className='fa fa-id-card mr-1'), href='http://www.joshmongeau.com/'), 
                        html.Br(),
                        html.Span(' ', className='mr-1'), 
                        html.Br(),
                        html.A(html.I(className='fa fa-hand-spock mr-1'), href='http://dataanalyticsnyc.com/'), 
                        html.Span(' ', className='mr-1'), 
                        html.Br(),
                        html.Span(' ', className='mr-1'),
                        html.Br(), 
                    ], 
                    className='lead', style={ 'fontSize': 18}
                )
            )
        )
    )
)

# Layout docs:
# html.Div: https://dash.plot.ly/getting-started
# dcc.Location: https://dash.plot.ly/dash-core-components/location
# dbc.Container: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-12', fluid=True), 
    html.Hr(), 
    footer
])


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/insights':
        return insights.layout
    elif pathname == '/process':
        return process.layout
    else:
        return dcc.Markdown('## Page not found')

# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    application.run(debug=True)