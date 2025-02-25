def reverse(num):
    for i in range(len(num)-1,-1,-1):
        print(num[i],end="")

num=input("Enter an integer:")
reverse(num)