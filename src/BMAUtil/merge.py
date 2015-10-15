'''
Created on Oct 14, 2015

@author: Wuga
'''
import numpy as np
from scipy.spatial import Voronoi
import Vorplots
import Constants
import DataOperation as DO
import DataPreprocess as DP
import vorpartition
import copy

from numpy.oldnumeric.rng_stats import variance
def merge(ridge_points,previous_model):
    pairs_to_merge=[]
    min=1e10
    for pairs in ridge_points:
        temp=abs(float(previous_model[pairs[0]][1])-float(previous_model[pairs[1]][1]))
        if min>temp:
            min=temp
            pairs_to_merge=pairs
    ridge_points=ridge_points.tolist()
    ridge_points.remove(pairs_to_merge.tolist())
    ridge_points=np.array(ridge_points)
    new_mu=(float(previous_model[pairs_to_merge[0]][1])+float(previous_model[pairs_to_merge[1]][1]))/2
    if float(previous_model[pairs_to_merge[0]][1])!=float(previous_model[pairs_to_merge[1]][1]):
        new_sigma=np.var([float(previous_model[pairs_to_merge[0]][1]),float(previous_model[pairs_to_merge[1]][1])])
    else:
        new_sigma=float(previous_model[pairs_to_merge[0]][2])
    new_model=copy.deepcopy(previous_model)
    for node in new_model:
        if node[3]==new_model[pairs_to_merge[0]][3] or node[3]==new_model[pairs_to_merge[1]][3]:
            node[1]=new_mu
            node[2]=new_sigma
            node[3]= new_model[pairs_to_merge[0]][3]       
    return new_model,ridge_points

# def rotate(l,n):
#     return l[n:] + l[:n]
# 
# def region_merge(a,b,shared):
#     minia=min(a.index(shared[0]),a.index(shared[1]))
#     maxia=max(a.index(shared[0]),a.index(shared[1]))
#     if not (minia==0 and maxia!=1):
#         a=rotate(a,maxia)
#     minib=min(b.index(shared[0]),b.index(shared[1]))
#     maxib=max(b.index(shared[0]),b.index(shared[1]))
#     if not (minib==0 and maxib!=1):
#         b=rotate(b,maxib)
#     if a[0]==b[0]:
#         b=b[::-1]
#     new_region=a+b[1:]
#     new_region.pop()
#     return new_region
        
# print 1e10
# a = [1,2,3]
# b = [1,4,3]
# x= list(set(a) & set(b))
# print x
# x2=region_merge(a, b, x)
# print x2

# LOCATION=Constants.filelocations.GOOGLE_NOMINATIM_HOUSEPRICE
# df=DO.readgeofile(LOCATION)
# train,test,train_index,test_index=DO.dataseperator(df)
# train=DP.elim(train)
# train = train.reset_index(drop=True)
# bmamodel,vertices,vor=vorpartition.partition(train)
# ridge_points=vor.ridge_points
# print len(ridge_points)
# modellist=[]
# modellist.append(copy.deepcopy(bmamodel))
# bmamodel_old=bmamodel
# for i in range(1000):
#     bmamodel_new,ridge_points=merge(ridge_points,bmamodel_old)
#     modellist.append(copy.deepcopy(bmamodel_new))
#     bmamodel_old=bmamodel_new
# print modellist[0]
# print modellist[1000]
# print len(ridge_points)
