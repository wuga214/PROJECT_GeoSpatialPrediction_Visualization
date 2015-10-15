'''
Created on Sep 30, 2015

@author: Wuga
'''
import numpy as np
from sklearn.gaussian_process import GaussianProcess

# theta0 : double array_like, optional
# An array with shape (n_features, ) or (1, ). The parameters in the autocorrelation model. 
# If thetaL and thetaU are also specified, theta0 is considered as the starting point for 
# the maximum likelihood estimation of the best set of parameters. Default assumes isotropic 
# autocorrelation model with theta0 = 1e-1.

def gpregression(train_location,train_price,test_location):
    X = np.array(train_location)
    T = np.array(test_location)
    y = np.array(train_price)
    gp1 = GaussianProcess(theta0=1e50)
    gp1.fit(X, y)
    f1,MSE1 = gp1.predict(T,eval_MSE = True)
    return f1,MSE1

# x1=np.array([2.5,7])
# y1=np.cos(x1)
# t1=[2.6]
# f1,MSE1=gpregression(x1[:,None], y1, t1)
# print y1
# print f1
# print MSE1