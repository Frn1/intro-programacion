from pathlib import Path

if __name__ == "__main__":
    nombre_archivo = Path(__file__).parent.joinpath("datos.txt")

    with open(nombre_archivo, "r") as archivo:
        texto_completo = archivo.read()
        cant_lineas = texto_completo.count("\n")
        cant_palabras = len(texto_completo.split())
        cant_caracteres = len(
            texto_completo
        )  # - cant_lineas - texto_completo.count(" ")
        print(f"Lineas: {cant_lineas}")
        print(f"Palabras: {cant_palabras}")
        print(f"Caracterers: {cant_caracteres}")
