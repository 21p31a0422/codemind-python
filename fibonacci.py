def fibanocci(n):
    out = []
    prev, nxt = 0, 1 
    for i in range(n):
        out.append(prev)
        tmp = prev
        prev = nxt
        nxt += tmp
    return out
    
print(*fibanocci(int(input())))