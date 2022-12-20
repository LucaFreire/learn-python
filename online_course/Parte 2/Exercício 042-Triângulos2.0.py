'''Refaça o programa dso triângulos mostrando o tipo de triângulo:
Equilátero:Todos os lados iguais;
Isósceles:Dois lados iguais;
Escaleno:Todos os lados diferentes.'''

a=int(input("Digite Sua Primeria Medida: "))
b=int(input("Digite Sua Segunda Medida: "))
c=int(input("Digite Sua Terceira Medida: "))

if a+b>c and b+c>a and c+a>b:
    if a==b and c==a and b==c: # Vídeo: a == b == c
        print("Nome Do Triângulo: Equilátero (Todos os Lados Iguais)")
    elif a==b or a==c or b==c:
        print("Nome Do Triângulo: Isósceles (Dois Lados Iguais)")
    elif a!=b and a!=c and b!=c: # Vídeo: a != b != c != a
        print("Nome Do Triângulo: Escaleno (Todos os Lados Diferentes)")
else:
    print("Não É Possível Criar Um Triângulo!")