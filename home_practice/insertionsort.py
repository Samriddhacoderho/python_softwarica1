a=[3,10,5,6,8,1]
for i in range(1,len(a)):
    temp=a[i]
    j=i-1
    while(j>=0 and a[j]>temp):
        a[j+1]=a[j]
        j-=1
    a[j+1]=temp

print(a)
