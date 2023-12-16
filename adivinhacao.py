import random

def jogar():
    print('***************************************')
    print('*** Bem vindo ao Jogo da Advinhação ***')
    print('***************************************', end="\n\n")
    print('Você terá algumas tentativas para acertar')
    print('   o número que pensei entre 1 e 100!')

    numero_secreto = random.randint(1, 100)
    print('\nQual nível de dificuldade será o jogo?')
    print('(1) Fácil   (2) Médio   (3) Difícil')
    dificuldade = int(input())
    pontos = 100

    if (dificuldade == 1):
        tentativas = 10
    elif (dificuldade == 2):
        tentativas = 5
    else:
        tentativas = 3

    for n in range(1, tentativas + 1):
        print(f'\nVamos a sua tentativa número: {n} de {tentativas}')
        chute = input('Digite sua tentativa: ')
        chute_int = int(chute)

        if (chute_int < 1 or chute_int > 100):
            print('Você não sabe ler não??? Falei que o número está entre 1 e 50.')
            continue

        acertou = chute_int == numero_secreto
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto
        ponto_perdido = abs(numero_secreto - chute_int)

        if (acertou):
            print('\nParabéns, você acertou!!!!')
            break
        else:
            if (maior):
                print('\nSua tentativa foi maior que o número secreto, tente novamente!')
            elif (menor):
                print('\nSua tentativa foi menor que o número secreto, tente novemente!')
            pontos = pontos - ponto_perdido

    if (n == 6):
        print('O número pensado era ', numero_secreto)

    print(f'Sua pontuação foi de: {pontos}')
    print('\nFim de Jogo!!!!\n')

if (__name__ == "__main__"):
    jogar()
