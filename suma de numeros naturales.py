#suma naturales
class SN:
    def __init__(self,limite):
        self.limite = limite
        self.suma = 0
    def Calcular_suma(self):
        for i in range(1,self.limite+1):
            self.suma=self.suma+i
    
        return self.suma
def main():
    misuma=SN(10)
    resultado=misuma.Calcular_suma()
    print(f"la suma de los primeros {misuma.limite} numeros naturales es : {resultado}")
    

if __name__ == "__main__":
    main()
