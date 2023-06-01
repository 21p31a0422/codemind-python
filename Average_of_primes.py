import math
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
a = int(input())
arr = list(map(int, input(). split()))
prime_lst = [i for i in arr if isPrime(i) == True]
print('{:.2f}'.format(sum(prime_lst) / len(prime_lst)))