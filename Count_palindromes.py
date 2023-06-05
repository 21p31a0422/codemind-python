n = int(input())
arr = list(map(int, input(). split()))
palinds = len([i for i in arr if str(i) == str(i)[::-1]])
print(palinds)