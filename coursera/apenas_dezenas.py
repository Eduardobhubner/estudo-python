
x = float(input("Digite um número inteiro:"))
temp_rest = x % 10
x = x - temp_rest
x = x / 10
x = x % 10

print("O dígito das dezenas é",x)
