class GestorEstudiantes:
    def __init__(self):
        self.arreglo_a = []
        self.arreglo_b = []

    def agregar_estudiante_a(self, estudiante):
        self.arreglo_a.append(estudiante)

    def agregar_estudiante_b(self, estudiante):
        self.arreglo_b.append(estudiante)

    def estudiantes_unicos_a(self):
        return [est for est in self.arreglo_a if est not in self.arreglo_b]

    def estudiantes_unicos_b(self):
        return [est for est in self.arreglo_b if est not in self.arreglo_a]

    def estudiantes_comunes(self):
        return [est for est in self.arreglo_a if est in self.arreglo_b]

    def gestionar(self):
        while True:
            print("\nOpciones:")
            print("1. Agregar estudiante a A")
            print("2. Agregar estudiante a B")
            print("3. Mostrar estudiantes únicos en A")
            print("4. Mostrar estudiantes únicos en B")
            print("5. Mostrar estudiantes comunes")
            print("6. Salir (solo si hay al menos 10 en ambos arreglos)")

            opcion = input("Elige una opción: ")

            if opcion == '1':
                estudiante = input("Nombre del estudiante a agregar en A: ")
                self.agregar_estudiante_a(estudiante)
            elif opcion == '2':
                estudiante = input("Nombre del estudiante a agregar en B: ")
                self.agregar_estudiante_b(estudiante)
            elif opcion == '3':
                unicos_a = self.estudiantes_unicos_a()
                print("Estudiantes únicos en A:", unicos_a)
            elif opcion == '4':
                unicos_b = self.estudiantes_unicos_b()
                print("Estudiantes únicos en B:", unicos_b)
            elif opcion == '5':
                comunes = self.estudiantes_comunes()
                print("Estudiantes comunes en A y B:", comunes)
            elif opcion == '6':
                if len(self.arreglo_a) >= 10 and len(self.arreglo_b) >= 10:
                    print("Saliendo del programa...")
                    break
                else:
                    print("No se puede salir hasta que haya al menos 10 estudiantes en A y 10 en B.")
            else:
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    gestor = GestorEstudiantes()
    gestor.gestionar()
