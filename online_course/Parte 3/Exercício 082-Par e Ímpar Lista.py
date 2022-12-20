'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas valores
Pares e os valores Ímpares digitados.
No final, mostre o conteúdo das três listas geradas'''

Todos=[]
Ímpares=[]
Pares=[]
print("Digite um Número Negativo p/ Sair")
while True:
    num=int(input("Digite seu Número: "))
    if num<0:
        break
    Todos.append(num)
    if num%2==0:
        Pares.append(num)
    else:
        Ímpares.append(num)

print(f'Todos os Valores: {Todos}')
print(f'Valores Ímpares: {Ímpares}')
print(f'Valores Pares: {Pares}')
