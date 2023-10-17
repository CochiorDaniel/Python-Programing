def dict_compare(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        if sorted(dict1.keys()) != sorted(dict2.keys()):
            return False
        for key in dict1:
            if not dict_compare(dict1[key], dict2[key]):
                return False
        return True
    else:
        if isinstance(dict1, (int, float)) and isinstance(dict2, (int, float)):
            return dict1 == dict2
        else:
            if len(dict1) != len(dict2):
                return False
            else:
                for i in range(len(dict1)):
                    if dict1[i] != dict2[i]:
                        return False
            return True


dict1 = {
    "k1": {"subkey1": 420, "subkey2": [1, 2, 3, 9]},
    "k2": "v"
}

dict2 = {
    "k2": "v",
    "k1": {"subkey1": 420, "subkey2": [1, 2, 3, 9]}
}

print(dict_compare(dict1, dict2))