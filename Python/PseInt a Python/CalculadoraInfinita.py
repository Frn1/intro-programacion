def calculadora_infinita():
    while True:
        print("--- Operaciones ---")
        print(" 1. Sumar")
        print(" 2. Restar")
        print(" 3. Multiplicar")
        print(" 4. Dividir")
        print(" 5. Salir")
        operacion = int(input("Eliga su operacion: "))
        
        if operacion == 5:
            break
        elif operacion < 1 or operacion > 5:
            print("No reconozco esa operacion")
            continue
        
        num1 = float(input("Escriba el primer numero: "))
        num2 = float(input("Escriba el segundo numero: "))
        
        match operacion:
            case 1:
                print(f"Su resultado es {num1 + num2}")
            case 2:
                print(f"Su resultado es {num1 - num2}")
            case 3:
                print(f"Su resultado es {num1 * num2}")
            case 4:
                if num2 == 0:
                    print("No se puede dividir por 0")
                else:
                    print(f"Su resultado es {num1 / num2}")

if __name__ == "__main__":
    calculadora_infinita()