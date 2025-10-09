class Tabla:
    def __init__(self, numero):
        self.numero = numero

    def multiplicar(self):
        for i in range(1, 11):  
            operacion = self.numero*i
            print(f"{self.numero} x {i} = {operacion}")

def main():
    numero= int(input("ingrese un numero para generar su tabla:"))
    mitabla = Tabla(numero)  
    resultadof = mitabla.multiplicar()

if __name__ == "__main__":
    main()
