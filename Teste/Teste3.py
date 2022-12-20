from os import system

matriz=[]
vetor=[]

# Criando Tabuleiro
for i in range(6):
    for j in range(7):
        matriz.append(vetor)       
        for k in range(0,len(matriz)):
            matriz[k]=" "

# Mostrando Tabulerio
def Tabuleiro():
    count=0
    print("\n 1     2     3     4     5     6     7\n")
    for i in matriz:
        print(" ",i,end=" | ")
        count+=1
        if count==7:
            print()
            count=0
    print(42*"=")
            
# Gravidade das Colunas      
def gravidade(a,b,c,d,e,f,x="X"):  
    while True:
        # Linha 1
        if matriz[a]==" ":# Verificação de um vetor 
            matriz[a]=x # Símbolo: X ou O
            break
        # Linha 2          
        elif matriz[b]==" ":
            matriz[b]=x
            break
        # Linha 3           
        elif matriz[c]==" ":
            matriz[c]=x
            break
        # Linha 4           
        elif matriz[d]==" ":
            matriz[d]=x
            break
        # Linha 5          
        elif matriz[e]==" ":
            matriz[e]=x
            break
        else:
        # Linha 6
            matriz[f]=x
            break       
        
# Vereficação p/ ver se coluna já está cheia        
def verify(a,b):
    if matriz[a]=='X' or matriz[a]=='O':
        system("cls")
        print(f"Erro: Coluna {b} está cheia!")
        return True
        

# Main
def main():
    count=1
    while True:
        # Cálculo p/ definir jogador 1 ou 2
        if count%2==0:
            Num_Jogador=2
        else:
            Num_Jogador=1
        # Mostra Tabuleiro
        Tabuleiro()
        # while p/ tratamento de erros
        while 1:
            try:
                # Número da Coluna
                Escolha_Jogador=int(input(f"Jogador {Num_Jogador}, insira seu Número entre 1 e 7: "))            
                
                # Escolha do Jogador=1
                if Escolha_Jogador==1:
                    # Vereficação p/ ver se coluna já está cheia
                    if verify(0,1) == True:
                        break
                    # Preenchendo a coluna número 1              
                    if count%2==0:
                        gravidade(35,28,21,14,7,0,"O")#Símbolo p/ Jogador 2("O")
                    else:
                        gravidade(35,28,21,14,7,0)#Símbolo p/ Jogador 1("X")
                        
                # Escolha do Jogador=2 
                elif Escolha_Jogador==2:
                    if verify(1,2) == True:
                        break                  
                    if count%2==0:    
                        gravidade(36,29,22,15,8,1,"O")
                    else:
                        gravidade(36,29,22,15,8,1)
                        
                # Escolha do Jogador=3       
                elif Escolha_Jogador==3:
                    if verify(2,3) == True:
                        break
                    if Num_Jogador%2==0:
                        gravidade(37,30,23,16,9,2,"O")
                    else:
                        gravidade(37,30,23,16,9,2)
                
                # Escolha do Jogador=4           
                elif Escolha_Jogador==4:
                    if verify(3,4) == True:
                        break
                    if Num_Jogador%2==0:
                        gravidade(38,31,24,17,10,3,"O")
                    else:
                        gravidade(38,31,24,17,10,3)
                
                # Escolha do Jogador=5
                elif Escolha_Jogador==5:
                    if verify(4,5) == True:
                        break
                    if Num_Jogador%2==0:
                        gravidade(39,32,25,18,11,4,"O")
                    else:
                        gravidade(39,32,25,18,11,4)
                
                # Escolha do Jogador=6    
                elif Escolha_Jogador==6:
                    if verify(5,6) == True:
                        break
                    if Num_Jogador%2==0:
                        gravidade(40,33,26,19,12,5,"O")
                    else:
                        gravidade(40,33,26,19,12,5)
                        
                # Escolha do Jogador=7        
                elif Escolha_Jogador==7:
                    if verify(6,7) == True:
                        break
                    if Num_Jogador%2==0:
                        gravidade(41,34,27,20,13,6,"O")
                    else:
                        gravidade(41,34,27,20,13,6)
                
                # Tratamento de Erro: Número Inválido!     
                else:
                    system("cls")
                    print("Erro: Número Inválido!")
                    break
                    
                system("cls")
                count+=1
            # Tratamento de Erro: Usuário Não Digitou um Número
            except:           
                system("cls")
                print("Erro: Digite um Número!")    
            break
