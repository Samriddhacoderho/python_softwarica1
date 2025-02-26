#11. Write a Python program to count the number of lines, words, and characters in a file.

def ok():
    with open("/Users/suhritsatyal/Desktop/python_softwarica1/sem1_all_practice/files/ques10.txt") as f:
        content=f.read()
        print("Characters=",len(content))
        f.seek(0)
        print("lines=",len(f.readlines()))
        f.seek(0)
        print("words=",len(content.split()))

ok()