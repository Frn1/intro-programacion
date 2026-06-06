from io import SEEK_END, SEEK_SET, TextIOWrapper
from pathlib import Path


def agregar_contacto(archivo: TextIOWrapper, nombre: str, telefono: str):
    archivo.seek(0, SEEK_END)

    # Cambiamos todas las "," por ",," para que puedan introducirse comas
    # Si empieza con una coma, ponemos un espacio al comienzo para que no ocurra ",,"
    # (espacios al comienzo y al final de cada valor se borran del texto)
    #
    # Si, se que este sistema no es perfecto, pero bue
    # Y si, se que me la sobre-complique

    nombre = nombre.replace(",", ",,")
    if nombre.startswith(","):
        nombre = " " + nombre

    telefono = telefono.replace(",", ",,")
    if telefono.startswith(","):
        telefono = " " + telefono

    archivo.write(f"{nombre},{telefono}\n")
    archivo.flush()


def leer_valor(archivo: TextIOWrapper) -> str | None:
    texto = ""
    coma_leida = False
    posicion_anterior = archivo.tell()

    while len(caracter := archivo.read(1)) != 0:
        if caracter == "\n":
            # Terminamos de leer cuando detectamos una linea nueva
            break
        elif coma_leida and caracter == ",":
            # Dos comas juntas se vuelven 1 coma
            coma_leida = False
        elif coma_leida and caracter != ",":
            # Leimos una coma, y despues vino otra cosa
            # Entonces devolvemos el archivo a despues de la coma para no causar problemas
            # y dejamos de leer ahi
            archivo.seek(posicion_anterior)
            break
        elif not coma_leida and caracter == ",":
            # Guardamos la posicion actual para mas tarde por si se necesita
            posicion_anterior = archivo.tell()
            coma_leida = True
            continue  # No quiero que se agrege
        texto += caracter
    if len(texto) == 0:
        return None
    # Borramos cualquier espacio que puede haber al final o al comienzo
    return texto.strip()


if __name__ == "__main__":
    nombre_archivo = Path(__file__).parent.joinpath("contactos.txt")

    with open(nombre_archivo, "a+") as archivo:
        while True:
            print("Elija una opción: ")
            print(" 1. Agregar contacto")
            print(" 2. Ver lista de contactos")
            print(" 3. Salir")
            print()

            seleccion = int(input("Su selección... "))
            match seleccion:
                case 1:
                    nombre = input("Ingrese el nombre: ")
                    telefono = input("Ingrese el telefono: ")
                    agregar_contacto(archivo, nombre, telefono)

                case 2:
                    print()
                    print("== Su lista de contactos ==")
                    print()
                    archivo.seek(0, SEEK_SET)
                    while True:
                        nombre = leer_valor(archivo)
                        if nombre is None:
                            break
                        print(f"{nombre}: ", end="")
                        telefono = leer_valor(archivo)
                        if telefono is None:
                            print("(Sin telefono registrado)")
                            break
                        print(f"{telefono}")

                case 3:
                    print("Adios!")
                    break

                case _:
                    print("No reconozco esa opción")
            print()
            print("---")
