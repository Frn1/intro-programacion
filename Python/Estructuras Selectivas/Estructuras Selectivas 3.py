def ejercicio3():
    limite_actual = float(input("Ingrese el limite actual de la tarjeta del cliente: "))
    tipo_de_tarjeta = int(input("Ingrese el tipo de la tarjeta del cliente: "))
    
    match tipo_de_tarjeta:
        case 1:
            porcentaje_de_aumento = 0.25
        case 2:
            porcentaje_de_aumento = 0.35
        case 3:
            porcentaje_de_aumento = 0.40
        case _:
            porcentaje_de_aumento = 0.50
    print(f"El nuevo limite para esa tarjeta del cliente será ${((1.0 + porcentaje_de_aumento) * limite_actual):.2f}")
            
    
if __name__ == "__main__":
    ejercicio3()