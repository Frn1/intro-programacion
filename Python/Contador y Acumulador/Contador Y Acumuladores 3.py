def ejercicio3():
    pares = 0
    impares = 0
    while True:
        numero = int(input("Ingrese el último número de la patente: "))
        if numero < 0:
            break
        elif numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print(f"{pares} vehículo(s) tenían patente con terminación par, y {impares} vehículo(s) tenían patente con terminación impar")

if __name__ == "__main__":
    ejercicio3()