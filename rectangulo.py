
class Rectangulo:
    def __init__(self,base,altura):
        self.__base=base
        self.__altura=altura
    
    
    def get_base(self):
        return slef._base
    def set_base(self,nuevo_base):
        if nuevo_base > 0:
            self.__base=nuevo_base
        else:
            print("base no  valida")
    def get_altura(self):
        return slef._altura
    def set_altura(self,nuevo_altura):
        if nuevo_altura > 0:
            self.__altura=nuevo_altura
        else:
            print("altura no  valida")
    
    def area(self):
        return self.__base*self.__altura
    def perimetro(self):
        return self.__base*2+self.__altura*2
    
    
rectangulo = Rectangulo(10,5)

print("area del circulo es:", round (rectangulo.area(),2))
print("perimetro del circulo es:",round (rectangulo.perimetro(),2))
rectangulo.set_base(19)
rectangulo.set_altura(5)
print("area del circulo es:", round (rectangulo.area(),2))
print("perimetro del circulo es:",round (rectangulo.perimetro(),2))

