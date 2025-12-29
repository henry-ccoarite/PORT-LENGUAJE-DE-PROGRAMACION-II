class FiguraGeometrica:
    def area(self):
        raise NotImplementedError

    def perimetro(self):
        raise NotImplementedError


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        resultado = 3.1416 * self.radio ** 2
        return resultado

    def perimetro(self):
        resultado = 2 * 3.1416 * self.radio
        return resultado


class Rectangulo(FiguraGeometrica):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        resultado = self.largo * self.ancho
        return resultado

    def perimetro(self):
        resultado = 2 * (self.largo + self.ancho)
        return resultado


class App:
    def __init__(self, figura):
        self.figura = figura

    def ejecutar(self):
        print("Área:", self.figura.area())
        print("Perímetro:", self.figura.perimetro())


opcion = input("Elige figura (circulo / rectangulo): ")

if opcion == "circulo":
    radio = float(input("Ingrese el radio: "))
    figura = Circulo(radio)

elif opcion == "rectangulo":
    largo = float(input("Ingrese el largo: "))
    ancho = float(input("Ingrese el ancho: "))
    figura = Rectangulo(largo, ancho)

else:
    print("Opción no válida")
    figura = None

if figura:
    app = App(figura)
    app.ejecutar()
