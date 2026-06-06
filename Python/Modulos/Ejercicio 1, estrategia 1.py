import random


def ejercicio1():
    elementos_restantes = [i for i in range(0, 101)]

    cant_numeros = int(input("Ingrese cuantos numeros quiere: "))
    if cant_numeros >= len(elementos_restantes):
        print("No puedo generar tantos numeros del 0 al 100 sin repetir")
        return

    random.shuffle(elementos_restantes)
    for i in range(cant_numeros):
        print(elementos_restantes.pop())


if __name__ == "__main__":
    ejercicio1()
