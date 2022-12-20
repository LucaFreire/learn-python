'''Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da finção criada:

A)De 1 até 10, de 1 em 1
B)De 10 até 0, de 2 em 2
C)Uma contagem personalizada'''

from time import sleep
def contador(inicio,fim,passo):
# A)    
    print("\nA) De 1 até 10, de 1 em 1:")
    for i in range(0,11):
        print(i, end=" ", flush=True) #Sem o flush=True, a animação ñ funciona
        sleep(0.3)
# B)   
    print("\n\nB) De 10 até 0, de 2 em 2:")
    for j in range(10,-1,-2):
        print(j, end=" ", flush=True)
        sleep(0.3)
# C)        
    print(f"\n\nC) Contagem Personalizada:")
#Se passo precisar ser neg. 
    if fim<inicio and 0<passo:
        passo=-passo
        fim= fim - 1
#Se apenas o fim for negativo        
    elif fim<=0 and 0>passo:
        fim= fim - 1
#Fim maior que início e passo neg.
    elif fim>inicio and passo<0: 
        passo=-passo
        fim= fim + 1 
#Se tudo for positivo
    else: 
        fim+=1
    for k in range(inicio,fim,passo):
        print(k, end=" ", flush=True)
        sleep(0.3)
a=int(input("Início: "))
b=int(input("Fim: "))
c=int(input("Passo: "))
contador(a,b,c)
