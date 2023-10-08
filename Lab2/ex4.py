def muzica(note, mutari, start_poz):
    song = []
    song.append(note[start_poz])
    for i in mutari:
        start_poz = start_poz+i
        song.append(note[start_poz % len(note)])

    return song

print(muzica(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
