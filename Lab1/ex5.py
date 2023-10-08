def spider(a):
    row_begin = 0
    row_end = len(a) - 1
    col_begin = 0
    col_end = len(a[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end + 1):
            print(a[row_begin][i])
        row_begin += 1
        for i in range(row_begin, row_end + 1):
            print(a[i][col_end])
        col_end -= 1
        for i in range(col_end, col_begin - 1, -1):
            print(a[row_end][i])
        row_end -= 1
        for i in range(row_end, row_begin - 1, -1):
            print(a[i][col_begin])
        col_begin += 1


matrix = [['f', 'i', 'r', 's'],
          ['n', '', 'l', 't'],
          ['o', 'b', 'a', ''],
          ['h', 't', 'y', 'p']]

spider(matrix)
