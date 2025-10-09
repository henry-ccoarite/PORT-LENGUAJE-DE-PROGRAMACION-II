#clase persona
#atributo nombre
#accion si es o no mayor de edad
#onjeto persona Maria 25
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
nombre= input("ingrese el nombre de la persona:")
edad= float(input("ingrese la edad de la persona:"))
persona= Persona(nombre,edad)
if persona.es_mayor_de_edad():
    print(f"{persona.nombre} es mayor de edad")
else:
    print(f"{persona.nombre} es menor de edad")

