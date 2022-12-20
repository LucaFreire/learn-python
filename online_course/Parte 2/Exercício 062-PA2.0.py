'''Melhore o desafio 061, perguntando para o usuário se ela quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar os termos.ter'''

ter=int(input("Digite o Termo: "))
raz=int(input("Digite a Razão: "))

termos=10
count=0
cálculo=0
quan=0

while True:  
    count+=1

    if count==termos:
        print(ter+cálculo)
        quan+=1
    else:
        print(ter+cálculo,end=" --> ")
        quan+=1
    cálculo+=raz
    
    if count==termos:
        termos=int(input("Digite a Quantidade de Termos: "))
        if termos==0:
            break
        else:
            count=0

print("Você Saiu!")
print(f"Quantidade de Termos Mostrados: {quan}")
