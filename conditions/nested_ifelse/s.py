days=int(input("Enter total number of working days:"))
absent=int(input("Enter total number of absent days:"))
per=((days-absent)/days)*100
if(per<75):
    print("Not eligible to sit for exam")
else:
    print("Eligible to sit for exam")