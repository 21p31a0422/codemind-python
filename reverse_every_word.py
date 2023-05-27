str_list = list(input(). split ())
out = []
for word in str_list:
    out.append(word[::-1])
print(*out)