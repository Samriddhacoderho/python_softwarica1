def repeating():
    i=1
    while(True):
        name=input("Enter name:")
        while(True):
            print(f'You entered {name} {i} times')
            if(i==3):
                break
            rep=input('Enter name again:')
            if(rep!=name):
                break
            else:
                i+=1
            
        if(i==3):
            break
    print(f'You entered {name} three times')

repeating()