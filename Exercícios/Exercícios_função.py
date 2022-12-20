# Exercício Senai Centro, prof: Alexander

# Aluno: Lucas Freire

#1) Faça uma função que recebe o raio de uma esfera e calcula o seu volume (v = 4/3.P
def Volume(raio):
    print( (4/3*3.14)*raio**3 )
#Volume(5)
   

# 2) Escreva um procedimento que receba um número inteiro e imprima o mês
#correspondente ao número. Por exemplo, 2 corresponde à “fevereiro”. O
#procedimento deve mostrar uma mensagem de erro caso o número recebido não
#faça sentido.
def Mes(num):
    Mes=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]  
    try:
        if num - 1 == -1:
            raise Exception        
        print(f"mês: {Mes[num-1]}")
    except:
        print("Numero invalido")
#Mes(12)


# 3) Faça uma função que recebe um valor inteiro e positivo e retorna o valor lógico
#Verdadeiro caso o valor seja primo e Falso em caso contrário.
def Primo(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
#print(Primo(2))
 

# 4) Escreva uma função que receba dois números inteiros x e y. Essa função deve
#verificar se x é divisível por y. No caso positivo, a função deve retornar 1, caso
#contrário zero.
def divisivel(x,y):
    if x % y == 0:
        return 1
    else:
        return 0
#print(divisivel(10,5))
           

# 5) Escreva uma função que calcule e retorne a distância
# entre dois pontos (x1, y1) e (x2, y2).
def distancia(x1,y1,x2,y2):    
    print( (((x2-x1)**2) - ((y2-y1)**2))**0.5 )
#distancia(2,5,10,10)
   
   
# 6) Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito
#perfeito quando ele é igual a soma dos seus divisores excetuando ele próprio. (Ex: 6
#é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor
#booleano.
def perfeito(num):
    lista=[]
    for i in range(1,num):
        if num % i == 0:
            lista.append(i)
        if sum(lista) == num:
            return True
        else:
            return False
#print(perfeito(28))


# 7) Escreva uma função media_final(p1, p2, ep1, ep2, ep3) que recebe as notas das
#provas p1 e p2 e as notas dos exercícios-programa ep1, ep2 e ep3 de um aluno.
#Devolve a média final deste aluno. A média final é dada por (2p+ep)/3, onde p =
#(p1+2p2)/3 e ep = (ep1+2ep2+3ep3)/6.
def media_final(p1,p2,ep1,ep2,ep3):
   
    p = (p1 + 2*p2)/3
    ep = (ep1+2*ep2+3*ep3)/6
    media = (2*p+ep)/3
   
    return media
#print(media_final(20,20,20,20,20))
   

# 8) Escreva uma função que compara duas datas que são dadas na forma dia, mês e
#ano. A função devolve 1 se a primeira data é maior que a segunda, 0 se são iguais e
#-1 se a segunda é maior que a primeira.
def data(dia1,mes1,ano1,dia2,mes2,ano2):
    
    if ano1>ano2:
        print("Primeira é Maior!")
    elif ano1<ano2:
        print("Segunda é Maior!")    
    elif ano1==ano2:
        if mes1>mes2:
            print("Primeira é Maior!")
        elif mes1<mes2:
            print("Segunda é Maior!")
        elif mes1 == mes2:
            if dia1>dia2:
                print("Primeira é Maior!")
            elif dia1<dia2:
                print("Segunda é Maior!")
            else:
                print("Mesma Data!")
#data(20,11,2010,20,11,2010)


# 9) Escreva uma função que recebe, por parâmetro, dois valores 
# X e Z e calcula e retorna X^Z (X elevado a Z).
def elevado(x,z):
    return x**z
#print(elevado(5,2))
        

# 10) Criar uma função que verifique quantas vezes um número inteiro x é divisível por um
#número inteiro y. A função deve retornar -1 caso não seja possível calcular
def divisivel(x):
    count=0
    for i in range(1,x+1):
        if x%i == 0:
            count+=1
    if count == 0:
        return -1
    else:
        return count
#print(divisivel(10))

    
# 11) Escreva uma função que recebe n maior que zero, e retorna seu fatorial.
def fatorial(num):
    count=1
    for i in range(1,num+1):
        count*=i
    return count
#print(fatorial(5))
    

# 12) Criar uma função que calcule e retorne o número de arranjos e outra que faça o
#mesmo para combinações. As entradas serão:
#n = Quantidade total de elementos no conjunto
#p = Quantidade de elementos por arranjo/combinação
def arranjoCombinacao(n,p):
    Combinacao = fatorial(n) / (fatorial(n-p))
    Arranjo = fatorial(n) / (fatorial(p)*fatorial(n-p))
    print(f"Combinação: {Combinacao}\nArranjo: {Arranjo}")
#arranjoCombinacao(6,2)


# 13) Escreva uma função que recebe n maior que zero e devolve o n-ésimo número
#harmônico, dado pelo valor da soma:
#1 + 1/2 + 1/3 + ... + 1/n
def numHarmonico(num):
    count=0
    for i in range(1,num+1):
        count+= 1/i
    print(count)
#numHarmonico(5)


#14) Escreva uma função que recebe n maior que zero e devolve o valor da soma:
#1/1! + 1/2! + 1/3! + ... + 1/n!
def harmonicoFatorial(num):
    count=0
    for i in range(1, num+1):
        count+= 1/fatorial(i)
    print(count)
#harmonicoFatorial(5)
