from os import system

antes_rio=["C","C","C","A","A","A"]
barco=[]
depois_rio=[]

count=0

def display():
    system("cls")
    print(45*"-")
    print(f"""Antes do Rio: 
Canibais: {antes_rio.count('C')}
Antropólogos: {antes_rio.count('A')}\n
Depois do Rio:
Canibais: {depois_rio.count('C')}
Antropólogos: {depois_rio.count('A')}\n
Barco Atual: {barco}""")
    print(45*"-")

def regra():
    if antes_rio.count("C") > antes_rio.count("A") and antes_rio.count("A")!=0 or depois_rio.count("C") > depois_rio.count("A") and depois_rio.count("A")!=0:
        print("Canibal Comeu Gente!")
        return True
        
        
while True:

    count+=1
    if count==1:
        display()
        Quem1 = input("Primeiro Tripulante A ou C: ").upper()
        while Quem1!="A" and Quem1!="C":
            display()
            print("Escolha Inválida, Digite Novamente!")
            Quem1 = input("Primeiro Tripulante A ou C: ").upper()
        barco.append(Quem1)
        antes_rio.remove(Quem1)
        a=regra()
        if a==True:
            display()
            print("Canibal Comeu Gente!")
            break


    Quem2 = input("Segundo Tripulante A ou C: ").upper()
    while Quem2!="A" and Quem2!="C" or Quem2 not in antes_rio:
        display()
        print("Escolha Inválida, Digite Novamente!")
        Quem2 = input("Segundo Tripulante A ou C: ").upper()
        

    antes_rio.remove(Quem2)
    barco.append(Quem2)

    display()
    if len(barco)>2:
        print("Muita Gente no Barco!")
        break

    
    a=regra()
    if a==True:
        break

    esc=input(f"Quem Vai Sair do Barco?[{barco}]: ").upper()
    while esc!=barco[0] and esc!=barco[1]:
        print("Escolha Inválida, Digite Novamente!")
        esc=input(f"Quem Vai Sair do Barco?[{barco}]: ").upper()   
    depois_rio.append(esc)
    barco.remove(esc)

    a=regra()
    if a==True:
        break

    if len(antes_rio)==0:
        print("\nAcabou, Todos os Antropólogos e Canibais atravessaram o rio!")
        break

    display()

print("\nFim")
