#Um programa que leia um número inteiro e diga se é primo ou não.

count=0
n=int(input("Digite seu Número: "))
for i in range(2,n):
    if n%i==0:
        print("Não é Primo.")
        count+=1
        break
if count==0:
    print("Primo!")
