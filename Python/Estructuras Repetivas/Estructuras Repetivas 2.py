def ejercicio2():
    total = 0.0
    productos = 0
    
    while True:
        precio = float(input(f"Ingresa el precio del producto {productos + 1}: "))
        if precio <= 0:
            break
        
        total += precio
        productos += 1 
    
    if productos <= 0:
        print("Usted no compró nada!")
        return

    print(f"Usted compró {productos} producto(s) con total ${total}")
    
if __name__ == "__main__":
    ejercicio2()