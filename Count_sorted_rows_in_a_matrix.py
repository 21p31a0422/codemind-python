r, c  = map(int, input(). split())
mat = [list(map(int, input(). split())) for i in range(r)]
cnt = 0
for row in mat:
    if row == sorted(row) or row[::-1] == sorted(row):
        cnt += 1
print(cnt)