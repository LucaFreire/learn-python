# Questão Primeira prova
def createStudent():
    Nome = input("Nome do Aluno: ")
    Num_Notas = int(input(f"Quantas Notas o {Nome} vai Cadastrar: "))
    Notas=[]

    for i in range(1,Num_Notas+1):
        Nota = float(input(f"{i}° Nota: "))
        Notas.append(Nota)

    Tudo =f"{Nome},{tuple(Notas)}\n"

    arq = open("Alunos4.txt","a")
    arq.write(str(Tudo))
    print(Tudo)
    arq.close()


def visualisarAluno():
    arq=open("Alunos4.txt","r")
    print("Alunos:\n")
    for i in arq:
        a=i.split(",")
        print(a[0])
    arq.close()
    
    with open("Alunos4.txt","r") as arq:
        Nome = input("Nome do Aluno: ")
        for j in arq:
            b=j.split(",")
            b[-1] = b[-1].replace("\n","")
            if Nome == b[0]:
                b = b[1:]
                for i in b:
                    if i[0] == "(":
                        b[i[0]].remove("(")
                    elif i[0] == ")":
                        b[i[0]].remove(")")
                print(b)

                

esc=int(input("1 - Cadastrar\n2 - Visualizar\n> "))
if esc == 1:
    createStudent() 
elif esc ==2:
    visualisarAluno()
