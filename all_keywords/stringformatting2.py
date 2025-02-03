# print('{}{}{}'.format(10,11,a=12)) #this does not work
# print('{} {a} {}'.format(10,11,a=12)) #this works
# print('{a}{}{}'.format(a=12,10,11)) #this does not work
# print('{a}{0}{1}'.format(10,11,a=12)) #this works

a=11
b=12
print(f'{a}{b}') #this works
print(f'{0}{1}') #this works

