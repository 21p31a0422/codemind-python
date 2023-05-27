def palind(n, mode):
    if mode == "nxt":
        out = 0
        for i in range(n + 1, n + 1000):
            if str(i) == str(i)[::-1]:
                out = i
                return out
    if mode == "prev":
        out = 0
        for i in range(n - 1, n - 1000, -1):
            if str(i) == str(i)[::-1]:
                out = i
                return out
n = int(input())
prev, nxt = palind(n, "prev"), palind(n, "nxt")
if (n - prev) < (nxt - n):
    print(prev)
elif (n - prev) > (nxt - n):
    print(nxt)
else:
    print(prev, nxt)