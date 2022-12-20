'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No Final, Mostre:
-A média de idade
-Qual é o nome do homem mais Velho
-Quantas mulheres têm menos de 20 anos'''

soma=0
velho=0
nome_velho=" "
mulher=0

for i in range (1,5):
    print()
    print(f"---Dados da {i}° Pessoa---")
    
    nom=str(input("Nome: ")).upper().strip()

    ida=int(input("Idade: "))
    if ida>velho:
        velho=ida
        nome_velho=nom

    sex=str(input("Sexo (M/F): ")).upper().strip()

    if sex!="F" and sex!="M":
        print("Sexo Inválido!")

    elif sex=="F" and ida<20:
        mulher+=1

    soma+=ida
    
print()
print(f"Média das Idades: {soma/i:.2f}")
print(f"Homem Mais Velho: {nome_velho}, com {velho} anos")
print(f"Mulheres menores de 20 anos: {mulher}")
