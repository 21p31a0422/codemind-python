def ascending(n, arr):
    for i in range(n - 1):
        if arr[i] >= arr[i + 1]:
            return 'no'
    return 'yes'
    
inp = int(input())
arr = list(map(int, input(). split()))
print(ascending(inp, arr))