'''Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla.
No final mostre:

A)Quantas vezes aparece o valor 9
B)Em que posição foi digitado o primeiro valor 3
C)Quais foram os números pares'''

'''num1=int(input("Digite o Seu 1° Valor: "))
num2=int(input("Digite o Seu 2° Valor: "))
num3=int(input("Digite o Seu 3° Valor: "))  #Funciona, porém o código fica maior
num4=int(input("Digite o Seu 4° Valor: "))

nums=num1,num2,num3,num4'''

nums=(int(input("Digite o Seu 1° Valor: ")), #Dessa Maneira é Mais Simples
int(input("Digite o Seu 2° Valor: ")),
int(input("Digite o Seu 3° Valor: ")),
int(input("Digite o Seu 4° Valor: ")))

print()
print("~~~~ Valores Pares ~~~~")
for i in nums:
 
    if i%2==0:
        print(i,end=" ")
    
print()
print(f'Números 9 Digitados: {nums.count(9)}')
print()
if nums.count(3)>=1: # --Vídeo-> if 3 in nums:
    print(f'Primeira Posição que o Número 3 foi Digitado: {nums.index(3)+1}°')
else:
    print("Nenhum 3 foi Digitado")
print()
