import adivinhacao
import forca

def escolhe_jogo():
    print("*********************************")
    print("********Lista de jogos*********!")
    print("*********************************")

    print("(1)Adivinhação, (2)Forca")
    jogo_escolhido = int(input("Escolha um dos jogos:"))

    if jogo_escolhido == 1:
        adivinhacao.jogar()
    elif jogo_escolhido == 2:
        forca.jogar()


if __name__ == "__main__":
    escolhe_jogo()

