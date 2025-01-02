# 4. Create a Python program that asks the user to guess the password.
#  The program should keep asking until the user enters "open sesame."
#  For each incorrect guess, print "Wrong password, try again." 
# When the correct password is entered, print "Access granted!"

while(True):
    passw=input("Enter password:")
    if(passw!='open sesame'):
        print('Wrong Password, Try Again')
    else:
        print('Access Granted')
        break