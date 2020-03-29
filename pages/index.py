# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px

# Imports from this application
from app import app
import plotly.figure_factory as ff
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df_china = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/China_Covid19-3-27.csv")
df_italy = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/Italy_Covid19-3-27.csv")
df_usa = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/Usa_Covid19-3-27.csv")
# df_usa_total_h = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/UsaTotal_Covid19-3-24.csv")
# df_italy_total_h = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/ItalyTotal_Covid19-3-24.csv")
# df_china_total_h = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/ChinaTotal_Covid19-3-24.csv")
diff_from_day_before= pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_ny/diff_from_day_before_county2.csv")

df_nyc = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_nyc/nyc_borough.csv")


#-----------------------fig

top = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_nyc/daily_num_cases_nyc.csv")
top5 = top.tail()

fig_bar_nyc_last_5_days = px.bar(top5, x='date_found_positive', y='New York',
             hover_data=['New York', 'date_found_positive'], color='New York',
             color_continuous_scale=[(0.00, "#553000"), (0.25, "#BF1F58"), (0.5, "#F2B2C0"),(0.75, "#94D6CC"),  (1.00, "#003D30")],
             labels={'date_found_positive':'Date'},
             text = 'New York', height = 220)

fig_bar_nyc_last_5_days.update_traces(texttemplate='%{text}', textposition='inside')

fig_bar_nyc_last_5_days.update_layout(
    showlegend=False,
    # title_text='DAILY NUMBER OF CASES<br>IN NEW YORK CITY',
    font=dict(
    size=12,
    color="#a3a3a3"
    ),
    xaxis_title="",
    yaxis_title="",
    plot_bgcolor='white',
    margin=dict(l=0, r=0, t=0, b=0),
    # annotations = annotationsDailyNYC,
)
fig_bar_nyc_last_5_days.update_layout(coloraxis_showscale=False)
fig_bar_nyc_last_5_days.update_xaxes(showticklabels=True)
fig_bar_nyc_last_5_days.update_yaxes(showticklabels=False)

fig_bar_nyc_last_5_days.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})

#---------------------------------------------

table_h = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_ny/percentage_change_County.csv")
table_h = table_h.tail(7)

fig_area_nyc_percentage_change = go.Figure()

fig_area_nyc_percentage_change = px.area(table_h, x='dates', y='New York',
             hover_data=['New York', 'dates'],
             text = 'New York',
             color_discrete_sequence=px.colors.qualitative.Pastel,
             line_shape='spline',
             height=210)


fig_area_nyc_percentage_change.update_layout(
    plot_bgcolor='white',
    showlegend=False,
    font_color="#a3a3a3",
)

fig_area_nyc_percentage_change.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})
#---------------------------------------------



age = ["0 to 17", "18 to 44", "45 to 64", "65 to 74 ", "75 and over", "Unknown"]
color1 = ["#d7e76f","#046162","#F686A9","#ffcece","#0497AE", "#047484"]

gender =["Female","Male"]
color2 = ["#52D3C3","#047484"]

# Create subplots: use 'domain' type for Pie subplot
fig_pie_nyc_age = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig_pie_nyc_age.add_trace(go.Pie(labels=age, values=[573, 12590, 10019, 3354, 2568, 54], name="Age Group",marker=dict(colors=color1)),
              1, 1)
fig_pie_nyc_age.add_trace(go.Pie(labels=gender, values=[12928,16192], name="Gender",marker=dict(colors=color2)),
              1, 2)


# Use `hole` to create a donut-like pie chart
fig_pie_nyc_age.update_traces(hole=.4, hoverinfo="label+percent+name+value",
                  hovertemplate = '<b>%{label}</b>'
                        '<br><b>Percentage</b>: %{percent}<br>'
                        '<b><b>Number of People</b>: %{value}<br>',
                  textposition='inside', textinfo='percent+label')

fig_pie_nyc_age.update_layout(
    title={
        'text':"DEMOGRAPHICS OF PEOPLE <br>WITH COVID-19 (29,158) IN<br>NYC AS OF MARCH 28, 2020 10 AM",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font_size=14,
    font_color="#05b9f0",
    showlegend=False,
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='Age Groups', x=0.18, y=0.5, font_size=13, showarrow=False),
        dict(text='Gender', x=0.81, y=0.5, font_size=18, showarrow=False)])


#---------------------------------------------


#DEATHS
age = ["0 to 17", "18 to 44", "45 to 64", "65 to 74 ", "75 and over"]
color1 = ["#0497AE","#046162","#F686A9","#ffcece","#0497AE"]

gender =["Female","Male"]
color2 = ["#d7e76f","#26505E"]

underlying_illness =["Had Underlying Illness","Did Not"]
color3 = ["#52D3C3","#046162"]

# Create subplots: use 'domain' type for Pie subplot
fig_pie_nyc_death_age = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]])
fig_pie_nyc_death_age.add_trace(go.Pie(labels=age, values=[0, 20, 104, 110, 216], name="Age Group",marker=dict(colors=color1)),
              1, 1)
fig_pie_nyc_death_age.add_trace(go.Pie(labels=gender, values=[181,269], name="Gender",marker=dict(colors=color2)),
              1, 2)
fig_pie_nyc_death_age.add_trace(go.Pie(labels=underlying_illness, values=[373,14,63], name="Underlying Illness",marker=dict(colors=color3)),
              1, 3)

# Use `hole` to create a donut-like pie chart
fig_pie_nyc_death_age.update_traces(hole=.4, hoverinfo="label+percent+name+value",
                  hovertemplate = '<b>%{label}</b>'
                        '<br><b>Percentage</b>: %{percent}<br>'
                        '<b><b>Number of People</b>: %{value}<br>',
                  textposition='inside', textinfo='percent+label')

fig_pie_nyc_death_age.update_layout(
    title={
        'text':"DEMOGRAPHICS OF PEOPLE WHO DIED (517) OF COVID-19 IN <br>NYC AS OF MARCH 28, 2020 2PM",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font_size=14,
    font_color="#05b9f0",
    showlegend=False,
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='Age Groups', x=0.10, y=0.5, font_size=13, showarrow=False),
                dict(text='Gender', x=0.5, y=0.5, font_size=18, showarrow=False),
                dict(text='Underlying Illness', x=0.91, y=0.5, font_size=11, showarrow=False)])

#---------------------------------------------
# from urllib.request import urlopen
# import json
# with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
#   counties = json.load(response)
mapbox_access_token = "pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
df = pd.read_csv('https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/Covid19-3-27.csv')
fig_map_top_center = go.Figure()

# fig_map_top_center = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.FIPS, z=df.Confirmed,
#                                     colorscale="YlOrRd", zmin=0, zmax=5,
#                                     marker_opacity=0.08, marker_line_width=0,showscale=False))

# fig_map_top_center.update_traces(showscale=False)  
fig_map_top_center.add_trace(go.Scattermapbox(
        lat=df["Lat"],
        lon=df["Long_"],
        mode='markers',
        text = df[["CITY","COUNTYNAME","Combined_Key", "Confirmed","Deaths"]],
        marker=go.scattermapbox.Marker(
            size=(df['log_conf'])**1.6,
            color=(df['log_conf']+7)**0.001,
            opacity=0.01
        ),
        hovertemplate ='<b>Location</b>:'+
        '%{text[1]},%{text[2]}<br>'+
      '<b>Confirmed</b>: %{text[3]}<br>'+
      '<b>Deaths</b>: %{text[4]}<br>'+
      '<b>on March 27, 2020</b>',
    ))

# fig_map_top_center.add_trace(go.Scattermapbox(
#         lat=df["Lat"],
#         lon=df["Long_"],
#         mode='markers + text',
#         text= df[["CITY","COUNTYNAME","Combined_Key", "Confirmed","Deaths"]],
#         marker=go.scattermapbox.Marker(
#             size=((df['log_conf'])**1.6)-(df['log_conf']**1.7)*(0.08),
#             color='rgba(166, 247, 235, 0.38)',
#             opacity=0.04
#         ),

#         textfont_size=12, 
#         texttemplate ='<b>Location</b>:'+
#         '%{text[1]},%{text[2]}<br>'+
#       '<b>Confirmed</b>: %{text[3]}<br>'+
#       '<b>Deaths</b>: %{text[4]}<br>'+
#       '<b>on March 27, 2020</b>',
#     ))
# fig_map_top_center.update_traces(textfont_size=12, texttemplate='%{text[1]}, %{text[2]}<br>'+
#       'Confirmed: %{text[3]}<br>'+
#       'Deaths: %{text[4]}')

fig_map_top_center.update_layout(
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                       "https://api.mapbox.com/styles/v1/lilysu/ck7v7bqqy08ae1irye0k0jcot/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
            ] 
        },

      ],
    autosize=True,
    height=600,
    hovermode='closest',
    showlegend=False,
    mapbox=dict(
        style='white-bg',
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=40.7465651,
            lon=-73.9905038
        ),
        pitch=0,
        zoom=7.7,
    ),
)




# fig_map_top_center = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.FIPS, z=df.Confirmed,
#                                     colorscale="YlOrRd", zmin=0, zmax=3,
#                                     marker_opacity=0.08, marker_line_width=0))
# fig_map_top_center.update_traces(showscale=False)

# fig_map_top_center.add_trace(go.Scattermapbox(
#         lat=df["Lat"],
#         lon=df["Long_"],
#         mode='markers',
#         marker=go.scattermapbox.Marker(
#             size=(df['log_conf'])**1.6,
#             color=(df['log_conf']+7)**0.001,
#             opacity=0.08
#         ),
#         hoverinfo='none',
#     ))

# fig_map_top_center.add_trace(go.Scattermapbox(
#         lat=df["Lat"],
#         lon=df["Long_"],
#         mode='markers',
#         text= df[["CITY","COUNTYNAME","Combined_Key", "Confirmed","Deaths"]],
#         marker=go.scattermapbox.Marker(
#             size=((df['log_conf'])**1.6)-(df['log_conf']**1.7)*(0.08),
#             color='rgba(166, 247, 235, 0.38)',
#             opacity=0.05
#         ),
#         hovertemplate ='<b>Location</b>: %{text[:2]}<br>'+
#       '<b>Confirmed</b>: %{text[3]}<br>'+
#       '<b>Deaths</b>: %{text[4]}',

#     ))


# fig_map_top_center.update_layout(
#     mapbox_layers=[
#         {
#             "below": 'traces',
#             "sourcetype": "raster",
#             "source": [
#                        "https://api.mapbox.com/styles/v1/lilysu/ck81nlmtm0fwq1iqkv33jiu2r/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
#             ] 
#         },

#       ],
#     autosize=True,
#     height=600,
#     hovermode='closest',
#     showlegend=False,
#     mapbox=dict(
#         style='white-bg',
#         accesstoken=mapbox_access_token,
#         bearing=0,
#         center=dict(
#             lat=38,
#             lon=-98
#         ),
#         pitch=0,
#         zoom=2.9,
#     ),
# )


# fig_map_top_center = go.Figure()
# fig_map_top_center.add_trace(go.Scattermapbox(
#         lat=us_cities["Lat"],
#         lon=us_cities["Long_"],
#         mode='markers',
#         marker=go.scattermapbox.Marker(
#             size=(us_cities['log_conf'])**1.6,
#             color=(us_cities['log_conf'])**0.001,
#             opacity=0.6
#         ),
#         hoverinfo='none',
#     ))

# fig_map_top_center.add_trace(go.Scattermapbox(
#         lat=us_cities["Lat"],
#         lon=us_cities["Long_"],
#         text = us_cities[["Deaths_str"]],
#         mode='text',
#         marker=go.scattermapbox.Marker(
#             size=((us_cities['log_conf'])**1.6)-(us_cities['log_conf']**1.7)*(0.04),
#             color='rgba(224, 21, 163, 0.31)',
#             opacity=0.5
#         ),
#         hoverinfo='none'
#     ))

# fig_map_top_center.add_trace(go.Scattermapbox(
#         lat=us_cities["Lat"],
#         lon=us_cities["Long_"],
#         mode='markers',
#         text= us_cities[["Combined_Key", "Confirmed","Deaths"]],
#         marker=go.scattermapbox.Marker(
#             size=((us_cities['log_conf'])**1.6)-(us_cities['log_conf']**1.7)*(0.08),
#             color='rgba(166, 247, 235, 0.38)',
#             opacity=1
#         ),
#         hovertemplate =
#       '<b>Location</b>: %{text[0]}<br>'+
#       '<b>Confirmed</b>: %{text[1]}<br>'+
#       '<b>Deaths</b>: %{text[2]}',
#     ))

# fig_map_top_center.update_layout(
#     mapbox_layers=[
#         {
#             "below": 'traces',
#             "sourcetype": "raster",
#             "source": [
#                        "https://api.mapbox.com/styles/v1/lilysu/ck81nlmtm0fwq1iqkv33jiu2r/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
#                 #"https://api.mapbox.com/styles/v1/lilysu/ck7v7bqqy08ae1irye0k0jcot/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
#             ] 
#         },

#       ],
#     autosize=True,
#     height=600,
#     hovermode='closest',
#     showlegend=False,
#     mapbox=dict(
#         style='white-bg',
#         accesstoken=mapbox_access_token,
#         bearing=0,
#         center=dict(
#             lat=38,
#             lon=-98
#         ),
#         pitch=0,
#         zoom=2.9,

#     ),
# )

# fig_map_top_center.update_traces(textfont_size=14, texttemplate='%{text} Deaths')
fig_map_top_center.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})
#---------------------------------------------------------------------------LINE CHART BY BOROUGH

borough = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
borough_colors = ['#553000','#94D6CC','#F3B3C2', '#006b54','#BF1F57']
fig_line_nyc_borough_day_change = go.Figure()
for i,j in zip(borough, borough_colors):
  fig_line_nyc_borough_day_change.add_trace(go.Scatter(x=df_nyc['date'], y=df_nyc[i], name = i, text=df_nyc[i],mode='lines+markers',hoverinfo='text+name', line=dict(color=j, width=4)))

fig_line_nyc_borough_day_change.update_layout(
    plot_bgcolor='white',
    showlegend=True,
    autosize=True,
    title_text='DAILY NUMBER OF CASES OF COVID-19 BY BOROUGH'
)
annotations = [ dict(xref='paper', yref='paper', x=0.5, y=-0.122,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the New York City Department of Health',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False)]
fig_line_nyc_borough_day_change.update_layout(annotations=annotations)

fig_line_nyc_borough_day_change.update_layout(
    plot_bgcolor='white'
)

#---------------------------------------------------------------------------BOROUGH STACKED CASES DAY TO DAY


fig_stacked_change_borough_cases = go.Figure()

borough = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
borough_colors = ['#553000','#94D6CC','#F3B3C2', '#006b54','#BF1F57']


for i,j in zip(borough, borough_colors):
  fig_stacked_change_borough_cases.add_trace(go.Scatter(x = df_nyc['date'], y = df_nyc[i],line_shape='spline', mode='lines', stackgroup='one', # define stack group
                           name = i, text=df_nyc[i], hoveron = 'points+fills', fillcolor=j,line=dict(width=0.5, color=j),
                           hovertemplate = "<b>" + i +"<br><b>%{text}</b>"+" Total Cases <br>on " + df_nyc['date']))
    
fig_stacked_change_borough_cases.update_traces(hoverinfo='text+name', mode='lines+markers')
fig_stacked_change_borough_cases.update_layout(
    plot_bgcolor='white',
    showlegend=True,
    title_text='NUMBER OF POSITIVE CASES OF COVID-19 BY BOROUGH STACKED TOGETHER'
)
annotations = [ dict(xref='paper', yref='paper', x=0.5, y=-0.13,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the New York City Department of Health',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False)]
fig_stacked_change_borough_cases.update_layout(annotations=annotations)

fig_stacked_change_borough_cases.update_layout(
    showlegend=False,
    annotations=[
        dict(
            x=0,
            y=-400,
            xref="x",
            yref="y",
            text="10764<br> total",
            showarrow=False,
            ax=0,
            ay=-40,
            font=dict(size=13, color='#000'),
        )
    ]
)

annotation_borough = []
for i,j in zip(range(0, 7), df_nyc['total']):
  annotation_borough.append(
        dict(
            x=i,
            y=-2000,
            xref="x",
            yref="y",
            text=str(j) +"<br> total",
            showarrow=False,
            ax=0,
            ay=-40))
annotation_borough.append(
  dict(xref='paper', yref='paper', x=0.5, y=-0.122,
  xanchor='center', yanchor='top',
  text='Data Provided by the New York City Department of Health',
  font=dict(family='Arial',
            size=12,
            color='rgb(150,150,150)'),
  showarrow=False))


fig_stacked_change_borough_cases.update_layout(
    plot_bgcolor='white',
    showlegend=True,
    annotations = annotation_borough
)



#---------------------------------------------------------------------------TIMESLIDER
import requests
df = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_ny/new_york_counties_timeslider.csv")

r = requests.get('https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/nys_geojson/new-york-counties.geojson')
geojson = r.json()

fig_map_nyc_timeslider = px.choropleth_mapbox(df, geojson=geojson, 
                           animation_frame="date", animation_group="total",
                           locations="county_full", 
                           featureidkey="properties.name",
                           center={"lat": 42.85, "lon":-75.9},
                           mapbox_style="carto-positron", zoom=5.7,
                           opacity = .7,
                           height = 720,
                           color = 'total',
                           color_continuous_scale=px.colors.sequential.Teal,
                           custom_data = ['March 27'],
                           #hover_data = ["date"],
                           labels = {"total":"Positive Cases", "county_full": "location"},
                           )


fig_map_nyc_timeslider.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
fig_map_nyc_timeslider.update_layout(coloraxis_showscale = False, showlegend = False)

#------------------------------------------------------------------------------------------COUNTY CASES
df_counties_overtime = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_ny/county_tableMarch28.csv")
df_counties_overtime = df_counties_overtime.head(15)


fig_line_ny_cumulative = px.bar(df_counties_overtime, x='index', y='March 28', 
             text='March 28', 
             color = 'March 28',
             height = 350,
             color_continuous_scale=px.colors.diverging.BrBG,
             labels={'New York State Counties':'County','March 28':'March 28th Confirmed Cases'})
fig_line_ny_cumulative.update_traces(texttemplate='%{text}', textposition='outside')
fig_line_ny_cumulative.update_layout(
    plot_bgcolor='white',
    showlegend=False,
    autosize=True,
    xaxis_title="",
    font=dict(
    color="#a3a3a3",)
    # title_text='NUMBER OF POSITIVE CASES OF COVID-19 BY COUNTY FOR THE TOP 20 COUNTIES'
)

fig_line_ny_cumulative.update_layout(coloraxis_showscale=False)
fig_line_ny_cumulative.update_layout(margin={"r":0,"t":15,"l":0,"b":0})

#------------------------------------------------------------------------------------------COUNTY day-to-day changes
table = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_nyc/daily_num_cases_nyc.csv") #table

table_h = table.tail(7)
collist = ['Nassau','New York', 'Suffolk', 'Rockland', 'Dutchess', 'Monroe','Dutchess', 'Westchester']
colors = [ '#56b3ae', '#3c8682', '#aa7d7d', '#aa7d7d', '#8b5b5b','#305f4b','#baa991','#4bd2fb']#'#99d1ce',

fig_line_ny_overtime = go.Figure()

for i, j in zip(collist, colors):
    fig_line_ny_overtime.add_trace(go.Scatter(x=table_h['date_found_positive'], y=table_h[i], name = i, text=table_h[i],mode='lines+markers',
    hoverinfo='text+name',line=dict(color=j, width=4)))


fig_line_ny_overtime.update_layout(
    yaxis=dict(
        title_text="Confirmed Cases"
    ),
    autosize=True,
    height=220,
    plot_bgcolor='white',
    showlegend=True,
    #title_text='DAILY NUMBER OF CASES BY COUNTY'
    font=dict(
    # family="Arial",
    color="#a3a3a3")
)
annotations = [ dict(xref='paper', yref='paper', x=0.5, y=-0.122,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the New York State Department of Health',
                              font=dict(family='Arial',
                                        size=12,
                                        color='#05b9f0'),
                              showarrow=False)]
fig_line_ny_overtime.update_layout(annotations=annotations)
fig_line_ny_overtime.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
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
#-------------------------------------------------------------------------------------STACKED COUNTIES



fig_stacked_change_county_cases = go.Figure()

collist = ['Albany', 'Allegany', 'Broome',
       'Chenango', 'Clinton', 'Columbia', 'Delaware', 'Dutchess', 'Erie',
       'Essex', 'Fulton', 'Genesee', 'Greene', 'Hamilton', 'Herkimer',
       'Jefferson', 'Livingston', 'Monroe', 'Montgomery', 'Nassau',
       'New York', 'Niagara', 'Oneida', 'Onondaga', 'Ontario', 'Orange',
       'Putnam','Rensselaer', 'Rockland', 'Saratoga',
       'Schenectady', 'Schoharie', 'Steuben', 'Suffolk', 'Sullivan', 'Tioga',
       'Tompkins', 'Ulster', 'Warren', 'Washington', 'Wayne', 'Westchester',
       'Wyoming']

color43=["#EAE324", "#EA8AA1","#92CBD2", "#58B69A","#102A6B", "#103D58","#4788A8","#C979A6", "#F2DFE7", "#C5B6DF",
         "#443947","#764D62","#EAE324", "#EA8AA1","#92CBD2", "#58B69A","#102A6B", "#103D58","#4788A8","#C979A6", 
         "#F2DFE7", "#C5B6DF","#443947","#764D62","#EAE324", "#EA8AA1","#92CBD2", "#58B69A","#102A6B", "#103D58",
         "#EAE324", "#EA8AA1","#92CBD2", "#58B69A","#102A6B", "#103D58","#4788A8","#C979A6", "#F2DFE7", "#C5B6DF",
         "#443947","#764D62"]


for i,j in zip(collist, color43):
  fig_stacked_change_county_cases.add_trace(go.Scatter(x = diff_from_day_before['dates'], y = diff_from_day_before[i],line_shape='spline', mode='lines', stackgroup='one', # define stack group
                           name = i, text=diff_from_day_before[i], hoveron = 'points+fills', fillcolor=j,line=dict(width=2.5, color=j),
                           hovertemplate = "<b>" + i + " County</b>" +"<br><b>%{text} </b>"+" New Cases <br>on " + diff_from_day_before['dates']))
    
fig_stacked_change_county_cases.update_traces(hoverinfo='text+name', mode='lines+markers')
fig_stacked_change_county_cases.update_layout(
    title_text='DAY-TO-DAY CHANGES IN NEW ADDITIONAL POSITIVE CASES BY COUNTY (drag-zoom to see detail)'
)
annotations = [ dict(xref='paper', yref='paper', x=0.5, y=-0.13,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the New York State Department of Health (Missing March 16th)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False)]
fig_stacked_change_county_cases.update_layout(annotations=annotations)

fig_stacked_change_county_cases.update_layout(
    showlegend=False,
    annotations=[
        dict(
            x=15,
            y=5,
            xref="x",
            yref="y",
            text="missing data",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
        )
    ]
)

annotation4 = []
for i,j in zip(range(27), diff_from_day_before['total']):
  annotation4.append(
        dict(
            x=i,
            y=-500,
            xref="x",
            yref="y",
            text=str(j)[:-2]+"<br> total",
            showarrow=False,
            #arrowhead=7,
            ax=0,
            ay=-40))

fig_stacked_change_county_cases.update_layout(
    plot_bgcolor='white',
    showlegend=True,
    annotations = annotation4
)



#-----------------------------------------------------------SINGLE STACK NEW YORK



fig_stacked_ny = go.Figure()

collist = ['New York']

color43=["#f8d8ed"]


for i,j in zip(collist, color43):
  fig_stacked_ny.add_trace(go.Scatter(x = diff_from_day_before['dates'], y = diff_from_day_before[i],line_shape='spline', mode='lines', stackgroup='one', # define stack group
                           name = i, text=diff_from_day_before[i], hoveron = 'points+fills', fillcolor=j,line=dict(width=2.5, color=j),
                           hovertemplate = "<b>" + i + " County</b>" +"<br><b>%{text} </b>"+" New Cases <br>on " + diff_from_day_before['dates']))
    
fig_stacked_ny.update_traces(hoverinfo='text+name', mode='lines+markers')
fig_stacked_ny.update_layout(
    title_text='DAY-TO-DAY CHANGES IN NEW ADDITIONAL POSITIVE CASES NEW YORK'
)
annotations = [ dict(xref='paper', yref='paper', x=0.5, y=-0.13,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the New York State Department of Health (Missing March 16th)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False)]
fig_stacked_ny.update_layout(annotations=annotations)

fig_stacked_ny.update_layout(
    showlegend=False,
    annotations=[
        dict(
            x=15,
            y=5,
            xref="x",
            yref="y",
            text="missing data",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
        )
    ]
)

annotation4 = []
for i,j in zip(range(27), diff_from_day_before['total']):
  annotation4.append(
        dict(
            x=i,
            y=-600,
            xref="x",
            yref="y",
            text=str(j)[:-2]+"<br> total",
            showarrow=False,
            #arrowhead=7,
            ax=0,
            ay=-40))

fig_stacked_ny.update_layout(
    plot_bgcolor='white',
    showlegend=True,
    annotations = annotation4
)


#------------------------------------------FIG 2

fig_area_world_day_changes = go.Figure()

fig_area_world_day_changes.add_trace(go.Scatter(x=df_italy["date"], y=df_italy["new_Confirmed"], #fill='tozeroy',fillcolor='#B0DAAE',
                    mode= 'lines', name = 'Italy',legendgroup="group3",
                    stackgroup='two',
                    line=dict(width=0.5, color='rgba(183, 224, 240, 0.94)'),
                    text="Italy<br>New Confirmed Cases <br>from the day before",hoveron = 'points+fills', 
                    hoverinfo = 'x+text+y'))

fig_area_world_day_changes.add_trace(go.Scatter(x=df_usa["date"], y=df_usa["new_Confirmed"],##fill='toself',fillcolor='rgba(133, 70, 216, 0.3)',
                    mode='lines',legendgroup="group2",
                    stackgroup='one',
                    line=dict(width=0.5, color='rgba(238, 175, 206, 0.82)'),
                    text="U.S.<br>New Confirmed Cases <br>from the day before",hoveron = 'points+fills', name = 'U.S.',
                    hoverinfo = 'x+text+y' # override default markers+lines
                    ))

fig_area_world_day_changes.add_trace(go.Scatter(x=df_china["date"], y=df_china["new_Confirmed"], #fill='tozeroy',fillcolor='#F4DBE5',
                    mode='lines', legendgroup="group1",
                    stackgroup='three',
                    line=dict(width=0.5, color='rgba(159, 133, 229, 0.51)'),
                    text="China<br>New Confirmed Cases <br>from the day before",hoveron = 'points+fills', name = 'China',
                    hoverinfo = 'x+text+y' # override default markers+lines
                    ))

annotat = []
annotat.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
            xanchor='center', yanchor='top',
            text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
            font=dict(family='Arial',
                    size=12,
                    color="#a3a3a3"),
            showarrow=False))

fig_area_world_day_changes.update_layout(
    annotations = annotat,
    yaxis=dict(title_text="Confirmed Cases",color='#05b9f0'),
    title = "DAY-TO-DAY NEW ADDITIONS IN CONFIRMED CASES IN U.S. VS. CHINA VS. ITALY",paper_bgcolor='rgba(0,0,0,0)',
    font=dict(family='Arial',
    color='rgb(37,37,37)'),
    plot_bgcolor='rgba(0,0,0,0)', 
)

#--------------------------------------------------------


#--------------------------------------------------fig_line_cumulative_us_italy_china


fig_line_cumulative_us_italy_china = go.Figure()

# Add surface trace
fig_line_cumulative_us_italy_china.add_trace(go.Scatter(x=df_usa['date'], y=df_usa['Confirmed'],
                    name = "US",
                    hovertext=df_usa["Confirmed"],
                    hoverinfo='text',
                    hovertemplate =
                    '<i>Date: </i>: %{x}'+
                    '<br><b>Confirmed: </b>: %{y:,}<br>',
                    line_shape='spline',
                    line_color='#68CEF3',
                    ))

fig_line_cumulative_us_italy_china.add_trace(go.Scatter(x=df_italy['date'], y=df_italy['Confirmed'],
                    name = "Italy",
                    hovertext=df_italy["Confirmed"],
                    hoverinfo='text',
                    hovertemplate =
                    '<i>Date: </i>: %{x}'+
                    '<br><b>Confirmed: </b>: %{y:,}<br>',
                    line_shape='spline',
                    line_color='#9e92f6',
                    ))

fig_line_cumulative_us_italy_china.add_trace(go.Scatter(x=df_china['date'], y=df_china['Confirmed'],
                    name = "China",
                    hovertext=df_china["Confirmed"],
                    hoverinfo='text',
                    hovertemplate =
                    '<i>Date: </i>: %{x}'+
                    '<br><b>Confirmed: </b>: %{y:,}<br>',
                    line_shape='spline',
                    line_color = '#e7b1c7',
                    ))

fig_line_cumulative_us_italy_china.update_traces(hoverinfo='text+name', mode='lines+markers')

# Update plot sizing
fig_line_cumulative_us_italy_china.update_layout(
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
        showticklabels=True,
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
fig_line_cumulative_us_italy_china.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)


annotations = []

annotations.append(dict(xref='paper', x=.992, y=66000,
                              xanchor='right', yanchor='bottom',
                              text='Italy',
                              font=dict(family='Arial',
                                        color='#9e92f6',
                                        size=20),
                              showarrow=False))

annotations.append(dict(xref='paper',  x=.992, y=97000,
                              xanchor='right', yanchor='bottom',
                              text='U.S.',
                              font=dict(family='Arial',
                                        color='#68CEF3',
                                        size=20),
                              showarrow=False))
annotations.append(dict(xref='paper', x=1.001, y=74500,
                              xanchor='right', yanchor='bottom',
                              text='China',
                              font=dict(family='Arial',
                                        color = '#e7b1c7',
                                        size=20),
                              showarrow=False))
# Title
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='CHINA VS. ITALY VS. UNITED STATES, COVID-19 CONFIRMED CASES',
                              font=dict(family='Arial',
                                        size=20,
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

all_annotations = [dict(xref='paper', x=1.002, y=74500,
                              xanchor='right', yanchor='bottom',
                              text='China',
                              font=dict(family='Arial',
                                        color = '#e7b1c7',
                                        size=20),
                              showarrow=False),
                   dict(xref='paper', x=0.992, y=66000,
                              xanchor='right', yanchor='bottom',
                              text='Italy',
                              font=dict(family='Arial',
                                        color='#9e92f6',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', x=0.992, y=97000,
                              xanchor='right', yanchor='bottom',
                              text='U.S.',
                              font=dict(family='Arial',
                                        color='#68CEF3',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='CHINA VS. ITALY VS. UNITED STATES, COVID-19 CONFIRMED CASES',
                              font=dict(family='Arial',
                                        size=20,
                                        color='rgb(37,37,37)'),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False)]


italy_annotations = [dict(xref='paper', x=0.992, y=74500,
                              xanchor='right', yanchor='bottom',
                              text='Italy',
                              font=dict(family='Arial',
                                        color='#9e92f6',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', x=0.992, y=97000,
                              xanchor='right', yanchor='bottom',
                              text='U.S.',
                              font=dict(family='Arial',
                                        color='#68CEF3',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='China vs. Italy vs. United States, Covid-19 Confirmed Cases',
                              font=dict(family='Arial',
                                        size=20,
                                        color='rgb(37,37,37)'),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False)]

china_annotations = [dict(xref='paper', x=1.01, y=74600,
                              xanchor='right', yanchor='bottom',
                              text='China',
                              font=dict(family='Arial',
                                        color = '#e7b1c7',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', x=0.999, y=97000,
                              xanchor='right', yanchor='bottom',
                              text='U.S.',
                              font=dict(family='Arial',
                                        color='#68CEF3',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='CHINA VS. ITALY VS. UNITED STATES, COVID-19 CONFIRMED CASES',
                              font=dict(family='Arial',
                                        size=20,
                                        color='rgb(37,37,37)'),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False)]

fig_line_cumulative_us_italy_china.update_layout(
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
                     args=[{"visible": [True, True, False]},
                           {
                            "annotations": italy_annotations}]),
                dict(label="Compare with China",
                     method="update",
                     args=[{"visible": [True, False, True]},
                           {
                            "annotations": china_annotations}]),
            ]),
        )
    ])


fig_line_cumulative_us_italy_china.update_layout(annotations=annotations)

#========================================================================

# top_labels = ['CONFIRMED', 'RECOVERED','DEATHS']
# top_labels_l = ['Confirmed', 'Recover', 'Die']

# colors = ['#d9f0f2', '#38cedc',
#           '#f2d4e0']

# x_data = df_usa_total_h[['Confirmed_normalized','Recovered_normalized','Deaths_normalized']].values

# y_data = df_usa_total_h['date'].values

# fig_us_compare = go.Figure()

# for i in range(0, len(x_data[0])):
#     for xd, yd in zip(x_data, y_data):
#         fig_us_compare.add_trace(go.Bar(
#             x=[xd[i]], y=[yd],
#             orientation='h',
#             marker=dict(
#                 color=colors[i],
#                 line=dict(color='rgb(248, 248, 249)', width=1)
#             )
#         ))

# fig_us_compare.update_layout(
#     xaxis=dict(
#         showgrid=False,
#         showline=False,
#         showticklabels=False,
#         zeroline=False,
#         domain=[0.15, 1]
#     ),
#     yaxis=dict(
#         showgrid=False,
#         showline=False,
#         showticklabels=False,
#         zeroline=False,
#     ),
#     barmode='stack',
#     paper_bgcolor='rgb(248, 248, 255)',
#     plot_bgcolor='rgb(248, 248, 255)',
#     margin=dict(l=120, r=10, t=140, b=25),
#     # margin=dict(l=1.20, r=.10, t=1.40, b=.25),
#     showlegend=False,
# )

# annotations1 = []

# for yd, xd in zip(y_data, x_data):
#     # labeling the first percentage of each bar (x_axis)
#     annotations1.append(dict(xref='x', yref='y',
#                             x=xd[0] / 2, y=yd,
#                             text= yd, # str(xd[0])[:2] + "% " + top_labels_l[0], #'{:.s}'.format(xd[0]) + '%',
#                             hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
#                             font=dict(family='Arial', size=14,
#                                       color='#6cc3cb'),
#                             showarrow=False))
#     # labeling the first Likert scale (on the top)
#     if yd == y_data[-1]:
#         annotations1.append(dict(xref='x', yref='paper',
#                                 x=(xd[0] / 2), y=1.05,
#                                 text=top_labels[0],
#                                 hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
#                                 font=dict(family='Arial', size=10,
#                                           color='rgb(186, 186, 186)'),
#                                 showarrow=False))
#     space = xd[0]
#     for i in range(1, len(xd)):
#             # labeling the rest of percentages for each bar (x_axis)
#             annotations1.append(dict(xref='x', yref='y',
#                                     x=space + (xd[i]/10), y=yd,
#                                     text= " ", 
#                                     hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
#                                     font=dict(family='Arial', size=24,
#                                               color='rgba(20, 137, 16, 0.77)'),
#                                     #hovertext = str(xd[i])[:2] + "% " + top_labels_l[i], #str(xd[i]) + '%',
#                                     showarrow=False))
#             # labeling the Likert scale
#             if yd == y_data[-1]:
#                 annotations1.append(dict(xref='x', yref='paper',
#                                         x=(space + (xd[i]/10))-8, y=1.05,
#                                         text=top_labels[i],
#                                         hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
#                                         font=dict(family='Arial', size=10,
#                                                   color='rgb(186, 186, 186)'),
#                                         showarrow=False))
#             space += xd[i]+7

# fig_us_compare.update_layout(annotations=annotations1 ,paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')




# fig_us_compare.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})

# #------------------------------------------------------

# top_labels = ['CONFIRMED', 'RECOVERED','DEATHS']
# top_labels_l = ['Confirmed', 'Recover', 'Die']

# colors = ['#d9f0f2', '#38cedc',
#           '#f2d4e0']

# x_data = df_italy_total_h[['Confirmed_normalized','Recovered_normalized','Deaths_normalized']].values

# y_data = df_italy_total_h['date'].values

# fig_italy_compare = go.Figure()

# for i in range(0, len(x_data[0])):
#     for xd, yd in zip(x_data, y_data):
#         fig_italy_compare.add_trace(go.Bar(
#             x=[xd[i]], y=[yd],
#             orientation='h',
#             marker=dict(
#                 color=colors[i],
#                 line=dict(color='rgb(248, 248, 249)', width=1)
#             )
#         ))

# fig_italy_compare.update_layout(
#     xaxis=dict(
#         showgrid=False,
#         showline=False,
#         showticklabels=False,
#         zeroline=False,
#         domain=[0.15, 1]
#     ),
#     yaxis=dict(
#         showgrid=False,
#         showline=False,
#         showticklabels=False,
#         zeroline=False,
#     ),
#     barmode='stack',
#     paper_bgcolor='rgb(248, 248, 255)',
#     plot_bgcolor='rgb(248, 248, 255)',
#     margin=dict(l=120, r=10, t=140, b=25),
#     # margin=dict(l=1.20, r=.10, t=1.40, b=.25),
#     showlegend=False,
# )

# annotations1 = []

# for yd, xd in zip(y_data, x_data):
#     # labeling the first percentage of each bar (x_axis)
#     annotations1.append(dict(xref='x', yref='y',
#                             x=xd[0] / 2, y=yd,
#                             text= yd, # str(xd[0])[:2] + "% " + top_labels_l[0], #'{:.s}'.format(xd[0]) + '%',
#                             hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
#                             font=dict(family='Arial', size=14,
#                                       color='#6cc3cb'),
#                             showarrow=False))
#     # labeling the first Likert scale (on the top)
#     if yd == y_data[-1]:
#         annotations1.append(dict(xref='x', yref='paper',
#                                 x=(xd[0] / 2), y=1.05,
#                                 text=top_labels[0],
#                                 hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
#                                 font=dict(family='Arial', size=10,
#                                           color='rgb(186, 186, 186)'),
#                                 showarrow=False))
#     space = xd[0]
#     for i in range(1, len(xd)):
#             # labeling the rest of percentages for each bar (x_axis)
#             annotations1.append(dict(xref='x', yref='y',
#                                     x=space + (xd[i]/10)+3.95, y=yd,
#                                     text= str(xd[i])[:1] + '% ' + top_labels_l[i], 
#                                     hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
#                                     font=dict(family='Arial', size=13,
#                                               color='#2c8590'),
#                                     #hovertext = str(xd[i])[:2] + "% " + top_labels_l[i], #str(xd[i]) + '%',
#                                     showarrow=False))
#             # labeling the Likert scale
#             if yd == y_data[-1]:
#                 annotations1.append(dict(xref='x', yref='paper',
#                                         x=(space + (xd[i]/10))-8, y=1.05,
#                                         text=top_labels[i],
#                                         hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
#                                         font=dict(family='Arial', size=10,
#                                                   color='rgb(186, 186, 186)'),
#                                         showarrow=False))
#             space += xd[i]-1.5

# fig_italy_compare.update_layout(annotations=annotations1 ,paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

# fig_italy_compare.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})

# #------------------------------------------------------


# top_labels = ['CONFIRMED', 'RECOVERED','DEATHS']
# top_labels_l = ['Confirmed', 'Recover', 'Die']

# colors = ['#d9f0f2', '#38cedc',
#           '#f2d4e0']

# x_data = df_china_total_h[['Confirmed_normalized','Recovered_normalized','Deaths_normalized']].values

# y_data = df_china_total_h['date'].values

# fig_china_compare = go.Figure()

# for i in range(0, len(x_data[0])):
#     for xd, yd in zip(x_data, y_data):
#         fig_china_compare.add_trace(go.Bar(
#             x=[xd[i]], y=[yd],
#             orientation='h',
#             marker=dict(
#                 color=colors[i],
#                 line=dict(color='rgb(248, 248, 249)', width=1)
#             )
#         ))

# fig_china_compare.update_layout(
#     xaxis=dict(
#         showgrid=False,
#         showline=False,
#         showticklabels=False,
#         zeroline=False,
#         domain=[0.15, 1]
#     ),
#     yaxis=dict(
#         showgrid=False,
#         showline=False,
#         showticklabels=False,
#         zeroline=False,
#     ),
#     barmode='stack',
#     paper_bgcolor='rgb(248, 248, 255)',
#     plot_bgcolor='rgb(248, 248, 255)',
#     margin=dict(l=120, r=10, t=140, b=25),
#     # margin=dict(l=1.20, r=.10, t=1.40, b=.25),
#     showlegend=False,
# )

# annotations1 = []

# for yd, xd in zip(y_data, x_data):
#     # labeling the first percentage of each bar (x_axis)
#     annotations1.append(dict(xref='x', yref='y',
#                             x=xd[0] / 2, y=yd,
#                             text= yd, # str(xd[0])[:2] + "% " + top_labels_l[0], #'{:.s}'.format(xd[0]) + '%',
#                             hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
#                             font=dict(family='Arial', size=14,
#                                       color='#6cc3cb'),
#                             showarrow=False))
#     # labeling the first Likert scale (on the top)
#     if yd == y_data[-1]:
#         annotations1.append(dict(xref='x', yref='paper',
#                                 x=(xd[0] / 2), y=1.05,
#                                 text=top_labels[0],
#                                 hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
#                                 font=dict(family='Arial', size=10,
#                                           color='rgb(186, 186, 186)'),
#                                 showarrow=False))
#     space = xd[0]
#     for i in range(1, len(xd)):
#             # labeling the rest of percentages for each bar (x_axis)
#             if i == 1:
#               annotations1.append(dict(xref='x', yref='y',
#                                       x=space+22.5, y=yd,
#                                       text= str(xd[i])[:4] + '% Recover',
#                                       hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
#                                       font=dict(family='Arial', size=14,
#                                                 color='#d0f1f0'),
#                                       #hovertext = str(xd[i])[:2] + "% " + top_labels_l[i], #str(xd[i]) + '%',
#                                       showarrow=False))
#               # labeling the Likert scale
#               if yd == y_data[-1]:
#                   annotations1.append(dict(xref='x', yref='paper',
#                                           x=(space + (xd[i])), y=1.05,
#                                           text=top_labels_l[i],
#                                           hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
#                                           font=dict(family='Arial', size=10,
#                                                     color='rgb(186, 186, 186)'),
#                                           showarrow=False))
#               space += xd[i]


# fig_china_compare.update_layout(annotations=annotations1 ,paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')


# fig_china_compare.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})

#------------------------------------------------------

columnTopAlert = dbc.Col(
    [
        html.Center(
            children=[
                # html.Img(src=app.get_asset_url('topBanner.png'), style={'display': 'block', 'height':80})
                #html.H6('New York State: 30,811 Confirmed cases', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':8}),
                #html.H6('Data Above from the New York State Dept. of Health march 25, 2 pm', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':15}),
            ]
        ),
    ],
    md=12,
)

columnTopLeft = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('NYC', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':5}),
            html.H6('Confirmed Cases', style={'fontSize':13, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':0}),
            html.H6('Last 5 Days', style={'fontSize':10, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
            # html.H1('38', style={'fontSize':60, 'color':'#05b9f0', 'marginBottom':0}),#fig_line_cumulative_us_italy_china
            ]
        ),
        dcc.Graph(figure=fig_bar_nyc_last_5_days),
        html.Center(
            children=[
            html.H6('Day-to-day % Increases', style={'fontSize':11, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':10}),
            html.H6('in Number of', style={'fontSize':10, 'color':'#05b9f0', 'marginTop':6, 'marginBottom':0}),
            html.H6('Confirmed Cases', style={'fontSize':10, 'color':'#05b9f0', 'marginTop':6, 'marginBottom':0}),
            html.H6('NYC', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':6, 'marginBottom':10}),
            ]
        ),
        dcc.Graph(figure=fig_area_nyc_percentage_change),
        html.Center(
            children=[
        html.H6('Data from NY State DOH on March 28, 3 pm', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':8}),
            ]
        ),
    ],
    md=3,
)

columnTopCenter = dbc.Col(
    [
        dcc.Graph(figure=fig_map_top_center,style={'paddingTop':0, 'paddingBottom':0}),
        html.Center(
            children=[
                html.H6('Please hover over dots for more info', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':15, 'marginBottom':0}),#fig_line_cumulative_us_italy_china
                html.H6('Data Provided by the Johns Hopkins University CSSE updated on March 28th.', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':0}),#fig_line_cumulative_us_italy_china
            ]
        ),
    ],
    md=6,
    )

columnTopRight = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('Positive Cases NYC', style={'fontSize':20, 'color':'#14c5fa', 'marginTop':0, 'marginBottom':8}),#fig_line_cumulative_us_italy_china
            html.H1('29,766', style={'fontSize':70, 'color':'#5CD8FE', 'marginBottom':0}),#fig_line_cumulative_us_italy_china
            html.H6('Deaths NYC', style={'fontSize':11, 'color':'#14c5fa', 'marginTop':20, 'marginBottom':0}),#fig_line_cumulative_us_italy_china
            html.H6('517', style={'fontSize':32, 'color':'#5CD8FE', 'marginTop':10}),#fig_line_cumulative_us_italy_china
            html.H6('Data above from NYS Dept. of Health march 28, 3 PM', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':0}),#fig_line_cumulative_us_italy_china
            html.H6('Positive Cases by Borough', style={'fontSize':20, 'color':'#208fb1', 'marginTop':20}),
            html.Img(src=app.get_asset_url('NYC_Covid-19_Cases_03-28_01.png'), style={'display': 'block', 'height':300}),
            html.H6('Data from NYC DOH, last updated there on March 28, 3 pm', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':30, 'marginBottom':8}),
            ]
        ),
    ],
    md=3,
)


columnNeighborhoods = dbc.Col(
    [
        html.Center(
            children=[
                html.Img(src=app.get_asset_url('ConfirmedCasesByNeighborhood.jpg'), style={'display': 'block', 'width':'100%', 'marginTop':70}),
                html.H6('Map Released by the  NYC DOH, on March 26', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':30, 'marginBottom':8}),
            ]
        )
    ],md=10,
)


column_nyc_stats = dbc.Col(
    [
        html.Center(
            children=[
                dcc.Graph(figure=fig_line_nyc_borough_day_change),
                dcc.Graph(figure=fig_stacked_change_borough_cases),
            ]
        )
    ],
    md=10
)

column0bottomCenter = dbc.Col(
    [
        html.Center(
            children=[
            html.Br(),
            html.Span(' ', className='mr-1'),
            html.Br(),
            html.Span(' ', className='mr-1'),
            dcc.Graph(figure=fig_pie_nyc_age),
            ]
        )
    ],
    md=12,
)
column0bottomCenter2 = dbc.Col(
    [
        html.Center(
            children=[
            dcc.Graph(figure=fig_pie_nyc_death_age),
            html.H6('Data for above pie charts from NYC DOH', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':80}),
            ]
        )
    ],
    md=12,
)

column1Left = dbc.Col(
    [
        html.Center(
            children=[
                dcc.Graph(figure=fig_map_nyc_timeslider),
            ]
        )
    ],
    md=6
)
column1Right = dbc.Col(
    [
        html.Center(
            children=[
                html.H6('NUMBER OF POSITIVE CASES OF COVID-19 BY COUNTY', style={'fontSize':18, 'color':'#05b9f0', 'marginTop':40, 'marginBottom':10}),
                html.H6('FOR THE TOP 15 COUNTIES RANKED BY THE MOST CASES', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':0}),
                dcc.Graph(figure=fig_line_ny_cumulative),
                html.H6('TOTAL POSITIVE CASES OF COVID-19 BY COUNTY OVER TIME', style={'fontSize':18, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':10}),
                html.H6('FOR THE TOP 8 COUNTIES RANKED BY THE MOST CASES', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':0}),
                dcc.Graph(figure=fig_line_ny_overtime),
            ]
        )
    ],
    md=6
)
column1bottomCenter = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('Data for above interactive charts from NY State DOH for March 28th', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':20, 'marginBottom':20}),
            ]
        )
    ],
    md=12,
)


column2Center = dbc.Col(
    [
        html.Center(
            children=[
            html.Br(),
            html.Span(' ', className='mr-1'),
            html.H6('NUMBER OF CONFIRMED CASES OF COVID-19', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':60, 'marginBottom':10}),
            html.H6('IN NEW YORK STATE BY COUNTY', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
            html.Img(src=app.get_asset_url('Covid-19_Cases_NYS_03-28_annotated.png'), style={'display': 'block', 'width':'100%'}),
            ]
        )
    ],
    md=7,
)
column2Right = dbc.Col(
    [
        html.Center(
            children=[
            html.Br(),
            html.Span(' ', className='mr-1'),
            html.Br(),
            html.Span(' ', className='mr-1'),
            html.H6('NUMBER OF CONFIRMED CASES OF COVID-19', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':30, 'marginBottom':10}),
            html.H6('IN NEW YORK STATE BY DATE', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
            html.Img(src=app.get_asset_url('Covid-19_Cases_NYS_2020-03-28.gif'), style={'display': 'block', 'width':'100%','marginTop':130, 'marginBottom':100}),
            ]
        )
    ],
    md=5,
)
column2bottomCenter = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('Data from NY State DOH, last updated there on March 28, 3 pm', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':8}),#fig_line_cumulative_us_italy_china
            ]
        )
    ],
    md=12,
)
columnStackedCounty = dbc.Col(
    [
        html.Center(
            children=[
            dcc.Graph(figure=fig_stacked_ny),
            dcc.Graph(figure=fig_stacked_change_county_cases),
            html.H6('Data from NY State DOH, last updated there on March 28, 3 pm', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':8}),#fig_line_cumulative_us_italy_china
            html.H6('Please be mindful that only a limited amount of people are given tests at this time.', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':8}),#fig_line_cumulative_us_italy_china
            ]
        )
    ],
    md=12,
)


column3CenterAll = dbc.Col(
    [
        html.Center(
            children=[
                html.Br(),
                html.Span(' ', className='mr-1'),
                html.Br(),
                html.Span(' ', className='mr-1'),
                #html.H6('DAY-TO-DAY CHANGES IN CONFIRMED CASES ITALY VS U.S. VS CHINA', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
                dcc.Graph(figure=fig_area_world_day_changes),
            ]
        )
    ]
)


# columnDistL = dbc.Col(
#     [
#         html.Center(
#             children=[
#                 html.H6('Status of Covid-19', style={'fontSize':16, 'color':'#05b9f0', 'marginTop':80, 'marginBottom':10}),
#                 html.H6('cumulative Cases Recorded in', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
#                 html.H6('U.S.', style={'fontSize':22, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
#                 html.Div(
#                     [
#                         dbc.Button("Confirmed", color="light", size="sm"),
#                         dbc.Button("Recovered", color="light", size="sm"),
#                         dbc.Button("Deaths", color="light", size="sm"),]),
#                         dcc.Graph(figure=fig_us_compare),
#                      ],
#                 ),
#             ],
#     md=12,
# )
# columnDistC = dbc.Col(
#     [
#         html.Center(
#             children=[
#                 html.H6('Status of Covid-19', style={'fontSize':16, 'color':'#05b9f0', 'marginTop':60, 'marginBottom':10}),
#                 html.H6('cumulative Cases Recorded in', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
#                 html.H6('Italy', style={'fontSize':22, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
#                 html.Div(
#                     [
#                         dbc.Button("Confirmed", color="light", size="sm"),
#                         dbc.Button("Recovered", color="light", size="sm"),
#                         dbc.Button("Deaths", color="light", size="sm"),]),
#                         dcc.Graph(figure=fig_italy_compare),
#                      ],
#                 ),
#             ],
#     md=12,
# )
# columnDistR = dbc.Col(
#     [
#         html.Center(
#             children=[
#                 html.H6('Status of Covid-19', style={'fontSize':16, 'color':'#05b9f0', 'marginTop':60, 'marginBottom':10}),
#                 html.H6('cumulative Cases Recorded in', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
#                 html.H6('China', style={'fontSize':22, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
#                 html.Div(
#                     [
#                         dbc.Button("Confirmed", color="light", size="sm"),
#                         dbc.Button("Recovered", color="light", size="sm"),
#                         dbc.Button("Deaths", color="light", size="sm"),]),
#                         dcc.Graph(figure=fig_china_compare),
#                      ],
#                 ),
#             ],
#     md=12,
# )

# columnDistbottomCenter = dbc.Col(
#     [
#         html.Center(
#             children=[
#             html.H6('Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':20, 'marginBottom':8}),#fig_line_cumulative_us_italy_china
#             ]
#         )
#     ],
#     md=12,
# )



column4CenterAll = dbc.Col(
    [
        html.Br(),
        html.Span(' ', className='mr-1'),
        dcc.Graph(figure=fig_line_cumulative_us_italy_china),
        html.Br(),
        html.Span(' ', className='mr-1'),
    ]
)


announcementsHeader = dbc.Col(
    [
        html.Center(
            children=[
            html.Img(src=app.get_asset_url('helpfulInfo.png'), style={'display': 'block', 'width':'100%'})
            ]
        )
    ],
    md=8,
)


annoucementsCenter = dbc.Col(
    [
        html.Center(
            children=[
                dbc.Jumbotron(
                    [
                        html.H1("Transit", className="display-4", style={"color":"#03607d"}),
                        html.P(
                            "MTA Bus Riders Ride for Free "
                            "(Express Bus Riders Still Pay)",
                            className="lead", style={"color":"#03607d"},
                        ),
                        html.Hr(className="my-2"),
                        html.P(
                            "Subway Service Cut by a Quarter", style={"color":"#03607d"}),
                        html.P("No. 4, 5, 6, 7 and the J and D lines, will run locally on all or part of their routes", style={"color":"#03607d"}),
                        html.P(dbc.Button("Read more", color="info", href="https://www.nytimes.com./2020/03/24/nyregion/coronavirus-nyc-mta-cuts-.html"), className="lead"),
                    ]
                )
            ]
        )
    ],
    md=8,
)


shopAnnouncementsCenter = dbc.Col(
    [
        html.Center(
            children=[
                dbc.Jumbotron(
                    [
                        html.H1("Special Shopping Hours", className="display-6", style={"color":"#03607d"}),
                        html.Span(' ', className='mr-1'),
                        html.P("Whole Foods are open one hour before their normal opening time for seniors 60 and above every day.", style={"color":"#03607d"}, className="lead"),
                        html.P("Trader Joe's are open just for seniors 65 and above 9 a.m. to 10 a.m. every day.", className="lead", style={"color":"#03607d"}),
                        html.Hr(className="my-2"),
                        html.P("Stop-and-Shop's are open 6 am to 7:30 am every day for those age 60 and older and younger customers with weakened immune systems.", style={"color":"#03607d"},className="lead"),
                        html.P("Costco's are open for seniors over age 60 on Tuesdays and Thursdays from 8 to 9 a.m.", style={"color":"#03607d"},className="lead"),
                        html.P("Walgreens has Tuesday weekly senior hour from 8 to 9 a.m., open to caregivers and immediate families, as well.", style={"color":"#03607d"},className="lead"),
                        html.Hr(className="my-2"),
                        html.P("Most top retailers have begun offering senior shopping hours, please look on their website for more information.", style={"color":"#03607d"}
                        ),
                        html.P(dbc.Button("Read more", color="info", href="https://www.cnbc.com/2020/03/19/coronavirus-how-senior-shopping-hours-work-at-stop-shop-other-grocers.html"), className="lead"),
                    ]
                )
            ]
        )
    ],
    md=8,
)

taxesAnnouncementsCenter = dbc.Col(
    [
        html.Center(
            children=[
                dbc.Jumbotron(
                    [
                        html.H1("Filing Income Tax", className="display-6", style={"color":"#03607d"}),
                        html.Span(' ', className='mr-1'),
                        html.P("New York State's income tax filing deadline is delayed until July 15, 2020.", style={"color":"#03607d"}, className="lead"),
                        html.Hr(className="my-2"),
                        html.P("Because New York State requires electronic filing, the date for filing state personal income taxes automatically travels with the federal filing date, which is now July 15. ", style={"color":"#03607d"}),
                        html.P(dbc.Button("Read more", color="info", href="https://www.tax.ny.gov/default.htm"), className="lead"),
                    ]
                )
            ]
        )
    ],
    md=8,
)

unemploymentAnnouncementsCenter = dbc.Col(
    [
        html.Center(
            children=[
                dbc.Jumbotron(
                    [
                        html.H1("Filing for Unemployment", className="display-6", style={"color":"#03607d"}),
                        html.Span(' ', className='mr-1'),
                        html.P("If you filed for unemployment during the COVID-19 pandemic, you do not need to prove you are searching for employment to make a claim. ", style={"color":"#03607d"}, className="lead"),
                        html.Hr(className="my-2"),
                        html.P("Department of Labor Commissioner Reardon has signed a new order that limits all work search activities for all unemployment claimants. No activities are required during the pandemic to receive unemployment benefits.", style={"color":"#03607d"}),
                        html.P(dbc.Button("Read more", color="info", href="https://labor.ny.gov/ui/how_to_file_claim.shtm"), className="lead"),
                    ]
                )
            ]
        )
    ],
    md=8,
)


selectedWritingsHeaderCenter = dbc.Col(
    [
        html.Center(
            children=[
                html.Img(src=app.get_asset_url('Covid19-Website-R7-000_0038_Layer-28.png'), style={'display': 'block', 'width':'100%'}),
                html.Img(src=app.get_asset_url('mindfulnessShopping.gif'), style={'display': 'block', 'width':'100%'}),
                html.Br(),
                html.Span(' ', className='mr-1'),
            ]
        )
    ],
    md=8,
)


collapseEniqueArticle = dbc.Col(
    [
        html.Center(
            html.Div(
                [
                    dbc.Card(
                        dbc.CardBody(
                        [
                            html.H4("Mindfulness When Shopping",className="card-text",style={'fontSize':32, 'marginTop':40, 'marginBottom':55}),
                            html.P(
                                "It’s difficult to stay home during this crisis if we’re ill-prepared. We have to stock up on food, snacks, vitamins, hand sanitizer and, of course, toilet paper. It’s important to have a clean booty during a pandemic.",className="card-text"
                            ),
                            html.P(
                                "That’s why shopping for quarantine life has become an event. Thanks to the hours of predictive programming instilled into our minds by post-apocalyptic movies centering on societal collapse, we haven’t been reduced to chaotic creatures. However, as someone who is still assisting customers, both young and old, I have noticed an array of mindfulness and lack thereof when it comes to shopping. ",className="card-text"
                            ),
                            html.P(
                                "So here are a few tips you can use to protect yourself and others when shopping.",className="card-text"
                            ),
                            html.H5("Mask & Gloves ",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                            html.P(
                                "Seriously. We’re at a point where you have to assume someone has touched the item you just grabbed, whether it’s an employee or another customer. It helps you, the employees, fellow customers, and your loved ones. The addition of the mask can help ease any anxieties that employees may have, and it adds a layer of protection for you, too. ",className="card-text"
                            ),
                            html.P(
                                "According to the Centers for Disease Control and Prevention (CDC), It is recommended to use nitrile gloves, natural rubber gloves, or polychloroprene gloves, as they provide higher elasticity than vinyl gloves. "
                            ),
                            html.P(
                                "For masks, as you may already know, the N-95 Respirator comes highly recommended, for its tight fight and ability to reduce 95 percent of the wearer’s exposure to small particles and large droplets. A surgical mask may work in a pinch, however, it will not provide the needed protection against smaller airborne particles."
                            ),
                            html.P(
                                "Ideally, it is suggested that these masks be thrown away after each use. But given the current deficiencies of Personal Protective Equipment (PPE) that hospitals are facing, it would be considerate if you did not hoard masks, which could be accomplished by giving each individual mask a longer service life."
                            ),
                            html.P(
                                "If possible, you can help by reaching out to local hospitals and donating masks. "
                            ),
                            html.H5("What to Do",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                            html.P(
                                "One store will not operate like the other, especially if you are frequenting independent pharmacies, grocery stores, and food processors. Make an attempt to learn their style of operations, checkout procedures, payment options, hours, and safety precautions.For example, Stop and Shop allow senior citizens (60-year-olds and over) to shop between 6-7:30 am, while Trader Joe’s is only allowing 30 customers in the store at one time.",className="card-text"
                            ),
                            html.P(
                                "Generally, you can avoid the crowds during the early mornings, because as the saying goes: the early bird catches the worm. Just pay attention to any updates that shops may have via their social media accounts, or call ahead if you’re not sure.",className="card-text"
                            ),
                            html.H5("Know What You Want",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                            html.P(
                                "For real, this isn’t the time to be window shopping. With the ever-increasing descent upon grocery stores and pharmacies, it’s imperative to have a list of the items you will be needing. "
                            ),
                            html.P(
                                "The quicker you are the quicker the checkout line will move, which will result in shorter exposure times. If you need help figuring out how to shop, refer to the god-awful film, “Jingle All the Way” starring Arnold Schwarzenegger and Sinbad.",className="card-text"
                            ),
                            html.H5("Gimme Some Space",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                            html.P(
                                "People are touching, smiling, and not respecting your personal space. The whole time my mind is thinking, 'Gimme some space, bro!' "
                            ),
                            html.P(
                                "Do you people even understand what’s happening out here? I’m not trying to add to the fear-mongering tactics some have accused the media of using, but if we don’t take this seriously we will be risking people’s health by extending this pandemic’s life span.",className="card-text"
                            ),
                            html.P(
                                "Please practice social distancing. Communicate clearly and thoroughly from the recommended six-foot distance. Keep in mind, that if you’re on a possible collision course with someone waving is one of the best non-verbal cues that you can rely on if you’re having trouble commanding a person’s attention.",className="card-text"
                            ),
                            html.P(
                                "Remember, if you can smell someone’s breath, cologne, or body odor you are too close.",className="card-text"
                            ),
                            html.H5("Wipe Everything Down",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                            html.P(
                                "Once you’re home, it’s important to wipe down any of the items you may have purchased, whether it’s packaged food products, produce, or home supplies. If it’s possible, designate an area at home that will be used to place outside items on. Wipe down this area after everything is put away. ",className="card-text"
                            ),
                            html.P(
                                "A thorough cleaning of fruits and veggies is crucial before they are stored away, even for fruits that are protected by an out layer, like oranges, bananas, and melons. A simple soak/wash in a bowl of water with vinegar (apple cider vinegar or white vinegar) and a gentle scrub with soap would suffice.",className="card-text"
                            ),
                            html.P(
                                "For those of you that use reusable bags, especially those made from cloth, it’s also essential to clean the bag, too. ",className="card-text"
                            ),
                            html.H5("R-E-S-P-E-C-T",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                            html.P(
                                "In America, we live in such a desensitized society that people watch police killings on their phones while eating their avocado toast. ",className="card-text"
                            ),
                            html.P(
                                "We lack empathy.", className="blockquote"
                            ),
                            html.P(
                                "You don’t care about my plight or the social injustices that affect me? Whatever. That was before this new situation engulfed America, and now we’re in this together.",className="card-text"
                            ),
                            html.P(
                                "So you may have looked down on or ignored the so-called low-skilled workers two months ago, but now we’re the ones you seek for cleanliness, supplies, food, transportation, education, and the normality that dissolved, due to this pandemic, yet you still yearn for to calm your anxieties. ",className="card-text"
                            ),
                            html.P(
                                "We don’t want to be out here, but we are. We’re risking our own health and that of our loved ones, which is making your life easier. Please take the time to show your appreciation in a non-condescending fashion. We are essential workers. ",className="card-text"
                            ),
                            html.Hr(),
                            html.P(
                                "Article written by",style={'fontSize':14, 'marginTop':45, 'marginBottom':0},
                                className="card-text"),
                            dbc.Button('Enrique Grijalva', color="link",href = "https://www.linkedin.com/in/enrique-grijalva-15833059", size="sm",style={'marginBottom':0, 'marginTop':0}), 
                            ]
                        ), color="light"
                    )
                ]
            )
        )
    ],
    md=8,
)


restoringPeaceCenter = dbc.Col(
    [
        html.Center(
            children=[
                html.Img(src=app.get_asset_url('restoringPeace.png'), style={'marginTop':60,'display': 'block', 'width':'100%'}),
                html.Br(),
                html.Span(' ', className='mr-1'),
                html.Div(
                    [
                        dbc.Card(
                            dbc.CardBody(
                            [
                                html.H4("Restoring Peace Within Yourself",className="card-text",style={'fontSize':32, 'marginTop':40, 'marginBottom':55}),
                                html.P(
                                    "We understand how a pandemic can create anxiety, panic and stress, especially with how fast the worldwide spread has been. We would like to help you restore peace of mind within yourself by introducing the mindfulness practice taught by Thich Nhat Hanh, the father of mindfulness. The following comes from the chapter “Restoring Peace Within Yourself” from his book True Love.",className="blockquote"
                                ),
                                html.P(
                                    "During the day, if you practice walking meditation, each step brings you back to the present moment; each step enables you to touch what is beautiful, what is true. And in this way, after a few weeks of practice, joy will become something possible, you will be able to undo many knots within yourself, and you will be able to transform negative energies into joy and peace. The Buddha said this: “The object of your practice should first of all be yourself. Your love for the other, your ability to love another person, depends on your ability to love yourself.” If you are not able to take care of yourself, if you are not able to accept yourself, how could you accept another person and how could you love him or her? So it is necessary to come back to yourself in order to be able to achieve the transformation.",className="card-text"
                                ),
                                html.P(
                                    "Each of us is a king who reigns over a very vast territory that has five rivers. The first river is our body, which we do not know well enough. The second is the river of sensations. Each sensation is a drop of water in this river. There are pleasant sensations, others that are unpleasant, and neutral sensations. To meditate is to sit down on the bank of the river of sensations and identify each sensation as it arises. The third is the river of perceptions, which it is necessary to observe. You must look deeply into their nature in order to understand. The fourth is the river of mental formations, of which there are fifty-one. And finally, the fifth is the river of consciousness.",className="card-text"
                                ),
                                html.P(
                                    "Our territory is really very vast, but we are not responsible kings or queens. We always try to dodge away and we do not keep up a real surveillance of our territory. We have the feeling that there are immense conflicts there, too much suffering, too much pain—that is the reason we are very hesitant to get back to our territory. Our daily practice consists in running away. If we have a moment free, we will make use of it to watch television or read a magazine article so we will not have to go back to our territory. We are afraid of the suffering that is inside us, afraid of war and conflicts.",className="card-text"
                                ),
                                html.P(
                                    "The practice of mindfulness, the practice of meditation, consists of coming back to ourselves in order to restore peace and harmony. The energy with which we can do this is the energy of mindfulness. Mindfulness is a kind of energy that carries with it concentration, understanding, and love. If we come back to ourselves to restore peace and harmony, then helping another person will be a much easier thing."
                                ),
                                html.P(
                                    "Caring for yourself, reestablishing peace in yourself, is the basic condition for helping someone else. So that the other can stop being a bomb, a source of pain for ourselves and others, you really have to help him to defuse the bomb. To be able to provide help, we have to have a little calm, a little joy, a little compassion in ourselves. This is what we get from mindfulness in everyday life, because mindfulness is not something that is only done in a meditation hall; it is also done in the kitchen, in the garden, when we are on the telephone, when we are driving a car, when we are doing the dishes."
                                ),
                                html.P(
                                    "If you can do it this way, three weeks are enough to transform the pain inside you, to bring back your joy in living, to cultivate the energy of compassion with which you can help the person you love. The practice of being there with what is beautiful and with what is healing is something we should do every day, and it is possible to do this in everyday life."
                                ),
                                html.P(
                                    "In order to support your mindfulness practice, you might be interested in trying some mobile apps, such as Insight Timer, Calm, Headspace, with which you can practice mindfulness wherever you go. Hope peace of mind and love be with you, especially in this extraordinarily challenging time!", className="blockquote"
                                ),
                                html.Hr(),
                                html.P('Excerpt from Zen Master Thich Nhat Hanh. "True Love:A Practice for Awakening the Heart."Penguin Random House, 2004. Chapter 8.',style={'fontSize':14, 'marginTop':45}, className="card-text"),
                                html.P('Intro and Afterword by',style={'fontSize':14},className="card-text"),
                                dbc.Button('Wen Ping Lin', color="link",href = "https://www.linkedin.com/in/wenpinglin", size="sm",style={'marginBottom':0, 'marginTop':0}), 
                            ]), color="light"
                        )
                    ])
                ]
            )
    ],
    md=8,
)


washHandsC = dbc.Col(
    [
        html.Center(
            children=[
            html.Img(src=app.get_asset_url('WashHands.jpg'), style={'display': 'block', 'width':'100%', 'marginTop':40})
            ]
        )
    ],
    md=6,
)

distanceCenter = dbc.Col(
    [
        html.Center(
            children=[
            html.Img(src=app.get_asset_url('SocialDistancing.png'), style={'display': 'block', 'width':'100%'})
            ]
        )
    ],
    md=6,
)


pod1 = [
    dbc.CardImg(src=app.get_asset_url('podcastButtonL.jpg'), style={'display': 'block', 'width':'70%'}, top=True),
    dbc.CardBody(
        [
            html.H5("What's your Plan", className="card-title"),
            html.P(
                "Are you prepared if you get sick?",
                className="card-text",
            ),
            dbc.Button("Plan", className="mr-1", color="info", href="https://www.diypreparedness.net/how-to-make-your-own-family-emergency-binder/"),
        ]
    ),
]

trisacard = [
    dbc.CardImg(src=app.get_asset_url('trisaBunny.gif'), style={'display': 'block', 'width':'70%'}, top=True),
    dbc.CardBody(
        [
            html.H5("Trisa's Picks", className="card-title"),
            html.P(
                "Watch things that make you laugh, smile, or feel good.",
                className="card-text",
            ),
            dbc.Button("To Playlist", className="mr-1", color="info",href='https://www.youtube.com/playlist?list=PL7ESOL-2KOIUs4s61OyCJ8oO9C5n996_b'),
        ]
    ),
]

pod2 = [
    dbc.CardImg(src=app.get_asset_url('podcast2.jpg'), style={'display': 'block', 'width':'70%'}, top=True),
    dbc.CardBody(
        [
            html.H5("Our go-to Podcasts", className="card-title"),
            html.P(
                "Get informed and work on a better self.",
                className="card-text",
            ),
            dbc.Button("Listen Now", className="mr-1", color="info", href="https://open.spotify.com/playlist/65XgqkWUTIdLZm9rXqTp3x"),
        ]
    ),
]


recsCenter = dbc.Col(
    [
        html.Center(
            children=[
                html.Span(' ', className='mr-1'),
                dbc.CardGroup(
                    dbc.Card(
                        dbc.CardBody(
                            dbc.CardColumns(
                                [
                                    dbc.Card(pod1, color="light"),
                                    dbc.Card(trisacard, color="light"),
                                    dbc.Card(pod2, color="light"),
                                ]
                            )
                        )
                    )
                )
            ]
        )
    ],
    md=10,
)


singleColumn = dbc.Col([],md=1)
doubleColumn = dbc.Col([],md=2)
tripleColumn = dbc.Col([],md=3)

@app.callback(
    Output("alert-auto", "is_open"),
    [Input("alert-toggle-auto", "n_clicks")],
    [State("alert-auto", "is_open")],
)
def toggle_alert(n, is_open):
    if n:
        return not is_open
    return is_open


# layout = dbc.Row([column1, column2])
layout = [
        dbc.Row([columnTopAlert]),
        dbc.Row([columnTopLeft, columnTopCenter, columnTopRight]),

        dbc.Row([singleColumn,columnNeighborhoods, singleColumn]), 
        dbc.Row([singleColumn,column_nyc_stats, singleColumn]),

        dbc.Row([column0bottomCenter]),
        dbc.Row([column0bottomCenter2]),

        dbc.Row([column1Left,column1Right]),
        dbc.Row([column1bottomCenter]),

        dbc.Row([column2Center, column2Right]),
        dbc.Row([column2bottomCenter]),

        dbc.Row([columnStackedCounty]),

        dbc.Row([column3CenterAll]),# New Cases Worldwide
        dbc.Row([column4CenterAll]),#Confirmed cases Italy, China US


        #Deaths, Confirmed, Recovered
        # dbc.Row([columnDistC, columnDistR, columnDistL]),
        # dbc.Row([columnDistbottomCenter]),  

        dbc.Row([doubleColumn,announcementsHeader,doubleColumn]),
        dbc.Row([doubleColumn, annoucementsCenter, doubleColumn]),
        dbc.Row([doubleColumn, shopAnnouncementsCenter, doubleColumn]),
        dbc.Row([doubleColumn, taxesAnnouncementsCenter, doubleColumn]),
        dbc.Row([doubleColumn, unemploymentAnnouncementsCenter, doubleColumn]),

        dbc.Row([doubleColumn, selectedWritingsHeaderCenter, doubleColumn]),

        dbc.Row([doubleColumn,collapseEniqueArticle, doubleColumn]),
        dbc.Row([doubleColumn,restoringPeaceCenter, doubleColumn]),

        dbc.Row([tripleColumn,washHandsC,tripleColumn]),

        dbc.Row([tripleColumn, distanceCenter, tripleColumn]),
        dbc.Row([singleColumn,recsCenter,singleColumn]),        
        ]

