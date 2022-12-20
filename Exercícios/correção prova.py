# Primeira prova Bosch ;

# ======================= Exercício 1 ======================= #


# def isTriangle(a, b, c):
#     if (abs(b-c)<a<b+c) and (abs(a-c)<b<a+c) and (abs(a-b)<c<a+b):
#         return typeoftriangle(a, b, c)
#     else:
#         return "Não é um triângulo"

# def typeoftriangle(a, b, c) -> str:
#         if a==b==c:
#             return "Equilátero"
#         elif a==b or a==c or b==c:
#             return "Isósceles"
#         else:
#              return "Escaleno"

# lado1 = int(input("Digite o lado a: "))
# lado2 = int(input("Digite o lado b: "))
# lado3 = int(input("Digite o lado c: "))

# print(isTriangle(lado1, lado2, lado3))
    



# ======================= Exercício 2 ======================= #



# times = {"Palmeiras":30, "Corinthians": 24, "Fluminense":17, "Vasco da Gama":12}

# rodadas = int(input("Digite o número de rodadas: "))

# pontos = [3, 0, 1]
# for i in range(rodadas):
#     for k in times:
#         resultado = int(input(f"Resultado da partida para {k}:\n1 - Vitória\n2 - Derrota\n3 - Empate\n> "))
#         times[k] += pontos[resultado-1]



# print(f"O time com mais pontos foi o {max(times,key=times.get)} com {times[max(times,key=times.get)]} pontos")
    

# ======================= Exercício 3 ======================= #

# import sys


# try:
#     numero = int(input("Digite um número inteiro: "))
#     if numero<=0:
#         raise Exception
# except:
#     print("Valor inválido")
#     sys.exit()

# soma = 0
# for i in str(numero):
#     soma += int(i)
# print(soma)




# ======================= Exercício 4 ======================= #

# feedback = ['a', 'c', 'a', 'a', 'c', 'a', 'b', 'd', 'd', 'c']


# wrongAnswers = []
# for i in range(len(feedback)):
#     resposta = input(f"Questão numero {i+1}: ").lower()
#     if resposta != feedback[i]:
#         wrongAnswers.append(i+1)
# print("This is your grade:", len(feedback) - len(wrongAnswers))

# print("Wrong Answers:", wrongAnswers)




# ======================= Exercício 5 ======================= #

# import random

# num = random.randint(1, 1000)
# tentativa = 0
# print(num)

# while True:
#     tentativa+=1
#     chute = int(input("Try to guess the number: "))
#     if chute == num:
#         print("Congratulation, you are right")
#         print(tentativa, "Tries")
#         break
#     if chute <= num+3 and chute >= num-3:
#         print("Almost there")
#     elif  chute > num:
#         print("Too High")
#     else:
#         print("Too Low")
        
# ======================= Exercício 6 ======================= #




# alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encryptPassword(password):
#     novaSenha = ""
#     for char in password:
#         if char.isalnum() == False:
#             novaSenha += "0"
#         elif char in alfabeto:
#             novaSenha += str(alfabeto.index(char.lower()))
#         else:
#             novaSenha += str(char)
#     return novaSenha

# def passwordToBin(string):
#     novaSenha = ""
#     senha = encryptPassword(string)
#     for i in senha:
#         novaSenha += format(int(i), "b").zfill(4)+"_"
#     return novaSenha[:-1]

# senha = input("> ")
# print(passwordToBin(senha))



# ======================= Exercício 7 ======================= #


print("Escola Paixão")
print("1 - Cadastrar alunos\n2 - Ler notas")
opcao = int(input("> "))
def CreateStudents():
    txt = open("AlunosNotas.txt", "a")
    quantA = int(input("Quantidade de alunos a cadastrar: "))
    for i in range(quantA):
        notas=[]
        nome = input(f"Aluno {i+1}: ")
        quantNotas = int(input("Quantidade de notas a cadastrar: "))
        for j in range(quantNotas):
            nota = input(f"Digite a nota {j+1}: ")
            notas.append(nota)
        conteudo = nome+","+(",".join(notas))+"\n"
        txt.write(conteudo)
    txt.close()
def encontrarAlunos():
    txt = open("AlunosNotas.txt", "r")
    for linha in txt:
        a = linha.split(",")
        print(a[0])
    txt.close()
 
    aluno = input("Nome do aluno: ")
 
    with open("AlunosNotas.txt", "r") as txt:
        for linha in txt:
            a = linha.split(",")
            a[-1] = a[-1].replace("\n", "")
            if a[0] == aluno:
                a = list(map(float,(a[1:])))  
                return sum(a)/len(a)
if opcao == 1:
    CreateStudents()
else:
    print("Média do Aluno:", encontrarAlunos())



# ======================= Exercício 8 ======================= #


# import pandas as pd
# import matplotlib.pyplot as plt





# df = pd.read_csv("netflix_titles.csv")

# df = df.dropna()

# americanos = df.loc[(df["type"] == "Movie") &
#                     (df["country"] == "United States") &
#                     (df.release_year <= 2020) &
#                     (df.release_year >= 2015)]



# y = americanos.release_year.value_counts()
# x = y.index

# plt.bar(x, y, zorder=2, color="black")
# plt.title("Filmes americanos 2015 - 2020")
# plt.grid(linestyle="dotted")
# plt.show()

# def convertToInt(line):
#     return int(line[:line.index("m")])

# filmesBr = df.loc[(df["type"] == "Movie") &
#                    (df["country"] == "Brazil")]

# filmesBr["duration"] = filmesBr.duration.apply(convertToInt)

# filmesMaisLongos = filmesBr.sort_values(by=["duration"], ascending=False)
# print(filmesMaisLongos[:5])

# filmesMaisLongos = filmesBr.nlargest(5,"duration",keep="all")
# print(filmesMaisLongos)





# ======================= Exercício 9 ======================= #






# import numpy as np

# array = np.random.randint(1, 10, (5, 5))

# print('\n', array)

# condition = (array %2 != 0)

# array[condition] = array[condition]**2

# print('\n', array)




