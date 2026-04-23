def carga_condicionada():
    valores = []
    
    print("Ingrese un valor negativo para terminar.")
    valor_ingresado = float(input(f"Ingrese el valor {len(valores) + 1}: "))
    while valor_ingresado >= 0:
        valores.append(valor_ingresado)
        valor_ingresado = float(input(f"Ingrese el valor {len(valores) + 1}: "))
    
    if len(valores) == 0:
        print("No se ingresaron valores.")
        return

    suma = 0.0
    for valor in valores:
        suma += valor
    print(f"\nEl promedio es {suma / len(valores)}")

if __name__ == "__main__":
    carga_condicionada()