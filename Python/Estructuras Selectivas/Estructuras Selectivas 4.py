def ejercicio4():
    cantidad_mas_alta = None
    for i in range(3):
        cantidad = float(input(f"Ingrese la cantidad {i + 1}: "))
        if cantidad_mas_alta == None:
            cantidad_mas_alta = cantidad
        elif cantidad_mas_alta < cantidad:
            cantidad_mas_alta = cantidad
    
    print(f"La cantidad más alta es {cantidad_mas_alta}")
    
if __name__ == "__main__":
    ejercicio4()