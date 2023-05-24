n = int(input())
arr = list(map(int, input(). split()))
a, b = map(int, input(). split())
lt, out = [], 0
for i in arr:
    if i < a or i > b:
        if out < i:
            out = i
if out == 0:
    print(-1)
else:
    print(out)