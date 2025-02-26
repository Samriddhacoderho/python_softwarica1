# 19. Write a program for Armstrong number using for loop and while loop

def arms(num):
    '''This function returns whether a number is armstrong or not'''
    order=len(num) #3
    temp=num #153
    s=0
    for digit in range(len(temp)-1,-1,-1): #2 1 0
        s=s+(int(temp[digit])**order)
        s=int(s)
    if(s==int(num)):
        return "Armstrong Number"
    else:
        return "Not Armstrong NUmber"

print(arms("9474"))

