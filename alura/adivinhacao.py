import random

print("********************************")
print("Bem vindo ao jogo de adivinhacao")
print("********************************")

numero_de_adivinhacao = random.randrange(1,11)

#print(numero_de_adivinhacao)
numero_de_tentativas = 3
rodada = 0

for rodada in range(1, numero_de_tentativas + 1):
    numero_do_usuario = int(input("digite um numero inteíro de 1 há 10: "))

    if(numero_do_usuario < 1 or numero_de_tentativas > 10):
        print("Você precisa escolher apenas um número de 1 há 100")
        continue

    acertou = numero_do_usuario == numero_de_adivinhacao
    maior = numero_do_usuario > numero_de_adivinhacao
    menor = numero_do_usuario < numero_de_adivinhacao

    if numero_do_usuario == numero_de_adivinhacao:
        print("Você acertou")
        break
    else:
        print("tentativas: {} de {}".format(rodada, numero_de_tentativas))
        if maior:
            print("Você chutou acima do numero secreto")
        elif menor:  # poderia colocar apenas else por ser condição booleana
            print("Você chutou abaixo do numero secreto")

print("fim de jogo")
