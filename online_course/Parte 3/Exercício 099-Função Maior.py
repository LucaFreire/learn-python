'''Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e 
dizer qual deles qual delas é o maior.'''
from time import sleep
def maior(*num):
    print("Números:", end=" ")
    for i in num:
        print(i, end=" ", flush=True)
        sleep(0.3)
    print(f"\n\nQuantidade de Números: {len(num)}\n")
    if len(num)==0:
        print("Nenhum Valor Informado!")
    else:
        print(f"Maior Número: {max(num)}")
    print(30*"-=")
    
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()