'''Crie um programa que leia a largura e a altura de uma parede em metros, 
calcule sua área e a quantidade de tinta necessária para pinta-la, 
sabendo que cada litro de tinta pinta uma área de 2m².'''

altura=float(input("Digite a altura de sua parede em metros: ")) 
largura=float(input("Digite a largura de sua parede em metros: "))
área= altura*largura
tinta= área/2
print(f'Tinta necessária: {tinta:.3}m²')
