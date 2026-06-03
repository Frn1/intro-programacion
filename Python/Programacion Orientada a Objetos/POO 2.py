class Rectangulo:
    base: float
    altura: float

    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def superficie(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)


def ejercicio2():
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))

    rect = Rectangulo(base, altura)
    print(f"La superficie es {rect.superficie()} y el perimetro es {rect.perimetro()}")


if __name__ == "__main__":
    ejercicio2()
