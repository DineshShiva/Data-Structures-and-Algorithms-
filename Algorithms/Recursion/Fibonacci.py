
def fibonacciIterative(number):
    lis = [0,1]
    if number < 2:
        return lis[-1]
    for i in range(2,number+1):
        lis.append(sum(lis[-2:]))
    return lis[-1]


print(fibonacciIterative(8))



def recursive_fibonacci(index):
    if index < 2:
        return index
    else:
      return  recursive_fibonacci(index-1) + recursive_fibonacci(index-2) #Every term in fib sequence = sum of previous two terms




print(recursive_fibonacci(8))
