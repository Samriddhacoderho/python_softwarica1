a=100
dict={
    a>=90 and a<=100:"A",
    a>=80 and a<89:"B",
    a<=70 and a>=0:"Fail"
}
if(True in dict):
    print(dict[True])
else:
    print("Invalid")