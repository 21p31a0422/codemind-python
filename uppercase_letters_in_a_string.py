def upper_count(s):
    count = 0
    for i in s:
        if 64 < ord(i) < 91:
            count += 1
    return count
    
string = input()
print(upper_count(string))