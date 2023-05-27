def vow_str(s):
    vowels, VOWELS, v, V = 'aeiou', 'AEIOU', [], []
    for i in vowels:
        if i in s:
            v.append(i)
    for i in VOWELS:
        if i in s:
            V.append(i)
    if len(v) == 5 or len(V) == 5:
        return True
    return False
string = input()
print(vow_str(string))