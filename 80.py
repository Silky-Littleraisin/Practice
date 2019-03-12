# coding : utf-8

import numpy as np
import bz2 
import re
fname='8210576.txt'
obj_f=''
obj_l=[]
with open(fname,'r') as obj:
   # for line in obj:
    #    obj_t.append(line)
    obj_t=obj.readlines()
total1=len(obj_t)

#print (obj_t)
#print(type(obj_t))
#pattern=re.compile('^(.|,|\!|\?|\;|\:|\(|\)|\[|\]|\'|\")|(.|,|\!|\?|\;|\:|\(|\)|\[|\]|\'|\")$')
pattern=re.compile('(^\W)|(\W$)')

for i,line in enumerate(obj_t):
    #obj_t.append(line.split()) 
    #obj_t.remove(line)
    a=line.split(" ")
 #   print(a)
    obj_l.append(a)
    print(i)
total2=len(obj_l)
cnt2=0
#print (obj_t)
for lst in obj_l:
    for item in lst:
        b=pattern.sub('',item)
       # item.replace('.','')
       # item.replace(',','')
      #  item.replace('!','')
       # item.replace('?','')
      #  item.replace(';','')
       # item.replace(':','')
        #item.replace('(','')
        #item.replace(')','')
      #  item.replace('[','')
       # item.replace(']','')
        #item.replace('\'','')
       # item.replace('\"','')

        if b !='':
            obj_f=obj_f+' '+b
    cnt2+=1
    if cnt2%(total2//100)==0:
        print('%.lf%% done'%(100*cnt2/total2))


with open("82105762.txt",'w') as obj:
    obj.write(obj_f)
#for i in range(10):
#   print(obj_t[i])
