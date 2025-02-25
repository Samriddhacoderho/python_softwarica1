with open ("/Users/suhritsatyal/Desktop/python_softwarica1/sem1_all_practice/filehandling/alltextfiles/second.txt","r") as f:
    f.tell()
    f.seek(4)
    print(f.tell())
    print(f.read(5))