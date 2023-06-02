n = int(input())
arr = list(map(int, input(). split()))
even = [i for i in arr if i % 2 == 0]
odd = [i for i in arr if i % 2 == 1]
e, o = 0, 0
while e < len(even) or o < len(odd):
    if e < len(even):
        print(even[e], end = ' ')
        e += 1
    if o < len(odd):
        print(odd[o], end = ' ')
        o += 1
if n % 2 != 0:
    print(0)