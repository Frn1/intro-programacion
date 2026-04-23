import random

def mayor_y_menor():
    valor_minimo, valor_maximo = 1, 30
    cantidad_de_numeros = 15
    
    # Inicializamos con estos numeros para asegurarnos que el programa
    # siempre pueda encontrar un numero mas chico o mas grande.
    numero_mas_chico, numero_mas_grande = valor_maximo, valor_minimo
    
    print("Los numeros son", end=" ")
    for i in range(cantidad_de_numeros):
        numero = random.randrange(valor_minimo, valor_maximo)
        
        if numero > numero_mas_grande:
            numero_mas_grande = numero
        if numero < numero_mas_chico:
            numero_mas_chico = numero
            
        print(numero, end="")
        if i != cantidad_de_numeros - 1:
            if i == cantidad_de_numeros - 2:
                print(" y ", end="")
            else:
                print(",", end=" ")
    print(".")
    
    print(f"El valor más grande es {numero_mas_grande} y el más chico es {numero_mas_chico}.")

if __name__ == "__main__":
    mayor_y_menor()