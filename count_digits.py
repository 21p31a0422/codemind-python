n = int(input())
arr = list(map(abs, list(map(int, input(). split()))))
digits = [len(str(i)) for i in arr]
print(*digits)