'''Crie um programa que leia vários números interios.O programa 
só vai parar quando o usuário digitar o valor 999(condição de parada)
No final mostra quantos números foram digitados e a soma. '''
num=0
soma=0
cont=0
while True:
    a=int(input(f"Digite seu {num} Número: "))
    if a==999:
        break
    else:
        num+=1
        cont+=1
        soma+=a
print(f"Soma: {soma} --- Quantiade de Números Digitados: {cont}")

