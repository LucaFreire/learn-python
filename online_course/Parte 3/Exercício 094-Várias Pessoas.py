#Crie um programa que leia nome, sexo e idade de várias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os
#dicionários em uma lista.No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade do grupo
#C) Uma lista com todas as mulheres.
#D) Uma lista com todas as pessoas com idade acima da média.

Dados=dict()
Lista=[]
while True:
    Dados.clear()
    Dados['Nome']=str(input("Digite o Nome: ")).title()
# Sexo
    Dados['Sexo']=str(input("Digite seu Sexo: ")).title()
    while Dados['Sexo'][0] != "F" and Dados['Sexo'][0] != "M":
        print("Sexo Inválido! Digite Novamente.")
        Dados['Sexo']=str(input("Digite seu Sexo: ")).title()
# Idade
    Dados['Idade']=int(input("Digite sua Idade: "))
# Add na Lista o Dicionário
    Lista.append(Dados.copy())
# Escolha de Continuação
    ESC=str(input("Deseja Continuar?[S/N]\n")).title()
    while ESC[0]!="S" and ESC[0]!="N":
        print("Escolha Inválida! Digite Novamente.")
        ESC=str(input("Deseja Continuar[S/N]?\n")).title()
    if ESC[0] == "N":
        break
# Pessoas Cadastradas
print(f"\nA) Número de Pessoas Cadastradas: {len(Lista)}")
# Média de Idade
CALCULO=0
for j in Lista:
    CALCULO+=j['Idade']
print(f"\nB) Média de Idade: {CALCULO/len(Lista):.2f}")
# Lista de Mulheres
print("\nC) Lista de Mulheres:", end=" ")
for i in Lista:
    if i['Sexo']=="F":
        print({i['Nome']}, end=" ")
# Acima da Média
print("\n\nD) Pessoas Acima da Média de Idade:", end=" ")
for k in Lista:
    if k['Idade']>=CALCULO/len(Lista):
        print(f"{k['Nome']} [{k['Idade']}]",end=" ")
