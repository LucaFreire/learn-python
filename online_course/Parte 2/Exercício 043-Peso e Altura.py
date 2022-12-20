'''Calcule o IMC de uma pessoa e mostre seu status.Tabela: 
 Abaixo de 18.5:Abaixo do Peso
Entre 18.5 e 25: Peso Ideal
25 até 30:Sobrepeso
30 até 40:Obesidade
Acima de 40: Obesidade Mórbida

Fórmula: Kg/m²'''

peso=float(input("Digite Seu Peso: Kg "))
metros=float(input("digite Seu Tamanho Em Metros: "))
cal=peso/(metros**2)
print(f"O IMC dessa pessoa é {cal:.1f}")
if cal<18.5:
    print("Abaixo do Peso!")
elif cal>=18.5 and cal<=25: #Vídeo: elif 18.5 <= cal < 25:
    print("Peso Ideal!")
elif cal>25 and cal<=30:
    print("Sobrepeso!")
elif cal>30 and cal<=40:
    print("Obesidade!")
elif cal>40:
    print("Obesidade Mórbida!")      