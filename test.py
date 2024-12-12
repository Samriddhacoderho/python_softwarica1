a=1,2,3
print(type(a))

a=1+2j
print(a.real,a.imag) #this works
a=2j
print(a.real,a.imag) #this works
a=2+j
print(a.real,a.imag) #this does not work

