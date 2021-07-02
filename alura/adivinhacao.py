print("********************************")
print("Bem vindo ao jogo de adivinhacao")
print("********************************")

numero_de_adivinhacao = 23
numero_de_tentativas = 3
rodada = 0

while (rodada < numero_de_tentativas):
    numero_do_usuario = int(input("digite um numero inteíro: "))

    acertou = numero_do_usuario == numero_de_adivinhacao
    maior = numero_do_usuario > numero_de_adivinhacao
    menor = numero_do_usuario < numero_de_adivinhacao

    if (numero_do_usuario == numero_de_adivinhacao):
        print("Você acertou")
        rodada += 1
    else:
        print("tentativas: {} de {}".format(rodada, numero_de_tentativas))
        rodada += 1
        if (maior):
            print("Você chutou acima do numero secreto")
        elif (menor):  # poderia colocar apenas else por ser condição booleana
            print("Você chutou abaixo do numero secreto")
print("fim de jogo")
