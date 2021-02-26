def vogal(x):
    vogais = ["a","e","i","o","u","A","E","I","O","U"]
    i = 0
    varVogal = False

    while (i < int(len(vogais))) and not varVogal:
        if x == vogais[i]:
            varVogal = True
        else:
            i = i + 1

    return varVogal