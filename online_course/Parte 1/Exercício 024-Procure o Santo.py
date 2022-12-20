#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

   #Dessa maneira não apenas fala se começa com Santo, o programa análisa o nome inteiro

a=str(input("Nome da cidade: ")).upper() 
b=a.find('SANTO') and a.strip()
if b==0:                                    #0 == True and -1== False, Meio Confuso
    print('Contém Santo no nome!')        
else:
    print("Não contém Santo no nome!")    

#Vídeo:

#cid=str(input("Nome da Cidade: ")).strip()
#print(cid[:5].upper() == 'SANTO')



