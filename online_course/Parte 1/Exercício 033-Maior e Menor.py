#Um programa que leia 3 números e diga o maior e menor número.

print(30*"=")
a=float(input("[A] Digite seu Primeiro Número: "))
b=float(input("[B] Digite seu Segundo Número: "))
c=float(input("[C] Digite seu Terceiro Número: "))
print(36*"=") 
if a>b>c:
    print(f"[A] é o maior: {a} e [C] é o menor: {c}")
if a>c>b:
    print(f"[A] é o maior: {a} e [B] é o menor: {b}")
if b>a>c:
    print(f"[B] é o maior: {b} e [C] é o menor: {c}")
if b>c>a:
    print(f"[B] é o maior: {b} e [A] é o menor: {a}")
if c>a>b:
    print(f"[C] é o maior: {c} e [B] é o menor: {b}")
if c>b>a:
    print(f"[C] é o maior: {c} e [A] é o menor: {a}")
if a==b or b==c or a==c:
    print("Valores Repetidos, Tente Novamente!")    


#Vídeo:

#a=float(input("[A] Digite seu Primeiro Número: "))
#b=float(input("[B] Digite seu Segundo Número: "))
#c=float(input("[C] Digite seu Terceiro Número: "))

#menor = a           Ele ja considera uma variável como menor e maior,
#if a>b and c<b:      Sendo assim não é necessário testar ela.
#   menor=c
#if a>c and c>b:
#    menor=b
#maior=a
#if c>b and c<a:
#    maior=c
#if c<b and b>a:
#    maior=b
#print(f'Menor: {menor}')
#print(f'Maior: {maior}')        



