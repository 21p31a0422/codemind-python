n, m = map(int, input(). split())
arr1 = list(map(int, input(). split()))
arr2 = list(map(int, input(). split()))
print(len(set(arr1 + arr2)) - len(set(arr1).intersection(arr2)))