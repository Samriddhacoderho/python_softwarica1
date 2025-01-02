# 1. Create a Python program that prompts the user to enter their age. 
# If the age is less than 18, print "You are a minor." If the age is 
# between 18 and 60, print "You are an adult." For ages over 60, print 
# "You are a senior citizen." The program should continue until the user 
# inputs "stop."

user_ans='.'
while(user_ans!='stop'):
    user_age=int(input("Enter your age:"))
    if(user_age<18):
        print('Minor')
    elif(18<=user_age<=60):
        print('Adult')
    else:
        print("You are a senior citizen")
    user_ans=input('Enter "stop" to stop or anything to continue:')
    if(user_ans.lower()=='stop'):
        print("Thank you for using our service")
        break
