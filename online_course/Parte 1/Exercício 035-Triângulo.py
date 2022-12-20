#Um programa que leia 3 medidas e diga se é possível criar um triângulo ou não.
a=float(input("Digite sua Primeira medida: "))
b=float(input("Digite sua Segunda medida: "))
c=float(input("Digite sua Terceira medida: "))

if a+b>c and c+a>b and b+c>a:
    print("Com essas medidas, SIM é possível criar um triângulo!")
else:
    print("Com essas medidas, NÃO é possível criar um triângulo!")    