s = input().split()
v, cnt = 'aeiouAEIOU', 0
for word in s:
    a, b = 0, len(word) - 1
    while a < b:
        if (word[a] in v and word[b] not in v) or (word[a] not in v and word[b] in v):
            cnt += 1
        a, b = a + 1, b - 1 
print(cnt)