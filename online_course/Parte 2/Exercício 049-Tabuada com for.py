#Tabuada com for.

num=int(input("Tabuada do 1 ao: "))
count=1
if num==0:
    print("Todos os Resultados=0")

for i in range (1,num+1):
    print()
    print(f"Tabuada do {count}")
    count+=1

    for a in range(1,11):
        print(f"{i} X {a} = {i*a}")

#Tabuada Simples

#num=int(input("Digite seu Número: "))
#for i in range(1,11):
#    print(f"{i} X {num} = {i*num}")
