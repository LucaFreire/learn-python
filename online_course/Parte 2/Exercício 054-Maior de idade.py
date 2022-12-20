'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date

agr=date.today().year

count=1
maior=0
menor=0
mut=0

for i in range (1,8):
    nasc=int(input(f"Ano de Nascimento da {count}° Pessoa: "))
    if agr-nasc>=18:
        maior+=1
    elif nasc>agr:
        mut+=1
    elif not agr-nasc>=18:
        menor+=1
    
    count+=1

if mut==0:
    print(f"Das 7 pessoas analisadas, {maior} são Maiores e {menor} são menores.")
else:
    print(f"{mut} são Mutantes que Ainda Não Nasceram... ")
    print(f"Das 7 pessoas analisadas, {maior} são Maiores e {menor} são Menores de Idade.")
    