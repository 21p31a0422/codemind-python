def fib(n):
    f, s = 0, 1
    for i in range(n + 1):
        if f == n:
            return True
        tmp = f
        f = s
        s += tmp
    return False
if fib(int(input())):
    print(True)
else:
    print(False)