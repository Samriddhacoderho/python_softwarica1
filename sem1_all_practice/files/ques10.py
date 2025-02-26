#10. Write a Python program to copy the contents of one file to another.

f=open("/Users/suhritsatyal/Desktop/python_softwarica1/sem1_all_practice/files/ques7.txt","r")
f2=open("/Users/suhritsatyal/Desktop/python_softwarica1/sem1_all_practice/files/ques10.txt","w")
f2.write(f.read())
f.close()
f2.close()