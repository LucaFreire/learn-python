"""Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de
uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto negado, opcional ou obrigatório nas eleições"""

def voto(ano):
    #Se a biblioteca for usada somente nessa função,
    #posso simplesmente colocar dentro dela
    from datetime import date
    #Ano atual
    hoje=date.today().year
    #Cálculo de idade
    idade=hoje-ano
    #Idade entre 18 e 64
    if idade>=18 and idade<65:
        voto=f"Idade {idade}: Voto Obrigatório"
    #Iadade entre 16 e 18 ou +65
    elif idade>=16 and idade<18 or idade>=65:
        voto=f"Idade {idade}: Voto Opcional"
    #Menor de 16
    elif idade<16:
        voto=f"Idade {idade}: Não Vota"
    #Retorna a situação do voto
    return voto


ano=int(input("Ano de Nascimento: "))
situação=voto(ano)
# OU: situação=voto(int(input("Ano de Nascimento: ")))
print(situação)
