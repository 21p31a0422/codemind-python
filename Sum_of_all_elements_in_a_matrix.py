r, c  = map(int, input(). split())
total = 0 
mat = [list(map(int, input(). split())) for i in range(r)]
for i in range(r):
    for j in range(c):
        total += mat[i][j]
print(total)