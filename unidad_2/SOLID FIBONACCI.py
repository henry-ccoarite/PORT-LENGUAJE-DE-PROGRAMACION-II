class CalculadoraHipotenusa:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método calcular")

class Hipotenusa(CalculadoraHipotenusa):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5

class App:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def ejecutar(self):
        print(self.calculadora.calcular())

hipotenusa = Hipotenusa(3, 4)
app = App(hipotenusa)
app.ejecutar()
