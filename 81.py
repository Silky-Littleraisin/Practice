import re
with open("82105762.txt") as obj:
    obj_1=obj.readline

with open ('80list.txt') as lst:
    lst1=lst.readlines()
#    print (lst1)
pattern1=re.compile('^([a-zA-Z]+ )+[a-zA-Z]+\n$')
for i in lst1:
    if pattern1.match(i):
        print (pattern1.match(i))

