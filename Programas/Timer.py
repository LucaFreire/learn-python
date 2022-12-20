import time
import os

while True:

    NUM=int(input("How many seconds: "))

    while NUM:
        minutos= NUM // 60
        sec= NUM % 60
        """hours= NUM // min {hours:02d}"""
        timer =f'{minutos:02d} {sec:02d}'
        print(timer, end ="\r")
        time.sleep(1)
        NUM-=1
    os.system("cls")
    print("FIM")
    esc=int(input("Deseja continuar?[1/0]: "))
    if esc == 0:
        break
print("Você Saiu!")

while True:

    HOURS=int(input("How many Hours: "))
    MIN=int(input("How many Minutes: "))
    NUM=int(input("How many Seconds: "))
    if NUM==MIN==HOURS==0:
        break
    while NUM:
        minutes= NUM // 60 
        sec= NUM % 60 
        hours= (NUM // 3600) 
        timer =f'{hours:02d} {minutes:02d} {sec:02d}'
        print(timer, end ="\r")
        time.sleep(1)
        NUM-=1
    os.system("cls")
    print("Time's Up!")
print("You Left")

