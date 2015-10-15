'''
Created on 09-22-2015

@author: Wuga
'''
#>>> from geopy.geocoders import Nominatim
#>>> geolocator = Nominatim()
#>>> location = geolocator.geocode("175 5th Avenue NYC")
#>>> print(location.address)
#Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
#>>> print((location.latitude, location.longitude))
#(40.7410861, -73.9896297241625)
#>>> print(location.raw)
#{'place_id': '9167009604', 'type': 'attraction', ...}

from geopy.geocoders.osm import Nominatim
import DataOperation as DO
import pandas as pd
import Constants
import time
def osm_nominatim(DataLocation):
#    DataLocation = r'C:\Users\Wuga\Documents\DATASETS\SFREHPDATA\HousingSales2012.csv'
    geolocator=Nominatim()
    df=DO.readfile(DataLocation)
    print df
    df['Location'][:]=[x[0:x.find('#')] if x.find('#')!=-1 else x for x in df['Location']]
    print df
    complete=df['Location'][3]+" San Francisco"
    print complete
    longlat=geolocator.geocode(complete)
    print((longlat.latitude,longlat.longitude))
    transed=[]
    #transed=[geolocator.geocode(x+" San Francisco", timeout=None) for x in df['Location'][:5]]#need to sleep for a sec
    for x in df['Location'][:5]:
        transed.append(geolocator.geocode(x+" San Francisco", timeout=10))
        time.sleep(2)
    transed_la=[x.latitude if x is not None else 0 for x in transed]
    transed_lo=[x.longitude if x is not None else 0 for x in transed]
    cood_price=zip(df['Price'],transed_la,transed_lo)
    df_cood_price=pd.DataFrame(data=cood_price, columns=['Price','Latitude','Longitude'])
    df_cood_price.to_csv(Constants.filelocations.OSM_NOMINATIM_HOUSEPRICE, header= True, index=False)
    print df_cood_price
    return

    