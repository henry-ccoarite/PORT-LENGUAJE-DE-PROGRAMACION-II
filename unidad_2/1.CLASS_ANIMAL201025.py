class Animal: 
    def hacerSonido(self):
        print("Sonido genérico")

class Perro(Animal):
    
    def ladrar(self):
        print("¡Guau!")

perro = Perro()
perro.hacerSonido()
perro.ladrar()
