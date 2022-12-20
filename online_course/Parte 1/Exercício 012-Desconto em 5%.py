#Crie um programa que calcule 5% de desconto

valor=float(input("Valor antes do desconto R$: "))
desconto=valor - (5/100*valor)
print(f"Valor antes do Desconto: R${valor}\n Valor após desconto de 5%: R${desconto:.2f}")