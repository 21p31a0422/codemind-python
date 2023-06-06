string = input(). split()
for word in string:
    print(abs(ord(max(word)) - ord(min(word))), end = ' ')