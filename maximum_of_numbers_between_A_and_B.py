def Max_num(arr, low, high):
    count = 0
    for i in arr:
        if low <= i <= high and i > count:
            count = i
    return count
    
n = int(input())
arr = list(map(int, input(). split()))
low, high = map(int, input(). split())
result = Max_num(arr, low, high)
if result:
    print(result)
else:
    print(-1)