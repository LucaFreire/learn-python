'''Crie um programa que tenha uma tupla com várias palavras.
Depois disso, você deve mostrar, para cada palavra, quais 
são suas vogais.(Não utilizar acentos)'''

Palavras=("Garrafa", "Livro", "Cubo", "Quadrado", "Teclado", "Batom",
"Caderno", "Celular", "Site", "Palavras", "Vogais")

for i in Palavras:
    print(f"Vogais da Palavra: {i}")
    print(f'A = {i.upper().count("A")}')
    print(f'E = {i.upper().count("E")}')
    print(f'I = {i.upper().count("I")}')
    print(f"O = {i.upper().count('O')}")
    print(f"U = {i.upper().count('U')}")
    print()
