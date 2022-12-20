with open('aabbcc.txt','r') as arquivo:
    palavra=input("Palavra: ")
    lista=arquivo.read().split()
    if palavra in lista:
        print(f"Palavra Encontrada {lista.count(palavra)} vez(es)")
    else:
        print("Palavra Não Encontrada!")   
    arquivo.close()
    