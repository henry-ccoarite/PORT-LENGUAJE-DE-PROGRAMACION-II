class Pitagoras:
    def __init__(self,catetoA,catetoB):
        self.catetoA = catetoA
        self.catetoB = catetoB

    def calcular_hipotenusa(self):
        return (self.catetoA**2 + self.catetoB**2)**(1/2)
catetoA= float(input("ingrese cateto A:"))
catetoB=float(input ("ingrese cateto B:"))

operacion = Pitagoras(catetoA,catetoB)

print ("La hipotenusa es ", operacion.calcular_hipotenusa())
