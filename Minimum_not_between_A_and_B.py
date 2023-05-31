n = int(input())
arr = list(map(int, input(). split()))
a, b = map(int, input(). split())
lst = [i for i in arr if i < a or i > b]
print(min(lst)) if len(lst) > 0 else print(-1)