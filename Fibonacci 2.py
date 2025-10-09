class Fibonacci:
    def __init__(self,cantidad):
        self.cantidad = cantidad
        self.a = 0
        self.b = 1
        self.contador = 0
    def generar_serie(self):
        print("serie de Fibonacci")
        while self.contador<self.cantidad:
            print (self.a,end=" ")
            c= self.a+self.b
            self.a=self.b
            self.b=c
            self.contador+=1

def main():
    mifibonacci=Fibonacci(10)
    mifibonacci.generar_serie()
if __name__=="__main__":
    main()
