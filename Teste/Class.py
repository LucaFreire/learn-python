class Calculadora_Simples:
    def _init_(self,valor1,valor2):     
        self.valor1=valor1
        self.valor2=valor2 
        
    def soma(self,valor1,valor2):
        return valor1+valor2
          
    def sub(self,valor1,valor2):
        return valor1-valor2
        
    def mul(self,valor1,valor2):
        return valor1*valor2
        
    def div(self,valor1,valor2):
        return valor1/valor2
        
Simples=Calculadora_Simples()

class Calculadora_Científica(Calculadora_Simples):
    def _init_(self,valor1):
        super()._init_(self,valor1)
    
    def raiz(self,valor1):
        return valor1**0.5
    
    def pot(self,valor1):
        return valor1**2

Científica=Calculadora_Científica()

print(Simples.soma(2,2))
print(Científica.pot(5))
print(Científica.raiz(25))
print(Científica.mul(4,4))
print(Simples.sub(10,4))
