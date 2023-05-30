n = int(input())
arr = list(map(int, input(). split()))
unq_even = [i for i in arr if i % 2 == 0]
print(sum(set(unq_even)))