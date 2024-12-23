print("Welcome to the Underwater World")

choice1 = input("Do you want to 'dive deeper' or 'surface'? ").lower()

if choice1 == "dive deeper":
    choice2 = input("Do you want to 'search for pearls' or 'chase the fish'? ").lower()
    if choice2 == "search for pearls":
        print("You found a rare pearl. You Win!")
    elif choice2 == "chase the fish":
        print("You got lost underwater. Game Over.")
    else:
        print("Invalid choice.")
elif choice1 == "surface":
    print("You returned safely.")
else:
    print("Invalid choice.")
