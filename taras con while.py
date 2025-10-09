class gestor_tareas:
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self,tarea):
        self.tareas.append(tarea)
        print("Tarea agregada")
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes")
        else:
            print("Traeas pendientes")
            for i, tarea in enumerate(self.tareas,1):
                print(f"{i} {tarea}")
mi_gestor = gestor_tareas()

while True:
    print ("\n-----MENU----")
    print("1. Agregar tareas")
    print("2. Mostrar tareas")
    print("3. salir")
    opcion= input("seleccione una opcion: ")

    if opcion == "1":
        tarea = input("escribe la tarea: ")
        mi_gestor.agregar_tarea(tarea)
    elif opcion == "2":
        mi_gestor.mostrar_tareas()
    elif opcion == "3":
        print("Saliendo del gestor de tareas")
        break
    else:
        print("Opcion no valida, intente denuevo")
    
    
        
