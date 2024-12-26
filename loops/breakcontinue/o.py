# 15. Python program that accepts a string and calculate the number of digits and letters and space

str='samriddha  123   hello1 '
countdigit=0
countchar=0
countsp=0

for i in str:
    if(i.isdigit()):
        countdigit+=1
    elif(i.isalpha()):
        countchar+=1
    else:
        countsp+=1
    
print("Total digits:",countdigit)
print("Total alphabets:",countchar)
print("Total spaces:",countsp)