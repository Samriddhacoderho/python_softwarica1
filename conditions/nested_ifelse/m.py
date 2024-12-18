salary = float(input("Enter your salary: "))
years = int(input("Enter your years of service: "))

if years > 5:
    bonus = (5/100) * salary
else:
    bonus = 0

print("Your net bonus amount is:", bonus)
