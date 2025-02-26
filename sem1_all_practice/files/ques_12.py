# 12. Write a function in python to count the number of lines from a text  file "story.txt"   which is not starting with an alphabet "T".

def func_this():
    with open("/Users/suhritsatyal/Desktop/python_softwarica1/sem1_all_practice/files/ques_12.txt") as f:
        count=0
        for i in f.readlines():
            if(i[0]!='T' and i[0]!='t'):
                count+=1
    print(count)


func_this()