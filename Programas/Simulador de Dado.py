'''1. SIMULADOR DE DADO
Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6
(ou uma faixa que você definir) e permitir que o usuário rode
o script quantas vezes quiser.'''
from random import randint
while True:
    escolha=str(input("Deseja jogar o dado [S/N]? ")).strip().upper()[0]
    if escolha=="N":
        break
    elif escolha=="S":
        print(f'Número do Dado: {randint(1,6)}')
        print()
    else:
        print("Escolha Inválida, Digite Novamente!")

print("Você Saiu do Simulador de Dado...")
