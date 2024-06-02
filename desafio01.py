"""
🚀 [Desafio 001] Desenvolvimento de um Script em Python para Contagem com Incremento
 O objetivo deste desafio é construir um script em Python que permita ao usuário realizar uma contagem a partir
 de um número inicial até um número final, somando um valor de incremento a cada iteração.
 Siga as especificações abaixo para completar o desafio:

 Especificações Gerais:
 O script deve ser executado via linha de comando e não requer interface gráfica.
 O usuário deverá fornecer três números como entrada: número inicial, número final e incremento.
 O script realizará uma contagem a partir do número inicial até o número final, somando o valor do incremento.
"""

import os

numI = int(input("Informe o número pelo qual você quer começar: "))
numF = int(input("Informe até onde você quer contar: "))
Inc = int(input("Você quer contar de quanto em quanto?: "))
i = numI

if Inc == 0:
    print('0 = loop')
else:
    if numI > numF:
        while i >= numF:
            print(i)
            i = i - Inc
        print('Números de {} até {} de forma decrescente.'.format(numI, numF))

    elif numI < numF:
        while i <= numF:
            print(i)
            i = i + Inc
        print('Números de {} até {} de forma crescente.'.format(numI, numF))
    else:
        print('Valores iguais.')

os.system('pause')
