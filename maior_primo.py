def maior_primo(x): 
    count = 0
    maior_primo = 0
    while (count <= x):
        if(eprimo(count) == True):
            maior_primo = count
            count += 1
        else:
            count += 1
    return maior_primo


def eprimo(x):
    total = 0
    for c in range (1, x + 1):
        if x % c == 0:
            total += 1
    if total == 2:
        return True
    else:
        return False
