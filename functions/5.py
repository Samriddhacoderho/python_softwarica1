# 4. write a program to display integer from of a list. given list=[1,"a","c",2,3,4]

def test(list):
    for i in list:
        i=str(i)
        if(i.isnumeric()):
            print(i)
        
test([1,'a','c',2,3,4])
