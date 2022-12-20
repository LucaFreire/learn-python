#Desenvolva um programa que leia seis números inteiros e mostre a soma dos que forem pares.
count=1
soma=0
for i in range (1,7):
    num=int(input(f"Digite o Valor do Número {count}: "))
    if num%2==0:
        soma+=num
    count+=1
print(f"Soma dos Números Pares: {soma}")
