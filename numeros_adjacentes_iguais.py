numero = int(input("Digite um número inteiro:"))

verificador = False
contador =  len(str(numero))
i = 0

if numero == 0:
    print("não")
else: 
    while not verificador and i < contador:
        count1 = numero % 10 
        numero = numero // 10
        count2 = numero % 10
        if count1 == count2:
            verificador = True
        else:
            i += 1
    if verificador:
        print("sim")
    else:
        print("não")
