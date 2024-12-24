# 18. Write a program to print numbers from 1 to 100 that are divisible by 5.

a=[]
for i in range(1,101):
    if(i%5==0):
        a.append(i)
print("All numbers between 1 to 100 that are divisible by 5 are:",a)