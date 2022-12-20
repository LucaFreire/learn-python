#Programa que leia o sexo, porém só aceita os valores "M" ou "F".
#Caso esteja errado, peça a digitação novamente.

sexo=str(input("Digite seu Sexo [M/F]: ")).upper().strip() #vídeo é utilizado o [0] p/ pegar a inicial

while sexo!="M" and sexo!="F": # vídeo: while sexo not in "M,F"
    sexo=str(input("Sexo Indefinido, Digite Novamente [M/F]: ")).upper().strip()

print("Sexo Registrado com Sucesso!")
