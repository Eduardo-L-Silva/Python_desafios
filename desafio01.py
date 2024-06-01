import os

"""
GRUPO 3
🚀 [Desafio 001] Desenvolvimento de um Script em Python para Contagem com Incremento

O objetivo deste desafio é construir um script em Python que permita ao usuário realizar uma contagem a partir de um número inicial até um número final, somando um valor de incremento a cada iteração. Siga as especificações abaixo para completar o desafio:

1. Especificações Gerais:
    - O script deve ser executado via linha de comando e não requer interface gráfica.
    - O usuário deverá fornecer três números como entrada: número inicial, número final e incremento.
    - O script realizará uma contagem a partir do número inicial até o número final, somando o valor do incremento.
"""
print("Bem Vindo negão!")
numI = int(input("Informe o número inicial: "))
numF = int(input("Informe o número final: "))
inc = int(input("Digite o incremento: "))

for n in range(numI, numF+1, inc):
    print(n)
print("\nFim do programa, contagem inicial de", numI, "até", numF,
      "de",inc, "em",inc, "com sucesso!")
os.system('pause')