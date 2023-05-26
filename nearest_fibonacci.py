num = int(input())
first, second = 0, 1
while first < num:
    prev = first
    first = second
    second += prev

if (num - prev) < (first - num): 
    print(prev)
elif (num - prev) > (first - num):
    print(first)
else:
    print(prev, first)