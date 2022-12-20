'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição aparece a primeira e a última vez.'''

x= str(input("Digite seu nome: ")).strip().lower()
print(f'Seu nome tem {x.count("a")} a(s)')
print(f'A primeira vez está em {(x.find("a")+1)-(x.count(" "))}°')
print(f'A última vez está em {(x.rfind("a")+1)-(x.count(" "))}°')