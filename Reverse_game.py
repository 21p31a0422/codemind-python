n = int(input())
arr = list(map(int, input(). split()))
for i in arr:
    if i > 0:
        print(int(str(i)[::-1]), end = ' ')
    else:
        print(int('-' + (str(abs(i))[::-1])), end = ' ')