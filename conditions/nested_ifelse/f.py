marks=[]
total=0
marks.append(70)
marks.append(80)
marks.append(90)
marks.append(0)
for i in marks:
    total+=i

per=total/4
if(per>=70):
    print("Distinction")
elif(per>=60):
    print("First")
elif(per>=40):
    print("Second")
else:
    print("Fail")

print("Total Marks:",total)
print("Percentage:",per)

