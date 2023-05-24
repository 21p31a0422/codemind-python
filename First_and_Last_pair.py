def func(n, arr):
    lst, tmp, boo = [], n, False
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n // 2) + 1
        boo = True
    for i in range(n):
        lst.append(arr[i])
        if i == (n-1) and boo:
            arr[tmp - 1] = 0
        lst.append(arr[tmp - 1])
        tmp -= 1
    return lst
n = int(input())
arr = list(map(int, input(). split()))
print(*func(n , arr))