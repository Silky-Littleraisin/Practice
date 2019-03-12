import numpy as np
import matplotlib.pylab as plt
import sys,os
sys.path.append (os.pardir)
from common.functions import *
'''def mean_squared_error (y,t):
    return 0.5*np.sum((y-t)**2)'''

def step_functions(x):
    if x>0:
        return 1
    else:
        return 0

def step_function(x):
     y=x>0
     return y.astype(np.int)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def relu(x):
    return np.maximum(0,x)

a=np.array([1,2,3,4])

print (a,np.ndim(a),a.shape,a.shape[0])

