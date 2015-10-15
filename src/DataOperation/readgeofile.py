'''
Created on 09-23-2015

@author: Wuga
'''
import pandas as pd
def readgeofile(LOCATION):
    df=pd.read_csv(LOCATION)
    #print df
    return df

# LOCATION='/Users/Wuga/Documents/DATA/SFREHPDATA/HousingSales2012PL_GOOGLE.csv'
# readgeofile(LOCATION)