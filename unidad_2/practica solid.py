class Calculadora:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método calcular")


class Suma(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a + self.b


class Resta(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a - self.b


class Multiplicacion(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a * self.b


class Division(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        if self.b == 0:
            raise ArithmeticError("No se puede dividir entre cero")
        return self.a / self.b


class App:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def ejecutar(self):
        print("Resultado:", self.calculadora.calcular())


def main():
    try:
        a = float(input("Ingrese a: "))
        b = float(input("Ingrese b: "))

        print("Suma")
        App(Suma(a, b)).ejecutar()

        print("Resta")
        App(Resta(a, b)).ejecutar()

        print("Multiplicación")
        App(Multiplicacion(a, b)).ejecutar()

        print("División")
        App(Division(a, b)).ejecutar()

    except ValueError:
        print("Error: Ingrese valores numéricos válidos")
    except ArithmeticError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
