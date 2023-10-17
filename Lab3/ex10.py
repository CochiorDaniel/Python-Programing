def crazy_loop(mapping: dict):
    visited = set()
    rez = []
    current_key = 'start'

    while current_key not in visited: # and current_key in mapping:
        visited.add(current_key)
        current_key = mapping[current_key]
        if current_key not in visited:
            rez.append(current_key)

    return rez


mapping1 = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = crazy_loop(mapping1)
print(result)
