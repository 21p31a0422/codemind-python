n = int(input())
arr = list(map(int, input(). split()))
a, b = map(int, input(). split())
total = sum([i for i in arr if a <= i <= b])
print(total)