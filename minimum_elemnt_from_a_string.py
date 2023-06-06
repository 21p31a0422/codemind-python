s = input(). split()
high = [i for i in s[-1] if 64 < ord(i) < 91]
low = [i for i in s[-1] if 96 < ord(i) < 123]

if low == []:
    print(min(high))
elif high == []:
    print(min(low))

elif min(high).lower() == min(low):
    print(min(low))
elif min(high).lower() < min(low):
    print(min(high))
elif min(high).lower() > min(low):
    print(min(low))