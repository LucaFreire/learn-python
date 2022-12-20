from time import sleep
from os import system
from pyautogui import click

while True:
    COUNT=0
    NUM=str(input("Quantos Clicks Você Deseja?\n"))
    if NUM == 0:
        break
    CLICKS=int(NUM)
    print("O Código vai ser executado em 5 segundos!")
    sleep(5)
    print("Começou!!!\n")
    while COUNT != int(NUM):
        click()
        CLICKS-=1
        COUNT+=1
        print(f'Clicks Restantes: {CLICKS:02d}', end=" \r")
    system("cls")
    print("\nFIM! [0 p/Sair]")
print("Você Saiu!")
