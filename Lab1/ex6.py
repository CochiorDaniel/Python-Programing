def palindrom(x):
    ogl = 0
    cpx = x

    while cpx:
        ogl = 10 * ogl + cpx % 10
        cpx = int(cpx / 10)

    if x == ogl:
        return True
    else:
        return False


p = input("Nr:")
este = palindrom(int(p))
print(este)
