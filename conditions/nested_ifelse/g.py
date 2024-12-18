a=eval(input("Enter bike price:"))
dict={
    a>100000:15,
    a>50000 and a<=100000:10,
    a<=50000 and a>=0:5
}
if(True in dict):
    print("Tax to be payed: {}%".format(dict[True]))
    print(f"Taxable Amount:{(dict[True]/100)*a}")
else:
    print("Invalid Error")