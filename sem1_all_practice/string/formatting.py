a='hi'
b='python'
c='bye'
print('{} {}'.format(a,b))
print('{1}{0}'.format(b,a))
# print('{}{1}'.format(a,b))  #gives error
# print('{a}{b}'.format(a,b))  #gives error
print('{a}{b}'.format(a='python',b='nice'))
print('{}{b}'.format(a,b='nice'))
print('{1}{b}{0}'.format(a,c,b='nice'))
print('{}{a}{}'.format(b,c,a='nice'))

# print(f'hello {}')  //error
print('hello {}{}{}'.format(10,20,30,a=40))
