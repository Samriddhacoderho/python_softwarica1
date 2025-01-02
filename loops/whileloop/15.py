# 9. Write a Python program that prompts the user to enter a number. 
# The program should determine whether the number is prime or not. 
# If the number is prime, print "The number is prime." Otherwise, print
#  "The number is not prime." Continue prompting the user until they enter "exit."

while(True):
    c=0
    user_ask=int(input("Enter a number:"))
    for i in range (2,int((user_ask/2)+1)):
        if(user_ask%i==0):
            c=1
            break
    if(c==1):
        print('Not a prime number')
    else:
        print('Prime number')
    
    user_ans=input("Enter 'exit' to stop or anything else to continue:")
    if(user_ans.lower()=='exit'):
        break
