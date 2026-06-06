# Sí, esto es una copia del juego.py :3

import random

minimo = 1000
maximo = 9999
numeroSecreto = random.randrange(minimo, maximo)

while True:
    numeroIngresado = int(input(f"Elija un número del {minimo} al {maximo}: "))
    if numeroIngresado == -1:
        print(f"El numero era {numeroSecreto}")
        break
    elif numeroSecreto == numeroIngresado:
        print("Felicitaciones! Usted encontró el número.")
        break
    elif numeroIngresado > numeroSecreto:
        print("Ese número es más chico. Intente de nuevo.")
    elif numeroIngresado < numeroSecreto:
        print("Ese número es más grande. Intente de nuevo.")
