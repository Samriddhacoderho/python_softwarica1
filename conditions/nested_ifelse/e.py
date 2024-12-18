#5. Check whether the user input number is even or odd and display it to user.
a=int(input("Enter a number:"))
bitmask=1<<0
if(bitmask & a==0):
    print("Number is even")
else:
    print("Number is odd")
