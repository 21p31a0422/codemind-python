n = int(input())
arr = list(map(int, input(). split()))
a, b = map(int, input(). split())
total = 0
for i in arr:
    if a <= i <= b:
        total += i
print(total)
