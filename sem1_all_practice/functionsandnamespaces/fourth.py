#map

numbers=[1,2,3,4,5]
def squaring(x):
    return x**2

print(list(map(squaring,numbers)))

#filter

numbers=[1,2,5,10,12,15,22,20,25,31,40]

filtering=lambda x:x%10==0

print(list(filter(filtering,numbers)))

#reduce

from functools import reduce

numbers=[1,2,3,4,5]
print(reduce(lambda x,y:x*y,numbers))