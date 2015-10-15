'''
Created on 09-25-2015

@author: Wuga
'''
import numpy as np
from scipy.spatial import Voronoi
import pandas as pd
def geojsonwrite(vor,regions,vertices,df):
    print df
    geo_json='{ "type": "FeatureCollection","features": ['
#    for x in vor.regions:
    feature_index=[]
    feature_value=[]
    for j in range(len(vor.points)):
        region_id=vor.point_region[j]
        feature_index.append('block'+str(j))
        feature_value.append(df['Price'][j])
        x=regions[region_id]
        if len(x) != 0 and -1 not in x:
            feature='{"type":"Feature","id":"block'+str(j)+'","properties":{"name":"block'+str(j)+'"},"geometry":{"type":"Polygon","coordinates":[['
            for i in range(len(x)):
                feature+= '['+repr(np.float(vertices[x[i]][1]))+','+repr(np.float(vertices[x[i]][0]))+'],'
            feature+= '['+repr(np.float(vertices[x[0]][1]))+','+repr(np.float(vertices[x[0]][0]))+']'
            feature+=']]}},'
            geo_json+=feature
    geo_json = geo_json[:-1]       
    geo_json+=']}'
    feature=zip(feature_index,feature_value)
    feature_csv=pd.DataFrame(feature,columns=['Id','Price'])
    return geo_json,feature_csv