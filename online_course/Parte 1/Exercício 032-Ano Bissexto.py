#Um programa que diz se o ano é bissexto ou não.

# Vídeo:

from datetime import date
ano=int(input("Digite o ano: "))
if ano == 0:
    ano=date.today().year
if ano%4==0 and ano%100 !=0 or ano%400==0:
    print(f'Em {ano}, o ano é Bissexto!')
else:
    print(f"Em {ano}, o ano NÃO é Bissexto")

    #Fiz pelo meme:

#ano=int(input("Digite o ano: "))
#dias=int(input(f"Digite a quantidade de dias no ano de {ano}: "))
#if dias >=367 or dias<=364:
#    print("Acho que você não vive nesse planeta!") 
#if dias==365:
#    print(f"{ano} é um ano comum!")
#if dias==366:
#    print(f"{ano} é um ano Bissexto!")    
