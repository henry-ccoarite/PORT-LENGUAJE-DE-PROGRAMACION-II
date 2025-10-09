class Numero:
    def __init__(self,cantidad):
        self.cantidad = cantidad
        self.contador = 0
    def generar_serie(self):
        print("numeros con while")
        while self.contador<self.cantidad:
            print (self.contador,end=" ")

            self.contador+=1

def main():
    minumero=Numero(10)
    minumero.generar_serie()
if __name__=="__main__":
    main()
