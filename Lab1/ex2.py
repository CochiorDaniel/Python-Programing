def vocale_count(input_str):
    nr_vocale = 0

    vocale = set("aeiouAEIOU")

    for c in input_str:
        if c in vocale:
            nr_vocale += 1

    return nr_vocale


prop = input("String:")
nr_voc = vocale_count(prop)
print("Nr vocale:", nr_voc)
