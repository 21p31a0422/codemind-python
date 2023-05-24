def ele_cnt(arr):
    lst, tmp = [], []
    for i in arr:
        if i not in tmp:
            lst.append(i)
            tmp.append(i)
            lst.append(arr.count(i))
    return lst

n = int(input())
array = list(map(int, input(). split()))
print(*ele_cnt(array))