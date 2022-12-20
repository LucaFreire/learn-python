
lista=[[0],[0],[0],[0],[0],[0],[0],[0],[0]]
count=0
def tabuleiro():
    for k, i in enumerate(lista):
        if k==3 or k==6 or k==9:
            print()
        print(i,end="")
        
def verify_horizontal():
    try:
        global count
        for k,i in enumerate(lista):
            tabuleiro()
            num=int(input("\nQual casa inserir: "))
            lista[num]=1
            if i[k] == 1:
                count+=1
            elif i[k]==0:
                count=0
            if count==3:
                raise Exception
    except:
        print("Alguém Venceu!")

def main():
    tabuleiro()
    verify_horizontal()
    
main()
    