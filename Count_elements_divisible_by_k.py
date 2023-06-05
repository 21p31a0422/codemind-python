n, k = map(int, input(). split())
arr = list(map(int, input(). split()))
elem = len([i for i in arr if i % k == 0])
print(elem)