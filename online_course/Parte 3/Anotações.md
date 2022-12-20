Part 3 - Anotações

--> No Python podemos começar uma Variável Composta por 3 maneiras:

    .() Tuplas #Não é Obrigatório o uso de parênteses nas tuplas
    .[] Listas
    .{} Dicionário

~~~~ Tuplas - Aula 16 ~~~~

-As Tuplas São IMUTÁVEIS

--> Exemplos com print():
    
    lanches=("Hambúrguer" , "Suco" , "Pizza" , "Pudim")

    .print(sorted(lanches)) -'Hambúrguer' , 'Pizza' , 'Pudim' , 'Suco' #Ele Organiza

    .print(lanches) - "Hambúrguer" , "Suco" , "Pizza" , "Pudim"
    .print(lanches[0]) -'Hambúrguer'
    .print(lanches[1]) -'Suco'
    .print(lanches[1:3]) -'Suco' , 'Pizza'
    .print(lanches[-2]) -'Pizza'
    .print(lanches[2:]) -'Pizza' , 'Pudim'
    .print(lanches[:2]) -'Hambúrguer' , 'Suco'
    .print(lanches[-3:]) -'Suco' , 'Pizza' , 'Pudim'

--> Exemplos com for:

    lanches=("Hambúrguer" , "Suco" , "Pizza")

    for i in lanches:
        print(f"Vou Comer {i}")
    print("Estou com Fome")

-'Vou Comer Hambúrguer'
-'Vou Comer Suco'
-'Vou Comer Pizza'
-'Estou com Fome'

    for cont in range(0,len(lanche)):
        print(lanche[cont])
    print("Comi Bastante")

-'Hambúrguer'
-'Suco'
-'Pizza'
-'Comi Bastante'

    for pos, i in enumerate(lanches):
        print(f"{pos+1}° Pedido: {i}") #pos+1 p/ iniciar o pedido no 1°
    print("Pedido Finalizado")

-'1° Pedido: Hambúrguer'
-'2° Pedido: Suco'
-'3° Pedido: Pizza'
-'Pedido Finalizado'

<h2> index , count , del: </h2>

    a=(2,5,4)
    b=(5,8,1,2)
    c= b + a

    .print(c) - 5,8,1,2,2,5,4 #Não Faz a Soma, Apenas Concatena.
    .print(len(c)) - 7
    .print(c.count(5)) - 2 #Contagem dos 5 no c
    .print(c.index(8)) - 1 #Localização do 8, iniciando-se a contagem do 0
    .del(c) #Deleta a Variável
    .print(c) - Erro

~~~~ Listas ~~~~

Lista = []
 
--> Comandos:

    -var.sort():Organiza o os Números da var

    -var.sort(reverse=True):Organiza em ordem decrescente
 
    -var=list(range(1,11)):Cria uma lista com os números de 1 a 10

    -len(var):Conta os Elementos da var (contagem se inicia do 0) 


    --Inserir Elementos e Sustitui-los:

    -var[2]="Elemento": Substitui o Objeto na posição 2 pelo Elemento 
    
    -var.append(): add um Elemento no final da lista

    -var.insert(0,Elemento): add o Elemento na Posição 0(Não substitui)


    --Apagar Elementos:

    -var.clear():Apaga Tudo de uma Lista

    -del var[2]:Deleta o Elemento 2 da Variável

    -var.pop[2]:Deleta o Elemento 2 da Variável
        (Normalmente esse Método é p/ Apagar o Último Elemento= var.pop())

    -var.remove[2]:Deleta o Elemento 2 da Variável

    -if 'obj' in var:
        var.remove('obj'): Se 'obj' estiver na var, remove o 'obj'

    --Outro:

    .a=[1,2,3,4]
    .b=a
    .b[2]=8
    .a=[1,2,8,4]
    .b=[1,2,8,4] #As duas Listas se modificaram, elas se ligaram entre si.

    caso queira fazer uma cópia: b=a[:]