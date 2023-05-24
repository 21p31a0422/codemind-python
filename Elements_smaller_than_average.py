n = int(input())
arr = list(map(int, input(). split()))
avg = sum(arr) // len(arr) 
c = 0 
for i in arr:
    if i <= avg:
        c += 1
print(c)