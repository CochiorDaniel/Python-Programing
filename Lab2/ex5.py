def under_diagonal_0(matrix):
    linii = len(matrix)
    coloane = len(matrix[0])

    if linii != coloane:
        return False

    for i in range (0,linii):
        for j in range(0,coloane):
            if(j < i):
                matrix[i][j] = 0

    return matrix

m = [[1, 2, 3, 8], [4, 5, 6, 9], [7, 8, 9, 6], [7, 8, 9, 6]]
m = under_diagonal_0(m)
for i in m:
    print(i)