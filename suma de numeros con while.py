class Suma:
    def __init__(self,):
        self.total = 0
    def sumar_num(self):
        print("calcula la suma de numeros ingresados")
        print("escribe numeros para sumar. Escribe ¨fin¨ para terminar")
        entrada=" "
        while entrada.lower()!= "fin":
            entrada = input("ingrese un numero; ")
            if entrada.isdigit():
                self.total+=int(entrada)
            elif entrada.lower() != "fin":
                print("entrada invalida. ingrese un numerio o ¨fin¨")
        print(f"la suma total es: {self.total}")

def main():
    calculadora=Suma()
    calculadora.sumar_num()
if __name__=="__main__":
    main()
