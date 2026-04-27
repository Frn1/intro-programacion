def ejercicio2():
    multiplo = int(input("Ingrese el múltiplo: "))
    
    # Imprime los primeros 12 números de la tabla de multiplicar
    # y los suma
    suma = 0
    for i in range(12):
        multiplicador = i + 1
        valor = multiplo * multiplicador
        suma += valor
        print(f"{multiplo} * {multiplicador} = {valor}")
    print(f"La suma de esta tabla es {suma}")

if __name__ == "__main__":
    ejercicio2()