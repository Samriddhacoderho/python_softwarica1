list=[]
list.append(int(input("Enter first age:")))
list.append(int(input("Enter second age:")))
list.append(int(input("Enter third age:")))
list.append(int(input("Enter fourth age:")))

for i in range(1,len(list)):
    temp=list[i]
    j=i-1
    while(j>=0):
        if(list[j]>temp):
            list[j+1]=list[j]
            j-=1
        else:
            break

    list[j+1]=temp

print(f"Oldest age={list[len(list)-1]}")
