import math

class Calculadora:
    def soma(self, a, b):
        return a + b
    
    def subtrai(self, a, b):
        return a - b
    
    def multiplica(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b
    
    def potencia(self, a, b):
        return a ** b
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Não é possível calcular o módulo por zero")
        return a % b
    
    def raiz_quadrada(self, a):
        if a < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo")
        return math.sqrt(a)
    
    def fatorial(self, a):
        if a < 0:
            raise ValueError("Não é possível calcular o fatorial de um número negativo")
        if not isinstance(a, int):
            raise ValueError("O fatorial só é definido para números inteiros")
        return math.factorial(a)
    
    def logaritmo(self, a, base=math.e):
        if a <= 0:
            raise ValueError("O logaritmo só é definido para números positivos")
        return math.log(a, base)

