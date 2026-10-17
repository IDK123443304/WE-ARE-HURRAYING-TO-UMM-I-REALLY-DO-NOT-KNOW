def factorial(x):
    '''
    This function calculates the factorial of a given number x using recursion.
    '''
    if x==0 or x==1:
        return 1
    else:
        return x * factorial(x-1)

num = int(input("Enter a number to calculate its factorial: "))
print("The factorial is:", factorial(num))
print(factorial.__doc__)