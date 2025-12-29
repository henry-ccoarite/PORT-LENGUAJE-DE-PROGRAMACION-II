class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        pass

class Perro(Animal):
    def hacerSonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacerSonido(self):
        return "¡Miau!"

perro = Perro("Rex")
gato = Gato("MiMi")

print(f"{perro.nombre} dice {perro.hacerSonido()}")
print(f"{gato.nombre} dice {gato.hacerSonido()}")

