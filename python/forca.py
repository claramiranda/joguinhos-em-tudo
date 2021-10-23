import random


def jogar():

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    letras_faltantes = letras_acertadas.count("_")

    enforcou = False
    acertou = False
    erros = 0

    imprime_mensagem_abertura()
    imprime_mensagem_status(letras_faltantes, letras_acertadas,erros)

    # gameloop
    while (not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas, letras_faltantes)
        else:
            erros += 1
            desenha_forca(erros)

        acertou = "_" not in letras_acertadas
        enforcou = erros == 7
        imprime_mensagem_status(letras_faltantes, letras_acertadas,erros)

    if (acertou):
        imprime_mensagem_vitoria()
    else:
        imprime_mensagem_derrota(palavra_secreta)

    print("Fim do jogo")


def carrega_palavra_secreta(primeira_linha_valida=0,nome_do_arquivo="palavras.txt"):
    arquivo = open(nome_do_arquivo,"r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(primeira_linha_valida, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta, chute, letras_acertadas, letras_faltantes):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
            letras_faltantes -= 1
        index += 1

def imprime_mensagem_status(letras_faltantes, letras_acertadas,erros):
    print("faltam {} letras: {} ".format(letras_faltantes, letras_acertadas))
    print("erros restantes: {}".format(erros))

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def imprime_mensagem_vitoria():
    print("\nParabaaaaains!\n")
    print("Você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_derrota(palavra_secreta):
    print("Puxa, não foi dessa vez que você conseguiu =(")
    print("Palavra secreta: {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()