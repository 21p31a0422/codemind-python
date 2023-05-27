def vow_count(s):
    count = 0 
    for i in s:
        if i in 'aeiou':
            count += 1
    return count

s_list = list(input(). split())
for word in s_list:
    print(vow_count(word), end = ' ')