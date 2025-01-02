# 33. Write a for loop which appends the type of each element in the first list to the second list.

firstlist=['a','b',1,2,1.4,[1,2],(1,),'\n']
secondlist=[]

for i in firstlist:
    secondlist.append(type(i))

print(secondlist)
