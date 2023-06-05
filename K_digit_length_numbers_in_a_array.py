n, k = map(int, input(). split())
arr = list(map(abs, list(map(int, input(). split()))))
k_dig_nums = len([i for i in arr if len(str(i)) == k])
print(k_dig_nums)