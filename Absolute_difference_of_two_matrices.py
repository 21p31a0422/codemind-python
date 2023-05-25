def abs_diff(n, matrix1, matrix2):
    result = [[0] * n for a in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = abs(matrix1[i][j] - matrix2[i][j])
    return result
    
N = int(input())
mat1 = [list(map(int, input(). split())) for x in range(N)]
mat2 = [list(map(int, input(). split())) for y in range(N)]
res = abs_diff(N, mat1, mat2)
for z in range(N):
    print(*res[z])