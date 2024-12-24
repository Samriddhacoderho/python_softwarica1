# 19. Write a program to find the largest number in a list: [3, 7, 2, 8, 5].

list=[3,7,2,8,5]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if(list[i]>list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp

print("Largest number is:",list[-1])


