import re

fname='questions-words.txt'
with open(fname) as file:
    f=file.readlines()
a=''
for line in f:
    a+=line 
pattern=re.compile(': family\n(.*?\n)*?:')

result=re.search(pattern,a)

with open('91_output.txt','w') as file:
    for line in f:
        file.write(line)