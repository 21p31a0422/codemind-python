n, m = map(int, input(). split())
arr1 = list(map(int, input(). split()))
arr2 = list(map(int, input(). split()))
com_ele1 = [i for i in arr1 if i not in arr2]
com_ele2 = [i for i in arr2 if i not in arr1]
print(*(com_ele1 + com_ele2))