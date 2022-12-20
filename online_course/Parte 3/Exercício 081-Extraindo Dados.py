'''Crie um programa que vai ler vários números e colocar em
uma lista. Mostre:

A)Quantos números foram digitados;
B)A lista de valores, ordenada de forma decrescente;
C)Se o valor 5 foi digitado e está ou não na lista.'''

lista=[]
count=0
print("Digite um Número Negativo p/ Sair")
while True:
    count+=1
    num=int(input(f"Digite seu {count}° Número: "))

    if num>=0:
        lista.append(num)
    else:
        break
print()
print("Tamanho da Lista:",len(lista))
print(f'Ordem decrescente: {sorted(lista,reverse=True)}')
if 5 in lista:
    print('O Valor 5 foi Digitado e está na Lista!')
    print()
else:
    print("O Valor 5 Não foi Digitado e Não está na lista.")
    print()
