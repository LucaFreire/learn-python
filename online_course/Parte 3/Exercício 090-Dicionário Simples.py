'''Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

dicionario={} # OU USAR dicionario=dict()
dicionario['nome'] = str(input("Digite seu Nome: "))
dicionario['media'] = float(input(f"Digite sua média {dicionario['nome']}: "))
if dicionario['media']>=7:
    dicionario['resultado'] = 'Aprovado'
    
elif 7> dicionario['media'] >=5 : # and dicionario['media'] <7:
    dicionario['resultado'] = "Recuperação"
    
else:
    dicionario['resultado'] = "Reprovado"
    
print(dicionario)
