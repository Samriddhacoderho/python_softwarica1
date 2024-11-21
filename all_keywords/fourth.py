stri="pYtHON"
print(stri.capitalize())
print(stri.upper())
print(stri.lower())
print(stri.count('O'))
print(stri.find('H'))
print(stri.replace('HELLO','JELLO'))
print(stri.split(" "))
print(len(stri.split(" ")))
print(stri.strip())
print(stri.swapcase())

stri2="Hello\"\" this is a escape test"  #if we want double quote as a string inside a double quoted string, use \ ani then enter the desired double quote. 
print(stri2)

stri3='python\bprogramming'  #\b bhanya backspace so euta backspace huncha ra n hatcha
print(stri3)
print('python\tprogramming')
print('python\tprogram'.expandtabs(tabsize=4))

a='python\rabc'
print(a)
a='pyt\rabcabc'
print(a)
print(r'Hello\nPython')
print('C:users\\python')
print(stri)
print(stri.center(6,"*"))  #

stri='python'
print(stri.ljust(2,"*"))

stri='pythonp'
b=stri.rfind('p')
print(b-len(stri))
