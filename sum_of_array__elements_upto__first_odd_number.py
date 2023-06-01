n = int(input())
arr = list(map(int, input(). split()))
total = 0
for i in arr:
    if i % 2 == 0:
        total += i
    else:
        print(total)
        break