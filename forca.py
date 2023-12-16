import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            print(f'Infelizmente você errou. Você tem mais {6-erros} tentativas!')
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_sucesso()
    else:
        imprime_mensagem_fracasso(palavra_secreta)
    print('Fim de jogo!')

def imprime_mensagem_abertura():
    print('****************************************')
    print('****** Bem vindo ao Jogo da Forca ******')
    print('****************************************', end="\n\n")

def carrega_palavra_secreta():
    palavra = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip().upper()
            palavra.append(linha)

    indice = random.randrange(0, len(palavra))
    palavra_secreta = palavra[indice]
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input('Diga uma letra: ')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_sucesso():
    print("Parabéns, você ganhou!")
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

def imprime_mensagem_fracasso(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   X               X       ")
    print("  X                 X      ")
    print(" X                   X  ")
    print(" |   XXXX     XXXX   |   ")
    print(" |   XXXX     XXXX   |     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" X__      XXX      __X     ")
    print("   |X     XXX     X|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   X_             _X       ")
    print("     X_         _X         ")
    print("       X_______X           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      _|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      _|_   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      _|_   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      _|_   ")
        print(" |       |    ")
        print(" |      |     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      _|_   ")
        print(" |       |    ")
        print(" |      | |   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == '__main__'):
    jogar()
