def zaza(tuple):
    l = []
    def key_function(item):
        if len(item) > 1 and len(item[1]) > 2:
            return item[1][2]
        return ''

    l = sorted(tuple, key=key_function)

    return l

print(zaza([('abc', 'bcd'), ('abc', 'zza')]))