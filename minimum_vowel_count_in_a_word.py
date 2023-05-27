def v_cnt(s):
    cnt = 0
    for i in s:
        if i in 'aeiou':
            cnt += 1
    return cnt

s_list = list(input(). split())
result = float('inf')
for word in s_list:
    if result > v_cnt(word):
        result = v_cnt(word) 
print(result)