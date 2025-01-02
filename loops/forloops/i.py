# 5.Write a program to print the following using forloop
# a. first 10 even numbers
# b.first 10 odd numbers

print("Even numbers are:",end="")
for i in range(2,11,2):
    print(i,end=",")

print("\nOdd numbers are:",end="")
for i in range(1,10,2):
    print(i,end=",")