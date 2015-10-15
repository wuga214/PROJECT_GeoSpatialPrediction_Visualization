'''
Created on Sep 30, 2015

@author: Wuga
'''
print(__doc__)
import numpy as np
from sklearn import neighbors

def knnregression(train_location,train_price,test_location):
    X = np.array(train_location)
    T = np.array(test_location)
    y = np.array(train_price)
    n_neighbors = 1
    weights ='distance'
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    knn.fit(X, y)
    f1=knn.predict(T)
    return f1

# x1=np.array([2.5,7])
# y1=np.cos(x1)
# t1=np.array([2.6,1])
# print x1[:,None]
# x1=np.array([[2.5,2],[7,1]])
# print x1
# f1=knnregression(x1, y1, t1)
# print y1
# print f1