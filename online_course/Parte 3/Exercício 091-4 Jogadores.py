'''Crie um programa onde 4 jogadores joguem um dado e
tenham resultados aleatórios. Guarde esses resultados
em um dicionário. no final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''

# Variável.items(): Mostra apenas os itens
# Variável.keys(): Mostra os nomes (keys)
# Variável.values(): Mostra apenas os valores obtidos

from time import sleep
from random import randint
jogadas=dict()
COUNT=1

for i in range(1,5):
    jogadas[f'jogador {i}'] = randint(1,6)
    print(f"jogador {i} Obteve: {jogadas[f'jogador {i}']}")
    sleep(1)
print("\nOrdem dos Vencedores:\n")

for x in sorted(jogadas, key= jogadas.get, reverse=True):
    print(f'{COUNT}°: {x}')
    COUNT+=1
