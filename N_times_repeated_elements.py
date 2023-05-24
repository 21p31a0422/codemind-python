def repeat(arr, k):
    k_rep_ele = []
    for i in arr:
        if k == arr.count(i) and i not in k_rep_ele:
            k_rep_ele.append(i)
    return k_rep_ele
    
n = int(input())
array = list(map(int, input(). split()))
K = int(input())
if repeat(array, K):
    print(*repeat(array, K))
else:
    print(-1)