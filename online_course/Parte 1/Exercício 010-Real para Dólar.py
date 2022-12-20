'''Crie um programa que leia quanto dinheiro a pessoa tem na carteira e diga quantos dólares a pessoa pode comprar
Considere o dólar á 4.76 (3/25/2022)'''

c=float(input("Digite quantos R$ você tem: "))
a=c/4.76
e=c/5.23
print(f'Com R${c} você consegue comprar U${a:.2f} e €{e:.2f}')