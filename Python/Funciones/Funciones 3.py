def ejercicio3(texto: str) -> str:
    return (
        texto.replace("a", "A")
        .replace("e", "E")
        .replace("i", "I")
        .replace("o", "O")
        .replace("u", "U")
    )


if __name__ == "__main__":
    texto = input("Introduzca su texto: ")
    print(f"Salida: {ejercicio3(texto)}")
