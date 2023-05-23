r, c = map(int, input(). split())
odd_sum = even_sum = 0
mat = [list(map(int, input(). split())) for i in range(r)]
for j in range(r):
    for k in range(c):
        if mat[j][k] % 2 == 0:
            even_sum += mat[j][k]
        else:
            odd_sum += mat[j][k]
print(even_sum , odd_sum)