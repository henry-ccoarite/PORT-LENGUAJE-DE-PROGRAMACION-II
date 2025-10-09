#par o impar
class IP:
    def __init__(self,limite):
        self.limite = limite
    def clasificar(self):
        for i in range(0,self.limite+1):
            if i==0:
                print(f"{i}-nulo")
            elif i%2==0:
                print(f"{i}-par")
            else:
                print(f"{i}-impar")
    

def main():
    miclasificacion=IP(10)
    resultado=miclasificacion.clasificar()
    

if __name__ == "__main__":
    main()
