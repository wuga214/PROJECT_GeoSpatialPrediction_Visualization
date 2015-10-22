'''
Created on Oct 15, 2015

@author: Wuga
'''
import numpy as np
import operator
import Constants
import DataOperation as DO
import DataPreprocess as DP
import vorpartition
import copy
import BMAUtil

def weight(models,vertices,validation):
    likelihoods=[]
    dataregionidlist=findpointregion(models[0], vertices, validation)
    print dataregionidlist          
    q=5     
    for model in models:
        likelihood=[]
        for i in range(len(dataregionidlist)):
            if q>0:
                print float(validation['Price'][i]),float(model[dataregionidlist[i]][1])
                q=q-1
            likelihood.append(loggaussian(float(validation['Price'][i]), float(model[dataregionidlist[i]][1]), model[dataregionidlist[i]][2]))        
        likelihoods.append(sum(likelihood))
    print 'likelihoods'
    print likelihoods[0]
    weights=sumdifference(likelihoods)
    return weights

def findpointregion(model,vertices,dataset):
    dataregion=[]
    datasetmatrix=dataset.as_matrix()
    for data in datasetmatrix.tolist():
        for i in range(len(model)):
            if(BMAUtil.point_in_poly(float(data[1]),float(data[2]),model[i][0],vertices)):
                dataregion.append(i);
                break;
    return dataregion

def sumdifference(likelihoods):
    weights=[]
    for likeli1 in likelihoods:
        weight=[]
        for likeli2 in likelihoods:
            weight.append(likeli2-likeli1)
        weights.append(1/np.sum(np.exp(weight)))
    return weights;
        
                 
def loggaussian(x, mu, sig_sqr):
    return -np.log(np.sqrt(2*3.14*sig_sqr))/2-np.power(x-mu,2)/(2*sig_sqr)

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

LOCATION=Constants.filelocations.GOOGLE_NOMINATIM_HOUSEPRICE
df=DO.readgeofile(LOCATION)
print 'File Reading'
train,test,train_index,test_index=DO.dataseperator(df)
train=DP.elim(train)
train = train.reset_index(drop=True)
bmamodel,vertices,vor=vorpartition.partition(train)
#######
# print [vor.vertices[x] for x in vor.regions[vor.point_region[10]]]
# print [vertices[x] for x in bmamodel[10][0]]
#######
print 'Initial model established'
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
    bmamodel_new=BMAUtil.merge(pairs_to_merge,bmamodel_old,modellist[0])
    modellist.append(copy.deepcopy(bmamodel_new))
    bmamodel_old=bmamodel_new
    ridge_points=ridge_points.tolist()
    ridge_points.remove(pairs_to_merge.tolist())
    ridge_points=np.array(ridge_points)
print modellist[0]
print modellist[-1]
print 'model list generated'
weights=weight(modellist,vertices,test[:1])
print weights
print sum(weights)