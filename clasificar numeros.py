#clase numero
#atributo valor
#accion clasifircar
#objeto par impar nulo  
class numero:
    
    def __init__(self,valor):
        self.valor = valor
    
    def clasificar(self):
        if self.valor == 0:
            return "Nulo"
        elif self.valor % 2 ==0:
            return "Par"
        else:
            return "impar"
ejemplos = [numero(0), numero(2), numero(5)]

for num in ejemplos:
    tipo = num.clasificar()
    print(f"el  numero {num.valor} es {tipo}")
