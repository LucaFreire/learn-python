'''Melhore o jogo de adivinhação do Exercício 028, onde o pc escolhe um número entre 1 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final as tentativas.'''

from random import randint

ran=randint(0,10)
count=1

print("~~~~~~~~Jogo da Adivinhação~~~~~~~~")
print("Números Entre 0 e 10.")
esc=int(input("Digite seu Número: "))

while esc!=ran:
    if esc>ran:
        esc=int(input("Menos... Digite Outro Número: "))
    else:
        esc=int(input("Mais... Digite Outro Número: "))
    count+=1

if count==0:
    print("Acertou de Primeira, Parabéns!!!")
else:
    print(f"Acertou! Tentativas: {count}")
