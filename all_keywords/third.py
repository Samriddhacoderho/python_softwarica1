#memory comparision

#int
firstNum=2
secondNum=2
print(f'Integer: {id(firstNum)} {id(secondNum)} {firstNum is secondNum}')

print("\n")

#string
firstNum='ram'
secondNum='ram'
print(f'String: {id(firstNum)} {id(secondNum)} {firstNum is secondNum}')

print("\n")

#float
firstNum=2.0
secondNum=2.0
print(f'Float:{id(firstNum)} {id(secondNum)} {firstNum is secondNum}')

print("\n")

#tuple
firstNum=(1,)
secondNum=(1,)
print(f'Tuple: {id(firstNum)} {id(secondNum)} {firstNum is secondNum}')

print("\n")

#set
firstNum={1,2,3}
secondNum={4,5,6}
print(f'Set:{id(firstNum)} {id(secondNum)} {firstNum is secondNum}')

print("\n")

#list
firstNum=[1,2,3]
secondNum=[4,5,6]
print(f'List: {id(firstNum)} {id(secondNum)} {firstNum is secondNum}')

print("\n")

#dictionary
firstNum={
    'a':12,
    'b':'Ram'
}
secondNum={
    'a':12,
    'b':'Ram'
}
print(f'Dictionary: {id(firstNum)} {id(secondNum)} {firstNum is secondNum}')






