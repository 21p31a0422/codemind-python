def v_in_str(s):
    vow_out, vowels = [], 'aeiou'
    for i in vowels:
        if i not in s:
            vow_out.append(i)
    return vow_out
string = input()
if v_in_str(string):
    print(*v_in_str(string))
else:
    print(0)