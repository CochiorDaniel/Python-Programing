def cnt(*args, **kwords):
    simple = set(args)
    dupa_egal = set(kwords.values())
    count = 0

    for value in simple:
        if value in dupa_egal:
            count += 1

    return count


result = cnt(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)
