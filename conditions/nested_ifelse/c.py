print("Welcome to Treasure Land")
direction=input("Choose 'left' or 'right':")
if(direction!='left' and direction!='right'):
    print("Invalid choice")
else:
    if(direction=='right'):
        print("Game over")
    else:
        swimwait=input("Enter 'swim' or 'wait':")
        if(swimwait!='swim' and swimwait!='wait'):
            print("Invalid choice")
        else:
            if(swimwait=='swim'):
                print("Game over")
            else:
                color=input("Enter 'red' 'blue' or 'yellow':")
                if(color!='red' and color!='blue' and color!='yellow'):
                    print("Invalid choice")
                else:
                    if(color=='blue' or color=='red'):
                        print("Game over")
                    else:
                        print("You win")
