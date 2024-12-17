
# a=eval(input("Enter your marks:"))
# if(a>80):
#     print("A")
# elif(a>60 and a<=80):
#     print("B")
# elif(a>50 and a<=60):
#     print("C")
# elif(a>45 and a<=50):
#     print("D")
# elif(a>25 and a<=45):
#     print("E")
# else:
#     print("F")

a=45
dict={
    "A":a>80 and a<=100,
    "B":a>60 and a<=80,
    "C":a>50 and a<=60,
    "D": a>45 and a<=50,
    "E":a>25 and a<=45,
    "F":a<=25 and a>=0
}
keys=list(dict.keys())
values=list(dict.values())
print(keys[values.index(True)])






