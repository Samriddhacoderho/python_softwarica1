
age = int(input("Enter your age: "))

if age >= 18:
    degree = input("Do you have a degree? (yes/no): ").lower()
    if degree == 'yes':
        experience = int(input("Enter your work experience in years: "))
        if experience > 3:
            print("Highly Eligible")
        elif 1 <= experience <= 3:
            print("Eligible")
        else:
            print("Under Review")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
