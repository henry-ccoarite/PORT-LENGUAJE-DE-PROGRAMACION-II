from typing import TypeVar, Generic
import math

T = TypeVar('T', int, float)

class FiguraGeometrica(Generic[T]):
    def area(self) -> float:
        raise NotImplementedError

    def perimetro(self) -> float:
        raise NotImplementedError


class Rectangulo(FiguraGeometrica[T]):
    def __init__(self, base: T, altura: T):
        base_f = float(base)
        altura_f = float(altura)
        if base_f <= 0 or altura_f <= 0:
            raise ValueError("Datos inválidos")
        self.base = base_f
        self.altura = altura_f

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)


class Circulo(FiguraGeometrica[T]):
    def __init__(self, radio: T):
        radio_f = float(radio)
        if radio_f <= 0:
            raise ValueError("Dato inválido")
        self.radio = radio_f

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio


try:
    r: Rectangulo[int] = Rectangulo(4, 3)
    print("RECTÁNGULO")
    print("Área:", r.area())
    print("Perímetro:", r.perimetro())

    c: Circulo[float] = Circulo(5)
    print("\nCÍRCULO")
    print("Área:", c.area())
    print("Perímetro:", c.perimetro())

except ValueError as e:
    print("Error:", e)
