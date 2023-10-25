def aparitii_dict(str):
    x = dict()
    for ch in str:
        if ch not in x.keys():
            x[ch] = 1
        else:
            x[ch] += 1

    return x

str = "Ana has apples."
print(aparitii_dict(str))