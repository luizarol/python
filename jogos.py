import forca
import adivinhacao

def escolhe_jogo():
    print("*******************************************")
    print("Olá! Bem vindo!!!! Escolha o seu jogo:")
    print("*******************************************")

    print("(1) Forca  (2) Adivinhação")

    jogo = int(input("Qual o jogo?"))

    if (jogo == 1):
        print("Jogando forca!")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação!")
        adivinhacao.jogar()

if(__name__ == "__main__"):\PycharmProjects\jogos
    escolhe_jogo()

