n = int(input())
arr = list(map(int, input(). split()))
unq_even_count = [i for i in arr if i % 2 == 0]
print(len(set(unq_even_count)))