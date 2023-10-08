def lipeste(*liste):
    listaaa = []
    t = tuple ()
    m = 0
    for l in liste:
        if len(l) > m:
            m = len(l)

    i = 0
    for i in range (0,m):
        for l in liste:
            if i < len(l):
                t += (l[i],)
            else:
                t += (None,)
        listaaa.append(t)
        t = tuple ()

    return listaaa

print(lipeste([1,2,3], [5,6,7], ["a", "b", "c"]))
