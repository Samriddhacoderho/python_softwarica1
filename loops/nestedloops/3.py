for i in range(6):
    for j in range(5):
        if(j==0 or j==4) and i!=0:
            print("*",end=" ")
        elif(j==1 or j==2 or j==3) and (i==0 or i==3):
            print("*",end=" ")
        else:
            print(end="  ")
    print()