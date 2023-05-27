def count_vowels(s):
    count = 0
    for i in s:
        if i in 'aeiouAEIOU':
            count += 1
    return count
string = input()
if count_vowels(string):
    print(count_vowels(string))
else:
    print(0)