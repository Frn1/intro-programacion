def ejercicio4():
    n = int(input("Factorial de... "))
    if n < 0:
        print(f"No se puede calcular el factorial de {n}")
        return
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    print(f"El factorial de {n} es {resultado}")
    
if __name__ == "__main__":
    ejercicio4()