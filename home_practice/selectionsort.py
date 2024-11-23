a=[5,4,3,2,1]
for i in range(len(a)):  #01234
    for j in range(i,(len(a)-1)):  #0123
        if(a[i]>a[j+1]):
            temp=a[i]
            a[i]=a[j+1]
            a[j+1]=temp
print(a)