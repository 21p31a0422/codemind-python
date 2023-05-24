n = int(input())
arr = list(map(int, input(). split()))
c = 0
avg = sum(arr) // len(arr)
for i in arr:
    if i >= avg:
        c += 1
print(c)