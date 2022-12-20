'''Escreva um programa que pergunte dois números inteiros e compare-os.
Mostrando: O Primeiro Valor é Maior; O Segundo Valor é Maior;
Não Existe Valor Maior, os Dois São Iguais.'''

a=int(input("Digite seu Primeiro Número: "))
b=int(input("Digite seu Segundo Número: "))

if a==b:
    print("Não Existe Valor Maior, os Dois São Iguais.")
elif a>b:
    print("O Primeiro Número é Maior!")
else:
    print("O Segundo Número é Maior!")
