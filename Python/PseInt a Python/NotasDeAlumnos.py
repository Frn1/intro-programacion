class Alumno:
    def __init__(self, nombre: str, nota1: float, nota2: float):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

def notas_de_alumnos():
    estudiantes = []
    
    while True:
        print("\n--- Menú ---")
        print(" 1: Registrar nuevo alumno")
        print(" 2: Mostrar promedios de todos los alumnos")
        print(" 3: Salir")
        seleccion = int(input("Su selección: "))
        
        match seleccion:
            case 1:
                num_estudiante = len(estudiantes) + 1
                nombre_ingresado = input(f"Ingrese el nombre del estudiante {num_estudiante}: ")
                nota1_ingresada = float(input(f"Ingrese la primera nota del estudiante {num_estudiante}: "))
                nota2_ingresada = float(input(f"Ingrese la segunda nota del estudiante {num_estudiante}: "))
                estudiantes.append(Alumno(nombre_ingresado, nota1_ingresada, nota2_ingresada))
                print(f"Alumno {nombre_ingresado} registrado correctamente.")
            case 2:
                if len(estudiantes) == 0:
                    print("No hay ningún alumno registrado!")
                    continue
                for i in range(len(estudiantes)):
                    print(f"{estudiantes[i].nombre}, Promedio: {(estudiantes[i].nota1 + estudiantes[i].nota2) / 2}")
            case 3:
                print("Adiós! :3")
                break
            case _:
                print("No reconozco esa opción.")
    

if __name__ == "__main__":
    notas_de_alumnos()