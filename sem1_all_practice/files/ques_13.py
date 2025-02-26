# 13. Write a function display() in python to read 
# lines from a text file “softwarica.txt”, and display those words, which are less than 4 characters.

def display():
    '''This function displays those words from a file which are less than 4 characters'''
    with open("/Users/suhritsatyal/Desktop/python_softwarica1/sem1_all_practice/files/ques_12.txt") as f:
        lst=f.read().split()
        for i in lst:
            if(len(i)<4):
                print(i)

display()
print(display.__doc__)