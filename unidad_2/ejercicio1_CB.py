class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= monto

    def mostrar_saldo(self):
        print(f"Saldo de {self.titular}: {self.saldo}")

def prueba_cuenta_bancaria():
    c1 = CuentaBancaria("Ana", 500)
    c2 = CuentaBancaria("Luis", 300)

    c1.depositar(200)
    c1.retirar(100)
    c1.mostrar_saldo()

    c2.retirar(500)
    c2.mostrar_saldo()

def main():
    print("<<<==============PROBANDO CUENTA BANCARIA===============>>>")
    prueba_cuenta_bancaria()
if __name__ == "__main__":
    main()
