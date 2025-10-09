class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base*self.altura
    
    def calcular_perimetro(self):
        return self.base*2 + self.altura*2
    
operacion = Rectangulo(5,6)

print ("el area es:", operacion.calcular_area())
print ("el perimetro es:", operacion.calcular_perimetro())
