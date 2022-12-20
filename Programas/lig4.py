#Para apagar terminal
from os import system

Matriz=[]
Vetor=[]

# Criando Tabuleiro
def Criar_Tabuleiro():
    for i in range(6):
        for j in range(7):
            Matriz.append(Vetor)       
            for k in range(0,len(Matriz)):
                Matriz[k]=" "
Criar_Tabuleiro()


# Mostrando Tabuleiro
def Mostrar_Tabuleiro():
    count=0
    print(17*"=","TABULEIRO",17*"=")
    print("\n    1     2     3     4     5     6     7\n")
    for i in Matriz:
        print(f" | {i}",end="  ")
        count+=1
        if count==7:
            print(" |")
            count=0
    print(45*"=")


# Gravidade das Colunas
def Gravidade(a,b,c,d,e,f,x="X"):  
    while True:
        # Linha 1
        if Matriz[a]==" ":# Verificação de um Vetor 
            Matriz[a]=x # Símbolo: X ou O
            break
        # Linha 2          
        elif Matriz[b]==" ":
            Matriz[b]=x
            break
        # Linha 3           
        elif Matriz[c]==" ":
            Matriz[c]=x
            break
        # Linha 4           
        elif Matriz[d]==" ":
            Matriz[d]=x
            break
        # Linha 5          
        elif Matriz[e]==" ":
            Matriz[e]=x
            break
        else:
        # Linha 6
            Matriz[f]=x
            break      


# Vereficação p/ ver se coluna já está cheia        
def Verify(a,b):
    if Matriz[a]=='X' or Matriz[a]=='O':
        system("cls")
        print(f"Erro: Coluna {b} já está cheia!")
        return True


# Funções Para vereficar se nome inserido está vazio
def Nomee1(Nome):
    if Nome=="":
        Nome="Estranho 1"
    return Nome
    
def Nomee2(Nome):
    if Nome=="":
        Nome="Estranho 2"
    return Nome
    

# Main
def main():

    print(18*"=","LIG4",18*"=")
    Input_Primeiro_Jogador=input("\nNome do 1° Jogador: ").strip()
    Input_Segundo_Jogador=input("\nNome do 2° Jogador: ").strip()
    system("cls")
    Nome1=Nomee1(Input_Primeiro_Jogador)
    Nome2=Nomee2(Input_Segundo_Jogador)
    count=1

    while True:
        # Cálculo p/ definir jogador 1 ou 2
        if count%2==0:
            Nome=Nome2
        else:
            Nome=Nome1
            
        Mostrar_Tabuleiro()
        # while p/ tratamento de erros
        while 1:
            try:
                
                # Número da Coluna
                Escolha_Jogador=int(input(f"{Nome}, insira seu Número entre 1 e 7: "))            
                               
                # Escolha do Jogador==1
                if Escolha_Jogador==1:
                    
                    # Vereficação p/ ver se coluna já está cheia
                    if Verify(0,1) == True:
                        break
                    
                    # Preenchendo a coluna número 1              
                    if Nome==Nome2:
                        Gravidade(35,28,21,14,7,0,"O")#Símbolo p/ Jogador 2("O")
                    else:
                        Gravidade(35,28,21,14,7,0)#Símbolo p/ Jogador 1("X")
                        
                # Escolha do Jogador==2 
                elif Escolha_Jogador==2:
                    if Verify(1,2) == True:
                        break                  
                    if Nome==Nome2:    
                        Gravidade(36,29,22,15,8,1,"O")
                    else:
                        Gravidade(36,29,22,15,8,1)
                        
                # Escolha do Jogador==3       
                elif Escolha_Jogador==3:
                    if Verify(2,3) == True:
                        break
                    if Nome==Nome2:
                        Gravidade(37,30,23,16,9,2,"O")
                    else:
                        Gravidade(37,30,23,16,9,2)
                
                # Escolha do Jogador==4           
                elif Escolha_Jogador==4:
                    if Verify(3,4) == True:
                        break
                    if Nome==Nome2:
                        Gravidade(38,31,24,17,10,3,"O")
                    else:
                        Gravidade(38,31,24,17,10,3)
                        
                # Escolha do Jogador==5
                elif Escolha_Jogador==5:
                    if Verify(4,5) == True:
                        break
                    if Nome==Nome2:
                        Gravidade(39,32,25,18,11,4,"O")
                    else:
                        Gravidade(39,32,25,18,11,4)
                
                # Escolha do Jogador==6    
                elif Escolha_Jogador==6:
                    if Verify(5,6) == True:
                        break
                    if Nome==Nome2:
                        Gravidade(40,33,26,19,12,5,"O")
                    else:
                        Gravidade(40,33,26,19,12,5)
                        
                # Escolha do Jogador==7        
                elif Escolha_Jogador==7:
                    if Verify(6,7) == True:
                        break
                    if Nome==Nome2:
                        Gravidade(41,34,27,20,13,6,"O")
                    else:
                        Gravidade(41,34,27,20,13,6)
                
                # Tratamento de Erro: Número Inválido!     
                else:
                    system("cls")
                    print("Erro: Digite um Número Válido!")
                    break
                    
                system("cls")
                count+=1
                
            # Tratamento de Erro: Usuário Não Digitou um Número
            except:           
                system("cls")
                print("Erro: Digite um Número!")    
            break
main()
