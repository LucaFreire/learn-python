'''Um programa que faça várias tabuadas, o programa é interrompido
se o número digitado for negativo.'''

tab=0
count=1
num=int(input("Número da Tabuada: "))
while count<=10:

    if num>=0:
        print(f"{count} X {num} = {count*num}")
        count+=1
    
    else:
        break

    if count==11:
        print(10*"~~")
        num=int(input("Número da Tabuada: "))
        count=1
        print(10*"~~")

print("Você Saiu")
    


