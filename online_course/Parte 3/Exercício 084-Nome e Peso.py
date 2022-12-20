'''Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''


pessoas = []
while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])
    if input('Quer continuar? [S/N] ') not in 'sS':
        break
print(30 * '-=')
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
maior_peso = max([p for n, p in pessoas])
print(f'O maior peso foi de {maior_peso:.1f}Kg. ', end='')
print(f'Peso de {[n for n, p in pessoas if p == maior_peso]}')
menor_peso = min([p for n, p in pessoas])
print(f'O menor peso foi de {menor_peso:.1f}Kg. ', end='')
print(f'Peso de {[n for n, p in pessoas if p == menor_peso]}')


#dados=[]
#pesados=[]
#leves=[]
#nom=[]
#pesos=[]
#COUNT=0
#while True:
#    dados.append(str(input("Digite o Nome: ")))
#    dados.append(float(input("Digite o Peso em Kg:  ")))
#    COUNT+=1
#    ESCOLHA=str(input("Deseja Continuar? [S/N]: ")).strip().upper()
#    if ESCOLHA[0]=="N":
#        break
#
#for i in dados:
#    if type(i) == str:
#        nom.append(i)
#    if type(i) == float and i >= 80:
#        pesados.append(nom[:])
#        pesos.append(i)
#        nom.pop()
#    elif type(i) == float and i<= 80:
#        leves.append(nom[:])
#        pesos.append(i)
#        nom.pop()
#
#print()
#print(f'Número de Pessoas Cadastradas: {COUNT}')
#print(f"Maior peso Kg {max(pesos)} -- {pesados}")
#print(f'Menor peso Kg {min(pesos)} -- {leves}')
