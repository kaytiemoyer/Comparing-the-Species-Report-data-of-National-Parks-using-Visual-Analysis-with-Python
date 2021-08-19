# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import Point, Polygon

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
species.info()
parks.info()
crs={'init':'epsg:4326'}

base = gpd.read_file("C:/Users/Kaytie/Desktop/shp/us500.shp")
type(base)
base.head()
base.info()
base.plot()

geometry = [Point(xy) for xy in zip(parks["Longitude"], parks["Latitude"])]
geodata = gpd.GeoDataFrame(parkshort, crs=crs, geometry=geometry)
geodata.plot()

fig, ax = plt.subplots(figsize=(4,4))
base.plot(ax=ax, facecolor='cadetblue', edgecolor='w', alpha=1,linewidth=1)
geodata.plot(ax=ax, color='black', markersize=5);
fig.suptitle('National Parks of the United States', fontsize=12)
plt.xlim([-168,-67])
plt.savefig("parkgeodata")

parks_sorted=parks.sort_values('Acres', ascending=False)
parks_sorted

plt.figure(figsize=(20,20))
plt.barh(parks_sorted['Park Name'], parks_sorted['Acres'], color='#86bf91', height=0.85)
plt.ylabel("National Park", fontsize='14', fontweight='bold', rotation=45)
plt.xlabel("Thousands of Acres", fontsize='14', fontweight='bold')
plt.xticks(fontsize='10')
plt.yticks(fontsize='10')
plt.margins(y=0.01)
plt.title("The Acreage of National Parks in the United States", loc='left', fontsize='20', fontweight='bold')
plt.gcf().subplots_adjust(bottom=0.35, top=0.7)
plt.tight_layout()
plt.savefig("NPAcreagetotal.png", bbox_inches='tight', pad_inches=0.0)
plt.show()

park5 = parks.drop(['State', 'Park Code', 'Latitude', 'Longitude'], axis=1)
park5.info()
dfpark5 = park5
dfparkt5=dfpark5.sort_values(by=['Acres'], ascending=False).head(5)
dfparkb5=dfpark5.sort_values(by=['Acres'], ascending=False).tail(5)
dfmerge1=pd.concat([dfparkt5,dfparkb5])
dfmerge1

dfmerge1.plot.bar(x='Park Name',y='Acres', figsize=(20,20), legend=None, color='#86bf91')
plt.title('A Comparison of the 5 Largest and 5 Smallest National Parks by Acreage', loc='left', fontsize=20, fontweight='bold')
plt.gcf().subplots_adjust(bottom=0.35, top=0.7)
plt.subplots_adjust(bottom=0.5)
plt.xticks(rotation=45, fontsize='10', ha='right')
plt.yticks(fontsize='10')
plt.xlabel('National Park', fontsize='14', fontweight='bold')
plt.ylabel('Millions of Acres', labelpad=50, rotation=45, fontsize='14', fontweight='bold')
plt.tight_layout()
plt.savefig("5acres.png")
plt.show()

species2.head()
totalspecies=species2["Park Name"].value_counts(sort=True)
totalspecies

totalspecies.plot.barh(y='Park Name', figsize=(20,20), width=0.85, color='#9370db')
plt.title('Total Species Report Count from National Parks', loc='left', fontsize=20, fontweight='bold')
plt.subplots_adjust(left=0.3)
plt.xticks(fontsize='10')
plt.yticks(fontsize='10')
plt.xlabel('Number of Reports', labelpad=10, fontsize='14', fontweight='bold')
plt.ylabel('National Park', labelpad=50, rotation=45, fontsize='14', fontweight='bold')
plt.tight_layout()
plt.savefig("totalspeciescount.png")
plt.show()


species3 = species2.drop(['Species_ID','Category','Record_Status'], axis=1)
species3.info()

dfspeciest5 = species3.value_counts(['Park Name'], ascending=False).head(5)
dfspeciesb5 = species3.value_counts(['Park Name'], ascending=False).tail(5)
dfmerge2 = pd.concat([dfspeciest5,dfspeciesb5])
dfmerge2

dfmerge2.plot.bar(y='Park Name', figsize=(20,20), color='#9370db')
plt.title('A Comparison of the 10 National Parks with the Highest and Lowest Species Reports', loc='left', fontsize=20, fontweight='bold')
plt.gcf().subplots_adjust(bottom=0.35, top=0.7)
plt.subplots_adjust(left=0.8)
plt.xticks(fontsize='10', rotation=45, ha='right')
plt.yticks(fontsize='10')
plt.ylabel('National Park', labelpad=30, rotation=45, fontsize='14', fontweight='bold')
plt.xlabel('Count of Species Reports', fontsize='14', fontweight='bold')
plt.tight_layout()
plt.savefig("5speciescount")
plt.show()


count = species3.value_counts(['Park Name']).to_frame()
count.info()

ultimate = pd.merge(park5, count, on='Park Name')
ultimate.head()
ultimate.columns = ['Park Name', 'Acres', 'Reports']

ultimate.plot(kind="scatter", x='Acres', y='Reports', c='#039dfc', edgecolor='black', linewidth=0.5, figsize=(15,7))
plt.title('Relationship of National Park Acreage to Species Reports', loc='left', fontsize=13, fontweight='bold')
plt.gcf().subplots_adjust(bottom=0.35, top=0.7)
plt.subplots_adjust(left=0.8)
plt.xticks(fontsize='10')
plt.yticks(fontsize='10')
plt.xlabel('Millions of Acres', fontsize='10', fontweight='bold')
plt.ylabel('Thousands of Reports', labelpad=55, rotation=25, fontsize='10', fontweight='bold')
plt.tight_layout()
plt.savefig("scatter comparison")
plt.show()


parkstate= parks.drop(['Longitude', 'Latitude', 'Park Code'], axis=1)
conver = pd.merge(parkstate, count, on='Park Name')
conver.columns = ['Park Name', 'State', 'Acres', 'Reports']

conver.plot(kind='scatter', x='State', y='Acres', c='#86bf91', edgecolor='black', linewidth=0.5, figsize=(15,7))
plt.title('Relationship of National Park Acreage to the State location', loc='left', fontsize=20, fontweight='bold')
plt.xlabel('State', fontsize='14', fontweight='bold')
plt.xticks(rotation=45)
plt.ylabel('Millions of Acres', labelpad=40, rotation=65, fontweight='bold', fontsize='14')
plt.tight_layout()
plt.savefig("scatterstateacre.png", bbox_inches='tight')
plt.show()


conver.plot(kind='scatter', x='State', y='Reports', c='#9370db', edgecolor='black', linewidth=0.5, figsize=(15,7))
plt.title('Relationship of the number of Species Reports to the State location', loc='left', fontsize=20, fontweight='bold')
plt.xlabel('State', fontsize='14', fontweight='bold')
plt.xticks(rotation=45)
plt.ylabel('Thousands of Reports', labelpad=55, rotation=45, fontsize='14', fontweight='bold')
plt.tight_layout()
plt.savefig("scatterstatereport")
plt.show()

