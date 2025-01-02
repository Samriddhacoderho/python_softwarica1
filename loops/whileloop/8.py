import random as rs


user_ans='.'

while(user_ans!='exit'):
    a=rs.randint(1,30)
    b=rs.randint(1,30)
    res=int(input(("Enter result of two random numbers:")))
    if(res==a*b):
        print("Correct Answer")
    else:
        print("Incorrect Answer, Try Again")
        
    user_ans=input("Enter 'exit' to stop, or anything to continue:")
    if(user_ans==exit):
        break




