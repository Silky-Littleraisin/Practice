import numpy as np
import matplotlib.pylab as plt
import sys,os
sys.path.append (os.pardir)
from common.functions import *
from common.functions import numberical_gradient
from collections import OrderedDict

class TwoLayerNet:
     def __int__(self,input_size,hidden_size,output_size,weight_init_std=0.01):
        self.params={}
        self.params['W1']=weight_init_std*np.random.randn(input_size,hidden_size)
        self.params['b1']=np.zeros(hidden_size)
        self.params['W2']=weight_init_std*np.random.randn(hidden_size,output_size)
        self.params['b2']= np.zeros(output_size)

        self.layers=OrderedDict()
        self.layers['Affine1']=Affine(self.params['W1'],self.params['b1'])
        self.layers['ReLu']=Relu()
        self.layers['Affine2']=Affine(self.params['W2'],self.params['b2'])

        self.lastLayer=SoftmaxWithLoss()
     
     def predict(self,x):
         for layer in self.layers.values():
             x=layer,forward(x)
         return x

     def loss (self,x,t):
        y=self.predict(x)
        return self.lastLayer.forward()

     def  accuracy(self,x,t):
        y=self.predict(x)
        y=np.argmax(y,axis=1)
        if t.ndim!=1:t=np.argmax(t,axis=1)
        
        accuracy=np.sum(y==t)/flooat(x.shape[0])
        return accuracy

     def numberical_gradient(self,x,t):
        loss_W=lambda W: self.loss(x,t)

        grads={}
        grads['W1']=numberical_gradient(loss_W,self.paras['W1'])
        grads['b1']=numberical_gradient(loss_W,self.paras['b1'])


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

#a=np.array([1,2,3,4])

#print (a,np.ndim(a),a.shape,a.shape[0])

