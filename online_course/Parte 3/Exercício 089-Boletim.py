'''Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.'''
import os
Lista=[]
COUNT=1
while True:
    NOME=str(input(f"Digite o Nome do {COUNT}° Aluno: ")).title()
    NOTA1=float(input("Primeira Nota: "))
    NOTA2=float(input("Segunda Nota: "))
    Lista.append([NOME,NOTA1,NOTA2])
    os.system("cls")
    print("Aluno Cadastrado com Sucesso!\n")
    
    ESCOLHA=str(input("Deseja Continuar? [s/n]\n")).title()[0]
    while ESCOLHA!='S' and ESCOLHA!='N':
        print("Escolha Inválida, Digite Novamente!")
        ESCOLHA=str(input("Deseja Continuar? [s/n]\n")).title()[0]
    if ESCOLHA == 'N':
        break
    elif ESCOLHA == 'S':
        COUNT+=1
        os.system("cls")
        
os.system("cls")
print(f"NOME{'MÉDIA':>17}")
print("________________________")
for i, l in enumerate (Lista):
    print(f"{Lista[i][0]:<16}", end="")
    print(f"{(Lista[i][1]+Lista[i][2])/2:.1f}")
    print("________________________")
print("\nDigite 999 P/Sair")
while True:
    ESC=str(input("Ver Notas do Aluno: ")).title()
    if ESC == '999':
        break
    for i, j in enumerate (Lista):
        if Lista[i][0] == ESC:
            print(f"{'NOME':>4}              {'1° Nota':>4}        {'2° Nota':>4}")
            print(f"{Lista[i][0]}             {Lista[i][1]:>4}           {Lista[i][2]:>4}\n")
os.system("cls")
print("Você Saiu")
