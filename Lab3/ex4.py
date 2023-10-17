def build_xml(tag, contend, **key_val):
    s = "\"<"
    s += tag + " "
    for t in key_val.items():
        s += str(t[0]) + "=\"" + str(t[1]) + "\"\\"
    s += ">" + contend + "\""

    return s


f = build_xml("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid ")
print(f)
