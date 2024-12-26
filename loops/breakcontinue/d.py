# 4. write a program to display integer from of a list. given list=[1,"a","c",2,3,4]

list=[1,'a','c',2,3,4]
for i in list:
    i=str(i)
    if(i.isalpha()):
        print(i)
