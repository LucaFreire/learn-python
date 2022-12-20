'''The same teacher, wants to raffle one in four students to present a work.
Create a system where the machine ruffle a student in order, to present the job.'''

from random import shuffle


a=input("Primeiro Aluno: ")
b=input("Segundo Aluno: ")
c=input("Terceiro Aluno: ")
d=input("Quarto Aluno: ")

lista=[a,b,c,d]
shuffle(lista)

print(f'Ordem: {lista}')