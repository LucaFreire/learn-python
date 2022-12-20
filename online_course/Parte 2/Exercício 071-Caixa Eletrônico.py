'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunta ao usuário qual será o valor a ser sacado(n° inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs: considere cédulas de R$50, R$20, R$10 e R$1.'''

ced50=ced20=ced10=ced1=0
val=int(input("Valor a Sacar: R$ "))
sobra=val
while True:
    
    while sobra-50>=0: #Se utilizado o if, são tipos diferentes de cálculo, mas funciona...
        sobra-=50
        ced50+=1

    while sobra-20>=0:
        sobra-=20
        ced20+=1

    while sobra-10>=0:
        sobra-=10
        ced10+=1
    
    while sobra-1>=0:
        sobra-=1
        ced1+=1
    
    if sobra<=0:
        print("~~~~~~ Cédulas e Moedas ~~~~~~")
        print(f"Cédulas de R$50: {ced50:.0f}")
        print(f"Cédulas de R$20: {ced20:.0f}")
        print(f"Cédulas de R$10: {ced10:.0f}")
        print(f"Moédas de R$1: {ced1:.0f}")
        print()
        print("Deseja Continuar? Digite 0 Caso Queira Sair")
        val=int(input("Valor a Sacar: R$ "))
        if val==0:
            break
        sobra=val
        ced50=ced20=ced10=ced1=0
    
print("Você Saiu!")
