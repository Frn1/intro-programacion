def ejercicio1():
    nombre = input("Introduzca un nombre: ")
    # Duplica el string, y lo invierte utilizando creando un slice con
    # un parametro de "paso" de -1, haciendo que empieze 
    # al final de la lista y termine al comienzo
    print(nombre[::-1])
        
if __name__ == "__main__":
    ejercicio1()