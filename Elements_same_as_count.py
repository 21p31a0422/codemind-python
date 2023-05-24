def super_ele(arr):
    list_se = []
    for i in arr:
        if i == arr.count(i) and i not in list_se:
            list_se.append(i)
    return list_se
    
n = int(input())
array = list(map(int, input(). split()))
if super_ele(array):
    print(*super_ele(array))
else:
    print(-1)