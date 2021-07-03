def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")




    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        chute = input("Selecione uma letra")
        chute = chute.strip()
        chute = chute.upper()

        index = 0
        for letra in palavra_secreta.upper():
            if(letra == chute):
                print("Você acertou, ela existe na posição {}".format(index))
            index = index +1

        print("Jogando...")

    print("Fim do jogo")






if __name__ == "__main__":
    jogar()
