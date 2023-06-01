n = int(input())
arr = list(map(int, input(). split()))
print(sum(arr[:int(n / 2)]))
print(sum(arr[int(n / 2):]))