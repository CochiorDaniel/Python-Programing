def prime_numbers(*numbers):
    res = []
    ok = 1
    for num in numbers:
        ok = 1
        for i in range (2, num//2+1):
            if num % i == 0:
                ok = 0
        if ok == 1:
            res.append(num)

    return res

print(prime_numbers(1,2,3,4,5,6,7,8,9,13,17,23,88,64))