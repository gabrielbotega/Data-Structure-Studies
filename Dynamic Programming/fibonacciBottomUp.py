# Big O: O(n-1) => O(n)

"""
This is quite efficient, however if I want to run this code n times, it'll consume O(n) n times.
Therefore, it might be useful to use Memoization in this case as well. Therefore, if I want to run this one more time, I'll have O(1).
The down side about memoization is the memory usage. Therefore, you need to think about what is good for you, what is the most costly.
"""

counter = 0

def fib(n):
    fibList = [0, 1]
    global counter
    for index in range(2, n+1):
        counter += 1
        nextFib = fibList[index - 1] + fibList[index - 2]
        fibList.append(nextFib)
    return fibList[n]


n = 35

print(f'\nfib of {n} = {fib(n)}')
print(f'\nCounter of fib{n} = {counter}')
