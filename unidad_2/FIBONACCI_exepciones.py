def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("Debe ingresar un número entero.")
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
    try:
        numero = int(input("Ingrese un número entero: "))
        resultado = fibonacci(numero)
        print(f"Fibonacci({numero}) = {resultado}")
    except ValueError as ve:
        print("Error de valor:", ve)
    except TypeError as te:
        print("Error de valor:", te)
    except Exception as e:
        print("Error inesperado:", e)

if __name__ == "__main__":
    main()
