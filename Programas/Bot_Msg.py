import os
import time
import pyautogui as spam

COUNT=0

msg=input("Digite sua Mensagem: ")
print()
LIMITE_MSG=str((input("Número de Mensagens: ")))

#Caso o Usuário Digite Algo Errado
while (LIMITE_MSG != '0' and LIMITE_MSG != '1' and LIMITE_MSG != '2' and LIMITE_MSG != '3'
and LIMITE_MSG != '4' and LIMITE_MSG != '5' and LIMITE_MSG != '6' and
LIMITE_MSG != '7' and LIMITE_MSG !='8' and LIMITE_MSG != '9'):
    LIMITE_MSG=str((input("Número Inválido, Digite Novamente: ")))

os.system("cls") #Utilizado Para Limpar o Terminal

#Tempo Para o Código Começar a Executar
print()
print("VOCÊ TEM 10 SEGUNDOS PARA CLICAR NA CAIXA DE MENSAGENS DO WHATSAPP!")
time.sleep(10)

#Spam de Mensagens
while COUNT <int(LIMITE_MSG):
    spam.typewrite(msg)
    spam.press("Enter")
    COUNT+=1
