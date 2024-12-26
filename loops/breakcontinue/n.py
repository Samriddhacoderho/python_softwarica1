# 13. Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types

list=[1,2,3,'d',4,5,'a']
intlist=[]
charlist=[]
for i in list:
    if(isinstance(i,int)):
        intlist.append(i)
    else:
        charlist.append(i)

print('Integer list:',intlist)
print('Character list:',charlist)