import math
from typing import TypeVar

T = TypeVar('T', int, float)

def calcular_hipotenusa(cateto_a: T, cateto_b: T) -> T:
    return math.sqrt(cateto_a**2 + cateto_b**2)

def main():
    try:
        a = float(input("Ingresar valor de A: "))
        b = float(input("Ingresar valor de B: "))
        
        print("Hipotenusa =", calcular_hipotenusa(a, b))
    except ValueError:
        print("Error: debe ingresar números válidos.")

main()

print("Hipotenusa =", calcular_hipotenusa(3, 4))
print("Hipotenusa =", calcular_hipotenusa(5.5, 2.2))

