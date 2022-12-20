'''Faça um rpograma que leia um ângulo qualquer e mostre na tela 
o valor do seno, cosseno e tangente desse ângulo.'''

import math

ang=float(input("Digite o valor do ângulo: "))
sen=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang)) #radians transforma a operação para ângulos
tan=math.tan(math.radians(ang))
print(f"Cosseno:{cos:.2f}  Seno:{sen:.2f}  Tangente:{tan:.2f}")
