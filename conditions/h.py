n=eval(input("Enter a number:"))
dict={
    n%3==0:"Fizz",
    n%5==0:"Buzz",
    n%3==0 and n%5==0:"FizzBuzz"
}
if(True in dict):
    print(dict[True])
else:
    print(n)
