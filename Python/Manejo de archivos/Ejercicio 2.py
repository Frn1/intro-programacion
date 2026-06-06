from pathlib import Path

if __name__ == "__main__":
    nombre_archivo = Path(__file__).parent.joinpath("mensaje.txt")

    with open(nombre_archivo, "r") as archivo:
        palabra = "python"
        veces = archivo.read().lower().count(palabra)
        print(
            f"La palabra {palabra} aparece {veces} {'vez' if veces == 1 else 'veces'}"
        )
