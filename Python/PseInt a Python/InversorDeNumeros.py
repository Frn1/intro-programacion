def inversor_de_numeros():
    cantidad_de_numeros = 10
    numeros = []
    print(f"Ingrese los {cantidad_de_numeros} números")
    for i in range(cantidad_de_numeros):
        numeros.append(int(input(f"Ingrese el número {i + 1}: ")))
    print("El orden opuesto de los numeros es:")
    for i in range(cantidad_de_numeros):
        print(numeros[-i - 1])

if __name__ == "__main__":
    inversor_de_numeros()