def fib(n):
    if n in {0, 1}:
        return n
    return fib(n - 1) + fib(n - 2)
    
lst = [fib(n) for n in range(int(input()))]
print(*lst)