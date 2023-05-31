n = int(input())
arr = list(map(int, input(). split()))
a, b = map(int, input(). split())
mini = 100000
for i in arr:
    if a <= i <= b and mini > i:
        mini = i
mini = mini if mini != 100000 else -1
print(mini)