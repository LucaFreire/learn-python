'''Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final nostre os valores pares e ímpares em ordem crescente.'''


números=[[] , []]
for i in range (1,8):
    num=int(input(f"Digite seu {i}° Número: "))
    if num%2==0:
        números[0].append(num)
    else:
        números[1].append(num)

print(f"Pares: {sorted(números[0])}")
print(f"Ímpares: {sorted(números[1])}")

#OU 
#números.sort[0]
#números.sort[1] 
#print(f"Pares: {números[0]}")
#print(f"Ímpares: {números[1]}")
