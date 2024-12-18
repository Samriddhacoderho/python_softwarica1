age=int(input("Enter age:"))
gender=input("Enter gender(M/F):")
if((gender!='M' and gender!='F') or age<=0):
    print("Invalid gender or age")
else:
    dict={
        age>=18 and age<30 and gender=='M':700,
        age>=18 and age<30 and gender=='F':750,
        age>=30 and age<40 and gender=='M':800,
        age>=30 and age<40 and gender=='F':850
    }
    print("Wage is",dict[1])

