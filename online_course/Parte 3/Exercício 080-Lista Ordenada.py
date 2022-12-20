'''Crie um programa onde o usuário possa digitar cinco valores 
numéricos e cadastre-os em uma lista, já na posição correta 
da inserção (sem usar o sort()).No final, mostre a lista ordenada'''

lista=[]
Crescente=[]
Decrescente=[]
count=0
for i in range(1,6):
    lista.append(int(input(f"Digite seu {i}° Número: ")))
print(45*"=")
print(f'Lista Digitada: {lista}')
print(45*"=")

while count!=5:

    Crescente.insert(0,max(lista))
    Decrescente.append(max(lista))
    lista.remove(max(lista))
    count+=1

print(f'Lista em Ordem Crescente: {Crescente}')
print(45*"=")
print(f'Lista em Ordem Decrescente: {Decrescente}')
print(45*"=")
