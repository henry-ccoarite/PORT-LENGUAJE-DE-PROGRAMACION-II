class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError("Las subclases deben implementar este método")

    def perimetro(self):
        raise NotImplementedError("Las subclases deben implementar este método")

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2*(self.base + self.altura)
    
rectangulo = Rectangulo(4,6)
print(f"Nombre: {rectangulo.nombre}.2f")
print(f"Área: {rectangulo.area():.2f}")
print(f"Perímetro: {rectangulo.perimetro():.2f}")
