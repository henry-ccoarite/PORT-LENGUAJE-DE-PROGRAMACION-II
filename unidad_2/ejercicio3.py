class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        return self.salario

class EmpleadoTiempoCompleto(Empleado):
    def calcular_pago(self):
        return self.salario

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        super().__init__(nombre, salario_por_hora)
        self.horas_trabajadas = horas_trabajadas

    def calcular_pago(self):
        return self.salario * self.horas_trabajadas

if __name__ == "__main__":
    empleados = [
        EmpleadoTiempoCompleto("Roberto", 2500),
        EmpleadoPorHoras("Mario", 20, 80),
        EmpleadoTiempoCompleto("Carla", 3000),
        EmpleadoPorHoras("Carlos", 18, 95)
    ]
    for emp in empleados:
        print(f"Empleado: {emp.nombre} - Pago: ${emp.calcular_pago()}")
