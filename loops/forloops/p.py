# 15. Sum : 1 to 10 (or any number) using for loop.

start=int(input("Enter start number:"))
end=int(input("Enter end number:"))

sum=0
for i in range(start,end+1):
    sum+=i

print(f"Sum of {start} to {end} is {sum}")
