numero = float(input("Entrada do número que desejar:"))
vezesLoop = len(str(numero))
contador = 0
i = 0
resultado = 0

while i <= vezesLoop:
    resultado = numero % 10
    contador = contador + resultado
    numero = numero // 10
    i = i + 1
print("A soma dos números é",contador)
    

