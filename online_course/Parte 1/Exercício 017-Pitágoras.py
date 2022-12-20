'''Faça um programa que leia o comprimentodo do cateto oposto e do cateto adjacente de 
um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''

# Jeito Macho de se fazer:

opo=float(input("Cateto Oposto: "))
adj=float(input("Cateto Adjacente: "))
cal=(opo**2+adj**2)**(1/2)
print(f"Valor da Hipotenusa: {cal:.2f}")

# Nutella:

#import math # or from math import hypot
#opo=float(input("Cateto Oposto: "))
#adj=float(input("Cateto Adjacente: "))
#cal=math.hypot(opo,adj)
#print(f"Valor da Hipotenusa: {cal:.2f}")

