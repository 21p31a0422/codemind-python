string = list(input().split())
length = float('-inf')
for word in string:
    if len(word) > length:
        length = len(word)
print(length)