def apples(N,K): #function definition
    '''This function returns the number of apples each
    student gets and the remaining apples in
    basket'''
    each_student=K//N
    rem_apples=K%N
    return (each_student,rem_apples)

N=int(input("Enter no. of students:"))
K=int(input("Enter no. of apples:"))
e,r=apples(N,K) #function calling
print(f'Each student gets {e} apples and there are {r} apples remaining.')
print(apples.__doc__)

