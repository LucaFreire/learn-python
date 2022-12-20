def forca():
    from random import choice
    #================== VARIÁVEIS E LISTAS ==================#
    count=0
    count_len=0
    lista_facil=["celular","carteira"]
    lista_medio=["palavra","ola"]
    lista_dificil=["abacaxi","cadeira"]
    agr=[]
    agr_new=[]
    #======================== OPÇÕES ==========================#
    while True:
        try:
            dif=int(input("1-Fácil\n2-Médio\n3-Difícil\n> "))
            if dif==1:
                palavra=choice(lista_facil)
            elif dif==2:
                palavra=choice(lista_medio)
            elif dif==3:
                palavra=choice(lista_dificil)
            else:
                raise Exception
            break
        except:
            print("Número Inválido, Digite Novamente!")
            
    for i in palavra:
        agr.append(i)
        agr_new.append("_")
    #======================== MAIN ==========================#
    while True:
        for k in agr_new:
            print(k,end=" ")
        letra = input("\nDigite uma Letra: ")
        
        if letra in agr:
            agr_new[agr.index(letra)]=letra
            agr[agr.index(letra)]="0"
            count_len+=1
        else:
            count+=1
            
        if count_len == len(palavra):
            for k in agr_new:
                print(k,end=" ")
            print("\nVocê Acertou a Palavra, Parabéns!")
            break
        elif count == 6:
            print(f"Você Perdeu!\nA Palavra: {palavra}")
            break
        
forca()
