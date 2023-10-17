def validate_dict(tuple: set, dic: dict):
    # (key, "prefix", "middle", "suffix")
    chilee = set()
    for t in tuple:
        cheie = t[0]
        chilee.add(cheie)
        pref = t[1]
        mid = t[2]
        suf = t[3]
        if cheie in dic.keys():
            s = dic[cheie]
            if not (s.startswith(pref) and s.endswith(suf) and not s.startswith(mid) and not s.endswith(
                    mid) and s.find(mid)):
                return False

    for key in dic:
        if key not in chilee:
            return False
    return True


s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}

print(validate_dict(s,d))