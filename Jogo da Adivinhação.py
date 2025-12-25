#Jogo da Adivinhação 25/12/25

import random

#variavel que guarda o numero aleatorio
numero_secreto = random.randint(1, 20)

#numero de tentativas
tentativas = 5

#enquanto for verdadeiro
while True:

    #ta rodar o código e se não for escrito o que se pede, informa um erro para não quebrar com uma letra
    try:

        print(f'Seu número de tentativas é ({tentativas})')
        #pede que o usuário escreva de 1 a 20
        chute = int(input('Digite o numero de 1 a 20: '))


        #se o chute for menor que 1 ou maior que 20, vai pedir para tentat novamente
        if chute < 1 or chute > 20:
            print('Tente um numero entre 1 e 20!')
            continue

        #se o chute for igual ao número secreto diz que acertou e a quantidade de tentativas
        if chute == numero_secreto:
            print(f'Você acertou com {tentativas} vidas restantes!')
            break #encerra o 'loop'

        #numero de tentativas mais 1 após ser escrito - fica aqui para não dar bug, agora ele verifica se é menor que 1 e maior que 20
        #e se o chute foi certo, então so começa a contar a vida caso não dê 'erro'
        tentativas = tentativas - 1

        if tentativas == 0:
            print('Suas tentativas acabaram!')
            print(f'o numero secreto era {numero_secreto}')
            break

        #se o chute for maior que o número, vai dar uma dica
        if chute < numero_secreto:
            print('Dê um chute maior!')

        # se o chute for menor que o número, vai dar uma dica
        elif chute > numero_secreto:
            print('Dê um chute menor!')

    #(try) da a mensagem do erro
    except ValueError:
        print('Digite um numero de 1 a 20!')