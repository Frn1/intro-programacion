def invertir_grupos_no_vocales(texto: str) -> str:
    salida: str = ""
    grupo: list[str] = []
    for c in texto:
        match c.lower():
            case "a" | "e" | "i" | "o" | "u":
                grupo.reverse()
                salida += "".join(grupo)
                grupo.clear()
                salida += c
            case _:
                grupo.append(c)
    # Nos aseguramos que no quede el resto del grupo afueras
    # Pero no lo espejeamos, pq eso no pasa cuando queda un
    # grupo de letras al final, como se ve en el ejemplo (por alguna razon)
    salida += "".join(grupo)

    return salida


def cifrar(texto: str) -> str:
    if len(texto) == 0:
        return texto

    paso1 = invertir_grupos_no_vocales(texto)

    paso2 = ""
    for i in range(len(paso1) // 2):
        paso2 += paso1[i]
        paso2 += paso1[-i - 1]
    # Si la cantidad de characteres es impar,
    # un caracter quedara fuera del bucle anterior.
    if len(paso1) % 2 == 1:
        paso2 += paso1[len(paso1) // 2]

    return paso2


def decifrar(texto: str) -> str:
    if len(texto) == 0:
        return texto

    caracteres: list[str] = [""] * len(texto)
    for i in range(len(texto) // 2):
        caracteres[i] = texto[i * 2]
        caracteres[-i - 1] = texto[i * 2 + 1]
    # Si la cantidad de characteres es impar,
    # un caracter quedara fuera del bucle anterior.
    if len(texto) % 2 == 1:
        caracteres[len(texto) // 2] = texto[-1]

    paso1: str = "".join(caracteres)

    paso2 = invertir_grupos_no_vocales(paso1)

    return paso2


if __name__ == "__main__":
    print(cifrar("Bond, James Bond"))
    print(cifrar("Aureliano Buendia"))
    print(cifrar("abcde"))
    print()

    print(decifrar("BdonJo s, dBneam"))
    print(decifrar("Aauirnedleiua nBo"))
    print(decifrar("aedbc"))
