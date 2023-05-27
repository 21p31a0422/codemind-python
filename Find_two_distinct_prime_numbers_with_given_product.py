def prime(n):
    if n == 1:
        return False
    for i in range(2, (n//2)+1):
        if n%i == 0:
            return False
    return True
n = int(input())
c = None
for i in range(2, n):
    if n % i == 0:
        if prime(n//i):
            c = [i, n//i]
            break
        break
if c != None:
    print(*c)
else:
    print(-1)