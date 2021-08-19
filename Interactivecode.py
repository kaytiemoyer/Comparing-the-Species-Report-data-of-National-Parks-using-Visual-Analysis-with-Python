# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:48:28 2021

@author: Kaytie
"""


import pandas as pd 
import matplotlib.pyplot as plt
import plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot
import plotly.graph_objects as go
from plotly.graph_objs import *
init_notebook_mode()

species = pd.read_csv('C:/Users/Kaytie/Desktop/School/Regis University/Summer 2021/MSDS 696/species.csv', low_memory=False)
species.head()
parks = pd.read_csv('C:/Users/Kaytie/Desktop/School/Regis University/Summer 2021/MSDS 696/parks.csv', low_memory=False)
parks.head()

species1 = species[(species.Occurrence=='Present') & (species.Record_Status
=='Approved')]
species2 = species1.drop(['Order', 'Family', 'Scientific_Name', 'Abundance', 'Seasonality', 'Conservation_Status'], axis=1)
species2.info()
species2["Park Name"].value_counts(sort=True)

parkshort = parks.drop(['State', 'Acres', 'Park Code'], axis=1)
parkshort.info()


parksch = parks.drop(['Park Code', 'Acres'], axis=1)
parksch.info()
species2.info()
speciesch = species2.drop(['Species_ID', 'Category', 'Common_Names', 'Record_Status', 'Nativeness'], axis=1)
speciesch.info()
mapch = pd.merge(speciesch, parksch, on='Park Name')
mapch.info()
count = species2.value_counts(['Park Name']).to_frame()
count.info()

u = pd.merge(mapch, count, on='Park Name')
u.info()
u.columns = ['Park Name', 'Occurrence', 'Unnamed: 13', 'State', 'Latitude', 'Longitude', 'Reports']

data = dict(type='choropleth', colorscale = 'sunset', zmax=3000, zmin=0, 
locations = u['State'], locationmode = 'USA-states',
z = u['Reports'], marker = dict(line = dict(color = '#ffe476',
                          width = 1)),colorbar = {'title':"Number of Reports"})
layout = dict(title = 'Number of Species Reports separated by State',
geo = dict(scope='usa',
           projection={'type': 'albers usa'}))
chmap = go.Figure(data = [data], layout = layout)
chmap.write_html("C:/Users/Kaytie/Desktop/School/Regis University/Summer 2021/MSDS 696/Final/choro.html")
plot(chmap)

fig = go.Figure(data=go.Scattergeo(
    lon = u['Longitude'],
    lat = u['Latitude'],
    text = u['Park Name'],
    mode = 'markers',
    marker_color = u['Reports']))
fig.update_layout(
        title = 'Locations of National Parks in the United States',
        geo_scope='usa')
plot(fig)
fig.write_html("C:/Users/Kaytie/Desktop/School/Regis University/Summer 2021/MSDS 696/Final/nationalparkscatter.html")


