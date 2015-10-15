'''
Created on 09-22-2015

@author: Wuga
'''
import geocoder
import DataOperation as DO
import pandas as pd
import numpy as np
import time
import Constants

def google_nominatim(DataLocation):
    df=DO.readfile(DataLocation)
    print df
    geolocator=geocoder.google('110 OTTER COVE TERRACE San Francisco')
    geolocator.latlng
    print geolocator.latlng
    transed=[]
    for x in df['Location']:
        transed.append(geocoder.google(x+" San Francisco", timeout=10).latlng)
        time.sleep(2)
    print transed
    nptransed=np.array(transed)
    transed_la = nptransed[:,0]
    transed_lo = nptransed[:,1]
    cood_price=zip(df['Price'],transed_la,transed_lo)
    df_cood_price=pd.DataFrame(data=cood_price, columns=['Price','Latitude','Longitude'])
    df_cood_price.to_csv(Constants.filelocations.GOOGLE_NOMINATIM_HOUSEPRICE, header= True, index=False)
    return

DataLocation = Constants.filelocations.ORIGINIAL_HOUSEPRICE
google_nominatim(DataLocation)