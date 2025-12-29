class VehiculoTerrestre:
    def conducir(self):
        print("Conduciendo por la carretera.")
        
    def frenar(self):
        print("El vehículo terrestre se ha detenido.")

class VehiculoAcuatico:
    def navegar(self):
        print("Navegando por el agua.")
        
    def fondear(self):
        print("El vehículo acuático ha fondeado.")

class VehiculoAnfibio(VehiculoTerrestre, VehiculoAcuatico):
    
    def __init__(self):
        self.modo_actual = "tierra"
        
    def transformar(self, modo):
        modo_lower = modo.lower()
        
        if modo_lower == "tierra":
            print("Cambiando al modo terrestre.")
            self.modo_actual = "tierra"
        elif modo_lower == "agua":
            print("Cambiando al modo acuático.")
            self.modo_actual = "agua"
        else:
            print(f"Modo '{modo}' no reconocido.")
    
    def conducir(self):
        if self.modo_actual == "tierra":
            super().conducir()
        else:
            print("ERROR: ¡El vehículo está en modo acuático! No puede conducir en tierra.")

    def navegar(self):
        if self.modo_actual == "agua":
            super().navegar()
        else:
            print("ERROR: ¡El vehículo está en modo terrestre! No puede navegar en agua.")
            
def main():
    anfibio = VehiculoAnfibio()
    
    print("--- MODO TIERRA (Acción correcta) ---")
    anfibio.transformar("Tierra")
    anfibio.conducir()
    anfibio.frenar()
    
    print("\n--- INTENTO INCORRECTO (Conducir en Agua) ---")
    anfibio.transformar("Agua")
    anfibio.conducir()

    print("\n--- MODO AGUA (Acción correcta) ---")
    anfibio.transformar("Agua")
    anfibio.navegar()
    anfibio.fondear()
    
    print("\n--- INTENTO INCORRECTO (Navegar en Tierra) ---")
    anfibio.transformar("Tierra")
    anfibio.navegar()

if __name__=="__main__":
    main()
