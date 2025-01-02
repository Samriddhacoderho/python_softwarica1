# 43. python program to check a number is perfect number

a=496
sum=0
list=[]
for i in range(1,int((a/2)+1)):
    if(a%i==0):
        sum+=i
if(sum==a):
    print("perfect number")
else:
    print("Not a perfect number")
