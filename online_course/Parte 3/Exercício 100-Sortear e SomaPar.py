'''Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteia() e somapar().A primeira
função vai sortear 5 números e vai colocá-los dentro da 
lista e a segunda função vai mostrar a soma entre todos
os valores Pares sorteados pela função anterior.'''
from random import randint
from time import sleep
Números=list()
def sorteia():
    while True:
        if len(Números) == 5:
            print("Números Sorteados:", end=" " )
            for a in Números:
                print(a, end=" ", flush=True)
                sleep(0.3)
            break
        Sort=randint(1,101)
        while Sort not in Números:
            Números.append(Sort)
            
def somepar():
    cal=0
    print("\nNúmeros Pares:", end=" ")
    for i in Números:
        if i%2==0:
            print(i, end=" ",flush=True)
            sleep(0.3)
            cal+=i
    print(f"\nSoma dos Números Pares: {cal}")
         
sorteia()
somepar()
