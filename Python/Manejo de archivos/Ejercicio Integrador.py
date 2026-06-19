from io import TextIOWrapper
from pathlib import Path

_nombre_archivo: Path = Path(__file__).parent.joinpath("notas.txt")


def menu(nombre: str, opciones: list[str | tuple[str, int]]) -> int:
    print(f"---{nombre}---")
    numeros_validos = []
    for i, opcion in enumerate(opciones):
        opcion_is_str = isinstance(opcion, str)
        numero: int = (i + 1) if opcion_is_str else int(opcion[1])
        numeros_validos.append(numero)
        texto: str = opcion if opcion_is_str else opcion[0]
        print(f" {numero}: {texto}")
    while True:
        seleccion = input("Elija una opción: ")
        if not seleccion.isnumeric():
            print("Eso no es un número válido, vuelva a elegir.")
            continue
        seleccion = int(seleccion)
        if seleccion not in numeros_validos:
            print("No reconozco esa opción.")
            continue
        return seleccion


def agregar_alumno_a_archivo(nombre: str, nota: float):
    with open(_nombre_archivo, "a") as archivo:
        nombre = nombre.replace(",", ",,")
        if nombre.startswith(","):
            nombre = " " + nombre

        nota_texto = str(nota).replace(",", ",,")
        if nota_texto.startswith(","):
            nota_texto = " " + nota_texto

        archivo.write(f"{nombre},{nota_texto}\n")
        archivo.flush()


def agregar_alumno():
    nombre: str
    while True:
        nombre = input("Introduzca el nombre del alumno: ").strip()
        if len(nombre) == 0:
            print("El nombre no puede estar vacio")
            continue
        break

    nota: float
    while True:
        nota_introducida = input(f"Introduzca la nota de {nombre}: ").strip()
        if not nota_introducida.isnumeric():
            print("Esa nota no es válida")
            continue
        nota = float(nota_introducida)
        if nota < 0:
            print("La nota no puede ser menor a 0")
            continue
        if nota > 10:
            print("La nota no puede ser mayor a 10")
            continue
        break

    agregar_alumno_a_archivo(nombre, nota)


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


class Notas:
    archivo: TextIOWrapper | None

    def _abrir_archivo(self):
        self.archivo = open(_nombre_archivo, "r")

    def __iter__(self):
        self._abrir_archivo()
        return self

    def __next__(self):
        if self.archivo is None:
            self._abrir_archivo()
        assert self.archivo is not None
        nombre = leer_valor(self.archivo)
        if nombre is None:
            self.archivo.close()
            raise StopIteration
        nota = leer_valor(self.archivo)
        if nota is None:
            self.archivo.close()
            raise StopIteration
        return (nombre, float(nota))


if __name__ == "__main__":
    while True:
        match menu(
            "Menú principal",
            [
                "Agregar nuevo alumno y nota",
                "Imprimir todos los datos",
                "Imprimir alumnos aprobados",
                "Calcular promedio, nota más alta y nota más baja",
                ("Salir", 0),
            ],
        ):
            case 1:
                agregar_alumno()
            case 2:
                print()
                print("--Notas--")
                for nombre, nota in Notas():
                    print(f"{nombre}: {nota}")
            case 3:
                print()
                print("--Alumnos aprobados--")
                for nombre, nota in Notas():
                    if nota < 4:
                        continue
                    print(f"{nombre} aprobó con {nota}")
            case 4:
                print()
                print("--Info--")
                cantidad_de_notas = 0
                suma = 0.0
                maximo = None
                minimo = None
                for nombre, nota in Notas():
                    suma += nota
                    if maximo is None or nota > maximo:
                        maximo = nota
                    if minimo is None or nota < minimo:
                        minimo = nota
                    cantidad_de_notas += 1
                print(f"Promedio: {suma / cantidad_de_notas}")
                print(f"Nota mas alta: {maximo}")
                print(f"Nota mas baja: {minimo}")
            case 0:
                break
        print()
