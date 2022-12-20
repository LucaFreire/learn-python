'''Crie uma tupla com os 20 primeiros clocados da tabela do Brasileirão,
Na ordem de colocação.Depois mostre: (11/5/2022)BR

A)Apenas os 5 Primeiros Colocados
B)Os Últimos 4 colocados da tabela 
C)Uma Lista com os Times em Ordem Alfabética
D)Em que posição na Tabela está o Time Coritiba'''

tab=('Corinthians', 'Santos', 'Avaí' ,'América-MG', 'Bragantino', 'São Paulo' ,'Atlético-MG', 'Botafogo',
'Internacional' ,'Coritiba', 'Cuiabá', 'Athletico-PR', 'Palmeiras', 'Flamengo', 'Fluminense', 'Goiás', 
'Ceará', 'Juventude', 'Atlético-GO', 'Fortaleza')


print(10*"~~")

count=1
print('Top 5:')
for i in tab[0:5]:
    print(f"{count}° {i}")
    count+=1

print(10*"~~")

count=17
print('Últimos 4:')
for i in tab[-4:]:
    print(f"{count}° {i}")
    count+=1

print(10*"~~")

print("Ordem Alfabética:")
for i in sorted(tab):
    print(i)

print(10*"~~")

print(f"Coritiba: {tab.index('Coritiba')+1}° Posição")

print(10*"~~")

