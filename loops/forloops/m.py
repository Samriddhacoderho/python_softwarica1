# 9. Write a program that prompts the user to input an integer and then outputs the number 
# with the digits reversed. For example, if the input is 12345, the output should be 54321.


#easy method
# a=input("Enter a number:")
# print("In reversed order:",end="")
# for i in range(len(a)-1,-1,-1):
#     print(a[i],end="")

#hard method
a=int(input("Enter a number:"))
n=a
s=0
while(n!=0):
    r=n%10
    s=(s*10)+r
    n=n//10

print("In Reversed order:",s)