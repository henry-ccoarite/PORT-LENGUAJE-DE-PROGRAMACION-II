class CATETO_A:
    def __init__(self, a):
        self.a = a

    def get_cuadrado_a(self):
        return self.a ** 2

class CATETO_B:
    def __init__(self, b):
        self.b = b

    def get_cuadrado_b(self):
        return self.b ** 2

class HIPOTENUSA(CATETO_A, CATETO_B):
    def __init__(self, a, b):
        CATETO_A.__init__(self, a)
        CATETO_B.__init__(self, b)
        self.c = 0

    def calcular_hipotenusa(self):
        a_cuadrado = self.get_cuadrado_a()
        b_cuadrado = self.get_cuadrado_b()
        
        c_cuadrado = a_cuadrado + b_cuadrado
        
        self.c = c_cuadrado **0.5
        return self.c
    
valor_a = 3
valor_b = 4

triangulo_rectangulo = HIPOTENUSA(valor_a, valor_b)
resultado_c = triangulo_rectangulo.calcular_hipotenusa()

print(f"Cateto A: {triangulo_rectangulo.a}")
print(f"Cateto B: {triangulo_rectangulo.b}")
print(f"Hipotenusa c: {resultado_c}")
