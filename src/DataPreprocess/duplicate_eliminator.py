'''
Created on Oct 1, 2015

@author: Wuga
'''
import Classifiers
import Constants
import DataOperation as DO
import numpy as np

def elim(df):
    #print df
    latlong,_=Classifiers.cut_loca_price(df)
    boolean=np.ones((len(latlong)), dtype=bool)
    boolean=np.invert(boolean)
    for i in range(len(latlong)):
        for j in range(i):
            if np.array_equal(latlong[i], latlong[j]):
                boolean[j]=True
    tokeep=np.where(np.invert(boolean))
    df=df.iloc[tokeep[0]]
    return df

# LOCATION=Constants.filelocations.GOOGLE_NOMINATIM_HOUSEPRICE
# df=DO.readgeofile(LOCATION)
# train,test,train_index,test_index=DO.dataseperator(df)
# print train['Latitude'][301],train['Longitude'][301]
# print train['Latitude'][577],train['Longitude'][577]
# redf=elim(train)
# print redf

    
    