n, m = map(int, input(). split())
arr1 = list(map(int, input(). split()))
arr2 = list(map(int, input(). split()))
com_ele = []
for i in arr1:
    if i in arr2 and i not in com_ele:
        com_ele.append(i)
print(*com_ele)