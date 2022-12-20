'''Crie um programa que crie uma  matriz de 3x3 e preencha
com valores lidos pelo teclado.'''


MATRIZ=[[0,0,0], [0,0,0], [0,0,0]]

#INPUT
for i in range(0,3):
    for l in range(0,3):
        MATRIZ[i][l]=int(input(f"Digite a sua [{i},{l}] Posição:  "))
#OUTPUT
for a in range(0,3):
    for b in range(0,3):
        print(f"[{MATRIZ[a][b]:^5}]", end="") # :^5 == Organiza os Espaços
    print()

# Método Não Prático

#pos0=int(input("Número da Posição [0,0]:"))
#pos1=int(input("Número da Posição [0,1]:"))
#pos2=int(input("Número da Posição [0,2]:"))
#pos3=int(input("Número da Posição [1,0]:"))
#pos4=int(input("Número da Posição [1,1]:"))
#pos5=int(input("Número da Posição [1,2]:"))
#pos6=int(input("Número da Posição [2,0]:"))
#pos7=int(input("Número da Posição [2,1]:"))
#pos8=int(input("Número da Posição [2,2]:"))

#print(f'''\nMATRIZ:
#[ {pos0} ] [ {pos1} ] [ {pos2} ]
#[ {pos3} ] [ {pos4} ] [ {pos5} ]
#[ {pos6} ] [ {pos7} ] [ {pos8} ]''')
