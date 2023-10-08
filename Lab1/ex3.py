def count_occurrences(substr, fullstr):
    return fullstr.count(substr)


substr1 = input("Substring:")
fullstr1 = input("Full string:")
nr = count_occurrences(substr1, fullstr1)
print(nr)


