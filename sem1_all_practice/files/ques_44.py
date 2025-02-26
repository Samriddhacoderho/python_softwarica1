# 44. 15.	A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased. The program should read three integers: the number of students in each of the three 


def min_desks_needed(class1, class2, class3):
    # Calculate desks required for each class (each desk seats 2 students)
    desks = (class1 + 1) // 2 + (class2 + 1) // 2 + (class3 + 1) // 2
    return desks

# Taking input from user
class1 = int(input("Enter number of students in class 1: "))
class2 = int(input("Enter number of students in class 2: "))
class3 = int(input("Enter number of students in class 3: "))

# Printing the result
print("Minimum desks required:", min_desks_needed(class1, class2, class3))
