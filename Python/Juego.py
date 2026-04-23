import random

minimo = 1
maximo = 100
numeroSecreto = random.randrange(minimo, maximo)

while True:
    numeroIngresado = int(input(f"Elija un número del {minimo} al {maximo}: "))
    if numeroSecreto == numeroIngresado:
        print("Felicitaciones! Usted encontró el número.")
        break
    elif numeroIngresado > numeroSecreto:
        print("Ese número es más chico. Intente de nuevo.")
    elif numeroIngresado < numeroSecreto:
        print("Ese número es más grande. Intente de nuevo.")