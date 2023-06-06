string = input().split()
count = 0
for word in string:
    if word[0] in 'aeiouAEIOU' and word[-1] not in 'aeiouAEIOU':
        count += 1
        
print(count)