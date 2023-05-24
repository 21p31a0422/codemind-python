n = int(input())
arr = list(map(int, input(). split()))
c, lst = 0, []
for i in arr:
    if i % 2 != 0 and i not in lst:
        lst.append(i)
        c += 1
print(c)