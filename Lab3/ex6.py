def tpl(l):
    s = set()
    for x in l:
        s.add(x)

    duplicate = len(l) - len(s)
    unice = len(s)

    return (unice, duplicate)


print(tpl([1, 1, 2, 2, 3, 4, 5, 5, 6]))
