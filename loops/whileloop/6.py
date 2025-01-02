sum=0
user_input=1
while(user_input!=0):
    user_input=int(input("Enter your number:"))
    sum+=user_input
    if(user_input!=0):
        print('Press 0 to stop:\n')

print(sum)