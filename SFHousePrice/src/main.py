'''
Created on 2015-10-1

@author: Wuga
'''

import DataOperation as DO
import Constants
import Classifiers
import DataPreprocess as DP

LOCATION=Constants.filelocations.GOOGLE_NOMINATIM_HOUSEPRICE
df=DO.readgeofile(LOCATION)
train,test,train_index,test_index=DO.dataseperator(df)

train=DP.elim(train)
train_latlong,train_price=Classifiers.cut_loca_price(train)
test_latlong,test_price=Classifiers.cut_loca_price(test)
f1=Classifiers.knnregression(train_latlong, train_price, test_latlong)
print f1
cost= Classifiers.mse_eval(f1, test_price)
print 'KNN: J(E)='+str(cost)
  
#The problem is caused by training data, it contains several data with same feature sets but different target value.
#We need a duplicate filter to eliminate such kind of data
f1,_=Classifiers.gpregression(train_latlong, train_price, test_latlong)
#print f1
cost= Classifiers.mse_eval(f1,test_price)
print 'GP: J(E)='+str(cost)