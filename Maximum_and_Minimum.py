def super_ele(arr):
    list_super_ele = []
    for i in arr:
        if i == arr.count(i) and i not in list_super_ele:
            list_super_ele.append(i)
    return list_super_ele
n = int(input())
array = list(map(int, input(). split()))
out = super_ele(array)
if out:
    print(min(out), max(out))
else:
    print(-1)