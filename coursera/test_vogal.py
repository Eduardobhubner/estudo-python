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

def test_vogala():
    assert vogal("a") == True

def test_vogale():
    assert vogal("E") == True

def test_vogali():
    assert vogal("i") == True

def test_vogalo():
    assert vogal("O") == True

def test_vogalu():
    assert vogal("u") == True

def test_vogalErro():
    assert vogal(1) == False