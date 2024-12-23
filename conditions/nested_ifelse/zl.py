print("Welcome to the Jungle Survival Challenge")

choice1 = input("Do you want to search for food or build a shelter? ").lower()

if choice1 == "search for food":
    choice2 = input("Do you want to hunt or gather? ").lower()
    if choice2 == "hunt":
        print("You were attacked by a wild animal. Game Over.")
    elif choice2 == "gather":
        print("You found enough food. You Win!")
    else:
        print("Invalid choice.")
elif choice1 == "build a shelter":
    print("You are safe for now. Keep going!")
else:
    print("Invalid choice.")
