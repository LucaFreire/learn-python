'''Um programa que calcule a média de 2 notas, mostrando:
Média Abaixo de 5.0: Reprovado
Média entre 5.0 e 6.9: Recuperação
Média 7.0 ou superior: Aprovado'''

nota=float(input("Digite sua Primeria nota: "))
notb=float(input("Digite sua Segunda nota: "))

cal=(nota+notb)/2

if cal<5.0:
    print(f"Sua nota é {cal:.1f}; Reprovado")
elif cal>=5.0 and cal<=6.9:
    print(f"Sua nota é {cal:.1f}; Recuperação")
elif cal>= 7.0:
    print(f"Sua nota é {cal:.1f}; Aprovado")
else:
    print("Nota Inválida!")            