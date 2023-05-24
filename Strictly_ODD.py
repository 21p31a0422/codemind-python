def strictly_odd(n, arr):
    for i in range(n):
        if i % 2 != 0:
            if arr[i] % 2 == 0:
                return False
    return True
N = int(input())
array = list(map(int, input(). split()))
print(strictly_odd(N, array))