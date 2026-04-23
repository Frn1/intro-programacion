from math import floor

def lista_a_texto(lista: list) -> str:
    salida = ""
    cantidad = len(lista)
    for i in range(cantidad):
        valor = str(lista[i])
        salida += valor
        if i != cantidad - 1:
            if i == cantidad - 2:
                salida += " y "
            else:
                salida += ", "
    return salida

# Busca un valor en una lista ORDENADA.
def busqueda_binaria(lista: list, valor_buscado) -> int | None:
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        med = izq + int(floor((der - izq) / 2))
        if lista[med] < valor_buscado:
            # Nos fuimos muy bajo
            izq = med + 1
        elif lista[med] > valor_buscado:
            # Nos fuimos muy alto
            der = med - 1
        else:
            # Lo encontramos! :3
            return med
    return None # No se encontró :(

def buscador_de_un_numero():
    numeros = [3, 5, 7, 8, 10, 12, 13, 16, 18, 29]
    numeros.sort()
    
    print(f"Los números son {lista_a_texto(numeros)}")
    
    valor_buscado = int(input("Ingrese el valor buscado: "))
    indice_encontrado = busqueda_binaria(numeros, valor_buscado)
    
    if indice_encontrado is not None:
        print(f"El número está en la posición {indice_encontrado + 1}")
    else:
        print("No se encontró el numero.")

if __name__ == "__main__":
    buscador_de_un_numero()