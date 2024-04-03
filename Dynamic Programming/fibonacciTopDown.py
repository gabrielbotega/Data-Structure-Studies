# O(2^n)
counter = 0
def fib(n):
    global counter
    counter += 1
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)



#####  With memoization
# O(2n - 1) => O(n)
memo = [None] * 100
fibonacciCounter = 0 
def fibonacci(n):
    global fibonacciCounter
    fibonacciCounter += 1

    if memo[n] is not None:
        return memo[n]

    if n == 0 or n == 1:
        return n
    
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

n = 35

print(f'\nfib of {n} = {fib(n)}')
print(f'\nCounter of fib{n} = {counter}')



print(f'\nfibonacci of {n} = {fibonacci(n)}')
print(f'\nCounter of fibonacci{n} = {fibonacciCounter}')


