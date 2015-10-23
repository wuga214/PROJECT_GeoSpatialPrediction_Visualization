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
def merge(pairs_to_merge,previous_model,original_model,initial_var):
    new_mu=[]
    new_sigma=[]
    for i in range(len(previous_model)):
        if previous_model[i][3]==previous_model[pairs_to_merge[0]][3] or previous_model[i][3]==previous_model[pairs_to_merge[1]][3]:
            new_mu.append(float(original_model[i][1]))
            #new_mu=new_mu+1
            new_sigma.append(float(original_model[i][1]))
    new_mu=sum(new_mu)/len(new_mu)
    new_sigma=np.var(new_sigma)
    if(new_sigma==0):
        new_sigma=initial_var
    new_model=copy.deepcopy(previous_model)
    for node in new_model:
        if node[3]==new_model[pairs_to_merge[0]][3] or node[3]==new_model[pairs_to_merge[1]][3]:
            node[1]=new_mu
            node[2]=new_sigma
            node[3]= new_model[pairs_to_merge[0]][3]       
    return new_model


def giveMeModels(bmamodel,vertices,vor):
    ridge_points=vor.ridge_points
    print len(ridge_points)
    modellist=[]
    modellist.append(copy.deepcopy(bmamodel))
    bmamodel_old=bmamodel
    while len(ridge_points)!=0:
        pairs_to_merge=[]
        min_difference=1e10
        for pairs in ridge_points:
            if float(bmamodel_old[pairs[0]][3])==float(bmamodel_old[pairs[1]][3]):
                ridge_points=ridge_points.tolist()
                ridge_points.remove(pairs.tolist())
                ridge_points=np.array(ridge_points)            
                continue
            temp=abs(float(bmamodel_old[pairs[0]][1])-float(bmamodel_old[pairs[1]][1]))
            if min_difference>temp:
                min_difference=temp
                pairs_to_merge=pairs
        if len(ridge_points)==0:
            break
        bmamodel_new=merge(pairs_to_merge,bmamodel_old,modellist[0])
        modellist.append(copy.deepcopy(bmamodel_new))
        bmamodel_old=bmamodel_new
        ridge_points=ridge_points.tolist()
        ridge_points.remove(pairs_to_merge.tolist())
        ridge_points=np.array(ridge_points)
    return modellist
