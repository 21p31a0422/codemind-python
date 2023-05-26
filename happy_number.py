def happy(n):
    tot = 0
    if n == 1 or n == 7:
        return True
    elif n < 10:
        return False
    for i in str(n):
        tot += pow(int(i), 2)
    return happy(tot)
n = int(input())
if happy(n):
    print(True)
else:
    print(False)