'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo a todas as informações possíveis sobre ela.'''

n=input("Escreva algo: ")
print(f'Tipo primitivo: {type(n)}')
print(f'É um número? {n.isnumeric()}')
print(f'É letra? {n.isalpha()}')
print(f'Tem letra, número ou letra com número? {n.isalnum()}')
print(f'É somente espaços? {n.isspace()}')
print(f'É tudo em maiúsculas? {n.isupper()}')
print(f'É tudo em minúsculas? {n.islower()}')
print(f'Está capitalizada? {n.istitle()}')
if n=="":
    print("Nada foi digitado? True")
else:
    print("Nada foi digitado? False")    


#print(type(n)):Mostra o tipo de algo que foi digitado.

#n.isnumeric: é um número? True ou False

#n.isalpha(): é letra? True ou False

#n.isalnum(): tem letra, número ou letra e número?

#n.isupper(): somente letras maiúsculas?

#n.isspace(): somente espaços?

#n.istitle(): está com maiúsculas e minúsculas?

#               OU

#n=input("Escreva algo: ")
#print("Tipo Primitivo: ",type(n))
#print('É um número?',n.isnumeric())
#print("É letra?",n.isalpha())
#print("Tem letra, número ou letra e número?",n.isalnum())
#print("É somente espaços?",n.isspace())
#print("É tudo maiúsculas?",n.isupper())
#print("Tudo em mínusculas?",n.islower())
#print("Está capitalizada?",n.istitle())


  