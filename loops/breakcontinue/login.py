def_userName='samriddha'
def_userPass='samriddha1234'

for i in range(2,-1,-1):
    user_askName=input("Enter username:")
    user_askPass=input("Enter password:")
    if(len(user_askName)==0 or len(user_askPass)<=8):
        print('Empty username or password')
        print('Attempts left:',i)
    else:
        if(user_askName!=def_userName or user_askPass!=def_userPass):
            print("Incorrect username or password")
            print('Attempts left:',i)
        else:
            print('Logged in succesfully')
            break
        if(i==0):
            print('You are blocked')
            break