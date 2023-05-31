def first_even(n, arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            return i

n = int(input())
arr = list(map(int, input(). split()))
print(sum(arr[:first_even(n, arr)]))