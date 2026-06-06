def maximo(valores: list[float]) -> float:
    max = valores[0]
    for v in valores:
        if v > max:
            max = v
    return max


def minimo(valores: list[float]) -> float:
    min = valores[0]
    for v in valores:
        if v < min:
            min = v
    return min


def promedio(valores: list[float]) -> float:
    suma = 0.0
    for v in valores:
        suma += v
    return suma / len(valores)


def menores_a_0(valores: list[float]) -> int:
    contador = 0
    for v in valores:
        if v < 0:
            contador += 1
    return contador


if __name__ == "__main__":
    temps = [
        -0.1,
        3.1,
        1.9,
        -3.8,
        4.7,
        -4.7,
        6.9,
        -0.3,
        -4.9,
        -1.4,
        4.7,
        6.4,
        -1.7,
        5.2,
        9.0,
        -4.5,
        1.4,
        -2.6,
        -2.8,
        4.0,
        6.9,
        -0.4,
        8.5,
        4.3,
        5.3,
        8.6,
        8.1,
        3.4,
        -0.9,
        1.8,
    ]
    print("==== Temperaturas de julio ====")
    for temp in temps:
        print(f" {temp:.2f} °C")

    print("==== Temperaturas ====")
    print(f"Mínimo: {minimo(temps):.2f} °C")
    print(f"Máximo: {maximo(temps):.2f} °C")
    print(f"Promedio: {promedio(temps):.3f} °C")
    print(f"Días bajo cero: {menores_a_0(temps)} días")
