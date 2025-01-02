for i in range(7):
    for j in range(4):
        if(j==0 and (i!=0 and i!=6)):
            print("*",end=" ")
        elif(j==1 and (i==0 or i==6)):
            print("*",end=" ")
        elif(j==2 and (i==0 or i==4 or i==6)):
            print("*",end=" ")
        elif(j==3 and (i==0 or i==4 or i==5 or i==6)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()