class Coche:
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def mostrar_info(self):
        print(f"Coche:{self.marca} {self.modelo} {self.color}")
        
    def arrancar(self):
        print(f"Coche {self.marca} {self.modelo} {self.color} ha arrancado")
        
marca = input("ingrese la marca del coche:")
modelo = input("ingrese el modelo del coche:")
color = input("ingrese el color del coche:")

#crear un obleto

mi_coche = Coche(marca,modelo,color)

#usar metodos del objeto


mi_coche.mostrar_info()
mi_coche.arrancar()


