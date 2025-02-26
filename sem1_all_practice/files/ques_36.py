def fili():
    '''This function stores all characters except numbers from one file to another.'''
    with open("/Users/suhritsatyal/Desktop/python_softwarica1/sem1_all_practice/files/ques_36init.txt") as f:
        with open("/Users/suhritsatyal/Desktop/python_softwarica1/sem1_all_practice/files/ques_36fin.txt","w") as f2:
            for i in f.read():
                if (not(i.isnumeric())):
                    f2.write(i)

fili()

