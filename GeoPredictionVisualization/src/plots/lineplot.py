'''
Created on Oct 21, 2015

@author: Wuga
'''
import matplotlib.pyplot as plt
def lineplot(model_id,model_weight):
    plt.plot(model_id,model_weight)
    plt.yscale('log')
    plt.xlabel('model id')
    plt.ylabel('model weight')
    plt.show()