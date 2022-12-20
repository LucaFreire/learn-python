'''Um programa que jogue par ou ímpar com o computador.
O jogo é interrompido quando o jogador perder, mostrando o
total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
count=0

while True:
    escolha=str(input("Par ou Ímpar [P/I]: ")).strip().upper()[0]

    if escolha!="P" and escolha!="I":
        print("Escolha Indefinida, Digite Novamente!")
        print()

    else:
        num=int(input("Digite seu Número: "))
        pc=randint(1,11)

        if (pc+num)%2==0 and escolha=="P" :
            print(f"Escolha do PC: {pc}")
            print(f"~~~~ Deu {pc+num} ~~~~ PAR VENCEU!")
            print()
            count+=1

        elif (pc+num)%2!=0 and escolha=="I":
            print(f"Escolha do PC: {pc}")
            print(f"~~~~ Deu {pc+num} ~~~~ ÍMPAR VENCEU!")
            print()
            count+=1
            
        else:
            print(f"Escolha do PC: {pc}")
            print(f"~~~~ Deu {pc+num} ~~~~\nVocê Escolheu {escolha} e PERDEU.")
            break

print(f"Vitórias: {count}")
