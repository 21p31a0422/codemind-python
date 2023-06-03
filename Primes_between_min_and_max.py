import math
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
inp = int(input())
arr = list(map(int, input(). split()))
low, high, count = arr.index(min(arr)), arr.index(max(arr)), 0

for i in range(inp):
    if (low <= i <= high and isPrime(arr[i]) == True) or (high <= i <= low and isPrime(arr[i]) == True):
        count += 1
    
print(count)