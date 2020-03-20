# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app
import plotly.figure_factory as ff
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd



# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# column1 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
        
#             #### Your Value Proposition

#             Emphasize how the app will benefit users. Don't emphasize the underlying technology.

#             ✅ RUN is a running app that adapts to your fitness levels and designs personalized workouts to help you improve your running.

#             ❌ RUN is the only intelligent running app that uses sophisticated deep neural net machine learning to make your run smarter because we believe in ML driven workouts.

#             """
#         ),
#         dcc.Link(dbc.Button('Your Call To Action', color='primary'), href='/predictions')
#     ],
#     md=2,
# )


# table_data = [['Team', 'Wins', 'Losses'],
#               ['Montréal<br>Canadiens', 18, 4],
#               ['Dallas Stars', 18, 5],
#               ['NY Rangers', 16, 5],
#               ['Boston<br>Bruins', 13, 8],
#               ['Chicago<br>Blackhawks', 13, 8],
#               ['LA Kings', 13, 8],
#               ['Ottawa<br>Senators', 12, 5],
#               ['Boston<br>Bruins', 13, 8],
#               ['Chicago<br>Blackhawks', 13, 8],
#               ['LA Kings', 13, 8],
#               ['Ottawa<br>Senators', 12, 5]]

# fig4 = ff.create_table(table_data, height_constant=60)

# # Update the margins to add a title and see graph x-labels.
# fig4.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 50})

#------------------------------------

# import plotly.graph_objects as go
# from plotly.colors import n_colors
# import numpy as np
# np.random.seed(1)

# colors = n_colors('rgba(255, 255, 255, 0)', 'rgba(205, 248, 215, 0.6)', 9, colortype='rgb')
# a = np.random.randint(low=0, high=9, size=10)
# b = np.random.randint(low=0, high=9, size=10)
# c = np.random.randint(low=0, high=9, size=10)

# fig4 = go.Figure(data=[go.Table(
#   header=dict(
#     values=['<b>Column A</b>', '<b>Column B</b>', '<b>Column C</b>'],
#     line_color='white', fill_color='white',
#     align='center',font=dict(color='rgba(50, 112, 90, 0.8)', size=23)
#   ),
#   cells=dict(
#     values=[a, b, c],
#     line_color=[np.array(colors)[a],np.array(colors)[b], np.array(colors)[c]],
#     fill_color=[np.array(colors)[a],np.array(colors)[b], np.array(colors)[c]],
#     align=['center', 'center'], font=dict(color='rgba(50, 112, 90, 0.8)', size=30), height = 80
#     ))
# ])
# fig4.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 60})



# gapminder = px.data.gapminder()
# fig1 = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)


import plotly.graph_objects as go

top_labels = ['Strongly<br>agree', 'Agree', 'Neutral', 'Disagree',
              'Strongly<br>disagree']

colors = ['rgba(191, 253, 229, 0.68)', 'rgba(208, 251, 222, 0.48)',
          'rgba(208, 251, 222, 0.8)', 'rgba(208, 251, 222, 0.8)',
          'rgba(223, 251, 234, 1)']

x_data = [[21, 30, 21, 16, 12],
          [24, 31, 19, 15, 11],
          [27, 26, 23, 11, 13],
          [27, 26, 23, 11, 13],
          [29, 24, 15, 18, 14]]

y_data = ['03-17-2020',
          '03-16-2020',
          '03-15-2020',
          '03-14-2020',
          '03-13-2020',
          '03-12-2020']

fig = go.Figure()

for i in range(0, len(x_data[0])):
    for xd, yd in zip(x_data, y_data):
        fig.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
            )
        ))

fig.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=120, r=10, t=140, b=25),
    showlegend=False,
)

annotations = []

for yd, xd in zip(y_data, x_data):
    # labeling the y-axis
    annotations.append(dict(xref='paper', yref='y',
                            x=0.14, y=yd,
                            xanchor='right',
                            text=str(yd),
                            font=dict(family='Arial', size=14,
                                      color='rgb(67, 67, 67)'),
                            showarrow=False, align='right'))
    # labeling the first percentage of each bar (x_axis)
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text=str(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='rgb(248, 248, 255)'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.1,
                                text=top_labels[0],
                                font=dict(family='Arial', size=14,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=14,
                                              color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i]/2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=14,
                                                  color='rgb(67, 67, 67)'),
                                        showarrow=False))
            space += xd[i]

fig.update_layout(annotations=annotations)
fig.layout.margin.update({'t':0, 'b':0, 'r': 25, 'l': 50})

#---------------------------------------------

mapbox_access_token = "pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txcjE4NDAwNngzZms0ZndzNGM3dG0ifQ.gXrN0wMYVhqUp7t1LOHEwA"
#open(".mapbox_token").read()

df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-16-2020.csv')

fig1 = go.Figure()

fig1 = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_data=["Country/Region",'Confirmed', 'Deaths'],
                        size='Confirmed', zoom=2, color = 'Confirmed', color_continuous_scale=px.colors.sequential.Purp, size_max=50,height=600)

fig1.update_layout(
    mapbox_style="white-bg",
    hovermode='closest',
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                "https://api.mapbox.com/styles/v1/lilysu/ck7v7bqqy08ae1irye0k0jcot/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
            ] 
        },
        # {
        #     "sourcetype": "raster",
        #     "source": ["https://geo.weather.gc.ca/geomet/?"
        #                "SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857"
        #                "&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR_1KM_RDBR&TILED=true&FORMAT=image/png"],
        # }
      ])
fig1.update_layout(coloraxis_showscale = False)
fig1.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})

#---------------------------------------------------------------------------

import plotly.graph_objects as go
import numpy as np

title = 'Main Source for News'
labels = ['Television', 'Newspaper', 'Internet', 'Radio']
colors = ['rgb(67,67,67)', 'rgb(115,115,115)', 'rgba(206, 248, 218, 1)', 'rgb(189,189,189)']

mode_size = [8, 8, 12, 8]
line_size = [2, 2, 4, 2]

x_data = np.vstack((np.arange(2001, 2014),)*4)

y_data = np.array([
    [74, 82, 80, 74, 73, 72, 74, 70, 70, 66, 66, 69],
    [45, 42, 50, 46, 36, 36, 34, 35, 32, 31, 31, 28],
    [13, 14, 20, 24, 20, 24, 24, 40, 35, 41, 43, 50],
    [18, 21, 18, 21, 16, 14, 13, 18, 17, 16, 19, 23],
])

fig4 = go.Figure()

for i in range(0, 4):
    fig4.add_trace(go.Scatter(x=x_data[i], y=y_data[i], mode='lines',
        name=labels[i],
        line=dict(color=colors[i]),
        connectgaps=True,
    ))

    # endpoints
    fig4.add_trace(go.Scatter(
        x=[x_data[i][0], x_data[i][-1]],
        y=[y_data[i][0], y_data[i][-1]],
        mode='markers',
        marker=dict(color=colors[i], size=mode_size[i])
    ))

fig4.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
    ),
    autosize=True,
    # margin=dict(
    #     autoexpand=False,
    #     l=100,
    #     r=100,
    #     t=110,
    # ),
    showlegend=False,
    plot_bgcolor='white'
)

annotations = []

# Adding labels
for y_trace, label, color in zip(y_data, labels, colors):
    # labeling the left_side of the plot
    annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                                  xanchor='right', yanchor='middle',
                                  text=label + ' {}%'.format(y_trace[0]),
                                  font=dict(family='Arial',
                                            size=16),
                                  showarrow=False))
    # labeling the right_side of the plot
    annotations.append(dict(xref='paper', x=0.95, y=y_trace[11],
                                  xanchor='left', yanchor='middle',
                                  text='{}%'.format(y_trace[11]),
                                  font=dict(family='Arial',
                                            size=16),
                                  showarrow=False))
# Title
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Main Source for News',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
# Source
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: PewResearch Center & ' +
                                   'Storytelling with data',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))

fig4.update_layout(annotations=annotations)

fig4.update_layout(margin={"r":50,"t":0,"l":12,"b":30})

#========================================================================

x1 = np.random.randn(200)
x2 = np.random.randn(200) + 2

group_labels = ['Group 1', 'Group 2']

colors = ['#7FA6EE', '#B8F7D4']

# Create distplot with curve_type set to 'normal'
fig2 = ff.create_distplot([x1, x2], group_labels, bin_size=.5,
                         curve_type='normal', # override default 'kde'
                         colors=colors)

# Add title
fig2.update_layout(title_text='Onset of Symptoms vs Confirmed Cases')
# fig.show()





fig3 = go.Figure()
fig3.add_trace(go.Bar(
    name='Control',
    x=['Trial 1', 'Trial 2', 'Trial 3'], y=[3, 6, 4],
    error_y=dict(type='data', array=[1, 0.5, 1.5])
))
fig3.add_trace(go.Bar(
    name='Experimental',
    x=['Trial 1', 'Trial 2', 'Trial 3'], y=[4, 7, 3],
    error_y=dict(type='data', array=[0.5, 1, 2])
))
fig3.update_layout(barmode='group')
# fig.show()

#------------------------------------------------------
# fig5 = go.Figure()

# # Constants
# img_width = 900
# img_height = 700
# scale_factor = 0.5

# # Add invisible scatter trace.
# # This trace is added to help the autoresize logic work.
# fig5.add_trace(
#     go.Scatter(
#         x=[0, img_width * scale_factor],
#         y=[0, img_height * scale_factor],
#         mode="markers",
#         marker_opacity=0
#     )
# )

# # Configure axes
# fig5.update_xaxes(
#     visible=False,
#     range=[0, img_width * scale_factor]
# )

# fig5.update_yaxes(
#     visible=False,
#     range=[0, img_height * scale_factor],
#     # the scaleanchor attribute ensures that the aspect ratio stays constant
#     scaleanchor="x"
# )

# # Add image
# fig5.add_layout_image(
#     dict(
#         x=0,
#         sizex=img_width * scale_factor,
#         y=img_height * scale_factor,
#         sizey=img_height * scale_factor,
#         xref="x",
#         yref="y",
#         opacity=1.0,
#         layer="below",
#         sizing="stretch",
#         source="https://i.ibb.co/x5tbNfh/Covid-19-Cases-NYS-2020-03-01-15.gif")
# )

# # Configure other layout
# fig5.update_layout(
#     width=img_width * scale_factor,
#     height=img_height * scale_factor,
#     margin={"l": 0, "r": 0, "t": 0, "b": 0},
#     autosize=True,
# )

# # Disable the autosize on double click because it adds unwanted margins around the image
# # More detail: https://plot.ly/python/configuration-options/
# fig5.show(config={'doubleClick': 'reset'})


column1a = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('% Hospitalized', style={'fontSize':16, 'color':'rgba(206, 248, 218, 1)', 'marginTop':22, 'marginBottom':0}),#fig4
            html.H1('19', style={'fontSize':92, 'color':'rgba(206, 248, 218, 1)', 'marginBottom':0}),#fig4
            ]
        ),
        dcc.Graph(figure=fig),
    ],
    md=2,
)

column1 = dbc.Col(
    [
        dcc.Graph(figure=fig1),
    ],
    md=7,
)


column2 = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('Positive Cases NYC', style={'fontSize':16, 'color':'rgba(206, 248, 218, 1)', 'marginTop':22, 'marginBottom':0}),#fig4
            html.H1('644', style={'fontSize':90, 'color':'rgba(206, 248, 218, 1)', 'marginBottom':0}),#fig4
            html.H6('Deaths NYC', style={'fontSize':16, 'color':'rgba(206, 248, 218, 1)', 'marginBottom':0}),#fig4
            html.H1('7', style={'fontSize':60, 'color':'rgba(206, 248, 218, 1)', 'marginBottom':0}),#fig4
            ]
        ),
        #dcc.Graph(figure=fig5),#fig4
    ],
    md=3,
)

# column2a = dbc.Col(
#     [
#         html.H1('644'
#         ),#fig4
#     ],
#     md=3,
# )

column3 = dbc.Col(
    [
        dcc.Graph(figure=fig2),
    ]
)

column4 = dbc.Col(
    [
        dcc.Graph(figure=fig3),
    ]
)

# layout = dbc.Row([column1, column2])
layout = [dbc.Row([column1a, column1, column2]), 
        dbc.Row([column3]),
        dbc.Row([column4]),]

