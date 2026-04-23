def venta_de_entradas_de_cine():
    asientos = [False] * 10
    
    while True:
        print("\n--- Menú ---")
        print(" 1: Ver asientos")
        print(" 2: Vender entrada")
        print(" 3: Salir")
        seleccion = int(input("Su selección: "))
        
        match seleccion:
            case 1:
                for i in range(len(asientos)):
                    print(f"Asiento {i + 1} ", end="")
                    if asientos[i] == False:
                        print("libre")
                    else:
                        print("ocupado")
            case 2:
                asiento = int(input("Ingrese el número de asiento que va a vender: ")) - 1
                
                if asiento >= 0 and asiento < len(asientos):
                    if asientos[asiento] == False:
                        asientos[asiento] = True
                        print(f"Asiento {asiento + 1} vendido correctamente")
                    else:
                        print(f"Asiento {asiento + 1} ya está ocupado")
                else:
                    print("Ese asiento no existe")
            case 3:
                print("Adiós! :3")
                break
            case _:
                print("No reconozco esa opción.")
    

if __name__ == "__main__":
    venta_de_entradas_de_cine()