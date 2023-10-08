def pal_nums(numbers):
    palindroame = []
    for num in numbers:
        ogl = 0
        cpnum = num
        while cpnum:
            ogl = 10 * ogl + cpnum % 10
            cpnum = cpnum // 10
        if num == ogl:
            palindroame.append(num)

    n = len(palindroame)
    max_pal = max(palindroame)

    return (n, max_pal)

print(pal_nums([121, 234, 1001, 111222111, 89, 999]))