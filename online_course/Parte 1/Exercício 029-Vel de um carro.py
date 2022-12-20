'''Se o carro ultrapassar 80km/h,mostre uma mensagem dixendo que ele foi multado.
A multa vai custar R$7,00 por km acima do limite.'''

a=int(input("Digite sua Velocidade: "))
if a<=80:
    print("Você está dentro do limite, pode prosseguir!")
else:
    mul=(a-80)*7
    print("Você Ultrapassou o Limite, Multado!")
    print(f"Multa: R${mul:.2f}")    