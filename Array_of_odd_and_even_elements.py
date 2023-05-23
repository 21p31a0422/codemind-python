n = int(input())
arr = list(map(int, input(). split()))
even = [i for i in arr if i % 2 == 0]
odd = [i for i in arr if i % 2 == 1]
print(*odd, *even)