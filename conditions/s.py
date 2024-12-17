a=0
dict={
    "Winter":a==12 or a==1 or a==2,
    "Spring":a==3 or a==5 or a==6,
    "Summer":a==6 or a==7 or a==8,
    "Autumn":a==9 or a==10 or a==11
}
print(list(dict.keys())[list(dict.values()).index(1)]) if 1 in dict.values() else print("Error")