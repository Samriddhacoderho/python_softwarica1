for i in range(6):
    for j in range(17):
        if(j==0 or j==4) and (i!=0):
            print("*",end=" ")
        elif(j==1 or j==2 or j==3) and (i==0 or i==3):
            print("*",end=" ")
        elif(j==7):
            print("*",end=" ")
        elif(j==8 or j==9) and (i==0 or i==3 or i==5):
            print("*",end=" ")
        elif(j==10) and (i!=0 and i!=6):
            print("*",end=" ")
        elif(j==13) and (i!=0 and i!=5):
            print("*",end=" ")
        elif(j==14 or j==15 or j==16) and (i==0 or i==5):
            print("*",end=" ")
        else:
            print(end="  ")
    print()