# coding : utf-8

import numpy as np
obj_t=[]
with bz2.open("enwiki-20150112-400-r10-105752.txt",'r') as obj:
    for line in obj:
        obj_t.append(line)
        
for i in range(10):
    print(obj_t[i])
