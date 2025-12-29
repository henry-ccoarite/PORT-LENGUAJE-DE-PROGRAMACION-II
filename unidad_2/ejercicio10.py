from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
animales = [
    Perro("Rex"),
    Gato("Misifú")
]

for a in animales:
    print(a.nombre, "-", a.hacer_sonido())
