# 24. given list is [1,2,3,4] but expected output is [1,8,27,64]

list=[1,2,3,4]
newlist=[]
for i in list:
    newlist.append(i**3)

print(newlist)