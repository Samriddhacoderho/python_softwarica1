print("Welcome to the Space Adventure")

choice1 = input("Do you want to 'land on Mars' or 'fly to Jupiter'? ").lower()

if choice1 == "land on mars":
    choice2 = input("Do you want to 'explore' or 'build a base'? ").lower()
    if choice2 == "explore":
        print("You found alien artifacts. You Win!")
    elif choice2 == "build a base":
        print("You ran out of resources. Game Over.")
    else:
        print("Invalid choice.")
elif choice1 == "fly to jupiter":
    print("Your spaceship crashed. Game Over.")
else:
    print("Invalid choice.")
