stri="pYtHON"
print(stri.capitalize())
print(stri.upper())
print(stri.lower())
print(stri.count('O'))
print(stri.find('H'))
print(stri.replace('HELLO','JELLO'))
#print(stri.replace('He','Z'))  it gives Zllo such that stri='Hello'
print(stri.split(" "))
print(len(stri.split(" ")))
print(stri.strip())
print(stri.title())  #if stri=python programming, harek word ko first letter lai capitalize garcha. 
print(stri.swapcase())  #lower lai capital, and vice versa garcha

# Make trans method
a='python'
b=a.maketrans('p','z')
print(b) #This gives dictionary. {p ko ascii value: z ko ascii value}
print(a.translate(b))  #Now, this gives zython. 
#b=a.maketrans('py','z')  this gives error. so multiple letters lai single letter le replace garna milne is only possible for .replace() method.

#ASCII Value a-z=97-122
#A-Z: 65-90
# 0-9: 48-57

stri2="Hello\"\" this is a escape test"  #if we want double quote as a string inside a double quoted string, use \ ani then enter the desired double quote. 
print(stri2)

stri3='python\bprogramming'  #\b bhanya backspace so euta backspace huncha ra n hatcha
print(stri3)
print('python\tprogramming')
print('python\tprogram'.expandtabs(tabsize=4))


# tabsize ra \t ko sab code: use chat gpt to make it explain this below code snippet:
print("Python Programming")
print("Python\tProgramming") #gives me 2 spaces

print("Pythona\tProgramming")
print("Pythona Programming")

print("Pythonaa1234Programming")
print("Pythonaa\tProgramming")

print("Python1234Programming")
print("Python\tProgramming".expandtabs(tabsize=5))

# use chat gpt mathi ko code explain garna. USE PYTHON ONLINE COMPILER

a='python\rabc'
print(a)
a='pyt\rabcabc'
print(a)
print(r'Hello\nPython')
print('C:users\python')
print(stri)
print(stri.center(6,"*"))  #

stri='python'
print(stri.ljust(8,"*"))

stri='pythonp'
b=stri.rfind('p')
print(b-len(stri))
