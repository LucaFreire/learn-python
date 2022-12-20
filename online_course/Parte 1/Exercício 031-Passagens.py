'''um programa que pergunte a distância de uma viagem em km.Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.'''
km=int(input("Digite a Distância de sua Viagem: "))
if km<=200:
    valor= km*0.50
    print(f"Sua viagem é menor de 200km, sendo assim você deve pagar R${valor:.2f}")
else:
    valor= km*0.45
    print(f"Sua viagem é maior de 200km, sendo assim você deve pagar R${valor:.2f}")
      
    #Maneira simplificada: valor= km *0.50 if km <= 200 else km * 0.45