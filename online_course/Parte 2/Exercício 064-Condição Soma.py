'''Um programa que leia vários números interios, o programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles.'''

num=0
count=1
som=0
while True:
    
    num=int(input(f"Digite seu {count}° Número [999 p/Sair]: "))
    if num==999:
        break
    else:
        som+=num
        count+=1
    
print(f"Qunatidade de Números Digitados: {count-1} /// Soma: {som}")

