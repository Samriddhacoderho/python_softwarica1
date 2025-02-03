# 8.  given list is [1,2,3,4] but expected output in new list [2,3,4,5]

def test(list):
    newlist=[]
    for i in list:
        newlist.append(i+1)
    return newlist

print(test([1,2,3,4]))