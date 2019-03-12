# coding : utf-8
import re


fname='database.htm'
with open (fname) as obj:
    obj_r=obj.readlines()

pattern=re.compile('.*?<TD>([a-zA-z]+|([a-zA-z]+ )+[a-zA-z]+)</TD>.*?')
list=[]



with open('list.txt','w') as obj_t:
    for line in obj_r:
        col=pattern.match(line)
      #  for line in col:
        if col:
            if len(col.group(1))!=2:
                obj_t.write(col.group(1))
                obj_t.write('\n')

