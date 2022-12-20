'''Um programa que calcule o valor a ser pago por um produto,
considerando seu preço normal e condição de pagamento:

à vista dinheiro/cheque: -10%
à vista no cartão:-5%
2X no cartão:Preço Normal
3x ou mais no cartão:+20% de juros'''

print(f'{"Lusquinha Loja":~^40}')
pre=float(input("Digite o Valor da Compra: R$ "))
print("""[0]à vista dinheiro/cheque: -10%
[1]á vista cartão: -5%
[2]2x no cartão:Preço Normal
[3]3x ou mais no cartão:+20% juros""")
met=int(input("Digite seu Método de Pagamento: "))

if met==0:
    print(f"Sua compra agora é R${pre-(10/100*pre):.2f}.")
elif met==1:
    print(f"Sua compra agora é R${(pre-5/100*pre):.2f}.")
elif met==2:
    print(f"Sua compra agora é R${pre:.2f}")        
elif met==3:
    print(f"Sua compra agora é R${pre+(20/100*pre):.2f}.")
else:
    print("Digite um valor Válido")        