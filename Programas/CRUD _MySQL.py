#CRUD_MySQL
from multiprocessing import connection
import os
import mysql.connector

connection = mysql.connector.connect(
  host="localhost", # 127.0.0.1:3306
  user="root",
  password="1467",
  database="projeto"
)

cursor = connection.cursor()

while True:
    print()
    print(82*"~")
    print(f"{'PÁGINA INICIAL':^82}")
    print(82*"~")
    print()
    ESCOLHA=str(input((f'''
{'CRUD COM PRODUTOS':^82}

{'ESCOLHAS:':^82} 

[0]p/ SAIR

[1]p/ ADICIONAR 

[2]p/ VISUALIZAR

[3]p/ ATUALIZAR

[4]p/ EXCLUIR

Digite seu Número: ''')))
    os.system("cls") #Utilizado para limpar o terminal


    if ESCOLHA=='0': # SAIR
        break


    elif ESCOLHA=='1': #CRIAR


        print()
        print(82*"=")
        print(f"{'ADICIONAR PRODUTO':^82}".title())
        print(82*"=")
        print()

        NOME_PRODUTO=str(input("Digite o Nome do Produto: ")).title() #Inserir Nome do Produto
        print()
        valor_produto= float(input("Valor: R$ "))  #Inserir Valor do Produto
        print()
        quantidade_produto= int(input("Quantidade do Produto: "))

        comando_editar = (f"INSERT INTO projeto.vendas (nome, valor, quantidade) VALUES \
        ('{NOME_PRODUTO}',{valor_produto}, {quantidade_produto})")
        cursor.execute(comando_editar)
        connection.commit()
        os.system("cls")
        print()
        print("Você Adicionou um Produto!")


    elif ESCOLHA=='2': #VISUALIZAR

        COMANDO_VISUALIZAR = "SELECT * FROM projeto.vendas"
        cursor.execute(COMANDO_VISUALIZAR)
        resultado=cursor.fetchall()
        print()
        print(82*"=")
        print(f"{'TABELA DE PRODUTOS':^82}")
        print(82*"=")
        print()
        for i in resultado:
            print(f"Produto: {i[0]:^10} | R$ {i[1]:^8.2f} p/Item | Qtd: {i[2]:^7} | \
            Mercadoria: R$ {i[1]*i[2]:.2f}")
            print(82*"-")
            print()


    elif ESCOLHA=='3': #ATUALIZAR

        print()
        print(82*"=")
        print(f"{'ATUALIZAR PRODUTO':^82}")
        print(82*"=")
        print()

        COMANDO_VISUALIZAR = "SELECT * FROM projeto.vendas" #Tabela
        cursor.execute(COMANDO_VISUALIZAR)
        resultado=cursor.fetchall()
        print(82*"-")
        print(f"{'TABELA ATUALIZADA':^82}")
        print(82*"-")
        print()
        for i in resultado:
            print(f"Produto: {i[0]:^10} | R$ {i[1]:^8.2f} p/Item | Qtd: {i[2]:^7} | \
            Mercadoria: R$ {i[1]*i[2]:.2f}")
            print(82*"-")
            print()

        ALTERAR_PRODUTO=str(input('Nome do Produto que Deseja Alterar:  ')).title()
        print()
        print("Deseja Alterar o Valor ou a Quantidade?")
        MIN_ESC=str(input("[1]p/ Valor e [2]p/ Quantidade, Seu número: "))

    while MIN_ESC!='1' and MIN_ESC!='2':
        print()
        print("[1]p/ Valor e [2]p/ Quantidade, Seu número: ")
        MIN_ESC=(str(input('Número Inválido, Digite Novamente: ')))

    if MIN_ESC=='1': #Alterar Valor
        print()
        alterar_valor=float(input("Novo Valor do Produto: R$ "))
        valor_produto=alterar_valor
        print()
        comando_atualizar=f'UPDATE projeto.vendas SET valor \
        = {alterar_valor}  WHERE nome = "{ALTERAR_PRODUTO}"'

    elif MIN_ESC=='2': #Alterar Quantidade
        print()
        alterar_quantidade=float(input("Nova Quantidade do Produto: "))
        comando_atualizar=f'UPDATE projeto.vendas SET quantidade = {alterar_quantidade} \
        WHERE nome = "{ALTERAR_PRODUTO}"'
        print()

        cursor.execute(comando_atualizar)
        connection.commit()
        os.system("cls")
        print(f"{ALTERAR_PRODUTO} Atualizado com Sucesso!")


    elif ESCOLHA=='4': #DELETAR

        print()
        print(82*"=")
        print(f"{'DELETAR PRODUTO':^82}")
        print(82*"=")
        print()
  
        COMANDO_VISUALIZAR = "SELECT * FROM projeto.vendas" #Tabela
        cursor.execute(COMANDO_VISUALIZAR)
        resultado=cursor.fetchall()
        print(82*"-")
        print(f"{'TABELA ATUALIZADA':^82}")
        print(82*"-")
        print()
        for i in resultado:
            print(f"Produto: {i[0]:^10} | R$ {i[1]:^8.2f} p/Item | Qtd: {i[2]:^7} | \
            Mercadoria: R$ {i[1]*i[2]:.2f}")
            print(82*"-")
            print()

        DELETAR_PRODUTO=str(input('Nome do Produto que Deseja Remover: ')).title()
        comando_deletar=f'DELETE FROM projeto.vendas WHERE nome = "{DELETAR_PRODUTO}"'
        cursor.execute(comando_deletar)
        connection.commit()
        os.system("cls")
        print(f"{DELETAR_PRODUTO} Removido Com Sucesso!")
  
    else:
        print("Número Inválido, Digite Novamente!")

print("Você Saiu!")
connection.commit()
connection.close()
