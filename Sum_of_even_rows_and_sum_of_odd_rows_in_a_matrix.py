r, c = map(int, input(). split())
mat = []
even = odd =0
for i in range(r):
    in_lt = list(map(int, input(). split()))
    mat.append(in_lt)
for j in range(r):
    if j % 2 == 0:
        even += sum(mat[j])
    else:
        odd += sum(mat[j])
print(even, odd)