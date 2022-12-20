'''Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. '''


MATRIZ=[[0,0,0], [0,0,0], [0,0,0]]
SOMA_TOTAL=0
#INPUT
for i in range(0,3):
    for j in range(0,3):
        MATRIZ[i][j]=int(input(f"Digite o Valor de [{i},{j}]: "))
        SOMA_TOTAL+=MATRIZ[i][j]
#OUTPUT
for a in range(0,3):
    for b in range(0,3):
        print(f"[{MATRIZ[a][b]:^5}]", end="")
    print()

MAIOR=max(MATRIZ[1][0], MATRIZ[1][1], MATRIZ[1][2])

#A)
print(f"soma da Matriz: {SOMA_TOTAL}")
#B)
print(f"Soma da Última Coluna: {MATRIZ[0][2]+MATRIZ[1][2]+MATRIZ[2][2]}")
#C)
print(f"Maior Valor da Segunda Linha: {MAIOR}")
