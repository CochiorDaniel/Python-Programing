def ascii_find(stringuri, x=1, flag=True):
    list = []
    for str in stringuri:
        l1 = []
        for i in range (0, len(str)):
            if flag == True:
                if ord(str[i]) % x == 0:
                    l1.append(str[i])
            if flag == False:
                if ord(str[i]) % x != 0:
                    l1.append(str[i])
        list.append(l1)

    return list

a=ascii_find( ["test", "hello", "lab002"],x = 2,  flag = False)
print(a)