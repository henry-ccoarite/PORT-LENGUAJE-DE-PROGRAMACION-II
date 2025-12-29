class Animal:
    def hacer_sonido(self):
        print("sonido genérico")

class Perro(Animal):
    def hacer_sonido(self):
        print("guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("miau")

animales = [Perro(), Gato(), Animal()]
for animal in animales:
    animal.hacer_sonido()
