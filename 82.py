import numpy as np 
import random 
#from scipy.sparse import lil_matrix, csr_matrix
import scipy.sparse as sp
with open('enwiki-20150112-400-r100-105762.txt','r') as obj:
    lines=obj.readlines()
   # print(lines)
    words=lines[0].split()
#print(words)
word_to_id={}
id_to_word={}

for word in words:
    if word not in word_to_id:
        new_id=len(word_to_id)
        word_to_id[word]=new_id
        id_to_word[new_id]=word

corpus=[word_to_id[w] for w in words]
#print(corpus)

'''def create_co_matrix(corpus,vocab_size,window_size=1):
    corpus_size=len(corpus)
    co_matrix=np.zeros((vocab_size,vocab_size),dtype=np.int32)

    for idx,word_id in enumerate(corpus):
        for i in range(1,windows_size=1):
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
'''
def create_co_matrix(corpus,vocab_size):
    corpus_size=len(corpus)
    co_matrix=sp.lil_matrix((vocab_size,vocab_size),dtype=np.int32)

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

def cos_similarity(x,y,eps=1e-8):
    nx=x/np.sqrt(np.sum(x**2)+eps)
    ny=y/np.sqrt(np.sum(x**2)+eps)
    return np.dot(nx,ny)
'''def ppmi(C,verbose=False,eps=1e-8):
    M=np.zeros_like(C,dtype=np.float32)
    N=np.sum(C)
    S=np.sum(C,axis=0)
    total=C.shape[0]*C.shape[1]
    cnt=0

    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            pmi=np.log2(C[i,j]*N/(S[j]*S[i])+eps)
            M[i,j]=max(0,pmi)

            if verbose:
                cnt += 1
                if cnt%(total//100)==0:
                    print ('%.lf%% done' % (100*cnt/total))
    return M
'''
def ppmi(C,verbose=False,eps=1e-8):
    M=sp.lil_matrix(C,dtype=np.float32)
    N=np.sum(C)
    S=np.sum(C,axis=0)
    total=C.shape[0]*C.shape[1]
    cnt=0

    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            pmi=np.log2(C[i,j]*N/(S[j]*S[i])+eps)
            M[i,j]=max(0,pmi)

            if verbose:
                cnt += 1
                if cnt%(total//100)==0:
                    print ('%.lf%% done' % (100*cnt/total))
    return M

vocab_size=len(word_to_id)
C=create_co_matrix(corpus,vocab_size)
W=ppmi(C,True)

U,S,V=np.linalg.svd(W)

#np.set_printoptions(precision=3)
print('covariance_matrix')
print(C)
print('-'*50)
print('PPMI')
print(W)
with open('82tokei.txt','w') as obj:
    for i in range(0,C.shape[0]):
        for j in range(0,C.shape[1]):

            obj.write(str(C[i,j]))
        obj.write('\n')
    obj.write('-'*50+'\n')
    for i in range(0,W.shape[0]):
        for j in range(0,W.shape[1]):

            obj.write(str(W[i,j]))
        obj.write('\n')
    obj.write('-'*50+'\n')
    for i in range(0,U.shape[0]):
        for j in range(0,U.shape[1]):

            obj.write(str(U[i,j]))
        obj.write('\n')


'''with open('82word_idx.txt','w') as obj:
    for idx,word in enumerate(words):

        i=random.randint(1,5)
        left_word=[]
        right_word=[]
        for j in range(0,i):
            left_idx=idx-j
            if left_idx>=0:
                left_word.append(id_to_word[corpus[left_idx]])
            
            right_idx=idx+j
            if right_idx < len(corpus):
                right_word.append(id_to_word[corpus[right_idx]])
        
        obj.write(word)
        obj.write(str(i))
        obj.write('\n')
        obj.write('(')
        for word in left_word:
            obj.write(word)
            obj.write('\t')
        obj.write(')')
        obj.write('\n')
        obj.write('[')
        for word in right_word:
            obj.write(word)
            obj.write('\t')
        obj.write(']')        
        obj.write('\n')
'''

    
    

