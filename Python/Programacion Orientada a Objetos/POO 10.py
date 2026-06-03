class Carrito:
    productos: list[str] = []

    def agregar(self, producto: str):
        self.productos.append(producto)

    def listar(self):
        print("Estos son los producto(s) en el carrito:")
        for producto in self.productos:
            print(f" - {producto}")
