class Vehiculo:
    def acelerar(self):
        return "Acelerando a gran velocidad"

class Volador:
    def volar(self):
        return "Despegando hacia el cielo"

class Avion(Vehiculo, Volador):
    def iniciar(self):
        return "Sistema del avión listo"

av = Avion()
print(av.iniciar())
print(av.acelerar())
print(av.volar())
