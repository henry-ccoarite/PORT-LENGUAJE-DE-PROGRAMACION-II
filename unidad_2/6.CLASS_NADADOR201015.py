class Nadador:  # CLASE BASE 1
    def nadar(self):
        print("Nadando en el agua")

class Volador:  # CLASE BASE 2
    def volar(self):
        print("Volando por el aire")

class Pato(Nadador, Volador):  # CLASE DERIVADA
    def graznar(self):
        print("¡Cuac!¡Cuac!")

class Cisne(Nadador, Volador):
    def graznar(self):
        print("¡Honk!¡Honk!")
        
cisne = Cisne()
cisne.nadar()
cisne.volar()
cisne.graznar()

pato = Pato()
pato.nadar()
pato.volar()
pato.graznar()
