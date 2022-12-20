'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos vai quitar.
Calcule o valor da prestação mensal, sabnedo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.'''

casa=float(input("Digite o preço da casa: R$ "))
sal=float(input("Digite seu salário: R$ "))
ano=int(input("Digite em quntos anos vocâ quer quitar a casa: "))

parcela=casa/(ano*12)
print(f"Sua casa de R${casa} dividida em {ano} ano(s), custará R${parcela:.2f} p/mês.")
if 30/100/sal>=parcela:
    print("Você poderá comprar a casa!")
else:
    print("Você Não poderá comprar a casa!")
