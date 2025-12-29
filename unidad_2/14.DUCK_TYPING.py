class Pajaro:
    def Volar(self):
        print("El pájaro vuela")

class Avion:
    def Volar(self):
        print("El avión vuela")

def hacer_Volar(obj):
    obj.Volar()

hacer_Volar(Pajaro())
hacer_Volar(Avion())
