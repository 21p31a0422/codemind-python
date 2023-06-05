def adding(n):
    tot = 0
    while n:
        tot += n % 10
        n //= 10
    return tot
    
    
n = int(input())
arr = list(map(int, input(). split()))
total = 0
for i in arr:
    total += adding(i)
    
print(total)