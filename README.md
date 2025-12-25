🎲 Jogo da Adivinhação
Um jogo de lógica simples via linha de comando (CLI) desenvolvido em Python. O objetivo é acertar o número secreto gerado aleatoriamente pelo computador.

📝 Sobre o Projeto
Este projeto foi desenvolvido como prática de lógica de programação em Python, utilizando estruturas de repetição (while), condicionais (if/else) e tratamento de exceções (try/except).

Data de criação: 25/12/2025

✨ Funcionalidades
Geração Aleatória: O jogo escolhe um número secreto entre 1 e 20 a cada nova execução.

Sistema de Vidas: O jogador possui um limite de 5 tentativas.

Dicas Dinâmicas: O sistema informa se o seu chute deve ser maior ou menor que o número tentado.

Validação de Entrada:

Impede que o programa feche com erro se o usuário digitar letras ou símbolos.

Não desconta vidas se o usuário digitar um número fora do intervalo (1 a 20).

🚀 Como Executar
Pré-requisitos
Ter o Python instalado em sua máquina.

Passo a Passo
Clone este repositório ou baixe o arquivo .py.

Abra o terminal na pasta do arquivo.

Execute o comando:

Bash

python nome_do_arquivo.py
🎮 Exemplo de Uso
Plaintext

Seu número de tentativas é (5)
Digite o numero de 1 a 20: 10
Dê um chute maior!

Seu número de tentativas é (4)
Digite o numero de 1 a 20: 15
Dê um chute menor!

Seu número de tentativas é (3)
Digite o numero de 1 a 20: 12
Você acertou com 3 vidas restantes!
🛠️ Tecnologias Utilizadas
Python 3

Biblioteca random (nativa)

Desenvolvido por [Diego Marques]
