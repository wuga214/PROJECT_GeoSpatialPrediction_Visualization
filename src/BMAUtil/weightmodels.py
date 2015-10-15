'''
Created on Oct 15, 2015

@author: Wuga
'''
import numpy as np
import operator
from scipy.spatial import Voronoi
import Vorplots
import Constants
import DataOperation as DO
import DataPreprocess as DP
import vorpartition
import copy
import BMAUtil

def weight(models):
    weights=[]
#     z=0
    for model in models:
        model_weight=[]
        for i in range(len(models[0])):
            model_weight.append(gaussian(float(models[0][i][1]), float(model[i][1]), float(model[i][2]))) 
#         if z<=2:
#             print model_weight;
#             z=z+1;            
        weights.append(prod(model_weight)) 
#     print weights
    partition_weights=sum(weights)
#     print partition_weights
    weights=[x/partition_weights for x in weights]
    return weights         
def gaussian(x, mu, sig_sqr):
    return np.exp(-np.power(x - mu, 2.) / (2*sig_sqr))
def prod(iterable):
    return reduce(operator.mul, iterable, 1)

LOCATION=Constants.filelocations.GOOGLE_NOMINATIM_HOUSEPRICE
df=DO.readgeofile(LOCATION)
train,test,train_index,test_index=DO.dataseperator(df)
train=DP.elim(train)
train = train.reset_index(drop=True)
bmamodel,vertices,vor=vorpartition.partition(train)
ridge_points=vor.ridge_points
print len(ridge_points)
modellist=[]
modellist.append(copy.deepcopy(bmamodel))
bmamodel_old=bmamodel
for i in range(1000):
    bmamodel_new,ridge_points=BMAUtil.merge(ridge_points,bmamodel_old)
    modellist.append(copy.deepcopy(bmamodel_new))
    bmamodel_old=bmamodel_new
print modellist[0]
print modellist[1000]
weights=weight(modellist)
print weights