n = int(input())
arr = list(map(int, input(). split()))
unq_odd = [i for i in arr if i % 2 == 1]
print(sum(set(unq_odd)))