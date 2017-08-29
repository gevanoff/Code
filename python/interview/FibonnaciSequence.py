def fib_rec(n):
    #base case
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

# Cache
n = 10
cache = [None]*(n+1)
def fib_dyn(n):
    #Base Case
    if n == 0 or n == 1:
        return n
    #Check Cache
    if cache[n] != None:
        return cache[n]
    #Keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return cache[n]

