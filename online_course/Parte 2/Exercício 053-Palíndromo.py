#Um programa que diz se é palíndromo ou não.

nome=str(input("Digite Algo: ")).upper().strip()
palavras=nome.split()
junto="".join(palavras)
inverso=junto[::-1]
print(f"Normal: {junto}")
print(f"Inverso: {inverso}")
if inverso==junto:
    print("É Um Palíndromo!")
else:
    print("Não É Um Palíndromo!")

    #Vídeo, outra forma:

'''nome=str(input("Digite Algo: ")).upper().strip()
palavras=nome.split()
junto="".join(palavras)
inver=" "

for i in range(len(junto)-1,-1,-1):
    inver+=junto[i]

print(f"Normal: {nome}")
print(f"Inverso: {inver}")
if inver==junto:
    print("É Palíndromo!")
else:
    print("Não É Um Palíndromo")'''