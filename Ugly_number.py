def ugly(n):
    if n == 1:
        return True
    elif n % 2 == 0:
        return ugly(n//2)
    elif n % 3 == 0:
        return ugly(n//3)
    elif n % 5 == 0:
        return ugly(n//5)
    return False
n = int(input())
if ugly(n) == True:
    print("Ugly Number")
else:
    print("Not Ugly Number")