class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

def maquina_expendedora():
    productos = [
        Producto("Coca-cola", 1200),
        Producto("Pepsi", 1100),
        Producto("7-up", 1500),
        Producto("Fanta", 20),
        Producto("Manaos", 1000),
    ]
    
    print("--- Máquina expendedora ---")
    print("Producto:")
    for i in range(len(productos)):
        print(f" {i + 1} - {productos[i].nombre}: {productos[i].precio} pesos")

    productoElegido = int(input("Eliga su prodcuto: ")) - 1
    if productoElegido < 0 or productoElegido > len(productos):
        print("Ese producto no está disponible.")
        return

    print(f"\nUsted eligió {productos[productoElegido].nombre}.")
    print(f"Debe pagar {productos[productoElegido].precio} pesos.")
    

if __name__ == "__main__":
    maquina_expendedora()