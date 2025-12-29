class Figura:
    def area(self):
        return 0

class Rectangulo(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Triangulo(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return (self.a * self.b) / 2

class Circulo(Figura):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.1416 * self.r * self.r

figuras = [
    Rectangulo(3, 7),
    Triangulo(10, 4),
    Circulo(2)
]

for fig in figuras:
    print(fig.area())
