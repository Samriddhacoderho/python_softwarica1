# 6. multiplication table of a given number

def test(num):
    for i in range(1,11):
        print(f'{num}X{i}={num*i}')
    
a=int(input("Enter a number:"))
test(a)
