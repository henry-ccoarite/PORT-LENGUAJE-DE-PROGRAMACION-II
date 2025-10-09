class Estadistica:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.datos = []

    def ingresar_datos(self):
        print(f"Ingrese {self.cantidad} datos numéricos:")
        for i in range(self.cantidad):
            valor = float(input(f"Dato {i+1}: "))
            self.datos.append(valor)

    def calcular_media(self):
        suma = 0
        for x in self.datos:
            suma = suma + x
        return suma / self.cantidad

    def calcular_varianza(self, media):
        suma_cuadrados = 0
        for x in self.datos:
            suma_cuadrados = suma_cuadrados + (x - media) ** 2
        return suma_cuadrados / self.cantidad

    def calcular_raiz(self, numero):
        # Método de Newton para la raíz cuadrada
        aproximacion = numero
        for _ in range(20):
            aproximacion = 0.5 * (aproximacion + numero / aproximacion)
        return aproximacion

    def mostrar_resultados(self):
        media = self.calcular_media()
        varianza = self.calcular_varianza(media)
        desviacion = self.calcular_raiz(varianza)

        print("\nResultados:")
        print(f"Media: {media:.2f}")
        print(f"Varianza: {varianza:.2f}")
        print(f"Desviación Estándar: {desviacion:.2f}")


def main():
    mi_estadistica = Estadistica(20)
    mi_estadistica.ingresar_datos()
    mi_estadistica.mostrar_resultados()

if __name__ == "__main__":
    main()
