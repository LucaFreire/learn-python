'''Escreva um programa que faça o computador "pensar" em um núermo inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
jogador=int(input("Digite seu número entre 1 e 5: "))
pc=randint(1,5)
print(f"Você escolheu {jogador} e BOT {pc}.")
if jogador==pc:
    print("Parabéns, Você Venceu!")
else:
    print("Você Perdeu, Tente Novamente!")
