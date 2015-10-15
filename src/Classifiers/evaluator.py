'''
Created on Sep 30, 2015

@author: Wuga
'''
import operator
import numpy as np

#this function return average difference between predicted value with true_value
def mse_eval(predicted_value, true_value):
    #print 'evaluation function'
    #print predicted_value
    #print true_value
    difference= map(operator.sub, predicted_value, true_value)
    difference=[abs(x) for x in difference]
    #print np.sum(np.power(difference,2))
    #print len(predicted_value)
    cost=np.sum(np.power(difference,2))/len(predicted_value)
    return cost

def cut_loca_price(df):
    latitude=[float(x) for x in df['Latitude']]
    longitude=[float(x) for x in df['Longitude']]
    latlong=np.column_stack((latitude,longitude))
    price=np.array([float(y) for y in df['Price']])
    return latlong,price


    