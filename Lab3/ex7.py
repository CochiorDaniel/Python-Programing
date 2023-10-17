def operatii(*sets):
    dix = dict()

    for i in range(0, len(sets)):
        for j in range(i + 1, len(sets)):
            dix["\"" + str(sets[i]) + " | " + str(sets[j]) + "\""] = sets[i].union(sets[j])
            dix["\"" + str(sets[i]) + " & " + str(sets[j]) + "\""] = sets[i].intersection(sets[j])
            dix["\"" + str(sets[i]) + " - " + str(sets[j]) + "\""] = sets[i].difference(sets[j])
            dix["\"" + str(sets[j]) + " - " + str(sets[i]) + "\""] = sets[j].difference(sets[i])

    return dix


print(operatii({1, 2}, {2, 3}))
