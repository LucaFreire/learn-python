from random import randint as Escolha_Caracteres

Letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
'w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
'S','T','U','V','W','X','Y','Z','!','@','#','$','%','?','&','*',')','(','<','>',
'[',']','{','}','|','=','+','_','-','°',0,1,2,3,4,5,6,7,8,9]
SENHA=''
COUNT=0
num=int(input("Quantidade de Dígitos da Senha: "))

while True:

    if COUNT==num:
        print(f"Senha Gerada: {SENHA}")

        COUNT=0
        SENHA=''

        print()
        num=int(input("Quantidade de Dígitos da Senha [0]p/ Sair: "))
        if num<=0:
            break

    else:
        pc=Escolha_Caracteres(0,83)
        SENHA+=str((Letras[pc]))
        COUNT+=1

print("Você Saiu")
