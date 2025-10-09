class Fibonacci:
    def __init__(self,cantidad):
        self.cantidad = cantidad
        self.serie=[]
    def generar_serie(self):
        a,b = 0,1
        for _ in range (self.cantidad):
            self.serie.append(a)
            a,b=b,a+b
        return self.serie

def main():
    cantidad = float(input("ingrese la cantidad de numeros fibonacci a imprimir:"))
    mifibonacci = Fibonacci(cantidad)
    resultado = mifibonacci.generar_serie()
    print(resultado)
if __name__=="__main__":
    main()
