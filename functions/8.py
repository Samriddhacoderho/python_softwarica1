# 7. reverse a list

def test(list):
    reversed=[]
    for i in range(len(list)-1,-1,-1):
        reversed.append(list[i])
    return reversed

print(test([1,2,3,4,5]))
