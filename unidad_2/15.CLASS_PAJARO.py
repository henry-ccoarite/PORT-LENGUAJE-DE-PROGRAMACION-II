class Pajaro:
    def mover(self):
        print("El pájaro vuela")
        
class Pez:
    def mover(self):
        print("El pez nada")
        
class Persona:
    def mover(self):
        print("La persona camina")

def desplazar(objeto):
    objeto.mover()

objetos = [Pajaro(), Pez(), Persona()]

for objeto in objetos:
    desplazar(objeto)

