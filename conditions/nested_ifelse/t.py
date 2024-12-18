p = float(input("Enter your percentage: "))

if p < 40:
    print("Failed")
elif 40 <= p < 55:
    print("Fair")
elif 55 <= p < 65:
    print("Good")
else:
    print("Excellent")
