'''Um programa que leia o sexo e idade de várias pessoas.A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer continuar.

 No final mostre:

A)Quantas pessoas tem mais de 18 anos
B)Quantos homens foram cadastrados
C)Quantas mulheres tem menos de 20 anos'''

men=0
maior=0
mul=0


while True:

    sexo=str(input("Sexo [M/F]:")).strip().upper()[0]
    if sexo !="M" and sexo!="F":

        print("Sexo Inválido, Digite Novamente!")
   
    else:
        idade=int(input("Idade: "))
        if idade>=18:
            maior+=1
            if sexo=="M":
                men+=1

        if sexo=="F" and idade<20:
            mul+=1

        esc=int(input("[0]p/ Sair e [!=0]p/ Continuar: "))

        if esc==0:
            break
        
print(f"Maiores de idade: {maior}")
print(f"Homens Cadastrados: {men}")
print(f"Mulheres abaixo de 20 anos: {mul}")
