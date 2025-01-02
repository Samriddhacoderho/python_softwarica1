# 41. program to check given number is armstrong or not

num=input("Enter a number:")
a=len(num)
num=int(num)
b=num
r=0
s=0

while(b!=0):
    r=b%10
    s=s+(r**a)
    b=b//10

if(s==num):
    print("Armstrong number")
else:
    print("Not armstrong number")
