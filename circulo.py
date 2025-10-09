import math
class Circulo:
    def __init__(self,radio):
        self.__radio=radio
    
    
    def get_radio(self):
        return slef._radio
    def set_radio(self,nuevo_radio):
        if nuevo_radio > 0:
            self.__radio=nuevo_radio
        else:
            print("radio no  valida")
    def area(self):
        return math.pi*self.__radio**2
    def perimetro(self):
        return 2*math.pi*self.__radio
    
    
circulo = Circulo(5)

print("area del circulo es:", round (circulo.area(),2))
print("perimetro del circulo es:",round (circulo.perimetro(),2))


