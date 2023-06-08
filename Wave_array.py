n = int(input())
arr = list(map(int, input(). split()))
check = 'i' if arr[0] < arr[1] else 'd'
boo = 'yes'
for i in range(1, n - 1):
    if arr[i] < arr[i + 1] and check == 'd':
        check = 'i'
    elif arr[i] > arr[i + 1] and check == 'i':
        check = 'd'
    else:
        boo = 'no'
        break
    
print(boo)