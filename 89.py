# coding : utf-8

import numpy as np
import bz2 
import re
import random
from util import most_similar, create_co_matrix,ppmi
#fname='enwiki-20150112-400-r10-105752.txt'
fname='enwiki-20150112-400-r100-10576.txt'
obj_f=''
obj_l=[]
with open(fname,'r') as obj:
   # for line in obj:
    #    obj_t.append(line)
    obj_t=obj.readlines()
total1=len(obj_t)

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
    #cnt2+=1
   # if cnt2%(total2//100)==0:
   #     print('%.lf%% done'%(100*cnt2/total2))


#with open("82105762.txt",'w') as obj:
 #   obj.write(obj_f)
#for i in range(10):
#   print(obj_t[i])


#obj_1=[]
#with open("82105762.txt") as obj:
 #   obj_1=obj.readline()
#print (obj_1)
with open ('80list.txt') as lst:
    lst1=lst.readlines()
#    print (lst1)
pattern1=re.compile('^([a-zA-Z]+ )+[a-zA-Z]+\n$')
lst2=[]
for i in lst1:
    if pattern1.match(i):
       # print (pattern1.match(i).group())
        lst2.append(pattern1.match(i).group())

#print(lst2)
for i in lst2:
    j=re.sub(' ','_',i)
    j=re.sub('\n','',j)
    i=re.sub('\n','',i)
    
    print(j)
    obj_f=re.sub(i,j,obj_f)
#with open("enwiki-20150112-400-r10-1057522.txt",'w') as obj:
 #   obj.write(obj_f)

words=obj_f.split()
#print(words)
word_to_id={}
id_to_word={}


#from scipy.sparse import lil_matrix, csr_matrix
import scipy.sparse as sp
from sklearn.utils.extmath import randomized_svd


for word in words:
    if word not in word_to_id:
        new_id=len(word_to_id)
        word_to_id[word]=new_id
        id_to_word[new_id]=word

corpus=[word_to_id[w] for w in words]
#print(corpus)


def create_co_matrix(corpus,vocab_size):
    corpus_size=len(corpus)
    co_matrix=np.zeros((vocab_size,vocab_size),dtype=np.int32)

    for idx,word_id in enumerate(corpus):
        #j=random.randint(1,5)

        for i in range(1,10):
            left_idx=idx-i
            right_idx=idx+i

            if left_idx>=0:
                left_word_id=corpus[left_idx]
                co_matrix[word_id,left_word_id]+=1

            if right_idx<corpus_size:
                right_word_id=corpus[right_idx]
                co_matrix[word_id,right_word_id]+=1
        return co_matrix

    return co_matrix

def cos_similarity(x,y,eps=1e-6):
    nx=x/np.sqrt(np.sum(x**2)+eps)
    ny=y/np.sqrt(np.sum(x**2)+eps)
    return np.dot(nx,ny)

def ppmi(C,verbose=False,eps=1e-3):
    M=np.array(C,dtype=np.float32)
    N=np.sum(C)
    S=np.sum(C,axis=0)
    total=C.shape[0]*C.shape[1]
    cnt=0

    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
           # print(C[i,j])
            pmi=np.log2(C[i,j]*N/(S[j]*S[i]+eps))
            #print(pmi)
            #print(type(pmi))
            #if pmi>=0:
            M[i,j]=max(pmi,0)
            #else:
             #    M[i,j]=0

            if verbose:
                cnt += 1
                if cnt%(total//100)==0:
                    print ('%.lf%% done' % (100*cnt/total))
    return M

vocab_size=len(word_to_id)
C=create_co_matrix(corpus,vocab_size)
print(C)
W=ppmi(C)
print(W)

U,S,V=randomized_svd(W,n_components=300,n_iter=5,random_state=None)
#print(U)
#U=U[:,:10]
#S=S[:10,:10]
#S=S[:,:10]
#V=V[:10,:]
#np.set_printoptions(precision=3)
#print('covariance_matrix')

#print('-'*50)
#print(S)
#print('PPMI')
#print(W)
querys=['United_States','United States','U.S','U.S.','England',]
for query in querys:
    most_similar(query,word_to_id,id_to_word,U,top=10)
with open('82tokei.txt','w') as obj:
    #for i in range(0,C.shape[0]):
     #   for j in range(0,C.shape[1]):
#
 #           obj.write(str(C[i,j]))
  #      obj.write('\n')
   # obj.write('-'*50+'\n')
    #for i in range(0,W.shape[0]):
     #   for j in range(0,W.shape[1]):
#
 #           obj.write(str(W[i,j]))
  #      obj.write('\n')
   # obj.write('-'*50+'\n')
    for i in range(0,U.shape[0]):
        for j in range(0,U.shape[1]):

            obj.write(str(U[i,j]))
        obj.write('\n')



    
    

