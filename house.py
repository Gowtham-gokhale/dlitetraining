d = [6, 7, 1, 3, 8, 2, 5]
e = len(d)
if e == 0:
    print(0)
elif e == 1:
    print(d[0])
else:
    f = d[0]
    g = max(d[0], d[1])
    for h in range(2, e):
        i = max(g, f + d[h])
        f = g
        g = i
    print(g)