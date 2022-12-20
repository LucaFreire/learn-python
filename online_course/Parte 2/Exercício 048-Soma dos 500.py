#Soma de todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
soma=0
count=0
for i in range(1,501):
    if not i%2==0 and i%3==0:
        soma+=i
        count+=1
print(f"Quantidade de Números:{count} /// Soma:{soma}  ")


