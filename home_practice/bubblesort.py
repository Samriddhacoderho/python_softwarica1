a=[5,4,3,2,1]
for i in range(len(a)):  #01234 1
    for j in range(len(a)-i-1):  #01234 0123
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)
