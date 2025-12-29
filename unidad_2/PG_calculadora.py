from typing import TypeVar, Generic

T = TypeVar('T', int, float)

class Calculadora(Generic[T]):
    def __init__(self, a: T, b: T):
        try:
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("Los valores deben ser int o float")
            self.a = a
            self.b = b
        except Exception as e:
            raise TypeError(f"Error al asignar valores: {e}")

    def sumar(self) -> T:
        try:
            return self.a + self.b
        except Exception as e:
            raise TypeError(f"Error en la suma: {e}")
    
    def restar(self) -> T:
        try:
            return self.a - self.b
        except Exception as e:
            raise TypeError(f"Error en la resta: {e}")

    def multiplicar(self) -> T:
        try:
            return self.a * self.b
        except Exception as e:
            raise TypeError(f"Error en la multiplicación: {e}")
    
    def dividir(self) -> float:
        try:
            if self.b == 0:
                raise ArithmeticError("No se puede dividir entre 0")
            return self.a / self.b
        except ArithmeticError as e:
            raise ArithmeticError(f"Error en la división: {e}")
        except Exception as e:
            raise TypeError(f"Error inesperado en la división: {e}")


def main():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        calc = Calculadora[float](a, b)

        print("Suma:", calc.sumar())
        print("Resta:", calc.restar())
        print("Multiplicación:", calc.multiplicar())
        print("División:", calc.dividir())

    except ArithmeticError as e:
        print("ERROR ARITMÉTICO:", e)
    except TypeError as e:
        print("ERROR DE TIPO:", e)
    except Exception as e:
        print("ERROR GENERAL:", e)


if __name__ == "__main__":
    main()
