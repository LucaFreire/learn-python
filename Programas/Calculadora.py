class Calculadora_Simples:
 
    def soma(self,valor1,valor2):
        return f"Soma: {valor1} + {valor2} = {valor1+valor2}"
        
    def subtração(self,valor1,valor2):
        return f"Subtração: {valor1} - {valor2} = {valor1-valor2}"
  
    def multiplicação(self,valor1,valor2):
        return f"Multiplicação: {valor1} X {valor2} = {valor1*valor2}"

    def divisão(self,valor1,valor2):
        return f"Divisão: {valor1} / {valor2} = {valor1/valor2}"

Comum=Calculadora_Simples()


class Calculadora_Científica(Calculadora_Simples):
            
    def potencia(self,valor1):
        return f"Potenciação: {valor1}² = {valor1**2}"

    def raiz(self,valor1):
        return f"Raiz: {valor1} = {valor1**0.5}"


Científica=Calculadora_Científica()

print(Comum.soma(5,4))

print(Científica.soma(5,5))

print(Científica.multiplicação(4, 6))

print(Científica.raiz(25))

print(Científica.divisão(25, 3))
