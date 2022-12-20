#Aprimore o desafio 093 para que ele funcione com vários
#jogadores, incluindo um sistema de visualização de detalhes
#do aproveitamento de cada jogador.
from os import system
Gol=[]
Dic={}
Lista=[]
COUNT=1
while True:
    system("cls")
    Dic.clear()
    Dic['Num.']=COUNT
    Dic['Nome']=str(input("Nome do Jogador: ")).title()
    Dic['Jogos']=int(input(f"Qunatidade de Jogos do {Dic['Nome']}: "))
    for i in range(1,Dic['Jogos']+1):
        Gol.append(int(input(f"Gols da {i}° Partida: ")))
    Dic['Gols']=Gol[:]
    Gol.clear()
    Lista.append(Dic.copy())
    COUNT+=1
    system("cls")
    print("Jogador Cadastrado com Sucesso!")
    ESC=str(input("Deseja Inserir Mais Jogadores?[S/N]")).upper()
    while ESC[0]!="S" and ESC[0]!="N":
        print("Escolha Inválida! Digite Novamente.")
        ESC=str(input("Deseja Inserir Mais Jogadores?[S/N]")).upper()
    if ESC[0]=="N":
        break
    
while True:
    print("\n\n   Aproveitamento de Jogadores")
    print(16*"__")
    print(f"NUM.{'JOGADOR':>15}{'TOTAL':>13}")
    for j,k in enumerate(Lista):
        print(f"{j+1:<12}{k['Nome']:<8}{sum(k['Gols']):>10}")
        print(16*"--")
    Escolha=int(input("Digite o Código do Jogador Para ver Mais [0 p/Sair]:\n"))
    if Escolha==0:
        break
    system("cls")
    for l in Lista:
        if l['Num.']==Escolha:
            print(f"\n\n~~Detalhes do {l['Nome']}~~")
            for m,n in enumerate(l['Gols']):
                print(f"{m+1}° Jogo: {n} Gols")
        else:
            print("Código Inválido! Digite Novamente.")
print("Fim")
