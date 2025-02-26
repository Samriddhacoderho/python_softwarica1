# 27. Python program to calculate the sum of all the odd numbers within the given
# range using while loop and for loop

def oddi(start,stop):
    sum=0
    for i in range(start,stop+1):
        if(i%2!=0):
            sum+=i
    return sum


print(oddi(1,5))