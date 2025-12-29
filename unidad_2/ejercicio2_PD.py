class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            print("Error: el precio no puede ser negativo.")
        else:
            self._precio = valor

    def aplicar_descuento(self, porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            print("Descuento inválido.")
        else:
            descuento = self._precio * (porcentaje / 100)
            self._precio -= descuento

def probar_productos():
    p1 = Producto("Laptop", 3000)
    p2 = Producto("Mouse", 50)

    p1.aplicar_descuento(20)
    print("Precio Laptop:", p1.precio)

    p2.aplicar_descuento(150)
    print("Precio Mouse:", p2.precio)

    p1.precio = -500
    print("Precio Laptop:", p1.precio)

def main():
    probar_productos()
if __name__ == "__main__":
    main()
