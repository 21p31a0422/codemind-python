def trans(r, c, mat):
    res = [[0] * r for i in range(c)]
    for i in range(r):
        for j in range(c):
            res[j][i] = mat[i][j]
    return res

def max_sum(mat):
    out = 0
    for row in mat:
        s = sum(row)
        if out < s:
            out = s
    return out

r, c = map(int, input(). split())
mat = [list(map(int, input(). split())) for i in range(r)]
print(max(max_sum(mat), max_sum(trans(r, c, mat))))
