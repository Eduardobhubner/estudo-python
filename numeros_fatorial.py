x = int(input("Digite o valor de n:"))

fatorado = False
result = 1

if x != 0 and x != 1:
    while not fatorado:
        result = result * x
        x = x - 1
        if x == 1:
            fatorado = True
else:
    result = 1
print(result) 