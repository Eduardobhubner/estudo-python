#numeros primos só podem ser divididos por ele e por 1 :)
x = int(input("Digite um número inteiro:"))
total = 0

for c in range (1, x + 1):
    if x % c == 0:
        total += 1
if total == 2:
    print("primo")
else:
    print("não primo")


