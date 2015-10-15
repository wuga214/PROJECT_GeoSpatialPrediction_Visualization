'''
Created on 09-23-2015

@author: Wuga
'''
import folium

import geocoder
import DataOperation as DO
import DataPreprocess as DP
import Vorplots as V
import Constants
import pandas as pd

g=geocoder.osm('San Francisco')
loca=g.latlng
print loca
LOCATION=Constants.filelocations.GOOGLE_NOMINATIM_HOUSEPRICE
df=DO.readgeofile(LOCATION)
train,test,train_index,test_index=DO.dataseperator(df)
map_osm = folium.Map(location=loca,tiles='Stamen Terrain', zoom_start=13, max_zoom=18)
for i in train_index:
    map_osm.circle_marker([df['Latitude'][i], df['Longitude'][i]], popup=df['Price'][i],radius=20,line_color='#AF5EFF', fill_color='#7F50AD')
for i in test_index:
    map_osm.circle_marker([df['Latitude'][i], df['Longitude'][i]], popup=df['Price'][i],radius=20,line_color='#962600', fill_color='#BA735B')
train=DP.elim(train)
train = train.reset_index(drop=True)
V.voronoiplot(DP.elim(train))
map_osm.geo_json(geo_path=r'autovoronoi.json', data_out='/Users/Wuga/Documents/DATA/SFREHPDATA/pricedata.json',data=pd.read_csv('/Users/Wuga/Documents/DATA/SFREHPDATA/pricedata.csv'),columns=['Id','Price'],key_on='feature.id', threshold_scale=[200000, 600000, 800000, 1000000, 12000000, 1500000], fill_color='YlOrRd', fill_opacity=0.1, line_opacity=0.2, legend_name='House Price 2012 SF')
map_osm.create_map(path=Constants.filelocations.MAP_HTML)