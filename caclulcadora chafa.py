class calculadora:
    def __init__ (self,a,b):
        self.__a=a
        self.__b=b
    def get_a(self):
        return self.__a
    def set_a(self,nuevo_a):
        if nuevo_a > 0:
            self.__a=nuevo_a
        else:
            print("numero no valida")
    def get_b(self):
        return self.__b
    def set_b(self,nuevo_b):
        if nuevo_b > 0:
            self.__b=nuevo_b
        else:
            print("numero no valida")
    def suma(self):
        return self.__a+self.__b
    def resta(self):
        return self.__a-self.__b
    def mult(self):
        return self.__a*self.__b
    def div(self):
        return self.__a/self.__b
cal=calculadora(2,5)

print("la suma de los numeros es:", int(cal.suma()))
print("la resta de los numeros es:", int(cal.resta()))
print("la multiplicacion de los numeros es:", float(cal.mult()))
print("la division de los numeros es:", float(cal.div()))
cal.set_a(8)
print("la suma de los numeros es:", int(cal.suma()))
print("la resta de los numeros es:", int(cal.resta()))
print("la multiplicacion de los numeros es:", float(cal.mult()))
print("la division de los numeros es:", float(cal.div()))
