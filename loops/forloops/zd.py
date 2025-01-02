vowels=['a','e','i','o','u']
str="nepalaeiou"
print("After removing vowels:")
for i in str:
    if(i not in vowels):
        print(i,end="")