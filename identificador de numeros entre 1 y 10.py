class Verificador:
    def __init__(self):
        self.entrada = ""

    def verificar(self):
        print("Programa que verifica si un número está entre 1 y 10")
        print("Escribe un número o 'fin' para terminar")

        while self.entrada.lower() != "fin":
            self.entrada = input("Ingrese un número: ")

            if self.entrada.lower() == "fin":
                break

            if self.entrada.isdigit():
                numero = int(self.entrada)
                if 1 <= numero <= 10:
                    print(f"{numero} está entre 1 y 10")
                else:
                    print(f"{numero} no está entre 1 y 10")
            else:
                print("Entrada inválida, ingrese un número o 'fin'.")

        print("Programa finalizado.")


def main():
    verificador = Verificador()
    verificador.verificar()


if __name__ == "__main__":
    main()
