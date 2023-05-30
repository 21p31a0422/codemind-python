n, val = int(input()), 0
arr = list(map(int, input(). split()))
low, high = map(int, input(). split())
for i in arr:
    if low <= i <= high and i > val:
        val = i
if val:
    print(val)
else:
    print(-1)