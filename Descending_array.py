n = int(input())
arr = list(map(int, input(). split()))
boo = "yes" if arr == sorted(arr, reverse = True) else "no"
print(boo)