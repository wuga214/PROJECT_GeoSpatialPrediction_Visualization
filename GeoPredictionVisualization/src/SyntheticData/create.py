'''
Created on Oct 21, 2015

@author: Wuga
'''
import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
import DataOperation as DO
import Constants

list=[2,1,2,2,1,2,9,9,9,9]

data_without_noise=[]
for x in range(len(list)):
    for y in range(len(list)):
        data_without_noise.append([list[x]*list[y],x,y])
print data_without_noise

data_with_noise=[]
for data in data_without_noise:
    for i in range(2):
        data_with_noise.append([data[0]+random.random()*10,data[1]+random.random(),data[2]+random.random()])
for data in data_without_noise:
    for i in range(2):
        data_with_noise.append([data[0]+random.random()*10,data[1]+random.random(),data[2]+random.random()])
print data_with_noise
print len(data_with_noise)

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