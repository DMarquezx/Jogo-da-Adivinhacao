

import random

numero_secreto = random.randint(1, 20)

tentativas = 5

while True:

    try:

        print(f'Seu número de tentativas é ({tentativas})')
        chute = int(input('Digite o numero de 1 a 20: '))


        if chute < 1 or chute > 20:
            print('Tente um numero entre 1 e 20!')
            continue

        if chute == numero_secreto:
            print(f'Você acertou com {tentativas} vidas restantes!')
            break

        tentativas = tentativas - 1

        if tentativas == 0:
            print('Suas tentativas acabaram!')
            print(f'o numero secreto era {numero_secreto}')
            break

        if chute < numero_secreto:
            print('Dê um chute maior!')

        elif chute > numero_secreto:
            print('Dê um chute menor!')

    except ValueError:

        print('Digite um numero de 1 a 20!')
