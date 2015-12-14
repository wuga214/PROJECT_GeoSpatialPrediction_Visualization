'''
Created on 12-12-2015

@author: Wuga
'''
import numpy as np
import random
import pandas as pd
import DataOperation as DO
import Constants
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def Euclidean(Point1,Point2):
    return np.linalg.norm(np.array(Point1)-np.array(Point2))
def InCirclue(position,mu,radius):
    return Euclidean(position, mu)<radius

data_with_noise=[]
for i in range(400):
    position=[random.random()*10,random.random()*10]
    mu1=[3,3]
    mu2=[7,7]
    radius1=5
    radius2=3.5
    if (InCirclue(position, mu1, radius1) and (not InCirclue(position, mu1, radius2))) or (InCirclue(position, mu2, radius1) and (not InCirclue(position, mu2, radius2))):
        data_with_noise.append([7+random.random()/2,position[0],position[1]])
    else:
        data_with_noise.append([6+random.random()/2,position[0],position[1]])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
colors = np.abs(np.array(data_with_noise)[:,0])
data=np.array(data_with_noise)
print colors
#for idx,data in enumerate(data_with_noise):
#    ax.scatter(data[1], data[2],data[0],c=colors[idx]*20)
ax.plot_trisurf(data[:,1],data[:,2],data[:,0],cmap=cm.jet, linewidth=0.2)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
for i in range(len(data_with_noise)):
    data_with_noise[i][0]='$'+str(data_with_noise[i][0])
df=pd.DataFrame(data_with_noise,columns=['Price','Latitude','Longitude'])
print df
DO.write(df,'../../sysnthetic.csv')

        
    
