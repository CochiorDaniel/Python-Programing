def cnt(x, *liste):
    l =[]
    res = []
    v = []
    for el in liste:
        for c in el:
            l.append(c)

    for el in l:
        if l.count(el) == x and v.count(el) < 1:
            res.append(el)
        v.append(el)

    return res

print(cnt(2,[1,2,3], [2,3,4],[4,5,6], [4,1, "test"]))