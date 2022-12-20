'''Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços na sequência.No final mostre uma listagem de preços,
organizando os dados em forma tabular.'''

Lista=("Água", 2.50, "Pão", 3.50, "Chocolate", 5.00, "Livro", 10.00,
"Lanterna", 20.00, "Boné", 50.00, "Tênis", 100.00,"Relógio", 150.00,) 
count=0
print(39*"=")
print(f"{'Produtos e Preços':^39}")
print(39*"=")

for i in Lista:
    if count==0:
        print(f"{i:-<30}",end="") #print(f"{i}{10*'-'}",end="") Dessa maneira fica menos organizado
        count+=1
    else:
        print(f"R$ {i:.2f}")
        count=0
