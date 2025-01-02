# 45. Write a program to determine whether a given number is a prime number.

num=23
for i in range(2,int(num/2+1)):
    if(num%i==0):
        print("Composite number")
        break
else:
    print("Prime number")