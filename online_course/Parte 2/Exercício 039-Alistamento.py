'''Faça um programa que leia o ano de nascimento de um jovem e mostre:
Se ele ainda vai se alistar; Mostre quanto tempo ainda falta 
Se é a hora de alistar
Se já passou do tempo de alistamento. Mostre quanto tempo já passou'''

from datetime import date
atual=date.today().year

ano=int(input("Digite Seu Ano de Nascimento: "))
age=atual-ano
print(f"Você Tem {age} Anos.")
if age<18:
    a=18-age
    print(f"Você Não Tem a Idade Para Se Alistar, em {a} Anos({atual+a}) Você Deverá Voltar Aqui!")
elif age==18:
    print("Você Está com 18 anos E Deverá Se Alistar Esse Ano!")
elif age>18:
    a=age-18
    print(f"Você Já Deveria Ter se Alistado Faz {a} Anos ({atual-a})!")
else:
    print("Digite um Número Válido!")
