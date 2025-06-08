counter = 0 

def fib(n):
    global counter
    counter+=1
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)


n = 30
print('\nFibonacci of', n, '=', fib(n))
print('\nCounter:', counter)