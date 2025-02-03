# 10. Given list is lst=[1,2,3,4] but print 1 2 and 4 only 

def test(list):
    for i in list:
        if(i!=3):
            print(i)

test([1,2,3,4])
