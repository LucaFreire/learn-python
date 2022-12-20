#Um programa que leia o peso de 5 pessoas.No final,
#Mostre qual foi o Menor e o Maior Peso lidos.
pes=0
maior=0
menor=0
count=1
for i in range(1,6):
    pes=float(input(f"Peso {count}° pessoa: kg "))

    if i==1:
        maior=pes
        menor=pes

    elif pes>maior:
        maior=pes

    elif pes<menor:
        menor=pes

    count+=1
    
print(f"Maior Peso: Kg {maior}")
print(f"Menor Peso: Kg {menor}")
