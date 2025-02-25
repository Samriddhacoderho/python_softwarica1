def largest():
    lst=[3,7,2,8,5]
    for i in range(0,len(lst)-1):
        if(lst[i]>lst[i+1]):
            large=lst[i]
    return large

print(f'The largest number is {largest()}')