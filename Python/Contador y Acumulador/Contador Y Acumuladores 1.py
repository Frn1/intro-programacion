def ejercicio1():
    menor = None
    mayor = None
    
    while True:
        numero = int(input("Introduzca un número: "))
        
        if numero < 0:
            break
        if menor == None or numero < menor:
            menor = numero
        if mayor == None or numero > mayor:
            mayor = numero
            
    if menor == None or mayor == None:
        print("No se introdujo ningún número")
        return
    
    print(f"El menor número es {menor} y el mayor número es {mayor}")

if __name__ == "__main__":
    ejercicio1()