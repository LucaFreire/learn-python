'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida 
 o primeiro e o último nome separadamente.'''

nom=str(input("Digite seu nome: ")).strip().split()
print(f"Primeiro Nome: {nom[0].title()}")
print(f"Último Nome: {nom[-1].title()}") 

#No vídeo o cara utilizou o len() para contar o split e com o número do len() você coloca -1.
#Porém, é mais fácil colocar o -1, pois ele vai 'pegar' os split de trás pra frente.
