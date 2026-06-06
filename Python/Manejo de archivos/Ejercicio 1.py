from pathlib import Path

if __name__ == "__main__":
    nombre_archivo = Path(__file__).parent.joinpath("estudiantes.txt")

    with open(nombre_archivo, "a") as archivo:
        for i in range(5):
            nombre = input(f"Introduzca el nombre del estudiante {i + 1}: ")
            archivo.write(nombre)
            archivo.write("\n")

    print("=== Lista de estudiantes ===")
    contador = 0
    with open(nombre_archivo, "r") as archivo:
        for nombre in archivo.readlines():
            contador += 1
            print(f"{contador}: {nombre.strip()}")
    print(f"Hay {contador} estudiante(s)")
