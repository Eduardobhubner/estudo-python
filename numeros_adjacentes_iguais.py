numero = int(input("Escreva um número inteiro para descobrir se há adjacentes iguais:"))

verificador = False
i = 0

while not verificador and i < len(str(numero)):
    count1 = numero % 10 
    numero = numero // 10
    count2 = numero % 10
    if count1 == count2:
        verificador = True
    else:
        i += 1
if verificador:
    print("Existe")
else:
    print("Não existe")