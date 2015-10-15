'''
Created on Sep 29, 2015

@author: Wuga
'''
import numpy as np
from scipy.spatial import Voronoi
import DataOperation as DO
import Constants
import Vorplots

def voronoiplot(df):
    Datalist=[]
    for i in df.index:
        #print i,[df['Latitude'][i],df['Longitude'][i]]
        Datalist.append([float(df['Latitude'][i]),float(df['Longitude'][i])] )
    points = np.array(Datalist)
    #print points
    vor = Voronoi(points)
    #voronoi_plot_2d(vor)
    region,vertices=Vorplots.voronoi_finite_polygons_2d(vor)
    print region
    geo_json,data_csv=DO.geojsonwrite(vor,region,vertices,df)
    print data_csv
    target = open(Constants.filelocations.VORONOI_GEOJSON, 'w')
    target.write(geo_json)
    target.close()
    data_csv.to_csv(Constants.filelocations.GEOJSON_CSV_DATA, header= True, index=False)
    return

# LOCATION='/Users/Wuga/Documents/DATA/SFREHPDATA/HousingSales2012PL_GOOGLE.csv'
# df=DO.readgeofile(LOCATION)
# train,test,train_index,test_index=DO.dataseperator(df)
# print [float(train['Latitude'][1]),float(train['Longitude'][1])] 
# voronoiplot(train)