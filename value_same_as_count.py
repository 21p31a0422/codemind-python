def value_count(arr):
    lst = []
    for i in arr:
        if i == arr.count(i) and i not in lst:
            lst.append(i)
    return len(lst)

n = int(input())
array = list(map(int, input(). split()))
print(value_count(array))