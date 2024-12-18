#tkinter and sqlite3

balance=5000
print("Welcome to the ATM")
list=[1,2,3,4]
print("1:Balance inquiry")
print("2:Withdraw cash")
print("3:Deposit cash")
print("4:Exit")

user_choice=eval(input("Enter your choice(1-4):)"))
if(user_choice not in list):
    print("Invalid choice")
else:
    if(user_choice==1):
        print(f"Your current balance is {balance}")
    elif(user_choice==2):
        withdraw_amount=int(input("Enter your withdraw_amount:"))
        if(withdraw_amount>balance):
            print("Insufficient Balance")
        else:
            balance-=withdraw_amount
            print(f"Withdrawn Successfully. New Balance={balance}")
    elif(user_choice==3):
        deposit_amount=int(input("Enter your deposit amount:"))
        if(deposit_amount<=0):
            print("Invalid amount.")
        else:
            balance+=deposit_amount
            print(f"Deposited successfully. New balance is {balance}")
    else:
        print("Thank you for choosing our service. Bye!")
        