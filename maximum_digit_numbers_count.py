n = int(input())
arr = list(map(int, input(). split()))
dig = float('-inf')
for i in arr:
    if len(str(i)) > dig:
        dig = len(str(i))
        MaxDigNums = []
        for i in arr:
            if len(str(i)) == dig:
                MaxDigNums.append(i)
print(*MaxDigNums)