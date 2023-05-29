import math as mt
def isPrime(n):
    for i in range(2, int(mt.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
n = int(input())
for i in range(n + 1, n + 10000):
    if str(i) == str(i)[::-1] and isPrime(i):
        print(i)
        break