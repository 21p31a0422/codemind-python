n = int(input())
arr = list(map(int, input(). split()))
lst =[]
for i in arr:
    if i not in lst:
        lst.append(i)
print(*lst)