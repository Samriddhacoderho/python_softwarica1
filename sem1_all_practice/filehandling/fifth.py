import pickle

a={"name":"Samriddha","age":19}

with open ("/Users/suhritsatyal/Desktop/python_softwarica1/sem1_all_practice/filehandling/alltextfiles/fifth.txt","wb") as f:
    pickle.dump(a,f)

with open ("/Users/suhritsatyal/Desktop/python_softwarica1/sem1_all_practice/filehandling/alltextfiles/fifth.txt","rb") as f1:
    print(pickle.load(f1))


