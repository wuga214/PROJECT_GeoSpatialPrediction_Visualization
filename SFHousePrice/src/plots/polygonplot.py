'''
Created on Oct 21, 2015

@author: Wuga
'''
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def polygonplot(model,vertices):
    patches=[]
    fig, ax = plt.subplots()
    colors=[int(float(x[1])*100) for x in model]
    print colors
    for i in range(len(model)):
        poly_index=model[i][0]
        polyx=[vertices[z][0] for z in poly_index]
        polyy=[vertices[z][1] for z in poly_index]
        poly=zip(polyx,polyy)
        polygon = Polygon(poly)
        patches.append(polygon)
        #cmap=matplotlib.cm.jet
    p = PatchCollection(patches, cmap=matplotlib.cm.jet, match_original=True,alpha=0.4)
    p.set_array(np.array(colors))
    ax.add_collection(p)
    ax.set_xlim(-0.5,10.5)
    ax.set_ylim(-0.5,10.5)
    plt.colorbar(p)

    plt.show()