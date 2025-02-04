# # a=1,2,3
# # print(type(a))

# # a=1+2j
# # print(a.real,a.imag) #this works
# # a=2j
# # print(a.real,a.imag) #this works
# # a=2+j
# # print(a.real,a.imag) #this does not work

# print("hi")

# def func_this(arr,tar,left,right):
#     while(left<=right):
#         mid=(left+right)//2
#         if(tar==arr[mid]):
#             return f"At {mid}"
#         elif(tar>arr[mid]):
#             left=mid+1
#             return func_this(arr,tar,left,right)
#         else:
#             right=mid-1
#             return func_this(arr,tar,left,right)
#     else:
#         return "The element is not present in the list"


# arr=[4,5,8,10,12,16]
# tar=4
# left=0
# right=len(arr)-1

# print(func_this(arr,tar,left,right))


print("hello","bad boy",sep=" ")
