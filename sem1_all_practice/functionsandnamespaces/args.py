# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum,args

# print(add(1,2,3,4,5,6,8,10))

def add(**kwargs):
    for i in kwargs.items():
        print(i)
    print(type(kwargs))

add(a=20,b=30)