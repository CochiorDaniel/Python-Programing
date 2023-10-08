def who_is_blind(matrix):
    linii = len(matrix)
    coloane = len(matrix[0])
    lista = []

    for j in range(0, coloane):
        for i in range(0, linii - 1):
            for k in range(i, linii):
                if matrix[k][j] < matrix[i][j]:
                    tuplu = (k, j)
                    lista.append(tuplu)

    return set(lista)


print(who_is_blind([[1, 2, 3, 2, 1, 1],
                    [2, 4, 4, 3, 7, 2],
                    [5, 5, 2, 5, 6, 4],
                    [6, 6, 7, 6, 7, 5]]))
