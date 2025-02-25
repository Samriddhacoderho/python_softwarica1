def login():
    '''This function validates a simple login system.'''
    
    def_un='admin'
    def_pass='1234'
    user_un=input("Enter username:")
    user_pass=input("Enter pass:")
    i=1
    while(i<=3):
        if(user_un==def_un and user_pass==def_pass):
            print("Login Successful")
            break
        else:
            i+=1
            if(i<=3):
                print("Incorrect, try again")
                user_un=input("Enter username:")
                user_pass=input("Enter pass:")
            else:
                print("Too many failed attempts")
                break

login()