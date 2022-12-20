'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. Mostre:

A)Qual é o total gasto na compra.
B)Quantos produtos custam mais de R$1000.
C)Qual é o nome do produto mais barato.'''

soma=0
caro=0
count=1
barato=0
nome=" "

while True:
    nom=str(input(f"Nome do {count}° Produto: ")).strip()
    pre=float(input("Preço: R$ "))

    if pre>=1000:
        caro+=1
    
    if count==1:
        barato=pre
        nome=nom
         
    elif pre<barato:
        barato=pre
        nome=nom

    soma+=pre
    count+=1
    print(15*"~~")
    esc=int(input("[0]p/ Sair e [!=0]p/ Continuar: "))
    print(15*"~~")
    if esc==0:
        break

print(f"Total Gasto: R${soma:.2f}")
print(f"Produtos Mais de R$1000: {caro}")
print(f"Produto Mais Barato: {nome} (R${barato:.2f})")
