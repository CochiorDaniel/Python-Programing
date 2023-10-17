def operatii(a,b):
    intersectu = set(a).intersection(b)
    unionu = set(a).union(b)
    a_minus_b = set(a).difference(b)
    b_minus_a = set(b).difference(a)

    return [intersectu, unionu, a_minus_b, b_minus_a]


list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

result = operatii(list_a, list_b)
print(result)