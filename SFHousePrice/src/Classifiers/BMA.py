'''
Created on Oct 15, 2015

@author: Wuga
'''
import numpy as np
from scipy.spatial import Voronoi
import Vorplots
import Constants
import DataOperation as DO
import DataPreprocess as DP
import copy
import BMAUtil

def BMAfit(train):
    bmamodel,vertices,vor=BMAUtil.partition(train)
    ridge_points=vor.ridge_points
    print len(ridge_points)
    modellist=[]
    modellist.append(copy.deepcopy(bmamodel))
    bmamodel_old=bmamodel
    for i in range(len(ridge_points)):
        pairs_to_merge=[]
        min_difference=1e10
        for pairs in ridge_points:
            if float(bmamodel_old[pairs[0]][3])==float(bmamodel_old[pairs[1]][3]):
                continue
            temp=abs(float(bmamodel_old[pairs[0]][1])-float(bmamodel_old[pairs[1]][1]))
            if min_difference>temp:
                min_difference=temp
                pairs_to_merge=pairs
#       ridge_points=ridge_points.tolist()
#       ridge_points.remove(pairs_to_merge.tolist())
#       ridge_points=np.array(ridge_points)
        bmamodel_new=BMAUtil.merge(pairs_to_merge,bmamodel_old)
        modellist.append(copy.deepcopy(bmamodel_new))
        bmamodel_old=bmamodel_new
    
    print modellist[0]
    print modellist[1000]
    print len(ridge_points)