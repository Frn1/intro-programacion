class Persona:
    nombre: str
    edad: int

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, {self.nombre} de {self.edad} año(s)!")


def ejercicio1():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))

    persona = Persona(nombre, edad)
    persona.saludar()


if __name__ == "__main__":
    ejercicio1()
