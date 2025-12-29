from typing import TypeVar

T = TypeVar('T', int, float)

class CalculadoraFactorial:
    def __init__(self, numero: T):
        self.numero = numero

    def calcular_factorial(self) -> int:
        n = int(self.numero)
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def main():
    try:
        n = int(input("Ingrese un número: "))
        cal = CalculadoraFactorial(n)
        print(f"El factorial de {n} es: {cal.calcular_factorial()}")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
