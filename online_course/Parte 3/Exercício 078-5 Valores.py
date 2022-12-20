'''Faça um programa que leia 5 valores numéricos e guarde-os
em uma lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista'''

lista=[]
maior=[]
menor=[]
for i in range(1,6):
    lista.append(int(input(f"Digite seu {i}° Número: ")))

for count, j in enumerate(lista): #count='Contador' , j= Elementos do parênteses 
    if j == max(lista):
        maior.append(count+1)
    
    elif j == min(lista):
        menor.append(count+1)

print(f"Maior Número: {max(lista)} -- Posição: {maior}")
print(f'Menor Número: {min(lista)} -- Posição: {menor}')
