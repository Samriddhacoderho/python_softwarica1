age=4
dict={
    age<13 and age>=0:"Child",
    age>=13 and age<=19:"Teenager",
    age>19:"Adult"
}
if(1 in dict):
    print(dict[1])
else:
    print("Invalid age")