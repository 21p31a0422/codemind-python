def vowels(s):
    unq_vowels = []
    for i in s:
        if i in 'aeiouAEIOU' and i not in unq_vowels:
            unq_vowels.append(i)
    return unq_vowels
string = input()
if vowels(string):
    print(*vowels(string))
else:
    print(-1)