str_list = list(input(). split ())
out = []
for i in range(len(str_list)):
    if i % 2 == 0:
        out.append(str_list[i][::-1])
    else:
        out.append(str_list[i])
print(*out)