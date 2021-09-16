Aarr = [2, 3, 4, 5, 0, 0, 0, 0]
Barr = [1, 2, 3, 4]

cur = len(Aarr) - 1
p1 = 3
p2 = len(Barr) - 1
while cur >= 0:
    print(cur)
    print(p1, p2)
    if Aarr[p1] > Barr[p2]:
        Aarr[cur], Aarr[p1] = Aarr[p1], Aarr[cur]
        cur -= 1
        p1 -= 1
    else:
        Aarr[cur], Barr[p2] = Barr[p2], Aarr[cur]
        cur -= 1
        p2 -= 1
    # A数组可能走的比B数组快
    while p1 < p2:
        Aarr[cur] = Barr[p2]
        p2 -= 1
        cur -= 1
print(Aarr)
