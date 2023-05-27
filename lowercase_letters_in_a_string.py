def low_count(s):
    count = 0
    for i in s:
        if 96 < ord(i) < 123:
            count += 1
    return count

string = input()    
print(low_count(string))