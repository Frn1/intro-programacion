def ejercicio3():
    numero_str = input("Introduzca un número: ")
    numeros_entre_separador = 3
    separador = "."
    
    # Utilizamos la operación de módulo/resto para calcular
    # la posición del primer separador
    primer_separador = len(numero_str) % numeros_entre_separador
    # Imprimimos los caracteres antes del primer separador,
    # ya que el for loop empieza en el primer separador
    # y eso significa que algunos caracteres podrían quedar
    # fuera del for loop.
    # Es importante notar que si la lóngitud del número es un
    # múltiplo de numeros_entre_separador, entonces esto va a
    # imprimir un string vacio, y entonces en el for loop 
    # compensamos por eso para que no imprima ",123,456".
    print(numero_str[:primer_separador], end="")
    
    # Si se introduce un número con menos dígitos 
    # que numeros_entre_separador, este for loop 
    # no corre ya que quedaría con un range que empieza
    # y termina con el mismo valor
    for comienzo in range(primer_separador, len(numero_str), numeros_entre_separador):
        # Se calcula el fin de los números entre este
        # separador y el siguiente (o el fin del texto, si nos pasamos)
        # No es necesario verificar la longitud por que el
        # slice de python nos lo permite
        fin = comienzo + numeros_entre_separador
        # No imprimimos un separador si es comienzo es 0,
        # ya que esta implementación hace que si se introduce
        # algo con longitud múltiplo de numeros_entre_separador,
        # este for loop empieza en 0. Por esa razón se imprimiría 
        # ",123,456" (por ejemplo) que no es correcto.
        if comienzo != 0:
            print(separador, end="")
        print(numero_str[comienzo:fin], end="")
    print()
    
if __name__ == "__main__":
    ejercicio3()