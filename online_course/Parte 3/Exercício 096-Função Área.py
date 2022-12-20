'''Faça um programa que tenha uma função chamada area(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''

def soma(Larg,Comp):
    print(f"Área de Seu Terreno: {Larg*Comp}m²")

a=int(input("Largura: "))
b=int(input("Comprimento: "))
soma(a,b)
