def nr_in_sir(sir):
    nr = 0
    fl = 0

    for i in range(len(sir)):
        while 48 <= ord(sir[i]) <= 57:
            nr = nr * 10 + int(sir[i])
            i = i + 1
            fl = 1
        if fl == 1:
            break

    return nr


print(nr_in_sir("ana are 2345 mere dar 34 sunt stricate dar aia e a sunat la 112"))
