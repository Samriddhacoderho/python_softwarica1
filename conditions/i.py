char='b'
dict={
    'vowel':['a','e','i','o','u']
}
if(char in list(dict.values())[0]):
    print(list(dict.keys())[0])
else:
    print("Consonent")
    