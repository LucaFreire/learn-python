'''Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista 
lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente.'''

lista=[]
count=1
print("Número Negativo p/ Sair")
while True:
    num=int(input(f"Digite seu {count}° Número: "))
    if num<0:
        break
    elif num not in lista:
        lista.append(num)
        count+=1
    else:
        print(f"{num} já foi Incluso na Lista!")  
print()
print(f'Lista em Ordem Crescente: {sorted(lista)}')
