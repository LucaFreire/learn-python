'''Faça umprograma que leia um número de 0  a 9999 e mostre na tela cada um dos dígitos separados
Ex: número: 1834; unidade:4, dezena:3, centena:8, milhar:1. '''

a=int(input("Digite seu Número:  "))
u= a // 1 % 10
d= a // 10 % 10
c= a // 100 % 10
m= a // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
