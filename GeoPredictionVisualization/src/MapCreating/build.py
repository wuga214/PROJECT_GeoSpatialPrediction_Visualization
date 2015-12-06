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

g=geocoder.osm('dublin,ireland')
loca=g.latlng
print loca
LOCATION=Constants.filelocations.DUBLIN_2010
df=DO.readgeofile(LOCATION)
train,test,train_index,test_index=DO.dataseperator(df)
map_osm = folium.Map(location=loca, zoom_start=9, max_zoom=18)
train=DP.elim(train)
train = train.reset_index(drop=True)
V.voronoiplot(DP.elim(train))
map_osm.geo_json(geo_path=r'autovoronoi.json', data_out='/Users/Wuga/Documents/DATA/SFREHPDATA/pricedata.json',data=pd.read_csv('/Users/Wuga/Documents/DATA/SFREHPDATA/pricedata.csv'),columns=['Id','Price'],key_on='feature.id', threshold_scale=[200000,250000,300000,350000,400000,500000], fill_color='YlOrRd', fill_opacity=0.5, line_opacity=0.5, legend_name='SF house price')
map_osm.create_map(path=Constants.filelocations.MAP_HTML)