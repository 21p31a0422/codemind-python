s = input().split()
small = sum([ord(min(word)) for word in s])
large = sum([ord(max(word)) for word in s])
print(abs(small - large))