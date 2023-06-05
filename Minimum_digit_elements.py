n = int(input())
arr = list(map(abs, list(map(int, input(). split()))))
digits = float('inf')
for i in arr:
    if len(str(i)) < digits:
        cnt = 0
        digits = len(str(i))
        for i in arr:
            if digits == len(str(i)):
                cnt += 1
print(cnt)