def count_vowels(s):
    cnt = 0
    for i in s:
        if i in 'aeiou':
            cnt += 1
    return cnt
str_lst = list(input().split())
v_cnt = []
for word in str_lst:
    v_cnt.append(count_vowels(word))
print(v_cnt.count(max(v_cnt)))