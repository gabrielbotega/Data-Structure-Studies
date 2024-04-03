def factorial(num):
    if num == 1 or num == 0:
        return 1
    
    n = num * factorial(num-1)
    
    return n


print(factorial(4))
    