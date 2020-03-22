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

df_china = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/China_Covid19-3-20.csv")
df_italy = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/Italy_Covid19-3-20.csv")
df_usa = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/Usa_Covid19-3-20.csv")
df_usa_total_h = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/UsaTotal_Covid19-3-20.csv")


#-----------------------fig

top_labels = ['CONFIRMED', 'RECOVERED','DEATHS']
top_labels_l = ['confirmed', 'recovered', 'deaths']

colors = ['#d9f0f2', '#38cedc',
          '#f2d4e0']

x_data = df_usa_total_h[['Confirmed_normalized','Recovered_normalized','Deaths_normalized']].values
y_data = df_usa_total_h['date'].values
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
        domain=[0.02, 1]
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
    # margin=dict(l=95, r=0, t=50, b=0),
    margin=dict(l=7, r=0, t=50, b=0),
    #margin=dict(l=40, r=0, t=50, b=0),
    showlegend=False,
)

annotations = []
for yd, xd in zip(y_data, x_data):
    # labeling the y-axis
    annotations.append(dict(xref='paper', yref='y',
                            x=0.14, y=yd,
                            xanchor='right',
                            text="", #str(yd)[5:],
                            font=dict(family='Arial', size=15,
                                      color='rgba(0, 0, 0, 0.25)'),
                            showarrow=False, align='right'))
    # labeling the first percentage of each bar (x_axis)
    annotations.append(dict(xref='x', yref='y',
                            x= xd[0] / 2, y=yd,
                            text= str(yd)[5:],#str(xd[0])[:2] + "% " + top_labels_l[0], #'{:.s}'.format(xd[0]) + '%',
                            hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='#008582'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=(xd[0] / 2) - 30, y=1.05,
                                text=top_labels[0],
                                hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                                font=dict(family='Arial', size=14,
                                          color='rgb(186, 186, 186)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/10)-53.5, y=yd,
                                    text= " ", 
                                    hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                                    font=dict(family='Arial', size=24,
                                              color='rgba(20, 137, 16, 0.77)'),
                                    #hovertext = str(xd[i])[:2] + "% " + top_labels_l[i], #str(xd[i]) + '%',
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=(space + (xd[i]/10))-45, y=1.05,
                                        text=top_labels[i],
                                        hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                                        font=dict(family='Arial', size=14,
                                                  color='rgb(186, 186, 186)'),
                                        showarrow=False))
            space += xd[i]+30

fig.update_layout(annotations=annotations,paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
# fig.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})

#---------------------------------------------

mapbox_access_token = "pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txcjE4NDAwNngzZms0ZndzNGM3dG0ifQ.gXrN0wMYVhqUp7t1LOHEwA"
#open(".mapbox_token").read()

df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-20-2020.csv')

fig1 = go.Figure()

fig1 = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_data=["Country/Region",'Confirmed', 'Deaths'],
                        size='Confirmed', zoom=1, color = 'Confirmed', color_continuous_scale=px.colors.sequential.Purp, size_max=40,height=600)

fig1.update_layout(
    mapbox_style="white-bg",
    hovermode='closest',
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                "https://api.mapbox.com/styles/v1/lilysu/ck81nlmtm0fwq1iqkv33jiu2r/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
                # purple "https://api.mapbox.com/styles/v1/lilysu/ck811j4xp18kf1iphb7bv365a/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
                # green "https://api.mapbox.com/styles/v1/lilysu/ck7v7bqqy08ae1irye0k0jcot/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
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
#---------------------------------------------------------------------------FIG 1Half
import requests
df = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/NYS_County_Covid19-3-20.csv")

r = requests.get('https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/new-york-counties.geojson')
geojson = r.json()

fig1Half = px.choropleth_mapbox(df, geojson=geojson, 
                           animation_frame="date", animation_group="total",
                           locations="county_full", 
                           featureidkey="properties.name",
                           center={"lat": 42.85, "lon":-75.9},
                           mapbox_style="carto-positron", zoom=6,
                           opacity = .9,
                           height = 750,
                           color = 'total',
                           color_continuous_scale=px.colors.sequential.Teal,
                           custom_data = ['15_Mar_Cov_Pos'],
                           #hover_data = ["date"],
                           labels = {"total":"Positive Cases", "county_full": "location"},
                           )


fig1Half.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig1Half.update_layout(coloraxis_showscale = False, showlegend = False)


#---------------------------------------------------------------------------SYMPTOM FIGURE

# x1 = np.random.randn(200)
# x2 = np.random.randn(200) + 2

# group_labels = ['Disease Transmitted', 'Signs of Symptoms']

# colors = ['#7FA6EE', '#B8F7D4']

# # Create distplot with curve_type set to 'normal'
# figA = ff.create_distplot([x1, x2], group_labels, bin_size=.5,
#                          curve_type='normal', # override default 'kde'
#                          colors=colors)

# # Add title
# figA.update_layout(title_text='IT TAKES ON AVERAGE OF 14 DAYS FOR THE SYMPTOMS TO APPEAR')

#------------------------------------------FIG 2

fig2 = go.Figure()

fig2.add_trace(go.Scatter(x=df_italy["date"], y=df_italy["new_Confirmed"], #fill='tozeroy',fillcolor='#B0DAAE',
                    mode= 'lines', name = 'Italy',legendgroup="group3",
                    stackgroup='two',
                    line=dict(width=0.5, color='rgba(183, 224, 240, 0.94)'),
                    text="Italy<br>New Confirmed Cases <br>from the day before",hoveron = 'points+fills', 
                    hoverinfo = 'text+y'))

fig2.add_trace(go.Scatter(x=df_usa["date"], y=df_usa["new_Confirmed"],##fill='toself',fillcolor='rgba(133, 70, 216, 0.3)',
                    mode='lines',legendgroup="group2",
                    stackgroup='one',
                    line=dict(width=0.5, color='rgba(238, 175, 206, 0.82)'),
                    text="U.S.<br>New Confirmed Cases <br>from the day before",hoveron = 'points+fills', name = 'U.S.',
                    hoverinfo = 'text+y' # override default markers+lines
                    ))

fig2.add_trace(go.Scatter(x=df_china["date"], y=df_china["new_Confirmed"], #fill='tozeroy',fillcolor='#F4DBE5',
                    mode='lines', legendgroup="group1",
                    stackgroup='three',
                    line=dict(width=0.5, color='rgba(159, 133, 229, 0.51)'),
                    text="China<br>New Confirmed Cases <br>from the day before",hoveron = 'points+fills', name = 'China',
                    hoverinfo = 'text+y' # override default markers+lines
                    ))

fig2.update_layout(
    title = "Day-to-day Changes in Cases in U.S. vs China vs Italy",paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
)

#--------------------------------------------------------

df_usa_t = df_usa.tail()
# df_italy_t = df_italy.tail()

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=df_usa_t["date"], y=df_usa_t["new_Confirmed"], fill='tozeroy',fillcolor='#F4DBE5',
                    mode='none', legendgroup="group1", showlegend=False,
                    text="U.S.<br>New Confirmed Cases <br>from the day before",hoveron = 'fills', name = 'U.S.',
                    hoverinfo = 'text+y' # override default markers+lines
                    ))

# fig3.add_trace(go.Scatter(x=df_usa_t["date"], y=df_usa_t["new_Confirmed"],fill='tonexty',fillcolor='rgba(133, 70, 216, 0)',
#                     mode='markers',marker=dict(color="rgba(133, 70, 216, 0.19)", size=12),legendgroup="group2",
#                     text="U.S.<br>New Confirmed Cases <br>from the day before",hoveron = 'points', name = 'U.S.',
#                     hoverinfo = 'text+y' # override default markers+lines
#                     ))

# fig3.add_trace(go.Scatter(x=df_italy_t["date"], y=df_italy_t["new_Confirmed"], fill='tonexty',fillcolor='#B0DAAE',
#                     mode= 'none', name = 'Italy',legendgroup="group3",
#                     text="Italy<br>New Confirmed Cases <br>from the day before",hoveron = 'fills', 
#                     hoverinfo = 'text+y'))

fig3.update_layout(
    title = "Day-to-day Increase<br>of Cases U.S.",paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
)
# fig3.update_layout(legend=dict(x=.07, y=0.92))
fig3.layout.margin.update({'t':30, 'b':0, 'r': 0, 'l': 10})

#--------------------------------------------------fig3a
fig3a = go.Figure()
fig3a.add_trace(go.Scatter(x=df_usa["date"], y=df_usa["new_Confirmed"], fill='tozeroy',fillcolor='#F4DBE5',
                    mode='none', legendgroup="group1",
                    text="U.S.<br>New Confirmed Cases <br>from the day before",hoveron = 'fills', name = 'U.S.',
                    hoverinfo = 'text+y' # override default markers+lines
                    ))

fig3a.add_trace(go.Scatter(x=df_usa["date"], y=df_usa["new_Confirmed"],fill='tonexty',fillcolor='rgba(133, 70, 216, 0)',
                    mode='markers',marker=dict(color="rgba(133, 70, 216, 0.19)", size=12),legendgroup="group2",
                    text="U.S.<br>New Confirmed Cases <br>from the day before",hoveron = 'points', name = 'U.S.',
                    hoverinfo = 'text+y' # override default markers+lines
                    ))

fig3a.add_trace(go.Scatter(x=df_italy["date"], y=df_italy["new_Confirmed"], fill='tonexty',fillcolor='#B0DAAE',
                    mode= 'none', name = 'Italy',legendgroup="group3",
                    text="Italy<br>New Confirmed Cases <br>from the day before",hoveron = 'fills', 
                    hoverinfo = 'text+y'))

fig3a.update_layout(
    title = "Day-to-day Increased Cases U.S. vs. Italy",paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
)
fig3a.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})

#--------------------------------------------------fig4


fig4 = go.Figure()

# Add surface trace
fig4.add_trace(go.Scatter(x=df_italy['date'], y=df_italy['Confirmed'],
                    name = "Italy",
                    hovertext=df_italy["Confirmed"],
                    hoverinfo='text',
                    hovertemplate =
                    '<i>Date: </i>: %{x}'+
                    '<br><b>Confirmed: </b>: %{y:,}<br>',
                    line_shape='spline',
                    line_color='#68CEF3',
                    ))

fig4.add_trace(go.Scatter(x=df_china['date'], y=df_china['Confirmed'],
                    name = "China",
                    hovertext=df_china["Confirmed"],
                    hoverinfo='text',
                    hovertemplate =
                    '<i>Date: </i>: %{x}'+
                    '<br><b>Confirmed: </b>: %{y:,}<br>',
                    line_shape='spline',
                    line_color='#9e92f6',
                    ))
fig4.add_trace(go.Scatter(x=df_usa['date'], y=df_usa['Confirmed'],
                    name = "US",
                    hovertext=df_usa["Confirmed"],
                    hoverinfo='text',
                    hovertemplate =
                    '<i>Date: </i>: %{x}'+
                    '<br><b>Confirmed: </b>: %{y:,}<br>',
                    line_shape='spline',
                    line_color = '#e7b1c7',
                    ))

fig4.update_traces(hoverinfo='text+name', mode='lines+markers')

# Update plot sizing
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
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    showlegend=False,
    plot_bgcolor='white'
)

# Update 3D scene options
fig4.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

# Default annotations
annotations = []
# for y_trace, label, color in zip(y_data, labels, colors):
    # labeling the left_side of the plot
annotations.append(dict(xref='paper', x=.990, y=39500,
                              xanchor='right', yanchor='bottom',
                              text='Italy',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False))

annotations.append(dict(xref='paper',  x=.99, y=11000,
                              xanchor='right', yanchor='bottom',
                              text='U.S.',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False))
annotations.append(dict(xref='paper', x=1.01, y=78600,
                              xanchor='right', yanchor='bottom',
                              text='China',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False))
# Title
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Covid-19 Confirmed Cases China vs. Italy vs. United States',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
# Source
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))

# Add Annotations with Buttons

all_annotations = [dict(xref='paper', x=1.01, y=78600,
                              xanchor='right', yanchor='bottom',
                              text='China',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                   dict(xref='paper', x=.990, y=39500,
                              xanchor='right', yanchor='bottom',
                              text='Italy',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', x=.99, y=11000,
                              xanchor='right', yanchor='bottom',
                              text='U.S.',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Covid-19 Confirmed Cases China vs. Italy vs. United States',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False)]


italy_annotations = [dict(xref='paper', x=.990, y=45000,
                              xanchor='right', yanchor='bottom',
                              text='Italy',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', x=.99, y=17000,
                              xanchor='right', yanchor='bottom',
                              text='U.S.',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Covid-19 Confirmed Cases China vs. Italy vs. United States',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False)]

china_annotations = [dict(xref='paper', x=1.01, y=78600,
                              xanchor='right', yanchor='bottom',
                              text='China',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', x=.99, y=45000,
                              xanchor='right', yanchor='bottom',
                              text='U.S.',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Covid-19 Confirmed Cases China vs. Italy vs. United States',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False)]

fig4.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            active=0,
            pad={"r": 10, "t": 40},
            showactive=True,
            x=0.06,
            xanchor="left",
            y=1.1,
            buttons=list([
                dict(label="Show All",
                     method="update",
                     args=[{"visible": [True, True, True]},
                           {
                            "annotations": all_annotations}]),
                dict(label="Compare with Italy",
                     method="update",
                     args=[{"visible": [True, False, True]},
                           {
                            "annotations": italy_annotations}]),
                dict(label="Compare with China",
                     method="update",
                     args=[{"visible": [True, True, False]},
                           {
                            "annotations": china_annotations}]),
            ]),
        )
    ])


fig4.update_layout(annotations=annotations)

#========================================================================


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


columnTopLeft = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('% Sick Enough to Be Hospitalized younger than 55', style={'fontSize':17, 'color':'#009996', 'marginTop':22, 'marginBottom':10}),#fig4
            html.H1('38', style={'fontSize':60, 'color':'#009996', 'marginBottom':0}),#fig4
            ]
        ),
        dcc.Graph(figure=fig3),
    ],
    md=2,
    #style={'paddingLeft':0,'paddingRight':0},
)

columnTopCenter = dbc.Col(
    [

        dcc.Graph(figure=fig1,style={'paddingTop':0, 'paddingBottom':0}),

    ],
    md=6,
    )


columnTopRight = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('Positive Cases NYC', style={'fontSize':18, 'color':'#009996', 'marginTop':22, 'marginBottom':10}),#fig4
            html.H1('4,408', style={'fontSize':85, 'color':'#009996', 'marginBottom':0}),#fig4
            html.H6('last updated march 21st 10:35PM', style={'fontSize':12, 'color':'#009996', 'marginBottom':0}),#fig4
            # html.H6('', style={'fontSize':10, 'marginTop':22, 'marginBottom':0}),
            html.H6('Positive Cases by County', style={'fontSize':18, 'color':'#9a76c6', 'marginTop':20}),
            # html.H1('43', style={'fontSize':68, 'color':'#009996', 'marginBottom':0}),#fig4
            # html.H6('', style={'fontSize':20, 'marginTop':22, 'marginBottom':0}),
            ]
        ),

        html.Center(
            children=[
            html.Img(src=app.get_asset_url('Covid-19_Cases_NYS_2020-03-20.gif'), style={'display': 'block', 'width':'100%'})
            ]
        )
    ],
    md=4,
)
# column0CenterAll = dbc.Col(
#     [
#         dcc.Graph(figure=figA),
#     ]
# )

column1Left = dbc.Col(
    [
        html.Center(
            children=[
                dcc.Graph(figure=fig1Half),
            ]
        )
    ],
    md=6
)

column1Right = dbc.Col(
    [
        html.Center(
            children=[
                html.H6('Proportion of Recovered and Deaths in New York State', style={'fontSize':18, 'color':'#009996', 'marginTop':0, 'marginBottom':0}),#fig4
                dcc.Graph(figure=fig),
            ]
        )
    ],
    md=6
)

column2CenterAll = dbc.Col(
    [
        dcc.Graph(figure=fig2),
    ]
)

column3CenterAll = dbc.Col(
    [
        dcc.Graph(figure=fig3a),
    ]
)

column4CenterAll = dbc.Col(
    [
        dcc.Graph(figure=fig4),
    ]
)

# layout = dbc.Row([column1, column2])
layout = [dbc.Row([columnTopLeft, columnTopCenter, columnTopRight]), 
        dbc.Row([column1Left, column1Right]),
        # dbc.Row([column1CenterAll]),
        dbc.Row([column2CenterAll]),
        dbc.Row([column3CenterAll]),
        dbc.Row([column4CenterAll]),]

