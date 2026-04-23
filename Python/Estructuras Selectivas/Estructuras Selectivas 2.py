def ejercicio2():
    precio = float(input("Ingresa el precio del producto: "))
    dinero_ingresado = float(input("Ingresa la cantidad de dinero ingresada: "))
    
    diferencia = dinero_ingresado - precio
    if diferencia < 0:
        print(f"El dinero ingresado es insuficiente. Faltan ${-diferencia}.")
    else:
        print(f"Su vuelto es ${diferencia}.")
    
if __name__ == "__main__":
    ejercicio2()