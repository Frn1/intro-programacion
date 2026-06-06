import random


def ejercicio1():
    numeros_ya_generados = []

    cant_numeros = int(input("Ingrese cuantos numeros quiere: "))
    if cant_numeros > 100:
        print("No puedo generar tantos numeros del 0 al 100 sin repetir")
        return

    for i in range(cant_numeros):
        while (numero := random.randint(0, 10)) in numeros_ya_generados:
            pass  # Genero un numero nuevo hasta que no este en la lista
        numeros_ya_generados.append(numero)
        print(numero)


if __name__ == "__main__":
    ejercicio1()
