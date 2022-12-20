'''Crie um programa onde o usuário digita um valor qualquer
que use parênteses. Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta'''

expressão=str(input("Digite sua Expressão: "))

count=0
for i in expressão:

    if i=="(":
        count+=1

    elif i==")":
        count-=1
        
    if count < 0:
        print("Inválido...")
        break

if count==0:
    print("Válido!!!")
