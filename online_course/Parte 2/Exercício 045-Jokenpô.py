#Jokenpô (o placar foi implementado após o conhecimento do while)

from time import sleep
from random import choice as escolha_pc

lista=["PEDRA","PAPEL","TESOURA"]
Vitórias_Jogador=0
Vitórias_Pc=0
Empates=0

while True:
    print(45*'=')
    Escolha=str(input("Deseja Jogar Jokenpô? [S/N]: ")).upper().strip()

    while Escolha[0]!='S' and Escolha[0]!="N":
        Escolha=str(input("Resposta Inválida, Digite Novamente: ")).strip().upper()
        
    if Escolha[0]=='N':
        break   

    else:
        for i in range(1,6):
            print(45*'=')
            pc=escolha_pc(lista)

            Jogada=str(input("Pedra, Papel, ou Tesoura: ")).strip().upper()

            while Jogada[0:2]!="PE" and Jogada[0:2]!="PA" and Jogada[0:2]!="TE":
                Jogada=str(input('Jogada Inválida, Digite Novamente: ')).strip().upper()

            print("Jó...")
            sleep(1)
            print('Ken...')
            sleep(1)
            print('Pôôôô!!!')
            print()


            if Jogada[0]=='P' and Jogada[1]=='E': #Jogador==PEDRA
                if pc=="TESOURA":
                    Vitórias_Jogador+=1
                    print("Sua Escolha: PEDRA")
                    print(f'PC: {pc}')
                    print()
                    print('Você Venceu!')

                elif pc=="PAPEL":
                    Vitórias_Pc+=1
                    print("Sua Escolha: PEDRA") 
                    print(f'PC: {pc}')
                    print()
                    print('Você Perdeu!')

                else:
                    Empates+=1
                    print("Sua Escolha: PEDRA")
                    print(f'PC: {pc}')
                    print()
                    print('Empate!')


            elif Jogada[0]=='P' and Jogada[1]=='A': #Jogador==PAPEL
                if pc=="TESOURA":
                    Vitórias_Pc+=1
                    print("Sua Escolha: Papel")
                    print(f'PC: {pc}')
                    print()
                    print('Você Perdeu!')

                elif pc=='PEDRA':
                    Vitórias_Jogador+=1
                    print("Sua Escolha: Papel")
                    print(f'PC: {pc}')
                    print()
                    print('Você Ganhou!')

                else:
                    Empates+=1
                    print("Sua Escolha: Papel")
                    print(f'PC: {pc}')
                    print()
                    print('Empate!')


            elif Jogada[0]=="T" and Jogada[1]=='E': #Jogador==TESOURA
                if pc=="PAPEL":
                    Vitórias_Jogador+=1
                   
                    print("Sua Escolha: Tesoura")
                    print(f'PC: {pc}')
                    print()
                    print('Você Ganhou!')

                elif pc=="PEDRA":
                    Vitórias_Pc+=1
                    print("Sua Escolha: Tesoura")
                    print(f'PC: {pc}')
                    print()
                    print('Você Perdeu!')

                else:
                    Empates+=1
                    print("Sua Escolha: Tesoura")
                    print(f'PC: {pc}')
                    print()
                    print('Empate!')


print(45*"=")
if Vitórias_Jogador>Vitórias_Pc:
    print("Você Venceu!!!")

elif Vitórias_Jogador<Vitórias_Pc:
    print("Você Perdeu...")

else:
    print("Vocês Impataram.")
    
print()
print(f'Vitórias do Jogador: {Vitórias_Jogador}')
print(f"Vitórias do PC: {Vitórias_Pc}")
print(f'Empates: {Empates}')
