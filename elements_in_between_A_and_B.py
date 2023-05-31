n = int(input())
arr = list(map(int, input(). split()))
a, b = map(int, input(). split())
elem = [i for i in arr if a <= i <= b]
print(*elem) if elem else print(-1)