s = input()
i, j, v, cnt = 0, len(s) - 1, 'aeiouAEIOU', 0
while i < j:
    if s[i] != ' ' and s[j] != ' ':
        if (s[i] in v and s[j] not in v) or (s[i] not in v and s[j] in v):
            cnt += 1
    i, j = i + 1, j - 1
    
print(cnt)