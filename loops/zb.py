# 40. program to check given number is palindrome or not

num=102
a=num
r=0
s=0
while(a!=0):
    r=a%10
    s=(s*10)+r
    a=a//10

if(s==num):
    print("Palindrome")
else:
    print("Not palindrome")