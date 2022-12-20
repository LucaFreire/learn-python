'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base da conversão:
1 para binário
2 para oxtal
3 para hexadecimal'''

num=int(input("Digite um Número Inteiro: "))
print("""Escolha Sua Base De Conversão:
[ 0 ] p/ BINÁRIO
[ 1 ] p/ OCTAL
[ 2 ] p/ HEXADECIMAL
""")
esc=int(input("Número de Escolha: "))

if esc==0:
    print(f"{num} em BINÁRIO: {bin(num)[2:]}")
elif esc==1:
    print(f"{num} em OCTAL: {oct(num)[2:]}")
elif esc==2:
    print(f"{num} em HEXADECIMAL: {hex(num)[2:]}")
else:
    print("Número Inválido!")