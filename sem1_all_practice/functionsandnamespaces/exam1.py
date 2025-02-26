
#Appending in a list
# lst=[1,2,3,4,5]
# lst.append([6,7,8])
# print(lst)

#Extending in a list
# lst.extend('String')
# print(lst)

#Inserting in a list
# lst.insert(4,'Nice')
# print(lst)

#Removing and popping out an element in a list
# lst=['Apple','Mango','Guava','Papaya']
# lst.remove('Apple')
# lst.pop(0)
# print(lst)

# a=[1,2,3,4]
# print(a.pop(a[2]))
# a.clear()
# del a
# print(a)


# a=[1,2,3,4]
# b=a
# print(a is b)
# c=list.copy(a)
# print(a is c)


# a=1,2,3
# print(type(a))


# a={1,2,3}
# a.add("Hi")
# print(a)
# a.update({4,5,6})
# print(a)

# a={1,2,3}
# a.update('String')
# print(a)

# a={1,2,3,4}
# # a.remove(5)
# a.discard(5)
# print(a)
# print(a.pop())

# a={1,2,3,4}
# b={3,4,5,6,7,8}
# c=a.union(b)
# print(c)
# a.intersection_update(b)
# print(a)

# a={1,2,3,4}
# b={5,6,5,6}
# print(a.symmetric_difference(b))
# print(a.isdisjoint(b))



# a={
#     'name':'Sam',
#     'age':19,
#     'weight':61
# }

# a['color']='green'
# print(a)

# print(a.pop('name'))
# print(a.popitem())

# a={
#     'name':'Sam',
#     'age':19,
#     'weight':61
#     }

# print(a.get('askdn','Not found'))


a={
    'name':'Sam',
    'age':19,
    'weight':61
}

for i in a:
    print(i)

for i in a.keys():
    print(i)

for i in a.values():
    print(i)

for i,j in a.items():
    print(f'{i} ={j}')


