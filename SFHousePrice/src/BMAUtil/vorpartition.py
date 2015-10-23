'''
Created on Oct 14, 2015

@author: Wuga
'''
from scipy.spatial import Voronoi
import numpy as np
import Vorplots
import Constants
import DataOperation as DO
import DataPreprocess as DP

def partition(df,initial_var):
    
    Datalist=[]
    for i in df.index:
        Datalist.append([float(df['Latitude'][i]),float(df['Longitude'][i])] )
    points = np.array(Datalist)
    #print points
    vor = Voronoi(points)
    sigma=initial_var
    regions,vertices=Vorplots.voronoi_finite_polygons_2d(vor)
    bmamodel=[]
    for i in range(len(vor.points)):
        region_id=vor.point_region[i]
        node=[regions[i],df['Price'][i],sigma,i]
        bmamodel.append(node)
    return bmamodel,vertices,vor

# LOCATION=Constants.filelocations.GOOGLE_NOMINATIM_HOUSEPRICE
# df=DO.readgeofile(LOCATION)
# train,test,train_index,test_index=DO.dataseperator(df)
# train=DP.elim(train)
# train = train.reset_index(drop=True)
# bmamodel,_=partition(train)
# print bmamodel