def_un='satyal'
def_pw='123s'

user_un=input("Enter your username:")
user_pw=input("Enter your password:")

attempts=2
while(attempts!=0):
    if(user_un==def_un and user_pw==def_pw):
        print("Logged in successfully")
        break
    else:
        print("Attempts left:",attempts)
        attempts-=1
    if(attempts==0):
        print("You are blocked")