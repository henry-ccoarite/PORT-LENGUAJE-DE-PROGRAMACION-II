class Motor:
    def encender(self):
        return "Motor listo"

    def funcionar(self):
        return "Motor funcionando"
    
class Auto:
    def __init__(self):
        self.m = Motor()

    def arrancar(self):
        return self.m.encender()

    def avanzar(self):
        return self.m.funcionar() + " - Auto avanzando"
    
carro = Auto()
print(carro.arrancar())
print(carro.avanzar())
