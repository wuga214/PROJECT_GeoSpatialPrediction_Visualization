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
    for i in range(1000):
        bmamodel_new,ridge_points=BMAUtil.merge(ridge_points,bmamodel_old)
        modellist.append(copy.deepcopy(bmamodel_new))
        bmamodel_old=bmamodel_new
    
    print modellist[0]
    print modellist[1000]
    print len(ridge_points)