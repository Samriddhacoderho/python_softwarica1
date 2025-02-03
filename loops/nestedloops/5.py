for i in range(7):
    for j in range(60):
        if(j==0 and (i==1 or i==2 or i==6)):
            print("?",end=" ")
        elif(j==1 or j==2) and (i==0 or i==3 or i==6):
            print("?",end=" ")
        elif(j==3 and (i==4 or i==5)):
            print("?",end=" ")
        elif(j==6 or j==10) and i!=0:
            print("?",end=" ")
        elif(j==7 or j==8 or j==9) and (i==0 or i==3 ):
            print("?",end=" ")
        elif(j==13 or j==17):
            print("?",end=" ")
        elif(j==14 or j==16) and i==1:
            print("?",end=" ")
        elif(j==15 and i==2):
            print("?",end=" ")
        elif(j==20):
            print("?",end=" ")
        elif j==21 and (i==0 or i==3):
            print("?",end=" ")
        elif j==22 and (i==0 or i==3 or i==4):
            print("?",end=" ")
        elif j==23 and (i==0 or i==3 or i==5):
            print("?",end=" ")
        elif(j==24 and (i==1 or i==2 or i==6)):
            print("?",end=" ")
        elif(27<=j<=31 and (i==0 or i==6)):
            print("?",end=" ")
        elif(j==29):
            print("?",end=" ")
        elif(j==34):
            print("?",end=" ")
        elif(35<=j<=37 and (i==0 or i==6)):
            print("?",end=" ")
        elif(j==38 and (i!=0 and i!=6)):
            print("?",end=" ")
        elif(j==41):
            print("?",end=" ")
        elif(42<=j<=44 and (i==0 or i==6)):
            print("?",end=" ")
        elif(j==45 and (i!=0 and i!=6)):
            print("?",end=" ")
        elif(j==48 or j==52):
            print("?",end=" ")
        elif(49<=j<=51 and i==3):
            print("?",end=" ")
        elif(j==55 or j==59) and i!=0:
            print("?",end=" ")
        elif(56<=j<=58) and (i==0 or i==3):
            print("?",end=" ")
        else:
            print(end="  ")
    print()
    


