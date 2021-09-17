class Calculadora:
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b
    def subtracao(self, a, b):
        return a - b
    def multiplicacao(self, a, b):
        return a * b
    def divisao(self a, b):
        return a / b
calculadora = Calculadora()
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())
