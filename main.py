'''

Neste jogo, há uma lista de palavras presentes, da qual nosso intérprete escolherá 1 palavra aleatória.
O usuário primeiro deve inserir seu nome e, em seguida, será solicitado a adivinhar qualquer letra.
Se a palavra aleatória contiver essa letra, ela será mostrada como saída (com o posicionamento correto),
caso contrário, o programa solicitará que você adivinhe outra letra. O usuário terá 12 tentativas (pode ser
alterado de acordo) para adivinhar a palavra completa.

'''

import random

print('================================\n'
      ' Jogo da Adivinhacao da Palavra\n'
      '================================')
#nome = input('Digite seu nome: ')

palavras = ['computador', 'ciencia', 'programacao', 'python', 'matematica', 'jogador', 'condicao', 'reverso', 'agua',
            'tabuleiro', 'placa', 'janela', 'porta', 'tecla', 'suco', 'carro']

#sorteando palavra
palavra_sorteada = random.choice(palavras)

#limitar número de tentativas
rodadas = len(palavra_sorteada) + 1

chutes = ''

while rodadas > 0:
    tentativas = 0

    for letra in palavra_sorteada:
        if letra in chutes:

            print(letra)
        else:
            print('_')
            tentativas += 1

    if tentativas == 0:
        print('Você venceu!')
        print(f'A palavra é: {palavra_sorteada}')
        break

    print()
    chute = input('Chute uma letra: ')
    chutes += chute

    if chute not in palavra_sorteada:
        rodadas -= 1
        print('Errado')
        print(f'Você tem mais {rodadas} tentativas')

        if rodadas == 0:
            print('Você perdeu')
            print(f'A palavra sorteada era: {palavra_sorteada}')
