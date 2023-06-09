# Wave Count
n = int(input())
arr = list(map(int, input(). split()))
check = 'i' if arr[0] < arr[1] else 'd'
cnt_time, cnt = 1, 0
for i in range(1, n - 1):
    if arr[i] > arr[i + 1] and check == 'i':
        check = 'd'
        if cnt_time == 1:
            cnt_time, cnt = 0, cnt + 1
        else:
            cnt_time = 1
    elif arr[i] < arr[i + 1] and check == 'd':
        check = 'i'
        if cnt_time == 1:
            cnt_time, cnt = 0, cnt + 1
        else:
            cnt_time = 1
    else:
        cnt = -1
        break
    
print(cnt)