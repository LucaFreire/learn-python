#Faça um programa utilizando o while que mostre a PA de um número

ter=int(input("Digite seu Termo: "))
raz=int(input("Digite sua Razão: "))

count=0
Pa=0
while 10!=count: 
    print(Pa+ter,end=" --> ")
    Pa+=raz
    count+=1
print("FIM")
