def count_special_char(s):
    count = 0
    for i in s:
        if i in '!@#$%^&*()-_+={}[]|\:;"<>,.?/~`':
            count += 1
    return count 
    
string = input()
print(count_special_char(string))