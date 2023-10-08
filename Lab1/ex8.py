def cati_de_1(x):
    y = bin(x)
    c = 0
    print(y)
    for char in y:
        if char == '1':
            c = c+1

    return c

print(cati_de_1(int(15)))