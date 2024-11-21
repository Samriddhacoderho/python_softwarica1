a=50
b=a
a=500
print(id(a))
print(b)
print(f'Hello{a} I am {b}')
print("\n")
comp=1+2j
print(comp.real)  #gives the real part of the complex object in the form of float
print(comp.imag) #gives the imaginary part of the complex object in the form of float


a=50
b=50

# a ra b ko memory location same huncha. ra immutable data types(in this case: int) ma duita identifier(a and b) ma same value/object(50) halechi duitai identifier ko memory location same huncha. 
print(a is b) #since memory location is same, so this is true

c=[1,2,3]
d=[1,2,3]
#but in the case of mutable data types(such as list), the above statement is not true, and the memory location differs
print(c is d)  #since memory location is different, so this is false