user_choice=input("Choose veg or non veg:")
if(user_choice.lower()=="veg"):
    user_vegchoice=input("Choose salad or pasta:")
    if(user_vegchoice.lower()=="salad"):
        print("Chosen Salad")
    else:
        print("Chosen Pasta")
else:
    user_nonvegchoice=input("Choose fish or chicken:")
    if(user_nonvegchoice.lower()=="fish"):
        print("Chosen FIsh")
    else:
        print("Chosen chicken")