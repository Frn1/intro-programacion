class Estudiante:
    nombre: str
    notas: list[float]

    def __init__(self, nombre: str, notas: list[float]) -> None:
        self.nombre = nombre
        self.notas = notas

    def promedio(self) -> float | None:
        cant_notas = len(self.notas)
        if cant_notas == 0:
            return None
        return sum(self.notas) / cant_notas

    def esta_aprobado(self) -> bool | None:
        promedio = self.promedio()
        if promedio is None:
            return None
        return promedio > 6.0


def ejercicio3():
    nombre = input("Ingrese el nombre del estudiante: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i + 1} del estudiante: "))
        notas.append(nota)

    estudiante = Estudiante(nombre, notas)
    promedio = estudiante.promedio()
    esta_aprobado = estudiante.esta_aprobado()
    print(
        f"El estudiante está {'aprobado' if esta_aprobado else 'desaprobado'} con un promedio de {promedio:.2f}"
    )


if __name__ == "__main__":
    ejercicio3()
