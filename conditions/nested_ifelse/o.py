import math
a = int(input("Enter the number of students in the first class: "))
b = int(input("Enter the number of students in the second class: "))
c = int(input("Enter the number of students in the third class: "))
print(f"Smallest Total desks required={math.ceil(a/2)+math.ceil(b/2)+math.ceil(c/2)}")
