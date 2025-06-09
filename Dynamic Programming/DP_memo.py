counter = 0
## Additional space this can be input verified
memo = [None] * 100

def fib(n):
    if memo[n] is not None:
        return memo[n]
    global counter
    counter +=1
    if n == 0 or n == 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

n = 35
print('\nFibonacci of', n, '=', fib(n))
print('\nCounter:', counter)