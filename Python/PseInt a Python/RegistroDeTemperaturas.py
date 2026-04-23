def temperaturas_a_texto(lista: list) -> str:
    salida = ""
    cantidad = len(lista)
    for i in range(cantidad):
        valor = f"{lista[i]} °C"
        salida += valor
        if i != cantidad - 1:
            if i == cantidad - 2:
                salida += " y "
            else:
                salida += ", "
    return salida

def registro_de_temperaturas():
    temperaturas = []
    
    cantidad_de_temperaturas = 7
    print(f"Ingrese las {cantidad_de_temperaturas} temperaturas")
    for i in range(cantidad_de_temperaturas):
        temperatura_ingresada = float(input(f"Ingrese el la temperatura {i + 1}: "))
        temperaturas.append(temperatura_ingresada)
    
    while True:
        print("\n--- Menu ---")
        print(" 1. Ver todas las temperaturas")
        print(" 2. Ver el promedio de las temperaturas")
        print(" 3. Ver el día más caluroso")
        print(" 4. Salir")
        seleccion = int(input("Su selección: "))
        
        match seleccion:
            case 1:
                print(f"Las temperaturas son {temperaturas_a_texto(temperaturas)}")
            case 2:
                suma = 0.0
                for valor in temperaturas:
                    suma += valor
                print(f"\nEl promedio es {suma / len(temperaturas)} °C")
            case 3:
                temp_mas_grande = temperaturas[0]
                for temperatura in temperaturas:
                    if temperatura > temp_mas_grande:
                        temp_mas_grande = temperatura
                print(f"La temperatura más grande es {temp_mas_grande} °C")
            case 4:
                print("Saliendo...")
                break
            case _:
                print("No reconozco esa opción")

if __name__ == "__main__":
    registro_de_temperaturas()