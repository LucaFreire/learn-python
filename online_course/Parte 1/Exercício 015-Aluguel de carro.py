'''Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado
calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.'''

km=float(input("Digite a distância percorrida em Km: "))
dias=int(input("Digite a quantidade de dias que o carro foi alugado: "))
print(f"Você alugou o carro por {dias} dias e deve pagar R${dias*60+km*0.15} por ter percorrido Km{km}!")