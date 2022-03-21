# Factorial iterative method
def factorial_iterative(number):
    factorial = 1
    for i in range(1,number+1):
        factorial *= i
    return factorial



print(factorial_iterative(int(input())))


# Factorial recursion method
def factorial_recursion(number):
    
    if number <= 1:
       return 1
    else:
        return  number*factorial_recursion(number-1)
        
print(factorial_recursion(int(input())))

