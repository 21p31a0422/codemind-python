def trans(r, c, mat):
    res = [[0] * r for i in range(c)]
    for i in range(r):
        for j in range(c):
            res[j][i] = mat[i][j]
    return res

def max_sum(r, c, mat):
    out = 0
    for i in range(r):
        s = sum(mat[i])
        if out < s:
            out = s
    return out

r, c = map(int, input(). split())
mat = [list(map(int, input(). split())) for i in range(r)]
print(max(max_sum(r, c, mat), max_sum(r, c, trans(r, c, mat))))