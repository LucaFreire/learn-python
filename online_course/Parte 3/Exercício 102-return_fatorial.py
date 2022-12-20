"""Crie um programa que tenha função fatorial() que receba
dois parâmetros: o primeiro que indique o número a calcular 
e o outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo
do fatorial"""

def fatorial(num=1,show=False):
    #Comentário p/ help(fatorial)
    '''num: Número p/ Fatoração
    True = Mostra o cálculo
    False = Mostra apenas o resultado (Padrão)'''
    print(f"Fatorial de {num}:", end=" ")
    #Cálculo
    Numero=1
    for i in range(num,0,-1):
        Numero*=i
        #Mostra o cálculo
        if show:
            if i>1:
                print(i,end=" x ")
            else:
                print(i,end=" = ")
    #Retorna o resultado
    Valor=Numero
    return Valor
#help(fatorial) 
Resultado=fatorial(5)
print(Resultado)
