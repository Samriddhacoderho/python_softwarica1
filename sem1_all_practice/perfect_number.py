def perfect(num): #function definition
    '''This function checks if a given number is a perfect number or not.'''
    lst=[]
    half=int(num/2)
    for i in range(1,half+1):
        if(num%i==0):
            lst.append(i)
    sum=0
    for j in lst:
        sum+=j

    if(sum==num):
        print("Perfect number")
    else:
        print("Not perfect number")

perfect(28) #Output: Perfect Number
perfect(17) #Output: Not percet number

print(perfect.__doc__)