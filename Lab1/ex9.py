def cea_mai_litera(sir):
    l = 'z'
    aparitii = 0
    aparitii_max = 0

    for i in range(len(sir)):
        if 65 <= ord(sir[i]) <= 90 or 97 <= ord(sir[i]) <= 122:
            litera = sir[i]
        else:
            continue
        for j in range(len(sir)):
            if sir[i] == sir[j]:
                aparitii += 1
        if aparitii > aparitii_max:
            aparitii_max = aparitii
            l = litera
        aparitii = 0

    return l

print(cea_mai_litera("an apple is not a tomato"))
print(cea_mai_litera("ana mer77^^*&*&*#$%^&*(&^%$#$%^&*()*&^%ge gg gg gg"))