'''Leia o ano de nascimento e mostre sua categoria na Natação:
Até 9 anos:Mirim
Até 14 anos:Infantil
Até 19 anos:Júnior
Até 25 anos:Sênior
Acima: Master'''

from datetime import date
atual=date.today().year


ano=int(input("Digite seu ano de nascimento: "))
cal=atual-ano
if cal<=9:
    print(f"Você tem {cal} anos; Mirim")
elif cal<=14:
    print(f"Você tem {cal} anos; Infantil")
elif cal<=19:
    print(f"Você tem {cal} anos; Júnior")
elif cal<=25:
    print(f"Você tem {cal} anos; Sênior")
elif cal>25:
    print(f"Você tem {cal} anos; Master")            