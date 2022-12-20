'''Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-os(com idade) em um dicionário
se por acaso a CTPS for diferente de 0, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date
import os
Dicionario=dict()

while True:
    Dicionario['Nome'] = str(input("Nome: ")).title()
    Idade = int(input("Ano de Nascimento: "))
    Dicionario['Idade'] = date.today().year - Idade
    Dicionario['CTPS'] = int(input("CTPS (0 Caso Não Tenha): "))
    if Dicionario['CTPS'] != 0:
        Dicionario['Ano de Contratação'] = int(input("Ano de Contratação: "))
        Dicionario['Salário'] = float(input("Salário:R$ "))
# Cálculo de Aposentadoria
        Contribuição=date.today().year - Dicionario['Ano de Contratação']
# Tem e Idade e Contribuição
        if Contribuição>=35 and Dicionario['Idade']>=65:
            Dicionario['Aposentadoria'] = "Aposentado"
# Não tem a Contribuição Necessária
        elif Contribuição>=35 and Dicionario['Idade']>=65:
            Dicionario['Aposentadoria'] = (f"Faltam {35-Contribuição}\
Anos de Contribuição\nE Você Já Tem a Idade de se Aposentar")
# Não Tem a Idade Necessária
        elif Contribuição>=35 and Dicionario['Idade']<=65:
            Dicionario['Aposentadoria'] = (f"Você Já tem a Contribuição Necessária\n\
Porém Faltam {65-Dicionario['Idade']} Anos Para Ter a Idade Necessária(65)")
# Não tem Ambos
        elif Contribuição<=35 and Dicionario['Idade']<=65:
            Dicionario['Aposentadoria'] = (f"Faltam {35-Contribuição} Anos de Contribuição\n\
E {65-Dicionario['Idade']} Anos Para Ter a Idade Necessária(65)")
# Visualização do Dicionário
    os.system("cls")
    for i in Dicionario:
        print(f"{i}: {Dicionario[f'{i}']}")
# Escolha de Continuação
    ESC=str(input("Deseja Continuar?[S/N]\n")).title()
# Caso seja Escolha Inválida
    while ESC[0]!="N" and ESC[0]!="S":
        os.system("cls")
        print("Escolha Inválida!")
        ESC=str(input("Deseja Continuar?[S/N]\n")).title()
    if ESC[0]=="N":
        break
print("Você Saiu")
