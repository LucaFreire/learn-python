from time import sleep
from random import choice as escolha_pc

lista=["PEDRA","PAPEL","TESOURA"]
VITORIAS_JOGADOR=0
VITORIAS_PC=0
EMPATES=0

while True:
    print(45*'=')
    ESCOLHA=str(input("Deseja Jogar Jokenpô? [S/N]: ")).upper().strip()

    while ESCOLHA[0]!='S' and ESCOLHA[0]!="N":
        ESCOLHA=str(input("Resposta Inválida, Digite Novamente: ")).strip().upper()
        
    if ESCOLHA[0]=='N':
        break

    else:
        for i in range(1,6):
            print(45*'=')
            pc=escolha_pc(lista)

            JOGADA=str(input("Pedra, Papel, ou Tesoura: ")).strip().upper()

            while JOGADA[0:2]!="PE" and JOGADA[0:2]!="PA" and JOGADA[0:2]!="TE":
                JOGADA=str(input('Jogada Inválida, Digite Novamente: ')).strip().upper()

            print("Jó...")
            sleep(1)
            print('Ken...')
            sleep(1)
            print('Pôôôô!!!')
            print()


            if JOGADA[0]=='P' and JOGADA[1]=='E': #Jogador==PEDRA
                if pc=="TESOURA":
                    VITORIAS_JOGADOR+=1
                    print("Sua Escolha: PEDRA")
                    print(f'PC: {pc}')
                    print()
                    print('Você Venceu!')

                elif pc=="PAPEL":
                    VITORIAS_PC+=1
                    print("Sua Escolha: PEDRA") 
                    print(f'PC: {pc}')
                    print()
                    print('Você Perdeu!')

                else:
                    EMPATES+=1
                    print("Sua Escolha: PEDRA")
                    print(f'PC: {pc}')
                    print()
                    print('Empate!')


            elif JOGADA[0]=='P' and JOGADA[1]=='A': #Jogador==PAPEL
                if pc=="TESOURA":
                    VITORIAS_PC+=1
                    print("Sua Escolha: Papel")
                    print(f'PC: {pc}')
                    print()
                    print('Você Perdeu!')

                elif pc=='PEDRA':
                    VITORIAS_JOGADOR+=1
                    print("Sua Escolha: Papel")
                    print(f'PC: {pc}')
                    print()
                    print('Você Ganhou!')

                else:
                    EMPATES+=1
                    print("Sua Escolha: Papel")
                    print(f'PC: {pc}')
                    print()
                    print('Empate!')


            elif JOGADA[0]=="T" and JOGADA[1]=='E': #Jogador==TESOURA
                if pc=="PAPEL":
                    VITORIAS_JOGADOR+=1
                    print("Sua Escolha: Tesoura")
                    print(f'PC: {pc}')
                    print()
                    print('Você Ganhou!')

                elif pc=="PEDRA":
                    VITORIAS_PC+=1
                    print("Sua Escolha: Tesoura")
                    print(f'PC: {pc}')
                    print()
                    print('Você Perdeu!')

                else:
                    EMPATES+=1
                    print("Sua Escolha: Tesoura")
                    print(f'PC: {pc}')
                    print()
                    print('Empate!')


print(45*"=")
if VITORIAS_JOGADOR>VITORIAS_PC:
    print("Você Venceu!!!")

elif VITORIAS_JOGADOR<VITORIAS_PC:
    print("Você Perdeu...")

else:
    print("Vocês Impataram.")
    
print()
print(f'Vitórias do Jogador: {VITORIAS_JOGADOR}')
print(f"Vitórias do PC: {VITORIAS_PC}")
print(f'EMPATES: {EMPATES}')
