'''
Created on 09-23-2015

@author: Wuga
'''
import pandas as pd
def write(DF, LOCATION):
    DF.to_csv(LOCATION,header=False,index=False)
    print "Write File Complete"
    return