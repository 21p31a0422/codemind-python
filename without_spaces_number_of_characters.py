s_list = list(input().split())
length = 0
for word in s_list:
    length += len(word)
print(length)