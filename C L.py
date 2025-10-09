class CL:
    def __init__(self,longitud,altura,ancho,JV,JH):
        self.longitud = longitud
        self.altura = altura
        self.ancho = ancho
        self.JV = JV
        self.JH = JH

    def calcular_CL(self):
        return 1/((self.longitud+JH)*(self.altura+JV))


longitud = float(input("ingrese la longitud del ladrillo:"))
altura = float(input("ingrese la altura del ladrillo:"))
ancho = float(input("ingrese el ancho del ladrillo:"))
JV = 0.015
JH = 0.015

operacion = CL(longitud,altura,ancho,JV,JH)

print ("la cantidad de ladrillos en un metro cuadrado es de:", operacion.calcular_CL()  )
print ("el valor total es de:", operacion.calcular_CL()*1.05,"por metro cuadrado.")
print ("La cantidad total de ladrillos en un area de 8.05 es de:", operacion.calcular_CL()*8.05*1.05)
