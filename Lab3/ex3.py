def dict_compare(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        if sorted(dict1.keys()) != sorted(dict2.keys()):
            return False
        for key in dict1:
            if not dict_compare(dict1[key], dict2[key]):
                return False
        return True
    else:
        return dict1 == dict2


dict1 = {
    "k1": {"s1": 420, "s2": [1, 2, 3, 9, "Ana", 3]},
    "k2": "v"
}

dict2 = {
    "k2": "v",
    "k1": {"s1": 420, "s2": [1, 2, 3, 9, "Ana", 3]}
}

print(dict_compare(dict1, dict2))