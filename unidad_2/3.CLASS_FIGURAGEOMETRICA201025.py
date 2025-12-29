class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError("Las subclases deben implementar este método")

    def perimetro(self):
        raise NotImplementedError("Las subclases deben implementar este método")


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return 3.141592 * (self.radio ** 2)

    def perimetro(self):
        return 2 * 3.141592 * self.radio

circulo = Circulo(5)
print(f"Nombre: {circulo.nombre}")
print(f"Área: {circulo.area():.2f}")
print(f"Perímetro: {circulo.perimetro():.2f}")      
    
