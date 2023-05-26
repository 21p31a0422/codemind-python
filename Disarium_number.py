tmp = n = int(input())
l, res = len(str(n)), 0
while n:
    res += pow(n % 10, l)
    l -= 1
    n //= 10
if res == tmp:
    print(True)
else:
    print(False)