n = int(input())
arr = list(map(int, input(). split()))
decimal = 0
val = 0
while n:
    decimal += arr[n - 1] * pow(2, val)
    val += 1
    n -= 1
print(decimal)