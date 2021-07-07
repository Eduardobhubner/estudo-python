import random


def jogar():
    inicializa_apresentacao()
    palavra_secreta = determina_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while not enforcou and not acertou:

        chute = input("Selecione uma letra")
        chute = chute.strip()  # remove todos os espaços em branco antes e depois da string
        chute = chute.lower()  # coloca todos os chars em letra minuscula

        index = 0

        if chute in palavra_secreta:
            for letra in palavra_secreta.lower():
                if letra == chute:
                    letras_acertadas[index] = letra

                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        letras_faltando = str(letras_acertadas.count('_'))  # .count() indica quantos elementos existe dentro da lista
        print('Ainda faltam acertar {} letras'.format(letras_faltando))
        print(letras_acertadas)
        print("Jogando...")

    if acertou:
        print("Você ganhou")
    else:
        print("Você Perdeu")

    print("Fim do jogo")


def inicializa_apresentacao():
    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")


def determina_palavra_secreta():
    palavras_sorteadas = []

    with open("palavras.txt") as palavras:
        for palavra in palavras:
            palavra = palavra.strip().lower()
            palavras_sorteadas.append(palavra)

    numero = random.randrange(0, len(palavras_sorteadas) + 1)
    palavra_secreta = palavras_sorteadas[numero]
    return palavra_secreta


if __name__ == "__main__":
    jogar()
