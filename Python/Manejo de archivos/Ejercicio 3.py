from io import SEEK_SET
from pathlib import Path

if __name__ == "__main__":
    nombre_archivo = Path(__file__).parent.joinpath("datos.txt")

    with open(nombre_archivo, "r") as archivo:
        primera_linea = archivo.readline()
        print(primera_linea)

        texto_restante = archivo.read()
        print(texto_restante)

        archivo.seek(0, SEEK_SET)

        texto_completo = archivo.read()
        print(texto_completo)
