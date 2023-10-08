def rime(cuvinte):
    l = []
    c = []
    v = []

    for cuv1 in cuvinte:
        c.append(cuv1)
        v.append(cuv1)
        for cuv2 in cuvinte:
            if cuv1 != cuv2:
                if cuv1[-2:] == cuv2[-2:]:
                    c.append(cuv2)
                    v.append(cuv2)
        if v.count(cuv1) <= 1:
            l.append(c)
        c = []


    return l

print(rime(['ana', 'banana', 'carte', 'arme', 'parte']))
