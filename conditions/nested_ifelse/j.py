n = int(input("Enter your grade: "))

if n < 25:
    print("D")
elif 25 <= n < 45:
    print("C")
elif 45 <= n < 50:
    print("B")
elif 50 <= n < 60:
    print("B+")
elif 60 <= n <= 80:
    print("A")
else:
    print("A+")
