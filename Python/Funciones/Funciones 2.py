def es_panvolica(palabra: str) -> bool:
    vocales = ("a", "e", "i", "o", "u")
    vocal_vista = [False] * len(vocales)
    for letra in palabra:
        todas_true = True
        for i in range(len(vocales)):
            if not vocal_vista[i] and letra == vocales[i]:
                vocal_vista[i] = True
            if todas_true and not vocal_vista[i]:
                todas_true = False
        if todas_true:
            return True
    return False


if __name__ == "__main__":
    print(f"educativo --> {es_panvolica('educativo')}")
    print(f"pedagogico --> {es_panvolica('pedagogico')}")
