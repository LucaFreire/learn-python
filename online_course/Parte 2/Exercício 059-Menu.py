'''Crie um programa que leia dois valores e mostre o menu abaixo e que faça o solicitado:

[ 1 ] p/ somar
[ 2 ] p/ multiplicar
[ 3 ] p/ mostrar o n° maior
[ 4 ] p/ novos números 
[ 5 ] p/ sair do programa '''

num1=int(input("Digite seu Primeiro Valor: "))
num2=int(input("Digite seu Segundo Valor: "))
escolha=0
while True:
    print('''
[ 1 ] p/ Somar
[ 2 ] p/ Multiplicar
[ 3 ] p/ Mostrar o N° Maior
[ 4 ] p/ Novos Números 
[ 5 ] p/ Sair do Programa
''')
    escolha=int(input("Digite seu Número de Escolha: "))
    print()

    if escolha==1:
        print(f"Soma: {num1} + {num2} = {num1+num2}")
    
    elif escolha==2:
        print(f"Multiplicação: {num1} X {num2} = {num1*num2}")
    
    elif escolha==3:
        if num1>num2:
            print(f"Número Maior: {num1}")
        elif num1<num2:
            print(f"Número Maior: {num2}")
        else:
            print("São os Mesmos Valores.")
    
    elif escolha==4:
        print("Substituir os Valores")
        print()
        num1=int(input("Digite seu Primeiro Valor: "))
        num2=int(input("Digite seu Segundo Valor: "))

    elif escolha==5:
        break

    else:
        print("Número de Escolha Inválido, Tente Novamente!")

print("você Saiu do Programa.")
