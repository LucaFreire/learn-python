'''Aumento de salário, se ganhar mais de que R$1250, calcule um aumento de 10%, 
para salários inferiores ou iguais, calcule um aumento de 15%'''
a=float(input("Digite seu salário: R$"))
if a>=1250:
    au=(10/100*a)+a
    print(f"De {a} você agora vai ganhar R${au:.2f}.(Aumento de 10%)")
else:
    aul=(15/100*a)+a
    print(f"De {a} você agora vai ganhar R${aul:.2f}.(Aumento de 15%)")    