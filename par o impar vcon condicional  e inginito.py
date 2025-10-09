class Clasificador:
    def __init__(self):
        self.total = 0

    def clasificar_num(self):
        print("Clasifica números como par, impar o nulo y calcula la suma.")
        print("Escribe números para analizar. Escribe 'fin' para terminar.")

        entrada = " "
        while entrada.lower() != "fin":
            entrada = input("Ingrese un número: ")

            if entrada.isdigit():
                numero = int(entrada)
                self.total += numero

                if numero == 0:
                    print(f"{numero} es nulo")
                elif numero % 2 == 0:
                    print(f"{numero} es par")
                else:
                    print(f"{numero} es impar")

            elif entrada.lower() != "fin":
                print("Entrada inválida. Ingrese un número o 'fin'.")

        print(f"\nLa suma total es: {self.total}")


def main():
    calculadora = Clasificador()
    calculadora.clasificar_num()


if __name__ == "__main__":
    main()
