'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por exetnso, de zero até vinte.Seu Programa deverá ler um número pelo teclado 
entre (0 e 20) e mostrá-lo por extenso.'''

num=('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ',
'ONZE','DOZE','TREZE','CATORZE','QUINZE','DEZESEIS','DEZESETE','DEZOITO','DEZENOVE','VINTE')

for i in num:
    esc=int(input("Digite um Número entre 0 e 20: "))

    if 0>esc or esc>20:
        break
    else:
        print(f"{esc} = {num[esc]}")

print("Você Saiu")
