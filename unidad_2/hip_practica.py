import math
from typing import TypeVar

T = TypeVar('T', int, float)

class TrianguloRectangulo:
    def __init__(self, cateto_a: T, cateto_b: T):
        self.a = cateto_a
        self.b = cateto_b

    def hipotenusa(self) -> T:
        return math.sqrt(self.a**2 + self.b**2)

    def area(self) -> T:
        return (self.a * self.b)/2

    def perimetro(self) -> T:
        return self.a + self.b + self.hipotenusa()

def main():
    try:
        a: T = float(input("Ingrese el valor del cateto A: "))
        b: T = float(input("Ingrese el valor del cateto B: "))

        if a <= 0 or b <= 0:
            raise ValueError("Los catetos deben ser Positivos.")

        triangulo = TrianguloRectangulo(a, b)
        print(f"\nResultados del triángulo rectángulo:")
        print(f"Cateto A: {a}")
        print(f"Cateto B: {b}")
        print(f"Hipotenusa: {triangulo.hipotenusa():}")
        print(f"Área: {triangulo.area():}")
        print(f"Perímetro: {triangulo.perimetro():}")

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Ocurrió un error inesperado:", e)

if __name__ == "__main__":
    main()
