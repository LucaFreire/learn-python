'''Crie um programa que gerencie o aproveitamento de um jogador 
de futebol. O progrma vai ler o nome do jogador e quantas partidas
ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total 
de gols feitos durante o campeonato.'''
from os import system
Dados=dict()
Total=0
Dados['Nome']=str(input("Digite o Nome do Jogador:\n")).title()
Dados['Jogos']=int(input(f"\nQuantidade de Jogos do {Dados['Nome']}:\n"))

for i in range(1,Dados['Jogos']+1):
    Dados[f'{i}° Jogo'] = int(input(f"\nQuantidade de Gols do {i}° Jogo: "))
    Total += Dados[f'{i}° Jogo']
    
system("cls")
Dados['Total de Gols']=Total
print(f"O {Dados['Nome']} Jogou {Dados['Jogos']} Jogos")

for a in Dados:
    print(f"{a}: {Dados[f'{a}']}")
print(Dados)
