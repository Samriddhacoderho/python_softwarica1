# 7. Accept five names from the user and write in a file 'softwarica.txt' (each name should write in separate line)?

list_this=[]
for i in range(5):
    list_this.append(input("Enter name"))

with open ("/Users/suhritsatyal/Desktop/python_softwarica1/sem1_all_practice/filehandling/alltextfiles/prac7.txt","w") as f:
    for i in range(5):
        f.write(list_this[i]+"\n")

