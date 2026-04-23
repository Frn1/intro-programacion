class Producto:
    def __init__(self, codigo: str, nombre: str, cantidad: int = 0):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad

# Busca un producto con ese código en el inventario, y devuelve su indice si lo encuentra
# O None si no existes
def pedir_codigo_de_producto(inventario: list[Producto]) -> int | None:
    codigo_producto = input("Ingrese el número de asiento que va a vender: ").upper().strip()
    for i in range(len(inventario)):
        if inventario[i].codigo == codigo_producto:
            return i
    return None

def mini_inventario():
    inventario = [
        Producto("A125FD", "Producto 1", 23),
        Producto("JE534F1", "Producto 2", 5),
        Producto("PW635JF", "Producto 3", 0),
        Producto("163BSD2", "Producto 4", 11),
        Producto("DFUTAD2", "Producto 5", 2),
    ]
    
    while True:
        print("\n--- Menú ---")
        print(" 1: Mostrar inventario")
        print(" 2: Vender producto")
        print(" 3: Reponer producto")
        print(" 4: Salir")
        seleccion = int(input("Su selección: "))
        
        match seleccion:
            case 1:
                for producto in inventario:
                    print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Cantidad en stock: {producto.cantidad}")
            case 2: # Vender producto
                indice = pedir_codigo_de_producto(inventario)
                
                if indice == None:
                    print("No se encontró el producto con ese código.")
                    continue
                
                if inventario[indice].cantidad <= 0:
                    print(f"No hay más stock para {inventario[indice].nombre}.")
                else:
                    inventario[indice].cantidad -= 1
                    print(f"{inventario[indice].nombre} vendido correctamente.")
            case 3: # Reponer producto
                indice = pedir_codigo_de_producto(inventario)
                
                if indice == None:
                    print("No se encontró el producto con ese código.")
                    continue
                
                cantidad_a_reponer = int(input(f"Ingrese la cantdad de {inventario[indice].nombre} a reponer: "))
                inventario[indice].cantidad += cantidad_a_reponer
                
                print(f"{inventario[indice].nombre} repuesto correctamente. Ahora hay: {inventario[indice].cantidad}.")
            case 4:
                print("Adiós! :3")
                break
            case _:
                print("No reconozco esa opción.")
    

if __name__ == "__main__":
    mini_inventario()