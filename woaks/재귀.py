def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
fib(5)

dic = {1:1, 2:1}
def fib_memoization(n):
    if n in dic:
        return dic[n]
    
    dic[n] = fib_memoization(n-1) + fib_memoization(n-2)
    return dic[n]
fib_memoization(38)

dic = {1:1, 2:1}
def fib_memoization(n):
    if n in dic:
        return dic[n]
    
    dic[n] = fib_memoization(n-1) + fib_memoization(n-2)
    return dic[n]
fib_memoization(5)

# fib(5)
# dic[5] = fib(4) + fib(3)

# fib(4)
# dic[4] = fib(3) + 1

# fib(3)
# dic[3] = 1 + 1