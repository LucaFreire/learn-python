'''Faça um programa que ajude um jogador a criar palpites
na Mega Sena. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta.'''

from random import randint

Lista=[]
Jogos=[]
COUNT=0
NUM_DE_JOGOS=int(input("Quantos Jogos Você Vai Fazer?\n"))
#INPUT
while COUNT!=NUM_DE_JOGOS:
    for i in range(0,6):
        num=randint(1,60)
        while num in Lista:
            num=randint(1,60)
        Lista.append(num)
    Lista.sort()
    Jogos.append(Lista[:])
    Lista.clear()
    COUNT+=1
#OUTPUT
for j in range(1,NUM_DE_JOGOS+1):
    print(f"\n{j}° Jogo: {Jogos[j-1]}")
