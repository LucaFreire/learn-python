'''Um programa que leia vários números(Até o usuário querer parar)
mostre no final: Média dos números, Maior e Menor Número.'''

num=0
count=1
maior=0
menor= 0
som=0
while True:
    num=int(input(f"Digite seu {count}° Número[-1 p/Sair]: "))

    if num<0:
        break

    elif count==1:
        maior=num
        menor=num 

    else:
        if maior<num:
            maior=num

        elif menor>num:
            menor=num

    som+=num
    count+=1
       
print(f"Maior:{maior}")
print(f"Menor: {menor}")
print(f"Média: {som/(count-1):.2f} ")
