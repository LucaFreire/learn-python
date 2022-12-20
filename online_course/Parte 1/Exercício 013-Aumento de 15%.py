#Faça um algoritmom que calcule um aumento de 15% de um salário.

atual=float(input("Digite seu salário atual: R$ "))
calculo=atual+(15/100)*atual
print(f"Seu Salário agora é de: R${calculo:.2f}")