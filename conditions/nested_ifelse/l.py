days=int(input("Enter number of days:"))
if(days<=0):
    print("Invalid error")
else:
    if(days<=5):
        charge=2*days
    elif(days>=6 and days<=10):
        charge=10+3*(days-5)
    elif(days>=11 and days<=15):
        charge=10+15+4*(days-10)
    else:
        charge=10+15+20+(days-15)*5

print("Your charge is {0}".format(charge))