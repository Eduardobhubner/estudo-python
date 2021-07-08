import random


def jogar():
    print("********************************")
    print("***Bem vindo ao jogo da forca***")
    print("********************************")

    ganhou = False
    enforcou = False

    palavra_secreta = determina_palavra_secreta()
    erro_permitido = escolha_dificuldade()

    construcao_da_palavra = ["_" for letra in palavra_secreta]

    letras_chutadas_erradas =[]
    count_erros = 0

    while not ganhou and not enforcou:

        print("tentativas {} de {}".format(count_erros, erro_permitido))
        print("letras tentadas sem sucesso: {}".format(letras_chutadas_erradas))
        print(construcao_da_palavra)
        letra_chute_do_jogador = input("Adivinhe a letra da palavra:").lower()

        if letra_chute_do_jogador in palavra_secreta:
            print("Você acertou a letra {}".format(letra_chute_do_jogador))
            index = 0
            for letra in palavra_secreta:
                if letra_chute_do_jogador == letra:
                    construcao_da_palavra[index] = letra
                index += 1
            ganhou = "_" not in construcao_da_palavra

        else:
            print("você errou")
            letras_chutadas_erradas.append(letra_chute_do_jogador)
            count_erros += 1
            enforcou = count_erros == erro_permitido

    if ganhou:
        print("Você acertou todas as letras da palavra {}. Parabéns!!!".format(palavra_secreta))
    else:
        print("Mais sorte na próxima, a palavra era {}".format(palavra_secreta))


def escolha_dificuldade():

    escolheu_dificuldade = False

    while not escolheu_dificuldade:

        print("(1) -- 3 chances, (2) -- 6 chances, (3) -- 9 chances")
        print("Qual nivel de dificuldade você esta disposto a enfrentar? ")
        nivel_de_dificuldade = int(input("Escolha um número de 1 a 3 "))

        if nivel_de_dificuldade == 1:
            return 3
        elif nivel_de_dificuldade == 2:
            return 6
        elif nivel_de_dificuldade == 3:
            return 9
        else:
            print("escolha apenas números de 1 a 3 espertinha(o)")


def determina_palavra_secreta():
    lista_palavras_secretas = []

    arquivo_palavras_secretas = open("palavras.txt", "r")
    for palavra in arquivo_palavras_secretas:
        lista_palavras_secretas.append(palavra.strip().lower())
    arquivo_palavras_secretas.close()
    numero_aleatorio = random.randrange(0, len(lista_palavras_secretas))
    palavra_secreta = lista_palavras_secretas[numero_aleatorio]
    return palavra_secreta


if __name__ == "__main__":
    jogar()
