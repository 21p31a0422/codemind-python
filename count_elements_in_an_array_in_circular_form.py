n = int(input())
arr = list(map(int, input(). split()))
arr, count = arr + arr[:2], 0
for i in range(n):
    if arr[i] % 2 != arr[i + 2] % 2:
        count += 1 
print(count)