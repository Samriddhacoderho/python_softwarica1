def charge(days):
    '''This function calculates charge for library accordingly'''
    if(days<=5):
        charges=days*2
        return charges
    elif(6<=days<=10):
        charges=5*2+(days-5)*3
        return charges
    elif(11<=days<=15):
        charges=5*2+5*3+(days-10)*4
        return charges
    else:
        charges=5*2+5*3+5*4+(days-15)*5
        return charges

days=int(input("Enter days:"))
print(charge(days))
print(charge.__doc__)