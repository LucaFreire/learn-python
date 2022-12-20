'''Um programa que leia o primeiro termo e a razão de uma PA(Progressão Aritmética).No final,
mostre os 10 primeiros termos dessa progressão.'''
ini=int(input("Primeiro Termo: "))
raz=int(input("Razão: "))

for i in range(ini, (ini+9*raz) + raz ,raz): #Fórmula: ini+(10-1)*raz (10: Décimo Termo)
    print(i,end=" --> ")
print("FIM")
