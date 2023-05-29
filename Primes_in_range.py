import math as mt
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(mt.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
low = int(input())
high = int(input())
count = 0
for j in range(low, high + 1):
    if isPrime(j):
        count += 1
print(count)