'''Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.'''
def escreva(txt):
    print(f"{(len(txt)+2)*'-'}")
    print("",txt)
    print(f"{(len(txt)+2)*'-'}")

    
a=str(input("Digite Algo: ")).upper()
escreva(a)
# OU escreva("Mensagem")