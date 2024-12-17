temp=30
dict={
    "It's hot stay hydrated":temp>30,
    "Enjoy the weather":temp>=15 and temp<=30,
    "It's cold, wear warm clothes":temp<15
}
keys=list(dict.keys())
values=list(dict.values())
print(keys[values.index(1)])