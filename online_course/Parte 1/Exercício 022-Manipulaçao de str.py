'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (sem considerar os espaços).
Quantas letras tem o primeiro nome. '''

nom=str(input("Digite seu nome: ")).strip() 
div=nom.split() 
print(f'Tudo Maiúsculas: {nom.upper()}')
print(f'Tudo Minúsculas: {nom.lower()}')
print(f'Quantas letras nome completo: {len(nom) - nom.count(" ")}')
print(f'Quantas letras o primeiro nome: {len(div[0])}')