import re

with open("corpus_80.txt") as obj:
    obj_1=obj.readline()

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
    obj_1=re.sub(i,j,obj_1)
with open("corpus2_80.txt",'w') as obj:
    obj.write(obj_1)