import math


def gcd(n):
    numbers = []

    while n:
        nr_dat = input()
        nr = int(nr_dat)
        numbers.append(nr)
        n = n - 1

    rezultat = numbers[0]
    for nr in numbers[1:]:
        rezultat = math.gcd(rezultat, nr)

    print(rezultat)


gcd(4)
