# 6. Write a Python program that generates a random number 
# between 1 and 10 and prompts the user to guess the number. 
# The program should provide hints such as "guess higher" or 
# "guess lower" based on the user's input. Once the user guesses
# the correct number, the program should display the number of 
# attempts it took to guess the correct number.

from random import randint as r
attempts=1
num=r(1,20)
while(True):
    user_num=int(input("Enter your guess number:"))
    if(user_num==num):
        print("Attempts used:",attempts)
        break
    else:
        if(user_num<num):
            print("Incorrect number:Guess higher")
            attempts+=1
        else:
            print("Incorrect number:Guess lower")
            attempts+=1