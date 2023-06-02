n = int(input())
arr = list(map(int, input(). split()))
even = [i for i in arr if i % 2 == 0]
odd = [i for i in arr if i % 2 == 1]
ei, oi = 0, 0
while ei < len(even) or oi < len(odd):
    if oi < len(odd):
        print(odd[oi], end = ' ')
        oi += 1
    if ei < len(even):
        print(even[ei], end = ' ')
        ei += 1
if n % 2 != 0:
    print(0)