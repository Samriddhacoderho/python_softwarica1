salary = float(input("Enter your salary: "))
years = int(input("Enter your years of service: "))

if years > 10:
    bonus = 0.10 * salary
elif 6 <= years <= 10:
    bonus = 0.08 * salary
else:
    bonus = 0.05 * salary

print("Your bonus is:", bonus)
