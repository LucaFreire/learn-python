#Crie um progrma que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome

a=input("Digite seu nome: ").strip() 
b=a.upper() 
print(f'Seu nome tem Silva? {"SILVA" in b}')
