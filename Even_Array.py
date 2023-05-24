def even_array(n):
    for i in n:
        if i % 2 != 0:
            return False
    return True
n = int(input())
arr = list(map(int, input(). split()))
if even_array(arr):
    print(True)
else:
    print(False)