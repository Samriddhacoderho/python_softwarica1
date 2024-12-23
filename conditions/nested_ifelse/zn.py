print("Welcome to the Haunted Castle")

choice1 = input("Do you want to 'enter the castle' or 'run away'? ").lower()

if choice1 == "enter the castle":
    door = input("Choose a door: 'red', 'green', or 'black': ").lower()
    if door == "red":
        print("You entered a room full of flames. Game Over.")
    elif door == "green":
        print("You found the treasure. You Win!")
    elif door == "black":
        print("You were captured by ghosts. Game Over.")
    else:
        print("Invalid choice.")
elif choice1 == "run away":
    print("You escaped safely.")
else:
    print("Invalid choice.")
