#7. Accept five names from the user and write in a file 'softwarica.txt' (each name should write in separate line)

with open("/Users/suhritsatyal/Desktop/python_softwarica1/sem1_all_practice/files/ques7.txt","w") as f:
    for i in range(5):
        name=input("Enter name:")
        f.write(name+"\n")
