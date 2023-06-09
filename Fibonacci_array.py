n = int(input())
arr = list(map(int, input(). split()))
boo = True
if n <= 2:
    boo = False
else:
    for i in range(2, n):
        if arr[i - 2] + arr[i - 1] != arr[i]:
            boo = boo and False
            break
print('yes') if boo else print('no')